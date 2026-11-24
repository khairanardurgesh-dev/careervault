# Task 012 Customer Access and Download Flow

## Authentication
- Email magic-link via Supabase Auth
- Session stored in cookies
- Protected routes check session server-side

## Customer Portal
- GET /api/downloads with Bearer token
- Server verifies user, finds customer, checks entitlements
- Returns list of available assets for entitled products

## Download Flow
1. Customer requests asset download → GET /api/downloads?assetId=xxx
2. Server verifies authentication token
3. Server finds customer, checks entitlement for asset's product
4. Server creates short-lived signed URL (5 min) from Supabase Storage
5. Server logs download event
6. Server returns signed URL to customer
7. Customer downloads from signed URL
