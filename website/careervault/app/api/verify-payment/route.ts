import type { NextRequest } from "next/server";
import { NextResponse } from "next/server";
import { createServiceRoleClient } from "@/lib/supabase";
import { verifyPaymentSignature } from "@/lib/razorpay";

export const dynamic = "force-dynamic";

export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const { razorpay_order_id, razorpay_payment_id, razorpay_signature, order_id } = body;

    if (!razorpay_order_id || !razorpay_payment_id || !razorpay_signature || !order_id) {
      return NextResponse.json({ message: "Missing required payment verification fields" }, { status: 400 });
    }

    // Verify payment signature
    if (!verifyPaymentSignature({ razorpayOrderId: razorpay_order_id, razorpayPaymentId: razorpay_payment_id, razorpaySignature: razorpay_signature })) {
      return NextResponse.json({ message: "Invalid payment signature" }, { status: 400 });
    }

    const supabase = createServiceRoleClient();

    // Verify order exists and matches
    const { data: order, error: orderError } = await supabase
      .from("orders")
      .select("*")
      .eq("id", order_id)
      .eq("razorpay_order_id", razorpay_order_id)
      .single();

    if (orderError || !order) {
      return NextResponse.json({ message: "Order not found or mismatch" }, { status: 404 });
    }

    if (order.status === "paid") {
      // Already processed (possibly via webhook)
      return NextResponse.json({ success: true, already_processed: true });
    }

    // Update order status
    const { error: updateError } = await supabase
      .from("orders")
      .update({ status: "paid", razorpay_payment_id })
      .eq("id", order.id);

    if (updateError) throw updateError;

    // Create entitlement (idempotent via unique constraint)
    const { error: entitlementError } = await supabase.from("entitlements").upsert({
      customer_id: order.customer_id,
      product_id: order.product_id,
      order_id: order.id,
      status: "active",
    }, { onConflict: "customer_id,product_id" });

    if (entitlementError) throw entitlementError;

    return NextResponse.json({ success: true });
  } catch (error) {
    console.error("Verify payment error:", error);
    return NextResponse.json({ message: "Internal server error" }, { status: 500 });
  }
}
