# TASK 016 — Deployment Report

## Summary

| Field | Value |
|---|---|
| GitHub repository | `https://github.com/khairanardurgesh-dev/careervault.git` |
| Branch | `main` |
| Commit hash | `050c792` (`050c792 Ignore nested .next build directory`) — verified locally and at `origin/main` |
| Actual application root directory | `website/careervault` |
| Vercel Root Directory | **Unknown — Vercel access unavailable.** Must be set to `website/careervault`. |
| Build command | Expected: `npm run build` / `next build` (default). Not executed successfully in local env. |
| Build result | **BLOCKED** locally (npm install timeouts/node_modules instability; see Build Verification Report). |
| Deployment ID | Not available — no Vercel access / no deployment performed. |
| Preview URL | Not created. Existing URL reported by task: `https://careervault-dusky.vercel.app` (currently serving default Next.js starter per task). |
| CareerVault actually displayed | **Not verified by this task.** Live site was reported as default Next.js starter; no corrected preview deployment could be created. |

## Pages Successfully Tested

None. No preview deployment was created and local production build did not complete.

## Failed / Blocked Tests

| Area | Status | Reason |
|---|---|---|
| Vercel config inspection | BLOCKED | No Vercel CLI/auth/API access; no `.vercel/project.json`. |
| Vercel config correction | BLOCKED | No access to change project settings. |
| Preview deployment | BLOCKED | No Vercel access; cannot create preview without authenticated project control. |
| Local production build | BLOCKED | npm install timeouts; node_modules instability; missing resolvable `@supabase/supabase-js` after repair attempts. |
| Live/preview page verification | BLOCKED | No corrected deployment available. |
| Responsive checks (375x812, 390x844, 768x1024, 1366x768) | NOT RUN | No deployment. |
| Console/network checks | NOT RUN | No deployment. |
| Payment/auth/download E2E | NOT RUN / BLOCKED | No deployment; no credentials; test-only policy. |

## Diagnosis

The repository contains two Next.js packages. `careervault/` (repo top-level) is a default `create-next-app` starter (Next 16.4.6, "Create Next App", default Vercel template content) — this matches the live symptom. The real CareerVault app is `website/careervault/` (Next 14.2.4, full CareerVault routes/components/lib/migrations). The most probable Vercel misconfiguration is **Root Directory not set to `website/careervault`**.

## Remaining Owner Actions

1. **Grant Vercel access** (CLI login/token or dashboard) or perform dashboard changes directly.
2. In Vercel Project Settings, set **Root Directory = `website/careervault`**. Confirm repo `khairanardurgesh-dev/careervault`, branch `main`.
3. Set Install Command to `npm install --legacy-peer-deps` if needed; keep Output Directory default.
4. Confirm Node.js version compatible with Next 14.2.4 (18.17+; 20.x LTS recommended).
5. Add required env var names with test/appropriate values in Preview environment only: `NEXT_PUBLIC_SUPABASE_URL`, `NEXT_PUBLIC_SUPABASE_ANON_KEY`, `SUPABASE_SERVICE_ROLE_KEY`, `RAZORPAY_KEY_ID`, `RAZORPAY_KEY_SECRET`, `RAZORPAY_WEBHOOK_SECRET`, `RESEND_API_KEY`, `EMAIL_FROM`, `EMAIL_REPLY_TO`. Do not use live Razorpay keys.
6. Commit/push the two local Task 016 build-fix edits after review: `website/careervault/tsconfig.json` (`@/*` path alias) and `website/careervault/app/checkout/page.tsx` (`"use client"`). These are required for a clean build.
7. Trigger a **Preview Deployment** from `main` (commit `050c792` + fix commit). Do not promote to production without explicit approval.
8. After preview deploy, re-run Task 016 Phase 6 verification checklist (branding, hero, 8 modules, pricing, nav, product/FAQ/contact/legal/checkout/login, responsive viewports, console/network errors).

## Final Status

**C — BLOCKED BY BUILD, ACCESS OR CONFIGURATION ISSUE**

Blocked by: no authenticated Vercel access (cannot inspect/correct settings or create preview deployment), and local build environment cannot complete a clean production build due npm install timeouts / node_modules instability. Evidence strongly indicates Vercel Root Directory misconfiguration (`careervault/` starter deployed instead of `website/careervault/`).
