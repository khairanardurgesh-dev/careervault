# Task 012 Integration Setup Guide

## Required External Services

### 1. Supabase
1. Create a Supabase project at supabase.com
2. Run migration: migrations/001_initial_schema.sql
3. Create storage bucket: careervault-products (private)
4. Set environment variables: NEXT_PUBLIC_SUPABASE_URL, NEXT_PUBLIC_SUPABASE_ANON_KEY, SUPABASE_SERVICE_ROLE_KEY

### 2. Razorpay
1. Create account at razorpay.com
2. Get test API keys from Dashboard
3. Set up webhook URL: https://yourdomain.com/api/webhooks
4. Set environment variables: RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET, RAZORPAY_WEBHOOK_SECRET

### 3. Resend (Email)
1. Create account at resend.com
2. Verify domain
3. Set environment variables: RESEND_API_KEY, EMAIL_FROM, EMAIL_REPLY_TO

## Deployment
1. Deploy to Vercel
2. Set all environment variables in Vercel dashboard
3. Run database migration on Supabase
4. Upload product assets to storage bucket
5. Configure Razorpay webhook
6. Test with Razorpay test mode
