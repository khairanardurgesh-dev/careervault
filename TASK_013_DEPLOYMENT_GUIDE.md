# Task 013 Deployment Guide

## 1. Required Accounts
| Account | Purpose | Required Before Launch |
|---------|---------|------------------------|
| Supabase | Database, auth, storage | Yes |
| Razorpay | Payment processing | Yes |
| Resend | Transactional email | Yes |
| Vercel | Hosting (recommended) | Yes |
| Domain | Production URL | Yes |

## 2. Required Environment Variables

### Supabase
```
NEXT_PUBLIC_SUPABASE_URL=https://your-project.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-anon-key
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key
```

### Razorpay
```
RAZORPAY_KEY_ID=rzp_test_xxxxx (or rzp_live_...)
RAZORPAY_KEY_SECRET=your-secret
RAZORPAY_WEBHOOK_SECRET=your-webhook-secret
```

### Resend (Email)
```
RESEND_API_KEY=re_xxxxx
EMAIL_FROM=noreply@yourdomain.com
EMAIL_REPLY_TO=support@yourdomain.com
```

## 3. Supabase Setup
1. Create Supabase project
2. Run migration: `website/careervault/migrations/001_initial_schema.sql`
3. Create storage bucket: `careervault-products` (private)
4. Upload product assets (ZIP and individual modules)
5. Enable RLS (already defined in migration)
6. Configure Auth: Email magic-link provider
7. Set authorized redirect URLs

## 4. Razorpay Setup
1. Create Razorpay merchant account
2. Generate test API keys
3. Configure webhook URL: `https://yourdomain.com/api/webhooks`
4. Webhook events: payment.captured, payment.failed, order.created, payment.refunded
5. Switch to live mode before production launch

## 5. Resend Setup
1. Create Resend account
2. Verify sender domain
3. Create API key
4. Verify EMAIL_FROM address

## 6. Deployment Process (Vercel)
1. Connect Git repository to Vercel
2. Add all environment variables in Vercel dashboard
3. Deploy project
4. Verify build succeeds
5. Test API routes on deployed URL
6. Configure Razorpay webhook to point to deployed URL
7. Run smoke tests

## 7. Smoke Tests
- [ ] Homepage loads
- [ ] Product page loads
- [ ] Checkout page loads
- [ ] Customer login page loads
- [ ] API health check
- [ ] Checkout API returns order
- [ ] Webhook API accepts requests
- [ ] Download API requires auth

## 8. Rollback Procedure
1. Revert Vercel deployment to previous commit
2. Do not run destructive database migrations
3. Verify Razorpay webhook points to previous URL
4. Monitor error logs

## 9. Live Payment Activation
- [ ] All test-mode scenarios verified
- [ ] Owner approval obtained
- [ ] Switch Razorpay to live mode
- [ ] Update Razorpay keys to live keys
- [ ] Verify first live transaction
- [ ] Monitor for 24 hours

## 10. Do Not
- [ ] Do not deploy without explicit approval
- [ ] Do not activate live payments without explicit approval
- [ ] Do not spend money on services without explicit approval
- [ ] Do not commit real credentials to repository
