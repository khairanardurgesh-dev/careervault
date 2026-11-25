# TASK 016B — Build Test Report

## Environment

| Item | Value |
|---|---|
| OS | win32 |
| Node | `v24.18.0` |
| npm | `11.16.0` |
| App directory | `website/careervault` |
| Lockfile | `website/careervault/package-lock.json` (generated) |

## Commands and Results

### 1. Clean dependency installation

Command:

```
Remove-Item -Recurse -Force node_modules, .next
npm install --legacy-peer-deps --no-audit --no-fund
```

Result: **PASS** — `added 397 packages in 4m`. `package-lock.json` created.

### 2. Dependency tree

Command: `npm ls --depth=0`

Result: **PASS**

```
+-- @supabase/supabase-js@2.119.2
+-- @types/node@20.19.43
+-- @types/react-dom@18.3.7
+-- @types/react@18.3.32
+-- autoprefixer@10.7.0
+-- eslint-config-next@14.2.35
+-- eslint@8.57.1
+-- next@14.2.35
+-- postcss@8.5.33
+-- react-dom@18.3.1
+-- react@18.3.1
+-- tailwindcss@3.4.19
`-- typescript@5.5.3
```

### 3. TypeScript validation

Command: `npx tsc --noEmit`

Result: **PASS** — exit code `0`, no diagnostics.

### 4. ESLint

Command: `npm run lint` (`next lint`)

Result: **PASS** — `✔ No ESLint warnings or errors`, exit code `0`.

### 5. Production build

Command: `npm run build` (`next build`)

Result: **PASS** — exit code `0`.

Key output:

```
▲ Next.js 14.2.35
✓ Compiled successfully
Linting and checking validity of types ...
✓ Generating static pages (19/19)
Finalizing page optimization ...
Collecting build traces ...
```

Route summary:

```
○ /                              Static
○ /account/library               Static
○ /account/login                 Static
○ /account/settings              Static
○ /account/verify                Static
○ /admin/dashboard               Static
ƒ /api/checkout                  Dynamic
ƒ /api/downloads                 Dynamic
ƒ /api/webhooks                  Dynamic
○ /checkout                      Static
○ /contact                       Static
○ /faq                           Static
○ /how-it-works                  Static
○ /payment/failed                Static
○ /payment/success               Static
○ /privacy                       Static
○ /product                       Static
○ /refund-policy                 Static
○ /terms                         Static
```

First Load JS shared: `87.3 kB`.

## Blocked / Not Run

| Test | Status | Reason |
|---|---|---|
| Vercel deployment | NOT RUN | No Vercel access; out of scope for this task |
| Live Supabase/Razorpay/Resend E2E | BLOCKED | No credentials configured; test-only policy |
| Browser/responsive/console checks | NOT RUN | No deployment |
| `npm audit` | NOT RUN | `--no-audit` used during install; not required for build |

## Notes

- The Next.js 14.2.4 security warning is addressed by upgrading to 14.2.35 (latest 14.2.x patched release), a minimal compatible update; React 18.3.1 and TypeScript 5.5.3 were not changed.
- The `Unknown env config "cache-dir"` warning is not emitted by this project (no `.npmrc`); it originates from user/global npm configuration outside the repository.
- No TypeScript or ESLint checks were disabled, and no placeholder modules or mocks were added.
