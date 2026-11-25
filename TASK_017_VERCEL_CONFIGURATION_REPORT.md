# TASK 017 — Vercel Configuration Report

## Vercel Access Status

| Item | Status |
|---|---|
| Vercel CLI installed | ❌ No |
| Vercel CLI authenticated | ❌ No |
| `.vercel/project.json` in repo root | ❌ No |
| `.vercel/project.json` in `website/careervault/` | ❌ No |
| Can inspect project settings via CLI | ❌ No |
| Can modify project settings via CLI | ❌ No |

**Conclusion**: No programmatic Vercel access available. All configuration must be done via Vercel Dashboard by the repository owner.

## Required Vercel Project Settings

| Setting | Required Value | Current (Unknown) | Action Required |
|---|---|---|---|
| Git Repository | `khairanardurgesh-dev/careervault` | Unknown | Verify in Dashboard |
| Production Branch | `main` | Unknown | Set to `main` |
| Root Directory | `website/careervault` | **Likely incorrect** (default is repo root) | **MUST SET** to `website/careervault` |
| Framework Preset | Next.js | Unknown | Auto-detect or set Next.js |
| Build Command | `npm run build` | Unknown | Set to `npm run build` |
| Install Command | `npm ci` | Unknown | Set to `npm ci` |
| Output Directory | `.next` (default) | Unknown | Leave default |
| Node.js Version | 20.x LTS | Unknown | Set to 20.x |

## Critical: Root Directory Misconfiguration

The repository contains **two** Next.js projects:
1. `careervault/` — Default `create-next-app` starter (Next.js 16.4.6)
2. `website/careervault/` — Actual CareerVault application (Next.js 14.2.35)

The current live deployment at `https://careervault-dusky.vercel.app` serves the **starter template** from `careervault/`, confirming the Root Directory is either unset (repo root) or set to `careervault/`.

**Required Action**: In Vercel Dashboard → Project → Settings → General → Root Directory, set to `website/careervault`.

## Owner Action Checklist (Exact Steps)

1. Open Vercel Dashboard: https://vercel.com/dashboard
2. Select project `careervault` (or create new from GitHub repo `khairanardurgesh-dev/careervault`)
3. Go to **Settings** → **General**
4. Find **Root Directory** — change from empty/`careervault` to `website/careervault`
5. Go to **Settings** → **Build & Development**
   - Build Command: `npm run build`
   - Install Command: `npm ci`
   - Output Directory: leave default (`.next`)
6. Go to **Settings** → **Node.js Version** → Select `20.x`
7. Go to **Settings** → **Environment Variables** → Add all variables from Phase 3 (see below)
8. Go to **Deployments** → Trigger new Preview deployment from `main` branch
9. Verify deployment logs show `website/careervault` as build path

## Configuration Differences: Starter vs Actual App

| Aspect | `careervault/` (starter) | `website/careervault/` (actual) |
|---|---|---|
| Next.js Version | 16.4.6 | 14.2.35 |
| React Version | 19.3.0 | 18.3.1 |
| TypeScript | ^5 | 5.5.3 |
| Tailwind | 4.x (Turbopack) | 3.4.x (PostCSS) |
| ESLint | ^9 | ^8.57.0 |
| App Structure | `src/app/` | `app/` (App Router) |
| Pages | Default starter only | 19 pages + 4 API routes |
| Product | None | CareerVault complete system |

## Environment Variables Required

See Phase 3 report. All must be added in Vercel Dashboard → Settings → Environment Variables for **Preview** environment.

## Dashboard Verification Steps

After Root Directory fix, the next Preview deployment should show in build logs:

```
> Cloning repository...
> Checking out main...
> Detected Next.js in website/careervault
> Installing dependencies with npm ci...
> Running build: npm run build
> █ Next.js 14.2.35
> ✓ Compiled successfully
> ✓ Generating static pages (19/19)
```

If logs show `Detected Next.js in careervault` or `Next.js 16.x`, Root Directory is still wrong.
