import crypto from "crypto";
import { getRazorpayKeyId, getRazorpayKeySecret, getRazorpayWebhookSecret } from "./env";

export async function createRazorpayOrder(params: {
  amount: number;
  currency: string;
  receipt: string;
}): Promise<{ id: string; amount: number; currency: string }> {
  const keyId = getRazorpayKeyId();
  const keySecret = getRazorpayKeySecret();
  const res = await fetch("https://api.razorpay.com/v1/orders", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: "Basic " + Buffer.from(`${keyId}:${keySecret}`).toString("base64"),
    },
    body: JSON.stringify(params),
  });
  if (!res.ok) throw new Error(`Razorpay order creation failed: ${res.status}`);
  return res.json();
}

export function verifyPaymentSignature(params: {
  razorpayOrderId: string;
  razorpayPaymentId: string;
  razorpaySignature: string;
}): boolean {
  const secret = getRazorpayKeySecret();
  const body = params.razorpayOrderId + "|" + params.razorpayPaymentId;
  const expected = crypto.createHmac("sha256", secret).update(body).digest("hex");
  const provided = params.razorpaySignature;
  if (typeof provided !== "string" || provided.length !== expected.length) {
    return false;
  }
  try {
    return crypto.timingSafeEqual(Buffer.from(expected), Buffer.from(provided));
  } catch {
    return false;
  }
}

export function verifyWebhookSignature(rawBody: string, signature: string): boolean {
  const secret = getRazorpayWebhookSecret();
  const expected = crypto.createHmac("sha256", secret).update(rawBody).digest("hex");
  try {
    return crypto.timingSafeEqual(Buffer.from(expected), Buffer.from(signature));
  } catch {
    return false;
  }
}
