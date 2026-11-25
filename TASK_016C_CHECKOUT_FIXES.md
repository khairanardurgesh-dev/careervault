# TASK_016C — Checkout Fixes Implemented

## Summary of Changes

### 1. Checkout Page: `app/checkout/page.tsx`
**Before**: Expected `data.payment_url` and redirected via `window.location.href`
**After**: Implements Razorpay Checkout.js flow
- Loads Razorpay Checkout.js script via `useEffect`
- Calls `/api/checkout` to get order details (`razorpay_order_id`, `key_id`, `amount`, `currency`)
- Opens Razorpay modal with correct options (prefill, theme, handler)
- On payment success callback: calls `/api/verify-payment` for signature verification
- On verification success: redirects to `/payment/success`
- On payment cancelled: shows error message
- On gateway load failure: shows user-friendly error

### 2. Verify Payment API: `app/api/verify-payment/route.ts` (NEW)
- **Endpoint**: POST `/api/verify-payment`
- **Request**: `{ razorpay_order_id, razorpay_payment_id, razorpay_signature, order_id }`
- **Verifies**: Payment signature using `verifyPaymentSignature()` (HMAC SHA256)
- **Checks**: Order exists and matches `razorpay_order_id`
- **Idempotent**: Returns success if order already `paid` (webhook may have processed)
- **Updates**: Order status to `paid`, sets `razorpay_payment_id`
- **Creates**: Entitlement via upsert (idempotent on `customer_id,product_id`)
- **Returns**: `{ success: true }` or error with appropriate status code

### 3. Contract Alignment
**Frontend ↔ Backend (checkout)**:
- Frontend sends: `{ name, email, mobile }`
- Backend returns: `{ success, order_id, razorpay_order_id, amount, currency, key_id }`
- Frontend uses: `key_id`, `amount`, `currency`, `razorpay_order_id` for Razorpay Checkout

**Frontend ↔ Backend (verify-payment)**:
- Frontend sends: `{ razorpay_order_id, razorpay_payment_id, razorpay_signature, order_id }`
- Backend verifies signature, updates order, creates entitlement
- Returns: `{ success: true }` or error

**Webhook** (unchanged, authoritative):
- Receives `payment.captured` event
- Verifies webhook signature
- Idempotent via `payment_events.provider_event_id`
- Updates order, creates entitlement

### 4. Security Preservation
- Server-controlled price: `product.price_in_paise` (399900) from DB
- Razorpay signature verification: HMAC SHA256 on both client callback and webhook
- Webhook raw-body verification
- Service-role key isolated to server
- Entitlement created only after verified payment (client verify OR webhook)
- RLS policies unchanged
- No client-side price trust
- Duplicate handling: webhook idempotency + verify-payment idempotency

### 5. Error Handling Coverage
| Scenario | Handled |
|---|---|
| Payment success | Client verify → success redirect |
| Payment failure | Razorpay `ondismiss` → error message |
| User cancellation | `modal.ondismiss` → error message |
| Invalid signature | Client verify returns 400 |
| Invalid webhook signature | Webhook returns 400 |
| Duplicate webhook | `payment_events` unique constraint |
| Duplicate client callback | Order status check returns success |
| Delayed webhook | Webhook processes after client verify |
| Order creation failure | Checkout API returns 500 |
| Gateway load failure | Frontend shows error, disables button |
