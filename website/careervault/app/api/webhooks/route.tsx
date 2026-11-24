import type { NextRequest } from "next/server";
import { NextResponse } from "next/server";
import { createServiceRoleClient } from "@/lib/supabase";
import { verifyWebhookSignature } from "@/lib/razorpay";

export async function POST(req: NextRequest) {
  try {
    const rawBody = await req.text();
    const signature = req.headers.get("x-razorpay-signature");

    if (!signature) {
      return NextResponse.json({ message: "Missing signature" }, { status: 400 });
    }

    if (!verifyWebhookSignature(rawBody, signature)) {
      return NextResponse.json({ message: "Invalid signature" }, { status: 400 });
    }

    const payload = JSON.parse(rawBody);
    const eventType = payload.event;
    const providerEventId = payload.id || payload.event_id;

    const supabase = createServiceRoleClient();

    // Idempotency check
    const { data: existing } = await supabase
      .from("payment_events")
      .select("id")
      .eq("provider_event_id", providerEventId)
      .single();

    if (existing) {
      return NextResponse.json({ success: true, duplicate: true });
    }

    // Record event
    await supabase.from("payment_events").insert({
      provider: "razorpay",
      provider_event_id: providerEventId,
      event_type: eventType,
      processing_status: "received",
    });

    // Process event
    if (eventType === "payment.captured") {
      const paymentEntity = payload.payload?.payment?.entity;
      const orderId = paymentEntity?.order_id;
      const paymentId = paymentEntity?.id;

      if (orderId && paymentId) {
        const { data: order } = await supabase
          .from("orders")
          .select("*")
          .eq("razorpay_order_id", orderId)
          .single();

        if (order) {
          await supabase
            .from("orders")
            .update({ status: "paid", razorpay_payment_id: paymentId })
            .eq("id", order.id);

          // Create entitlement (idempotent via unique constraint)
          await supabase.from("entitlements").upsert({
            customer_id: order.customer_id,
            product_id: order.product_id,
            order_id: order.id,
            status: "active",
          }, { onConflict: "customer_id,product_id" });
        }
      }
    }

    await supabase
      .from("payment_events")
      .update({ processing_status: "processed", processed_at: new Date().toISOString() })
      .eq("provider_event_id", providerEventId);

    return NextResponse.json({ success: true });
  } catch (error) {
    console.error("Webhook error:", error);
    return NextResponse.json({ message: "Webhook error" }, { status: 500 });
  }
}
