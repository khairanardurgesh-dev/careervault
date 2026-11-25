# TASK 016B — Source Audit

## Repository State

| Item | Value |
|---|---|
| Repository | `https://github.com/khairanardurgesh-dev/careervault.git` |
| Branch | `main` |
| Latest commit | `050c792 Ignore nested .next build directory` |
| Actual application directory | `website/careervault/` |
| Framework | Next.js 14.2.4 (source) → 14.2.35 (patched during repair) |
| Working tree at audit start | Modified `tsconfig.json`, `app/checkout/page.tsx` from Task 016; otherwise clean |

## Actual Directory Structure (application)

```
website/careervault/
  app/
    layout.tsx
    page.tsx
    globals.css
    account/{login,verify,library,settings}/page.tsx
    admin/dashboard/page.tsx
    api/{checkout,downloads,webhooks}/route.tsx
    checkout/page.tsx
    contact/page.tsx
    faq/page.tsx
    how-it-works/page.tsx
    payment/{success,failed}/page.tsx
    privacy/page.tsx
    product/page.tsx
    refund-policy/page.tsx
    terms/page.tsx
  components/shared/button.tsx
  lib/{env,supabase,razorpay,utils}.ts
  migrations/001_initial_schema.sql
  next.config.js
  package.json
  tailwind.config.js
  tsconfig.json
  .env.example
```

## Reported Missing-Import Errors

| # | Reported error | Referenced file | Exists in Git? | Actual root cause |
|---|---|---|---|---|
| 1 | `app/account/library/page.tsx` cannot resolve `@/components/shared/button` | `components/shared/button.tsx` | Yes (`website/careervault/components/shared/button.tsx`) | `tsconfig.json` had no `baseUrl`/`paths` alias for `@/*`; the file was never missing |
| 2 | `app/api/checkout/route.tsx` cannot resolve `@/lib/supabase` | `lib/supabase.ts` | Yes | Same missing `@/*` path alias |
| 3 | `app/api/checkout/route.tsx` cannot resolve `@/lib/razorpay` | `lib/razorpay.ts` | Yes | Same missing `@/*` path alias |
| 4 | `app/api/downloads/route.tsx` cannot resolve `@/lib/supabase` | `lib/supabase.ts` | Yes | Same missing `@/*` path alias |
| 5 | `app/api/webhooks/route.tsx` cannot resolve `@/lib/supabase` | `lib/supabase.ts` | Yes | Same missing `@/*` path alias |

No referenced module was omitted from Git, misnamed, or differently cased. `git ls-files` confirms all five files are tracked.

## TypeScript Configuration (before repair)

`website/careervault/tsconfig.json` contained `compilerOptions` but **no** `baseUrl` and **no** `paths`. Imports such as `@/components/shared/button` and `@/lib/supabase` therefore could not be resolved by TypeScript, Next.js webpack, or Vercel's build.

## Existing Supabase Implementation

`lib/supabase.ts` already used the official SDK:

- `createServiceRoleClient()` — server-side client using `SUPABASE_SERVICE_ROLE_KEY`, `autoRefreshToken: false`, `persistSession: false`.
- `createBrowserClient()` — browser-safe client using `NEXT_PUBLIC_SUPABASE_ANON_KEY`.

`lib/env.ts` validates required variables and throws explicit errors when missing. No hardcoded credentials. No fake/mock client.

## Existing Razorpay Implementation

`lib/razorpay.ts` already implemented:

- `createRazorpayOrder()` — server-side POST to `https://api.razorpay.com/v1/orders` using HTTP Basic auth from `RAZORPAY_KEY_ID` / `RAZORPAY_KEY_SECRET`.
- `verifyPaymentSignature()` — HMAC SHA256 over `order_id|payment_id`.
- `verifyWebhookSignature()` — HMAC SHA256 over the raw request body.

No Razorpay secret is exposed to client code. The module was not missing; only the alias resolution failed.

## Database / Migrations

`migrations/001_initial_schema.sql` defines `customers`, `products`, `orders`, `payment_events`, `entitlements`, `download_assets`, `download_events`, `email_events`, indexes, RLS enablement, RLS policies, and the default product with `price_in_paise = 399900` (₹3,999). No schema changes were made.

## Additional Build-Blocking Defects Found

| File | Defect | Impact |
|---|---|---|
| `app/layout.tsx` | `import { children, Metadata } from "next"` — `children` is not a Next export | TS2614 build failure |
| `app/layout.tsx` | `React.ReactNode` used without React import | TS error |
| `app/product/page.tsx` | `<div class="...">` instead of `className` | TS/JSX error |
| `app/product/page.tsx`, `app/page.tsx` | Unused `next/image` imports | Lint errors |
| `app/account/login/page.tsx` | `<Button>` used without import | TS error |
| `app/account/verify/page.tsx` | `<Button>` used without import | TS error |
| `app/payment/success/page.tsx` | `<Button>` used without import | TS error |
| `app/page.tsx` and `app/(marketing)/page.tsx` | Two pages both resolve to `/` | Route conflict / prerender crash (`clientModules` undefined) |
| `app/api/*/route.tsx` | Route handlers named `.tsx` | Non-standard; migrated to `.ts` |
| `app/globals.css` | `@apply` of undefined Tailwind tokens (`btn`, `primary`, `card`, `border`, `input`, `ring`, `accent`, `card-foreground`) and invalid `after-transition-w-0` | Tailwind build failure |
| `tailwind.config.js` | Only `navy`/`electric` colors defined | Missing design tokens |
| `postcss.config.js` | Missing | Tailwind not processed |
| `.eslintrc.json` | Missing | `next lint` non-interactive failure |
| `package.json` | Missing `@supabase/supabase-js`, `@types/*`, ESLint, Tailwind/PostCSS deps | Module/build failures |
| `app/contact/page.tsx`, `app/faq/page.tsx`, `app/page.tsx` | Unescaped `'`, `"` in JSX | `react/no-unescaped-entities` errors |

## npm `Unknown env config "cache-dir"` Warning

No `.npmrc` exists at repository root, `website/careervault/`, or `website/`. The warning originates from the user/global npm configuration or an environment variable such as `npm_config_cache_dir` outside this repository. It is not caused by project configuration and was not modified.

## Git-Tracked vs Local

All application source files are tracked. `node_modules/`, `.next/`, `next-env.d.ts`, and `.env` are ignored by the root `.gitignore`. `website/careervault/package-lock.json` is explicitly un-ignored and is now generated.
