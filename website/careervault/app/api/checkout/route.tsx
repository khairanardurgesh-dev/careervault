import type { NextRequest } from "next/server";
import { NextResponse } from "next/server";
import crypto from "crypto";
import { createServiceRoleClient } from "@/lib/supabase";
import { createRazorpayOrder } from "@/lib/razorpay";

export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const { name, email, mobile } = body;

    if (!name || !email) {
      return NextResponse.json({ message: "Name and email are required" }, { status: 400 });
    }

    const supabase = createServiceRoleClient();

    // Get product
    const { data: product } = await supabase
      .from("products")
      .select("*")
      .eq("slug", "complete-job-switch-system")
      .single();

    if (!product) {
      return NextResponse.json({ message: "Product not found" }, { status: 404 });
    }

    // Find or create customer
    let customer;
    const { data: existing } = await supabase
      .from("customers")
      .select("*")
      .eq("email", email)
      .single();

    if (existing) {
      customer = existing;
    } else {
      const { data: newCustomer, error } = await supabase
        .from("customers")
        .insert({ email, full_name: name })
        .select()
        .single();
      if (error) throw error;
      customer = newCustomer;
    }

    // Create pending order
    const { data: order, error: orderError } = await supabase
      .from("orders")
      .insert({
        customer_id: customer.id,
        product_id: product.id,
        amount_in_paise: product.price_in_paise,
        currency: product.currency,
        status: "pending",
        payment_provider: "razorpay",
      })
      .select()
      .single();

    if (orderError) throw orderError;

    // Create Razorpay order
    const razorpayOrder = await createRazorpayOrder({
      amount: product.price_in_paise,
      currency: product.currency,
      receipt: `order_${order.id}`,
    });

    // Update order with razorpay order id
    await supabase
      .from("orders")
      .update({ razorpay_order_id: razorpayOrder.id })
      .eq("id", order.id);

    return NextResponse.json({
      success: true,
      order_id: order.id,
      razorpay_order_id: razorpayOrder.id,
      amount: product.price_in_paise,
      currency: product.currency,
      key_id: process.env.RAZORPAY_KEY_ID,
    });
  } catch (error) {
    console.error("Checkout error:", error);
    return NextResponse.json({ message: "Internal server error" }, { status: 500 });
  }
}
