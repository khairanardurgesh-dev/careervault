# TASK 017 — Deployment Report

## Deployment Status

| Item | Status |
|---|---|
| Vercel CLI available | ❌ No |
| Vercel authenticated | ❌ No |
| GitHub connected to Vercel | ❌ Unknown (owner must verify) |
| Preview deployment triggered | ❌ Not triggered |
| Deployment successful | ❌ No deployment attempted |

## Blocker: No Vercel Access

**Cannot deploy without owner action.** The Vercel project Root Directory must be configured to `website/careervault` before any deployment can succeed.

## Required Owner Actions (Exact Sequence)

### 1. Vercel Project Configuration
- Open Vercel Dashboard → Select/Import `khairanardurgesh-dev/careervault`
- Settings → General → Root Directory = `website/careervault`
- Settings → Build → Build Command = `npm run build`
- Settings → Build → Install Command = `npm ci`
- Settings → Node.js Version = `20.x`

### 2. Environment Variables (Preview)
Add in Settings → Environment Variables (Preview scope):

| Variable | Example Value | Source |
|---|---|---|
| `NEXT_PUBLIC_SUPABASE_URL` | `https://xxxxx.supabase.co` | Supabase Dashboard |
| `NEXT_PUBLIC_SUPABASE_ANON_KEY` | `eyJ...` | Supabase Dashboard |
| `SUPABASE_SERVICE_ROLE_KEY` | `eyJ...` | Supabase Dashboard (secret!) |
| `RAZORPAY_KEY_ID` | `rzp_test_...` | Razorpay Test Dashboard |
| `RAZORPAY_KEY_SECRET` | `...` | Razorpay Test Dashboard (secret!) |
| `RAZORPAY_WEBHOOK_SECRET` | `...` | Generated for test webhook |
| `RESEND_API_KEY` | `re_...` | Resend Dashboard (test) |
| `EMAIL_FROM` | `noreply@test.domain` | Verified domain |
| `EMAIL_REPLY_TO` | `support@test.domain` | Verified domain |

### 3. Supabase Setup (Prerequisite)
- Create test Supabase project
- Run `website/careervault/migrations/001_initial_schema.sql`
- Create storage bucket `careervault-products`
- Enable Email auth, set redirect URL to Preview URL

### 4. Razorpay Test Setup (Prerequisite)
- Create Razorpay test account
- Get test Key ID / Secret
- Configure webhook URL: `https://<preview-url>/api/webhooks`
- Generate webhook secret

### 5. Trigger Preview Deployment
- After all above: Vercel Dashboard → Deployments → Deploy from `main`
- Or push to `main` (if auto-deploy enabled)

## Expected Build Log (Success)

```
Cloning repository...
Checking out main at 050c792...
Detected Next.js in website/careervault
Installing dependencies with npm ci...
Running build: npm run build
▲ Next.js 14.2.35
✓ Compiled successfully
Linting and checking validity of types...
✓ Generating static pages (19/19)
Finalizing page optimization...
Build completed successfully
```

## Expected Failure Modes (If Root Directory Wrong)

| Symptom | Cause |
|---|---|
| `Detected Next.js in careervault` | Root Directory = repo root or `careervault/` |
| `Next.js 16.x` | Building starter project |
| `Module not found: @/components/...` | Root Directory wrong, tsconfig paths not resolved |
| `Cannot find module next` | Install command wrong |

## Current Commit for Deployment

- **Commit**: `050c792` (plus staged Task 016B/016C changes)
- **Branch**: `main`
- **Application Root**: `website/careervault`

## Deployment Not Performed

No deployment was executed because:
1. No Vercel CLI/authentication
2. Root Directory not configured (critical blocker)
3. Required environment variables not set
4. Supabase/Razorpay test projects not verified

**Owner must complete configuration before deployment can proceed.**
