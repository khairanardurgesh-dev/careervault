# TASK 016C — Checkout Flow Audit

## Current Checkout Flow Analysis

### Frontend: `app/checkout/page.tsx`
- **Request**: POST `/api/checkout` with `{ name, email, mobile }`
- **Expects**: `data.payment_url` (redirect URL)
- **Actual behavior**: `window.location.href = data.payment_url`
- **Bug**: Backend does NOT return `payment_url` — returns `razorpay_order_id`, `key_id`, `amount`, `currency`, `order_id`

### Backend: `app/api/checkout/route.ts`
- **Creates**: Supabase order with `status: "pending"`, `amount_in_paise: product.price_in_paise` (399900 = ₹3,999)
- **Calls**: `createRazorpayOrder()` with amount, currency, receipt
- **Returns**: `{ success: true, order_id, razorpay_order_id, amount, currency, key_id }`
- **No `payment_url` field**

### Razorpay Integration: `lib/razorpay.ts`
- **`createRazorpayOrder()`**: Server-side POST to `https://api.razorpay.com/v1/orders` with Basic Auth
- **`verifyPaymentSignature()`**: HMAC SHA256 over `order_id|payment_id`
- **`verifyWebhookSignature()`**: HMAC SHA256 over raw body
- Uses official REST API (no Node SDK) — acceptable

### Webhook: `app/api/webhooks/route.ts`
- **Verifies**: Raw body signature via `verifyWebhookSignature()`
- **Idempotency**: `payment_events.provider_event_id` unique constraint
- **On `payment.captured`**: Updates order status to `paid`, creates entitlement via upsert
- **Authoritative**: Entitlement creation happens ONLY here

### Payment Success/Failed Pages
- **Static pages**: No verification logic
- **Success**: Shows `[Name]`, `[Order ID]` placeholders
- **Failed**: Links back to `/checkout`

### Database Schema
- `orders`: `razorpay_order_id` (unique), `razorpay_payment_id` (unique), `status` (pending/paid)
- `payment_events`: `provider_event_id` unique, `processing_status`
- `entitlements`: Unique on `(customer_id, product_id)`, created by webhook

## Root Cause

**Frontend/backend contract mismatch**: Frontend written for redirect-based flow (`payment_url`), backend implements Razorpay Checkout.js flow (returns order_id + key_id). The frontend never loads Razorpay Checkout.js or handles the payment callback.

## Required Fixes

1. **Frontend**: Load Razorpay Checkout.js, open modal with returned order details, handle success/failure callbacks
2. **Backend**: Add `/api/verify-payment` endpoint for client-side signature verification (immediate UX)
3. **Frontend**: On callback, call verify endpoint, then redirect to success/failed page
3. **Keep webhook** as authoritative for entitlement (already correct)
