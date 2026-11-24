# Task 012 Pre-Implementation Audit

## Current Implementation Status

### Checkout Route (app/api/checkout/route.tsx)
- Status: MOCK — uses placeholder Supabase client with fallback URLs
- Issues: No Razorpay order creation, no signature verification, no server-side price enforcement
- Required: Real Razorpay Orders API integration, server-side price loading, pending order creation

### Webhook Route (app/api/webhooks/route.tsx)
- Status: MOCK — signature verification always returns true
- Issues: No HMAC verification, no idempotency, no database updates
- Required: Raw body HMAC SHA256 verification, idempotent event processing

### Downloads Route (app/api/downloads/route.tsx)
- Status: MOCK — returns placeholder download URLs
- Issues: No authentication, no entitlement check, no signed URL generation
- Required: Server-side auth + entitlement verification + short-lived signed URLs

### Supabase Configuration
- Status: NOT CONFIGURED — no @supabase/supabase-js installed
- Issues: Fallback credentials used, no service role key handling
- Required: Real Supabase client with env validation

### Database Schema
- Status: NOT CREATED — no migration files exist
- Required: Full schema with RLS policies

### Environment Variables
- Status: .env.example exists with placeholders only
- Required: Complete configuration documentation

## Files to Create/Modify

### New Files
- lib/supabase.ts — Supabase client factory
- lib/razorpay.ts — Razorpay helper functions
- lib/env.ts — Environment validation
- migrations/001_initial_schema.sql — Database schema
- migrations/002_rls_policies.sql — RLS policies

### Modified Files
- app/api/checkout/route.tsx — Real order creation
- app/api/webhooks/route.tsx — Real signature verification
- app/api/downloads/route.tsx — Real authorization
- .env.example — Complete configuration

## Dependencies Required
- @supabase/supabase-js
- razorpay (optional, can use fetch)

## Risks
- No live Supabase/Razorpay credentials available for testing
- All integrations will be implemented but not live-verified

## Verification Method
- TypeScript type checking
- Unit tests with mocked providers
- Manual code review
- Documentation of external setup steps
