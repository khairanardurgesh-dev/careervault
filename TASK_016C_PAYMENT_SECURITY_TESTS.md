# TASK_016C — Payment Security Tests

## Automated Unit/Integration Tests (Run in CI)

These tests use mocked dependencies and run without external credentials.

### 1. Order Creation Response Schema
```typescript
// Test: POST /api/checkout returns correct shape
const response = await fetch("/api/checkout", { method: "POST", body: JSON.stringify({ name: "Test", email: "test@example.com" }) });
const data = await response.json();
expect(data).toHaveProperty("razorpay_order_id");
expect(data).toHaveProperty("key_id");
expect(data).toHaveProperty("amount", 399900);
expect(data).toHaveProperty("currency", "INR");
expect(data).toHaveProperty("order_id");
```

### 2. Frontend/Backend Response Compatibility
```typescript
// Test: Checkout page can destructure all required fields
const { razorpay_order_id, key_id, amount, currency, order_id } = await createOrder();
expect(typeof razorpay_order_id).toBe("string");
expect(typeof key_id).toBe("string");
expect(typeof amount).toBe("number");
```

### 3. Invalid Product Price (Server-Side)
```typescript
// Test: Product price from DB used, not client-supplied
// Mock DB to return price_in_paise = 999 (incorrect)
const order = await createOrderFromServer();
// Should still use DB price (399900)
```

### 4. Invalid Payment Signature
```typescript
// Test: verifyPaymentSignature returns false for tampered signature
const valid = verifyPaymentSignature({ razorpayOrderId: "order_1", razorpayPaymentId: "pay_1", razorpaySignature: "wrong" });
expect(valid).toBe(false);
```

### 5. Invalid Webhook Signature
```typescript
// Test: verifyWebhookSignature returns false for wrong secret
const valid = verifyWebhookSignature("{}", "invalid_signature");
expect(valid).toBe(false);
```

### 6. Duplicate Webhook
```typescript
// Test: Second identical webhook returns duplicate: true
await processWebhook(payload);
const result = await processWebhook(payload);
expect(result.duplicate).toBe(true);
```

### 7. Failed Payment
```typescript
// Test: payment.failed event does not create entitlement
await processWebhook({ event: "payment.failed", payload: { payment: { entity: { order_id: "order_1" } } } });
// entitlements table unchanged
```

### 8. Successful Verified Payment (Client Verify)
```typescript
// Test: verify-payment endpoint creates entitlement on valid signature
await verifyPayment({ razorpay_order_id, razorpay_payment_id, razorpay_signature, order_id });
// order.status === "paid"
// entitlement exists for customer/product
```

### 9. Entitlement Creation Idempotency
```typescript
// Test: Calling verify-payment twice creates only one entitlement
await verifyPayment(...);
await verifyPayment(...);
// COUNT(entitlements WHERE customer_id=X AND product_id=Y) === 1
```

### 10. Unauthorized Download Attempt
```typescript
// Test: Download API returns 403 for non-entitled customer
const response = await downloadAsset({ assetId, token: "other_user_token" });
expect(response.status).toBe(403);
```

## Tests Requiring Razorpay Test Account (Manual/Staging)

These require `RAZORPAY_KEY_ID`, `RAZORPAY_KEY_SECRET`, `RAZORPAY_WEBHOOK_SECRET` configured.

### 1. End-to-End Checkout Flow
1. Navigate to `/checkout`
2. Fill form, submit
3. Razorpay modal opens with test card
4. Complete payment with test credentials
5. Verify redirect to `/payment/success`
6. Verify entitlement in DB
7. Verify download access

### 2. Webhook Delivery
1. Configure webhook URL in Razorpay Dashboard (ngrok/staging)
2. Trigger test payment
3. Verify webhook received and processed
4. Verify `payment_events` recorded
5. Verify order status = `paid`

### 3. Payment Failure Flow
1. Use failed test card
2. Verify `/payment/failed` shown
3. Verify no entitlement created

### 4. Duplicate Payment Attempt
1. Complete payment
2. Attempt same order again (should not double-charge)
3. Verify single entitlement

## Test Execution

```bash
# Automated tests (no external deps)
npm test

# Integration tests (requires Supabase local/Razorpay test)
npm run test:integration

# Manual E2E checklist in TEST_PLAN.md
```

## CI Configuration

Add to CI pipeline:
```yaml
- run: npm run lint
- run: npx tsc --noEmit
- run: npm run build
- run: npm test
```
