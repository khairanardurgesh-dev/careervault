# TASK 017 — Payment Flow Security Review

## Scope

Review of the complete payment flow security:
- `app/api/checkout/route.ts` — Order creation
- `app/api/verify-payment/route.ts` — Client-side payment verification
- `app/api/webhooks/route.ts` — Server-authoritative webhook handling
- `lib/razorpay.ts` — Cryptographic verification utilities
- `lib/supabase.ts` — Database client isolation
- Database schema & RLS policies

## Security Architecture

```
┌─────────────┐     1. POST {name,email,mobile}      ┌──────────────────┐
│   Browser   │ ────────────────────────────────────▶ │ /api/checkout    │
└─────────────┘                                       │ (server-only)    │
                                                     │ • Validate input │
◀──────────────────────────────────────────────────── │ • Create order   │
   2. {razorpay_order_id, key_id,                     │ • Create Razorpay│
      amount, currency, order_id}                     │   order          │
                                                     └────────┬─────────┘
                                                              │
                          3. Load Razorpay.js                 │
                          4. Open modal with                  │
                             order_id, key_id,                │
                             amount, prefill                  │
                          5. User pays                        │
                          6. Razorpay calls handler           │
                          7. POST to /api/verify-payment      │
┌─────────────┐                                       ┌────────▼─────────┐
│   Browser   │ ────────────────────────────────────▶ │ /api/verify-     │
└─────────────┘   7. {razorpay_order_id,              │ payment          │
                   razorpay_payment_id,                │ (server-only)    │
                   razorpay_signature,                 │ • Verify HMAC    │
                   order_id}                           │ • Check order    │
                                                     │ • Update status  │
◀──────────────────────────────────────────────────── │ • Create entitle.│
   8. {success: true}                                 └────────┬─────────┘
                                                              │
                    9. Razorpay → Webhook                     │
                         (async, independent)                 │
┌─────────────────┐                                   ┌───────▼─────────┐
│   Razorpay      │ ─────────────────────────────────▶ │ /api/webhooks   │
│   (server)      │   Raw body + x-razorpay-signature  │ (server-only)   │
└─────────────────┘                                    │ • Verify HMAC   │
                                                       │ • Idempotency   │
                                                       │ • Update order  │
                                                       │ • Create entitle│
                                                       └─────────────────┘
```

## Security Requirements Verification

### 1. Server-Controlled Price ✅
| Check | Implementation | Status |
|---|---|---|
| Price from DB, not client | `app/api/checkout/route.ts` reads `product.price_in_paise` | ✅ |
| Price constant | Migration sets `399900` (₹3,999) | ✅ |
| Client cannot override | No `amount` in client request body | ✅ |

### 2. Razorpay Signature Verification (HMAC SHA256) ✅
| Location | Algorithm | Implementation |
|---|---|---|
| `lib/razorpay.ts::verifyPaymentSignature()` | HMAC SHA256 over `order_id|payment_id` | ✅ Constant-time compare |
| `lib/razorpay.ts::verifyWebhookSignature()` | HMAC SHA256 over raw body | ✅ Constant-time compare |
| `app/api/verify-payment/route.ts` | Calls `verifyPaymentSignature()` | ✅ |
| `app/api/webhooks/route.ts` | Calls `verifyWebhookSignature()` | ✅ |

**Key Security Properties**:
- Uses `crypto.timingSafeEqual()` for constant-time comparison
- Validates signature length before comparison
- Catches exceptions, returns `false` on error
- Webhook uses **raw request body** (not parsed JSON)

### 3. Webhook Idempotency ✅
| Mechanism | Implementation |
|---|---|
| Unique constraint | `payment_events.provider_event_id` UNIQUE |
| Check-before-insert | SELECT then INSERT |
| Duplicate handling | Returns `{success: true, duplicate: true}` |
| Status tracking | `processing_status`: received → processed |

### 4. Entitlement Creation ✅
| Property | Implementation |
|---|---|
| Server-only | Both verify-payment and webhook use service-role client |
| Idempotent | `entitlements` UNIQUE on `(customer_id, product_id)` + upsert |
| Authoritative source | Webhook is primary; verify-payment is fast-path |
| Race handling | If webhook processes first, verify-payment returns `already_processed: true` |

### 5. Service-Role Key Isolation ✅
| Check | Status |
|---|---|
| Never imported in client components | ✅ Only in `lib/supabase.ts` server functions |
| `createServiceRoleClient()` used only in API routes | ✅ |
| `createBrowserClient()` uses anon key only | ✅ |

### 6. Database RLS ✅
| Table | Policy | Status |
|---|---|---|
| `customers` | Select own (`auth.uid() = auth_user_id`) | ✅ |
| `orders` | Select own via customer subquery | ✅ |
| `entitlements` | Select own | ✅ |
| `download_assets` | No direct access (`USING (false)`) | ✅ |
| `payment_events` | No access (`USING (false)`) | ✅ |

### 7. No Client Trust ✅
| Check | Status |
|---|---|
| Client never receives service-role key | ✅ |
| Client never sets price | ✅ |
| Client callback verified server-side | ✅ `/api/verify-payment` |
| Webhook independent of client | ✅ Async, raw body verification |
| Entitlement not granted on client success alone | ✅ Webhook is authoritative |

## Vulnerability Assessment

| Potential Issue | Mitigation |
|---|---|
| Replay attack on verify-payment | Order status check + idempotent upsert |
| Race: webhook + verify-payment concurrent | Both use upsert with unique constraint |
| Client tampers with order_id | verify-payment validates `order.razorpay_order_id === body.razorpay_order_id` |
| Webhook signature bypass | Raw body + HMAC + timing-safe compare |
| Duplicate entitlement | UNIQUE constraint + upsert on conflict |
| Price manipulation | Price read from DB, never from client |

## Environment Variable Security

| Variable | Exposure | Required Scope |
|---|---|---|
| `NEXT_PUBLIC_SUPABASE_URL` | Public (browser) | Preview only |
| `NEXT_PUBLIC_SUPABASE_ANON_KEY` | Public (browser) | Preview only |
| `SUPABASE_SERVICE_ROLE_KEY` | **Secret** (server only) | Preview only |
| `RAZORPAY_KEY_ID` | Public (browser) | Preview only (test) |
| `RAZORPAY_KEY_SECRET` | **Secret** (server only) | Preview only (test) |
| `RAZORPAY_WEBHOOK_SECRET` | **Secret** (server only) | Preview only (test) |
| `RESEND_API_KEY` | **Secret** (server only) | Preview only |
| `EMAIL_FROM` / `EMAIL_REPLY_TO` | Config | Preview only |

**All must be configured in Vercel Preview environment only. Never Production until verified.**

## Test Verification Required

| Test | Method | Status |
|---|---|---|
| Invalid signature rejected | Unit test `verifyPaymentSignature` with bad sig | ⏳ |
| Invalid webhook signature rejected | Unit test `verifyWebhookSignature` with bad sig | ⏳ |
| Duplicate webhook returns duplicate | Integration test | ⏳ |
| Failed payment creates no entitlement | E2E with failed test card | ⏳ |
| Successful payment creates one entitlement | E2E with test card | ⏳ |
| Unauthorized download blocked | API test with wrong token | ⏳ |
| Client cannot set price | Verify checkout API ignores client amount | ⏳ |

## Security Review Conclusion

**Current code passes all static security checks.** The payment flow implements:
- Defense in depth (client verify + webhook)
- Constant-time cryptographic verification
- Idempotent state transitions
- Server-side price control
- Proper secret isolation
- RLS-enforced data access

**Remaining**: Requires live Preview deployment with test credentials to execute dynamic security tests.

## Sign-Off

| Reviewer | Date | Status |
|---|---|---|
| DevOps Engineer (Task 017) | 2026-11-25 | Code review complete — requires live test |
