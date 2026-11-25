# TASK 017 — Supabase Readiness Report

## Supabase Access Status

| Item | Status |
|---|---|
| Supabase CLI installed | ❌ Unknown (not checked) |
| Supabase project linked | ❌ No |
| Can run migrations via CLI | ❌ No |
| Dashboard access | ❌ Not verified |

**Conclusion**: No programmatic Supabase access verified. All database setup must be done via Supabase Dashboard or CLI by the owner.

## Required Migrations

| Migration | File | Status |
|---|---|---|
| 001_initial_schema.sql | `website/careervault/migrations/001_initial_schema.sql` | ⏳ Not applied (no live project access) |

**Migration Contents**:
- Tables: `customers`, `products`, `orders`, `payment_events`, `entitlements`, `download_assets`, `download_events`, `email_events`
- Indexes on foreign keys and lookup columns
- RLS enabled on all tables
- RLS policies: customers/orders/entitlements/download_events/email_events — own records only
- `download_assets` — no direct access
- `payment_events` — no customer access
- Default product: `complete-job-switch-system`, 399900 paise (₹3,999), INR

## Schema Verification Checklist

| Requirement | SQL Reference | Application Usage |
|---|---|---|
| `products.price_in_paise` | `399900` | Checkout API reads for amount |
| `orders.razorpay_order_id` | UNIQUE | Webhook + verify-payment lookup |
| `orders.razorpay_payment_id` | UNIQUE | Webhook update |
| `orders.status` | pending/paid | Checkout creates pending, webhook/verify sets paid |
| `entitlements` unique (customer_id, product_id) | ON CONFLICT upsert | Idempotent grant |
| `payment_events.provider_event_id` | UNIQUE | Webhook idempotency |
| RLS: customers select own | `auth.uid() = auth_user_id` | Download API auth |
| RLS: orders select own | subquery on customers | Download API auth |

## Application Query Compatibility

| Query Location | Tables | Verified Against Schema |
|---|---|---|
| `app/api/checkout/route.ts` | products, customers, orders | ✅ |
| `app/api/verify-payment/route.ts` | orders, entitlements | ✅ |
| `app/api/webhooks/route.ts` | payment_events, orders, entitlements | ✅ |
| `app/api/downloads/route.ts` | customers, entitlements, download_assets, download_events | ✅ |

**All queries use service-role client server-side. No client-side Supabase queries except auth.**

## Storage & Auth Configuration Required

| Item | Required | Status |
|---|---|---|
| Storage bucket: `careervault-products` | For `download_assets.asset_path` signed URLs | ⏳ Not created |
| Bucket policy: signed URL access only | Download API creates signed URLs | ⏳ Not configured |
| Auth provider: Email (magic link) | Login uses email verification | ⏳ Not configured |
| Auth redirect URLs | Preview URL + `/account/verify` | ⏳ Not configured |
| Auth email template | Custom magic link email | ⏳ Not configured |

## Environment Variables Required (Preview)

| Variable | Source | Purpose |
|---|---|---|
| `NEXT_PUBLIC_SUPABASE_URL` | Supabase Dashboard → Settings → API | Client + server |
| `NEXT_PUBLIC_SUPABASE_ANON_KEY` | Supabase Dashboard → Settings → API | Browser client |
| `SUPABASE_SERVICE_ROLE_KEY` | Supabase Dashboard → Settings → API | Server admin (never expose to browser) |

## Owner Action Checklist (Supabase)

1. **Create Supabase test project** (or use existing staging project)
2. **Run migration**: In Supabase Dashboard → SQL Editor, paste and run `001_initial_schema.sql`
3. **Create storage bucket**: `careervault-products` (private, not public)
4. **Configure bucket policy**: Allow signed URL generation (via service role)
5. **Enable Email auth**: Authentication → Providers → Email → Enable
6. **Set auth redirect URL**: Add Preview URL (e.g., `https://careervault-*.vercel.app/account/verify`)
7. **Copy API keys**: Settings → API → Project URL, anon key, service_role key
8. **Add to Vercel Preview env vars**: All three variables
9. **Test connection**: Deploy Preview, verify no Supabase connection errors in logs

## Connection Status

| Service | Configured | Connected | Tested |
|---|---|---|---|
| Supabase (PostgreSQL) | ❌ No env vars set | ❌ No | ❌ No |
| Supabase Auth | ❌ No project | ❌ No | ❌ No |
| Supabase Storage | ❌ No bucket | ❌ No | ❌ No |

**Database readiness: UNVERIFIED — requires owner Supabase project setup**
