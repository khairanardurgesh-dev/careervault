# Task 012 Database Schema Reference

See migrations/001_initial_schema.sql for full schema.

## Tables
- customers: id, auth_user_id, email, full_name, created_at, updated_at
- products: id, slug, name, description, price_in_paise, currency, version, is_active, created_at, updated_at
- orders: id, customer_id, product_id, amount_in_paise, currency, status, payment_provider, razorpay_order_id, razorpay_payment_id, created_at, updated_at
- payment_events: id, provider, provider_event_id, event_type, processing_status, received_at, processed_at, error_reference
- entitlements: id, customer_id, product_id, order_id, status, granted_at, revoked_at, created_at (unique on customer_id, product_id)
- download_assets: id, product_id, asset_name, asset_path, asset_type, version, is_active, created_at, updated_at
- download_events: id, customer_id, asset_id, outcome, created_at
- email_events: id, customer_id, message_type, provider_message_id, send_status, attempt_timestamp, error_reference

## RLS
All customer-facing tables have RLS enabled. Customers can only read their own records. Payment events and download_assets have no direct customer access.
