# TASK 016B — Fixes Implemented

## Root Cause Summary

All five reported unresolved imports shared one root cause: `website/careervault/tsconfig.json` lacked the `@/*` path alias. The referenced files existed and were tracked. Repairing the alias exposed additional genuine build defects (invalid layout import, duplicate `/` route, missing Button imports, invalid JSX attribute, Tailwind token/config gaps, route handler extension), which were also fixed.

## Files Added

| File | Purpose |
|---|---|
| `website/careervault/package-lock.json` | Reproducible dependency lockfile (397 packages) |
| `website/careervault/postcss.config.js` | Tailwind + Autoprefixer processing |
| `website/careervault/.eslintrc.json` | `next/core-web-vitals` ESLint config |

## Files Modified

| File | Change |
|---|---|
| `website/careervault/tsconfig.json` | Added `baseUrl: "."`, `paths: {"@/*": ["./*"]}`, `jsx: "preserve"`, `noEmit`, `allowJs`, `resolveJsonModule`, `isolatedModules`, `incremental`, Next plugin, standard include/exclude |
| `website/careervault/package.json` | Added `@supabase/supabase-js`; bumped `next`/`eslint-config-next` to `14.2.35`; added `@types/node`, `@types/react`, `@types/react-dom`, `eslint`, `tailwindcss`, `postcss`, `autoprefixer`; added `typecheck` script |
| `website/careervault/tailwind.config.js` | Added `background`, `foreground`, `card`, `popover`, `primary`, `secondary`, `muted`, `accent`, `border`, `input`, `ring` color tokens; broadened content globs |
| `website/careervault/app/globals.css` | Replaced undefined `@apply` tokens with valid Tailwind utilities; fixed `after-transition-w-0` → `after:transition-all`; removed duplicate custom `.text-primary`, `.text-white/60`, `.list-*` rules |
| `website/careervault/components/shared/button.tsx` | Rewrote as typed, accessible Button |
| `website/careervault/app/layout.tsx` | Fixed `next` import; added `ReactNode` type import |
| `website/careervault/app/page.tsx` | Removed unused `Image` import; escaped `What's` |
| `website/careervault/app/product/page.tsx` | `class` → `className`; removed unused `Image` import |
| `website/careervault/app/account/login/page.tsx` | Added missing `Button` import |
| `website/careervault/app/account/verify/page.tsx` | Added missing `Button` import |
| `website/careervault/app/payment/success/page.tsx` | Added missing `Button` import |
| `website/careervault/app/contact/page.tsx` | Escaped `'` as `&apos;` |
| `website/careervault/app/faq/page.tsx` | Escaped `"` as `&quot;` |
| `website/careervault/app/checkout/page.tsx` | Added `"use client"` (required for `useState`) |
| `website/careervault/app/api/checkout/route.ts` | Renamed from `route.tsx`; added `export const dynamic = "force-dynamic"`; removed unused `crypto` import |
| `website/careervault/app/api/downloads/route.ts` | Renamed from `route.tsx`; added `export const dynamic = "force-dynamic"` |
| `website/careervault/app/api/webhooks/route.ts` | Renamed from `route.tsx`; added `export const dynamic = "force-dynamic"` |
| `website/careervault/lib/razorpay.ts` | Use `getRazorpayKeyId()`; hardened `verifyPaymentSignature` length/try-catch checks |
| `website/careervault/app/(marketing)/page.tsx` | **Deleted** — duplicate `/` route conflicting with `app/page.tsx` |

## Button Component

`components/shared/button.tsx` now:

- Extends `React.ButtonHTMLAttributes<HTMLButtonElement>`.
- Supports `variant: "primary" | "outline"`, `asChild`, `loading`, `disabled`, `type`, `className`, and all native button props.
- `asChild` clones a single valid React element, merges `className`, and sets `aria-disabled` (no extra UI library).
- Native `<button>` path sets `type` (default `button`), `disabled` (disabled OR loading), and `aria-busy`.
- Uses existing `cn()` utility and existing `.btn`, `.btn-primary`, `.btn-outline` classes.
- No `any`; no new dependency.

## Supabase Integration

No new client pattern was invented. Existing `lib/supabase.ts` is retained:

- `createServiceRoleClient()` — server-only, service-role key, no session persistence.
- `createBrowserClient()` — anon key, browser-safe.
- `lib/env.ts` throws explicit errors for missing `NEXT_PUBLIC_SUPABASE_URL`, `NEXT_PUBLIC_SUPABASE_ANON_KEY`, `SUPABASE_SERVICE_ROLE_KEY`.
- Service-role key is never imported into client components.
- RLS policies and `001_initial_schema.sql` are unchanged.
- Checkout, webhook, and download routes continue to use server-side clients and entitlement checks.

Dependency added: `@supabase/supabase-js` (resolved 2.119.2).

## Razorpay Integration

Existing server-side implementation retained and hardened:

- `createRazorpayOrder()` uses `RAZORPAY_KEY_ID` / `RAZORPAY_KEY_SECRET` server-side only.
- Amount is server-controlled: checkout route reads `product.price_in_paise` from the database; migration default is `399900` paise (₹3,999).
- `verifyPaymentSignature()` uses HMAC SHA256 over `order_id|payment_id` with length and `timingSafeEqual` guards.
- `verifyWebhookSignature()` uses HMAC SHA256 over the raw request body.
- Webhook idempotency uses `payment_events.provider_event_id` unique constraint.
- Entitlement is created only in the verified `payment.captured` webhook path, not from a checkout redirect.
- No secret is exposed to the browser; `key_id` returned to the client is the public key.

No Razorpay SDK dependency was added because the existing implementation already uses the official server-side REST API; no mock success path was introduced.

## API Route Changes

- `app/api/checkout/route.tsx` → `route.ts`
- `app/api/downloads/route.tsx` → `route.ts`
- `app/api/webhooks/route.tsx` → `route.ts`

HTTP methods, request validation, response shapes, raw-body webhook handling, auth/entitlement checks, and idempotency are preserved. `export const dynamic = "force-dynamic"` added so request-dependent handlers are not statically prerendered.

## Dependency Changes

| Package | Before | After |
|---|---|---|
| `next` | 14.2.4 | 14.2.35 (latest patched 14.2.x) |
| `eslint-config-next` | absent | 14.2.35 |
| `@supabase/supabase-js` | absent (imported) | ^2.49.1 (resolved 2.119.2) |
| `@types/node` | absent | ^20.14.0 |
| `@types/react` | absent | ^18.3.3 |
| `@types/react-dom` | absent | ^18.3.0 |
| `eslint` | absent | ^8.57.0 |
| `tailwindcss` | absent | ^3.4.6 |
| `postcss` | absent | ^8.4.39 |
| `autoprefixer` | absent | ^10.4.19 |
| `react` / `react-dom` | 18.3.1 | 18.3.1 (unchanged) |
| `typescript` | 5.5.3 | 5.5.3 (unchanged) |

## Security Checks

- No `.env` file added or committed.
- `.env.example` contains placeholders only.
- No live/test secret values in source or reports.
- Service-role key remains server-only.
- RLS unchanged; no policy weakened.
- Webhook signature verification uses raw body.
- No production credentials modified.
- No force-push, no commit, no Vercel deployment performed.
