# CareerVault Phase Two - Security and QA Documentation

## 1. Security Checklist

### 1.1 Authentication & Access Control
- [ ] Supabase RLS policies active on all tables (orders, payments, entitlements, users)
- [ ] Row-level security prevents users from accessing other users' orders/data
- [ ] Magic link authentication flow tested: login → magic link → library access
- [ ] Non-purchasers cannot access product library
- [ ] Customer A cannot access Customer B's library
- [ ] Password reset/recovery flow does not expose other users' emails

### 1.2 Payment Security
- [ ] Razorpay secret key NEVER exposed in frontend bundles
- [ ] Razorpay signature verification implemented on all webhook endpoints
- [ ] Webhook signature verified using raw request body
- [ ] Idempotent webhook event processing (duplicate events handled safely)
- [ ] Payment status never trusted from browser; always verified server-side
- [ ] Order amount calculated from central product configuration, not from browser
- [ ] Razorpay test mode used for all development and testing
- [ ] Live payments only enabled after complete test-mode flow passes

### 1.3 File Delivery Security
- [ ] Product files never publicly accessible via permanent URLs
- [ ] Short-lived signed download URLs generated server-side
- [ ] Entitlement checks performed before generating download URLs
- [ ] Path traversal protection (validate storage keys, reject suspicious paths)
- [ ] File-type validation before download
- [ ] Complete ZIP delivery applies same entitlement checks as individual files
- [ ] Download events logged proportionally (no unnecessary personal data)

### 1.3 Input & Output Validation
- [ ] All API inputs validated (checkout form, webhook payloads)
- [ ] Output sanitised to prevent XSS
- [ ] Environment variables used for all secrets (no hardcoded keys)
- [ ] .env.example provided with placeholders only
- [ ] CSP (Content Security Policy) configured
- [ ] CSRF protection where relevant to implementation

### 1.4 Data Privacy
- [ ] No card details, CVVs, or UPI PINs stored anywhere
- [ ] Only minimal customer data: name, email, mobile (optional), order reference
- [ ] Download logs proportionate and privacy-conscious
- [ ] Customers can request data deletion via support email
- [ ] Cookie policy and consent where analytics are used

### 1.5 Admin Security
- [ ] Admin routes protected (authenticated sessions only)
- [ ] Admin cannot silently change payment status to "paid"
- [ ] Manual entitlement adjustments recorded with admin identity, reason, timestamp
- [ ] Admin cannot change another customer's entitlement status
- [ ] Audit logs for all administrative actions

## 2. Deployment Checklist

### 2.1 Environment Setup
- [ ] Production Supabase project configured
- [ ] Production Razorpay account with credentials
- [ ] Production domain verified with HTTPS
- [ ] Webhook URL pointed to production endpoint
- [ ] Transactional email domain verified with Resend/SendGrid
- [ ] Environment variables set in all environments (local, staging, production)
- [ ] .env.example created with placeholder values

### 2.2 Service Configuration
- [ ] Supabase:
  - [ ] Project created and configured
  - [ ] RLS policies written and tested
  - [ ] Database migrations run
  - [ ] Auth settings: magic link enabled, email templates configured
  - [ ] Storage bucket set up for product files with private access
- [ ] Razorpay:
  - [ ] Test mode credentials configured
  - [ ] Live mode credentials (pending)
  - [ ] Webhook endpoint registered and verified
  - [ ] Payment methods enabled (UPI, cards, netbanking)
- [ ] Email provider:
  - [ ] Resend or SendGrid account configured
  - [ ] Transactional templates: purchase confirmation, access email, payment pending, payment failure, product update
  - [ ] Sender domain verified

### 2.3 Vercel Deployment
- [ ] Production deployment on Vercel
- [ ] Custom domain configured with HTTPS
- [ ] Environment variables set in Vercel dashboard
- [ ] Preview deployments enabled for staging
- [ ] Redirects and rewrites configured for routing
- [ ] Edge config for performance optimization

### 2.3 Database & Migrations
- [ ] All Supabase migrations run in production
- [ ] Row-level security policies tested
- [ ] Indexes created for frequently queried fields
- [ ] Backup and recovery plan documented
- [ ] Database connection strings secured

## 3. Test Reports

### 3.1 Website Tests
- [ ] Homepage renders correctly on desktop, tablet, mobile
- [ ] Product page renders with all eight modules and six career tracks
- [ ] Pricing displayed correctly: ₹3,999 one-time payment
- [ ] Checkout validates required inputs (name, email)
- [ ] Mobile layouts work (burger menu, touch targets)
- [ ] Navigation works across all pages
- [ ] Legal pages (terms, privacy, refund-policy) load without errors
- [ ] Accessibility basics: heading hierarchy, alt text, color contrast

### 3.2 Payment Tests (Razorpay Test Mode)
- [ ] Successful payment flow: checkout → Razorpay → success redirect
- [ ] Failed payment flow: insufficient funds, card declined
- [ ] Cancelled checkout: user closes browser before payment
- [ ] Invalid signature: webhook rejects tampered payloads
- [ ] Duplicate webhook: idempotent processing, no double entitlements
- [ ] Delayed webhook: handled correctly without state corruption
- [ ] Browser closed after payment: verified payment still grants access
- [ ] Payment success with failed redirect: access granted via entitlement check
- [ ] Refund notification: webhook handled, entitlement reviewed

### 3.3 Portal Tests
- [ ] Valid purchaser can log in via magic link
- [ ] Non-purchaser cannot access product library (RLS test)
- [ ] Customer A cannot access Customer B's library (isolation test)
- [ ] Expired signed URL is rejected (403 or redirect to login)
- [ ] Valid download works: individual files open successfully
- [ ] ZIP opens successfully: all files present and not corrupted
- [ ] Individual files open: DOCX files readable, XLSX formulas work, PDFs render
- [ ] Returning customer can recover access via magic link
- [ ] Revoked entitlement cannot download protected files (403 or redirect)

### 3.4 Product Tests
- [ ] All eight modules present in portal and ZIP
- [ ] All six career tracks represented as specified
- [ ] Portal and ZIP contain matching versions (version number aligned)
- [ ] Filenames are readable and descriptive
- [ ] File sizes accurate in portal and ZIP
- [ ] No missing resources in ZIP
- [ ] No corrupted files in ZIP
- [ ] DOCX files open in Microsoft Word / LibreOffice
- [ ] XLSX formulas calculate correctly (salary calculator)
- [ ] PDFs render correctly (handbooks, checklists)

### 3.5 Security Tests
- [ ] No secret credentials in frontend bundles (grep audit)
- [ ] RLS policies work: non-admin users cannot query admin tables
- [ ] Admin routes protected: unauthenticated access redirected
- [ ] Webhook signatures verified: invalid signatures rejected
- [ ] Download endpoints check entitlement before serving files
- [ ] File storage is private: direct URL access returns 403
- [ ] Browser cannot manipulate product price (amount from config, not browser)

### 3.6 Edge Case Tests
- [ ] Payment completed but no access: entitlement check grants access
- [ ] Magic link not received: resend flow available
- [ ] Unable to download ZIP: retry support, customer support contact
- [ ] Corrupted or incomplete file: support request pathway
- [ ] Incorrect email entered during checkout: correction flow
- [ ] Product file compatibility: platform noted (Windows/Mac/Linux)
- [ ] Refund request: process documented, 7-day window enforced

## 4. Production Launch Checklist

### 4.1 Pre-Launch
- [ ] Domain verified and HTTPS active
- [ ] All environment variables configured in production
- [ ] Supabase RLS policies tested and active
- [ ] Razorpay test-mode flow passes completely
- [ ] Email templates tested (send test email to developer address)
- [ ] ZIP package integrity verified (all files present, not corrupted)
- [ ] Dashboard and portal access tested with test purchaser
- [ ] Support email configured and monitored
- [ ] Legal pages reviewed (no fabricated guarantees or claims)
- [ ] No critical security or payment issues outstanding

### 4.2 Launch Day
- [ ] Live deployment on Vercel with custom domain
- [ ] Live Razorpay credentials configured (small controlled transaction)
- [ ] First verified purchase recorded
- [ ] First access email sent
- [ ] First ZIP download successful
- [ ] Support team briefed on common issues
- [ ] Monitoring dashboard active (errors, failed payments, downloads)

### 4.3 Post-Launch (First 30 Days)
- [ ] Monitor payment success/failure rates
- [ ] Track download activity and edge cases
- [ ] Collect customer feedback on onboarding
- [ ] Review and update any content or policy discrepancies
- [ ] Weekly security review of logs
- [ ] Plan Phase Three features based on analytics

## 5. Risks and Unresolved Decisions

### 5.1 Known Risks
- **Razorpay integration dependent on merchant account approval**: Test mode used for development; live requires approved account
- **Supabase RLS policies require careful testing**: Minor misconfiguration could expose customer data
- **Email deliverability variable**: Spam filters may block transactional emails; fallback to manual support
- **ZIP file size**: Complete ZIP may be large (50-100MB); consider chunked download or streaming

### 5.2 Unresolved Decisions
- **Email provider**: Resend vs SendGrid vs AWS SES — decision based on cost, deliverability, and setup complexity
- **Admin auth method**: Supabase Auth magic link vs custom JWT-based admin session vs API key
- **Update policy detail**: Frequency and communication method for product version updates
- **Watermarking**: Whether to add discreet buyer email watermarks to PDF files (privacy vs usefulness)

## 6. Kilo Code Execution Notes

### 6.1 External Services
- No external service credentials embedded in code
- All secrets via environment variables with .env.example placeholders
- Development uses test mode for all payments and auth

### 6.2 Mock Data
- Frontend uses clearly labelled mock data where real API responses needed for UI
- Mock data never committed to appear as real customer data
- All real customer data flows through verified server-side endpoints

### 6.3 Build & Deploy
- `npm run build` must pass without errors
- `next start` must serve production build correctly
- Vercel deployment must use production environment variables
- No `console.log` statements in production-compiled code (or configured out)

### 6.4 Compliance
- No employment, salary, or interview success guarantees in copy
- All claims truthful and verifiable
- Refund policy clear and compliant with Indian consumer protection guidelines (as applicable)
- Privacy policy aligns with applicable data protection regulations