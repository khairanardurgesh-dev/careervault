# TASK_015_LIVE_WEBSITE_AUDIT.md

## Live Website Inspection Summary

### Live URL Inspected
- **URL:** https://careervault-dusky.vercel.app
- **Inspection method:** Direct fetch (markdown conversion)
- **Date:** November 24, 2026

## CRITICAL FINDING — Live Site Does Not Match Local Source

### Observation
The live Vercel deployment at `https://careervault-dusky.vercel.app` displays the **default Next.js starter template** ("Create Next App" page with Next.js logo), NOT the CareerVault application.

### Evidence
The live page contains:
- "Create Next App" heading
- Next.js logo (/next.svg)
- "Looking for a starting point? Edit page.tsx" text
- Vercel "Deploy Now" button
- Next.js documentation links

It does NOT contain:
- CareerVault branding or tagline
- The hero section with "Your next career move deserves a better strategy"
- The ₹3,999 pricing
- The eight module cards
- Checkout, account, or any CareerVault routes

### Local Source Code (C:\Users\Quick\Desktop\CareerVault\website\careervault)
The local source contains the complete CareerVault application:
- `app/page.tsx` — Homepage with hero, ₹3,999 pricing, CTA buttons
- `app/product/page.tsx` — Eight module cards, six career tracks, pricing
- `app/how-it-works/page.tsx` — Six-step purchase flow
- `app/faq/page.tsx` — Nine FAQ accordions
- `app/contact/page.tsx` — Support contact (support@careervault.in)
- `app/privacy/page.tsx`, `app/terms/page.tsx`, `app/refund-policy/page.tsx`
- `app/checkout/page.tsx` — Checkout form with Razorpay integration
- `app/payment/success/page.tsx`, `app/payment/failed/page.tsx`
- `app/account/library/page.tsx` — Eight module download cards
- `app/account/login/page.tsx`, `app/account/settings/page.tsx`, `app/account/verify/page.tsx`
- `app/admin/dashboard/page.tsx` — Admin dashboard
- `app/api/checkout/route.tsx` — Server-side Razorpay order creation
- `app/api/webhooks/route.tsx` — HMAC signature verification + idempotent processing
- `app/api/downloads/route.tsx` — Auth + entitlement verification + signed URLs
- `app/lib/env.ts`, `app/lib/razorpay.ts`, `app/lib/supabase.ts` — Integration helpers
- `app/migrations/001_initial_schema.sql` — Database schema + RLS policies
- `app/globals.css` — Navy/electric-blue design system

### Conclusion
The live Vercel deployment does **not** contain the CareerVault application. It appears to be deployed from a different/older commit or a different branch that contains only the default Next.js starter. The local source code on branch `main` (commit `5f23d98`) contains the complete CareerVault application but has **not been deployed** to the live Vercel preview.

---

## Pages Inspected (Local Source)

| Page | Path | Status |
|------|------|--------|
| Homepage | `app/page.tsx` | Present, complete |
| Product | `app/product/page.tsx` | Present, complete |
| How It Works | `app/how-it-works/page.tsx` | Present, complete |
| FAQ | `app/faq/page.tsx` | Present, complete |
| Contact | `app/contact/page.tsx` | Present, complete |
| Privacy Policy | `app/privacy/page.tsx` | Present, complete |
| Terms | `app/terms/page.tsx` | Present (not read) |
| Refund Policy | `app/refund-policy/page.tsx` | Present (not read) |
| Checkout | `app/checkout/page.tsx` | Present, complete |
| Payment Success | `app/payment/success/page.tsx` | Present, complete |
| Payment Failed | `app/payment/failed/page.tsx` | Present, complete |
| Account Library | `app/account/library/page.tsx` | Present, complete |
| Account Login | `app/account/login/page.tsx` | Present, complete |
| Account Settings | `app/account/settings/page.tsx` | Present, complete |
| Account Verify | `app/account/verify/page.tsx` | Present (not read) |
| Admin Dashboard | `app/admin/dashboard/page.tsx` | Present, has TS error |
| API Checkout | `app/api/checkout/route.tsx` | Present, server-side |
| API Webhooks | `app/api/webhooks/route.tsx` | Present, HMAC verified |
| API Downloads | `app/api/downloads/route.tsx` | Present, auth+entitlement |

---

## Issues Identified

### P0 — Critical (Build-Breaking)

| # | Issue | File | Severity | Evidence |
|---|-------|------|----------|----------|
| P0-1 | HTML comment `<!-- Cards -->` inside JSX causes TypeScript error TS1003/TS1382, breaking production build | `app/admin/dashboard/page.tsx:13` | Critical | `tsc --noEmit` reports: "Identifier expected" and "Unexpected token" at line 13 |

### P1 — Major User-Facing Defects

| # | Issue | File | Severity | Evidence |
|---|-------|------|----------|----------|
| P1-1 | CSS typo `focus-visible:ring-2relative` (missing space) in button styles | `app/globals.css:73` | High | Visual inspection of CSS |
| P1-2 | CSS class `text-primary-hover` referenced in `.btn-primary` but not defined in Tailwind config or CSS | `app/globals.css:77` | High | Visual inspection; `tailwind.config.js` has no `primary-hover` color |
| P1-3 | Empty route `app/(marketing)/page.tsx` (0 lines) — route group with no content | `app/(marketing)/page.tsx` | High | File read: 0 lines |
| P1-4 | Login page uses a `<Button type="submit" disabled>` wrapping a `<Link>` — inaccessible, confusing UX | `app/account/login/page.tsx:25-29` | High | Visual inspection |

### P2 — Usability / Design Issues

| # | Issue | File | Severity | Evidence |
|---|-------|------|----------|----------|
| P2-1 | Broken media query `@media (max-width) {` with no value in globals.css | `app/globals.css:140` | Medium | Visual inspection of CSS |
| P2-2 | No sitemap.xml or robots.txt | Project root | Medium | Visual inspection of file listing |
| P2-3 | Live Vercel preview shows default Next.js template instead of CareerVault app | Vercel deployment | High | Direct fetch of live URL |

### P3 — Minor Improvements

| # | Issue | File | Severity | Evidence |
|---|-------|------|----------|----------|
| P3-1 | No Open Graph / Twitter card meta tags beyond basic title/description | `app/layout.tsx` | Low | Visual inspection |
| P3-2 | Contact page lists support email as plain text link only (no form) | `app/contact/page.tsx` | Low | Visual inspection |

---

## Live Site Accessibility Limitation

Direct browser automation was not performed; the live site was inspected via markdown fetch. The live site shows the default Next.js starter, confirming it does not match the local CareerVault source. No customer data or accounts were accessed.

## Recommendation

The live Vercel deployment must be updated to deploy the local `main` branch (commit `5f23d98`) which contains the complete CareerVault application. **This requires owner approval for production deployment.** All P0/P1 fixes below must be applied to the local source before deployment.
