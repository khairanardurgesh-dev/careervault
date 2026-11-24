# Task 012 Payment and Webhook Flow

## Payment Flow
1. Customer submits checkout form → POST /api/checkout
2. Server loads product from DB, creates customer, creates pending order
3. Server creates Razorpay order via API
4. Server returns razorpay_order_id, amount, key_id to frontend
5. Frontend opens Razorpay Checkout with server-generated order
6. Customer completes payment
7. Frontend sends payment_id, order_id, signature to backend for verification
8. Backend verifies HMAC signature, updates order to paid, creates entitlement

## Webhook Flow
1. Razorpay sends POST /api/webhooks with raw body
2. Server reads raw body, verifies HMAC SHA256 signature
3. Server checks idempotency via provider_event_id
4. Server records payment_event
5. Server processes event (payment.captured → update order + create entitlement)
6. Server updates payment_event status to processed
7. Server returns 200 OK

## Idempotency
- Duplicate webhook deliveries are detected via provider_event_id unique constraint
- Duplicate entitlements prevented via upsert with onConflict
