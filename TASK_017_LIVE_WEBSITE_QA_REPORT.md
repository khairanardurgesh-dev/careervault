# TASK 017 — Live Website QA Report (Verification Checklist)

## Deployment Prerequisite

**No Preview URL exists yet.** This report documents the verification procedure to be executed once the owner deploys a Preview deployment.

## Preview URL
- **Expected format**: `https://careervault-<hash>.vercel.app` or `https://careervault-git-main-<user>.vercel.app`
- **To be filled after deployment**: `PREVIEW_URL = _______________`

## Test Matrix

### A. Marketing & Product Pages

| Page | URL Path | Desktop | Tablet | Mobile | Status |
|---|---|---|---|---|---|
| Homepage | `/` | ☐ | ☐ | ☐ | ⏳ |
| Product Details | `/product` | ☐ | ☐ | ☐ | ⏳ |
| How It Works | `/how-it-works` | ☐ | ☐ | ☐ | ⏳ |
| FAQ | `/faq` | ☐ | ☐ | ☐ | ⏳ |
| Contact | `/contact` | ☐ | ☐ | ☐ | ⏳ |
| Terms | `/terms` | ☐ | ☐ | ☐ | ⏳ |
| Privacy | `/privacy` | ☐ | ☐ | ☐ | ⏳ |
| Refund Policy | `/refund-policy` | ☐ | ☐ | ☐ | ⏳ |

**Verification Points**:
- [ ] CareerVault branding visible (logo, navy/electric color scheme)
- [ ] Hero section with "Your next career move deserves a better strategy"
- [ ] All 8 modules listed on `/product`
- [ ] Pricing shows ₹3,999 one-time payment
- [ ] Navigation links work
- [ ] CTAs navigate to `/checkout` and `/product`
- [ ] No layout overflow, text clipping, or broken images
- [ ] `electric-blue` links styled correctly

### B. Customer Experience

| Page | URL Path | Desktop | Tablet | Mobile | Status |
|---|---|---|---|---|---|
| Login | `/account/login` | ☐ | ☐ | ☐ | ⏳ |
| Account Verify | `/account/verify` | ☐ | ☐ | ☐ | ⏳ |
| Account Library | `/account/library` | ☐ | ☐ | ☐ | ⏳ |
| Account Settings | `/account/settings` | ☐ | ☐ | ☐ | ⏳ |
| Admin Dashboard | `/admin/dashboard` | ☐ | ☐ | ☐ | ⏳ |

**Verification Points**:
- [ ] Login form accepts email, shows "Continue" button
- [ ] Verify page shows success message with "Go to CareerVault" button
- [ ] Library shows 8 module cards with download buttons
- [ ] Settings shows purchase details + support links
- [ ] Admin dashboard shows stats cards (mock data)
- [ ] Protected routes redirect unauthenticated users (if auth implemented)

### C. Checkout Flow

| Step | URL Path | Desktop | Tablet | Mobile | Status |
|---|---|---|---|---|---|
| Checkout page load | `/checkout` | ☐ | ☐ | ☐ | ⏳ |
| Form validation | `/checkout` | ☐ | ☐ | ☐ | ⏳ |
| Razorpay modal opens | `/checkout` | ☐ | ☐ | ☐ | ⏳ |
| Test payment success | `/checkout` → Razorpay | ☐ | ☐ | ☐ | ⏳ |
| Payment success redirect | `/payment/success` | ☐ | ☐ | ☐ | ⏳ |
| Payment failure | `/payment/failed` | ☐ | ☐ | ☐ | ⏳ |

**Verification Points**:
- [ ] Checkout page loads without console errors
- [ ] Form requires Name + Email, Mobile optional
- [ ] Submit creates order via `/api/checkout` (check Network tab)
- [ ] Response contains: `razorpay_order_id`, `key_id`, `amount: 399900`, `currency: INR`
- [ ] Razorpay Checkout.js modal opens with correct prefill
- [ ] Test card: `4111 1111 1111 1111` / any future date / any CVV
- [ ] On success: client calls `/api/verify-payment` → redirects to `/payment/success`
- [ ] On cancel: modal `ondismiss` shows error message
- [ ] On failure: redirects to `/payment/failed`
- [ ] **No entitlement granted on client callback alone** — must verify via webhook

### D. Responsive Testing

| Viewport | Size | Pages Tested | Status |
|---|---|---|---|
| Mobile (iPhone SE) | 375×667 | Home, Product, Checkout, Library | ⏳ |
| Mobile (iPhone 12/13/14) | 390×844 | Home, Product, Checkout, Library | ⏳ |
| Tablet (iPad) | 768×1024 | Home, Product, Checkout, Library | ⏳ |
| Desktop (HD) | 1366×768 | All pages | ⏳ |
| Desktop (Full HD) | 1920×1080 | All pages | ⏳ |

**Check**: No horizontal scroll, touch targets ≥44px, text readable, navigation usable.

### E. Error Inspection

| Check | Tool | Expected | Status |
|---|---|---|---|
| Console errors | DevTools Console | Zero errors | ⏳ |
| Failed requests | Network tab | Zero 4xx/5xx (except expected) | ⏳ |
| Broken images | Network/Elements | None | ⏳ |
| Broken links | Manual click | None | ⏳ |
| API failures | Network tab | `/api/*` return 200/400/500 appropriately | ⏳ |
| Auth failures | Network + Application | No unexpected 401/403 | ⏳ |

## Test Results Template (Fill After Deployment)

```
PREVIEW_URL: _______________
DEPLOYMENT_COMMIT: _______________
TEST_DATE: _______________
TESTER: _______________

PAGES_PASS: ___ / 17
CHECKOUT_PASS: ___ / 7
RESPONSIVE_PASS: ___ / 5
ERRORS_FOUND: ___
BLOCKERS: _______________
```

## Notes

- All tests require **Razorpay test mode** credentials configured
- Supabase test project must be connected
- Download functionality requires storage bucket + signed URLs
- Admin dashboard shows mock data (no real backend yet)
