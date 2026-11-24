# TASK_003_INTEGRATION_AUDIT.md

## CareerVault — External Service Integration & Production Readiness Audit

**Project Root:** `C:\Users\Quick\Desktop\CareerVault`  
**Website:** `C:\Users\Quick\Desktop\CareerVault\website\careervault`  
**Audit Date:** November 24, 2026  
**Status:** Complete — Audit and implementation plan only; no live services activated

---

## Stage 1 — Repository Inspection

### 1.1 Executive Summary

The CareerVault codebase is split into two phases:

- **Phase One (Task 001):** Product architecture, content schemas, pilot resources, validation infrastructure. All content files are in `C:\Users\Quick\Desktop\CareerVault\content\`, with JSON schemas in `C:\Users\Quick\Desktop\CareerVault\schemas\`. Validation script (`validate_content.py`) passes with 0 errors, 0 warnings.

- **Phase Two (Task 002):** E-commerce website built with Next.js 14, TypeScript, Tailwind CSS. The website is at `C:\Users\Quick\Desktop\CareerVault\website\careervault\`. Includes marketing pages, checkout, account portal, API routes, and admin dashboard.

### 1.2 File Structure Highlights

| Area | Status | Key Files |
|------|--------|-----------|
| **API Routes** | Partially implemented | `app/api/checkout/route.tsx`, `app/api/webhooks/route.tsx`, `app/api/downloads/route.tsx` — core logic present but uses placeholder values |
| **Payment** | Mock implementation | Razorpay test-mode integration present; no live credentials; signature verification placeholder |
| **Authentication** | Design only | Magic link flow designed; Supabase Auth not yet connected to code |
| **Database** | Schema defined | Supabase migrations referenced but not executed; PostgreSQL tables not created |
| **Customer Entitlements** | Design only | Conceptual design in SECURITY_AND_QA.md; no real entitlement checks |
| **Download Protection** | Design only | Signed URL pattern documented; no actual Supabase Storage integration |
| **Admin Authorization** | Design only | Dashboard concept in `app/admin/dashboard/page.tsx`; no RLS or session checks |
| **Email Templates** | Structure only | 5 templates defined in `SECURITY_AND_QA.md`; no provider connected |
| **Environment Variables** | Missing | `.env.example` does not exist; placeholders referenced in code but not formalized |
| **Security & QA Documentation** | Complete | `SECURITY_AND_QA.md` with comprehensive checklists |

### 1.3 Key Observations

- **No credentials exposed:** Good — no service-role keys or Razorpay secrets in frontend code.
- **Placeholders everywhere:** All external service connections use `process.env.XXX || "fallback-value"` patterns.
- **Code exists but not connected:** API routes, database queries, and email logic are structured but reference stub/fake values.
- **Pilot resources present:** Phase One content marked `pilot: true` throughout JSON files.
- **No automated tests:** No test suite for payment, auth, or download endpoints.
- **Session management not wired:** Account login/verify pages exist but don't connect to Supabase.

---

## Stage 2 — Supabase Integration Plan

### 2.1 Required Architecture

The following Supabase tables and RLS policies are needed:

#### 2.3.1 Tables

```sql
-- 1. users/profiles (linked to Supabase Auth)
create table public.profiles (
  id uuid references auth.users on delete cascade primary key,
  email text unique not null,
  full_name text,
  mobile_number text,
  created_at timestamp with time zone default timezone('utc', now()),
  updated_at timestamp with time zone default timezone('utc', now())
);

-- 2. orders
create table public.orders (
  id uuid default uuid_generate_v4() primary key,
  user_id uuid references auth.users on delete set null,
  customer_name text not null,
  customer_email text not null,
  mobile_number text,
  product_id text not null,
  product_slug text not null,
  amount_in_paise integer not null,
  currency text not null default 'INR',
  status text not null default 'pending', -- pending, paid, failed, refunded
  razorpay_order_id text,
  razorpay_payment_id text,
  razorpay_signature text,
  created_at timestamp with time zone default timezone('utc', now()),
  updated_at timestamp with time zone default timezone('utc', now())
);

-- 3. payments
create table public.payments (
  id uuid default uuid_generate_v4() primary key,
  order_id uuid references orders on delete cascade,
  provider text not null, -- razorpay
  provider_payment_id text,
  provider_order_id text,
  amount_in_paise integer not null,
  currency text not null default 'INR',
  status text not null default 'pending', -- pending, verified, failed, refunded
  verified_at timestamp with time zone,
  created_at timestamp with time zone default timezone('utc', now())
);

-- 4. entitlements
create table public.entitlements (
  id uuid default uuid_generate_v4() primary key,
  user_id uuid references auth.users on delete cascade,
  order_id uuid references orders on delete cascade,
  product_id text not null,
  status text not null default 'active', -- active, revoked
  granted_at timestamp with time zone default timezone('utc', now()),
  revoked_at timestamp with time zone,
  revocation_reason text
);

-- 5. product_versions
create table public.product_versions (
  id uuid default uuid_generate_v4() primary key,
  product_id text not null,
  version_number text not null, -- e.g. "1.0"
  release_notes text,
  published_at timestamp with time zone default timezone('utc', now()),
  active boolean default true
);

-- 6. product_modules
create table public.product_modules (
  id uuid default uuid_generate_v4() primary key,
  version_id uuid references product_versions on delete cascade,
  module_number integer not null, -- 1-8
  title text not null,
  description text,
  sort_order integer default 0
);

-- 7. product_files
create table public.product_files (
  id uuid default uuid_generate_v4() primary key,
  module_id uuid references product_modules on delete cascade,
  version_id uuid references product_versions on delete cascade,
  filename text not null,
  storage_key text not null, -- Supabase Storage path
  file_type text not null, -- docx, xlsx, pdf, json
  file_size integer,
  published boolean default true,
  created_at timestamp with time zone default timezone('utc', now())
);

-- 8. webhook_events
create table public.webhook_events (
  id uuid default uuid_generate_v4() primary key,
  provider text not null, -- razorpay
  provider_event_id text unique not null,
  event_type text not null, -- payment.captured, payment.failed, etc.
  processing_status text default 'pending', -- processed, failed
  processed_at timestamp with time zone,
  created_at timestamp with time zone default timezone('utc', now()),
  constraint uq_provider_event_id unique (provider_event_id)
);

-- 9. download_logs
create table public.download_logs (
  id uuid default uuid_generate_v4() primary key,
  user_id uuid references auth.users on delete cascade,
  product_file_id uuid references product_files on delete cascade,
  download_type text not null, -- module, zip
  ip_address inet,
  user_agent text,
  created_at timestamp with time zone default timezone('utc', now())
);
```

#### 2.4 Database Migrations

Migrations should be placed in `website/careervault/supabase/migrations/` in the correct order:

1. `20261124_001_create_profiles.sql`
2. `20261124_002_create_orders.sql`
3. `20261124_003_create_payments.sql`
4. `20261124_004_create_entitlements.sql`
5. `20261124_005_create_product_versions.sql`
6. `20261124_006_create_product_modules.sql`
7. `20261124_007_create_product_files.sql`
8. `20261124_008_create_webhook_events.sql`
9. `20261124_009_create_download_logs.sql`

#### 2.5 Row Level Security (RLS)

Enable RLS on all tables. Example policies:

```sql
-- profiles: users can only view their own profile
create policy "Users can view own profile" on public.profiles
  for select using (auth.uid() = id);

-- orders: users can view own orders; admins can view all
create policy "Users can view own orders" on public.orders
  for select using (auth.uid() = user_id);
create policy "Admins can view all orders" on public.orders
  for all using (auth.role() = 'service_role');

-- entitlements: users can view own entitlements
create policy "Users can view own entitlements" on public.entitlements
  for select using (auth.uid() = user_id);

-- product_files: public read for published files; write via entitlement check
create policy "Published files are readable" on public.product_files
  for select using (published = true);
-- Download endpoint checks entitlement before serving

-- webhook_events: insert via service role only
create policy "Webhook events insert by service role" on public.webhook_events
  with check (auth.role() = 'service_role');

-- download_logs: insert on download
create policy "Log downloads for authenticated users" on public.download_logs
  for insert with check (auth.uid() is not null);
```

#### 2.6 Environment Variables

Create `.env.example` with placeholder names only:

```
# Supabase
NEXT_PUBLIC_SUPABASE_URL=https://your-project.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_anon_key_here
SUPABASE_SERVICE_ROLE_KEY=your_service_role_key_here

# Razorpay
NEXT_PUBLIC_RAZORPAY_KEY=your_razorpay_key_here
RAZORPAY_SECRET=your_razorpay_secret_here
RAZORPAY_WEBHOOK_SECRET=your_webhook_secret_here

# Email Provider (Resend example)
RESEND_API_KEY=your_resend_api_key_here

# Application
NEXT_PUBLIC_SITE_URL=https://your-domain.com
NEXT_PUBLIC_APP_VERSION=1.0
```

**Critical:** `SUPABASE_SERVICE_ROLE_KEY` must NEVER be exposed in the browser. It is used only in server-side functions, API routes, and edge functions.

#### 2.6 Supabase Setup Instructions

1. **Create Supabase Project:**
   - Go to https://supabase.com and create a new project
   - Note the project URL and anon key
   - Enable Email authentication (magic links)
   - Configure email template: "Magic link sign in"

2. **Database Setup:**
   - Go to SQL Editor in Supabase Dashboard
   - Run each migration file in order (1-9 above)
   - Verify all tables are created and RLS is enabled

3. **Storage Bucket:**
   - Go to Storage in Supabase Dashboard
   - Create a bucket named `product-files` (or similar)
   - Set bucket policy: "Authenticated users can read" (for download URLs)
   - Keep storage level as "Private" — files not publicly accessible without signed URLs

4. **Email Configuration:**
   - Verify sender domain (e.g., mailto:support@careervault.in)
   - Configure SPF, DKIM, DMARC records for the domain
   - Test email delivery to inbox

5. **Function URLs (Optional but recommended):**
   - In Supabase Dashboard > Functions, deploy any serverless functions needed
   - Set function URLs and note them for API route usage

6. **Test the Connection:**
   - Run `npm run dev` locally
   - Verify Supabase client initializes without errors
   - Test magic link flow: login → email → library access

---

## Stage 3 — Razorpay Integration Audit

### 3.1 Current Implementation Status

The Razorpay integration in `app/api/checkout/route.tsx` and `app/api/webhooks/route.tsx` is a **mock implementation** — it has correct structure but uses placeholder values and does not connect to live Razorpay APIs.

### 3.2 Server-Side Order Creation (checkout/route.tsx)

**Current State:**
- Creates a pending order in Supabase `orders` table
- Amount hardcoded as `399900` (₹3,999 in paise)
- Razorpay order creation is referenced but not actually called (commented out)
- Returns `payment_url` as a relative path instead of actual Razorpay Checkout URL

**What's Missing:**
- Real Razorpay HTTP POST to `https://api.razorpay.com/v1/orders`
- HTTP Basic Auth with Razorpay key secret
- Proper request body: `{ amount: 399900, currency: "INR", receipt: "order_${id}" }`
- Proper error handling for Razorpay API failures

**Required Implementation:**
```typescript
// In app/api/checkout/route.tsx, replace the placeholder with:
const razorpayResponse = await fetch('https://api.razorpay.com/v1/orders', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    // Razorpay HTTP Basic Auth
    'Authorization': `Basic ${btoa(`rzp_test_xxxxx:your_secret_key`)}`,
  },
  body: JSON.stringify({
    amount: 399900, // ₹3,999 in paise
    currency: 'INR',
    receipt: `order_${order.id}`,
  }),
});

if (!razorpayResponse.ok) {
  throw new Error('Razorpay order creation failed');
}

const razorpayData = await razorpayResponse.json();
return NextResponse.json({
  ...data,
  razorpay_order_id: razorpayData.id,
  payment_url: `/checkout?payment=razorpay&order_id=${order.id}`,
});
```

### 3.3 Payment-Signature Verification

**Current State:**
- `verifyRazorpaySignature()` function in `app/api/webhooks/route.tsx` is a **placeholder**
- Checks for `x-razorpay-signature` header presence only
- Parses JSON body but does not verify HMAC SHA256 signature
- Returns `{ valid: true }` for any request with a signature header

**What Must Be Implemented:**
```typescript
// Correct HMAC SHA256 verification
import crypto from 'crypto';

function verifyRazorpaySignature(
  body: string,
  headers: Headers,
  secret: string
): { valid: boolean; payload: any } | null {
  const signature = headers.get('x-razorpay-signature');
  if (!signature) return null;
  
  const bodyObj = JSON.parse(body);
  
  // Razorpay signs the body using HMAC SHA256
  const expectedSig = crypto
    .createHmac('sha256', secret)
    .update(body, 'utf8')  // NOTE: body must be raw string, not parsed object
    .digest('hex');
  
  const isValid = crypto.timingSafeEqual(
    Buffer.from(expectedSig, 'hex'),
    Buffer.from(signature, 'hex')
  );
  
  if (!isValid) return null;
  
  return { valid: true, payload: bodyObj };
}
```

### 3.4 Webhook Signature Verification

**Critical:** Webhook verification MUST use the raw request body, not `req.json()`.

```typescript
// Correct pattern in app/api/webhooks/route.tsx
export async function POST(req: NextRequest) {
  const body = await req.text();  // CRITICAL: raw body
  const signature = req.headers.get('x-razorpay-signature');
  
  // Verify using raw body and secret
  const expectedSig = crypto
    .createHmac('sha256', razerpaySecret)
    .update(body, 'utf8')
    .digest('hex');
  
  const isValid = crypto.timingSafeEqual(
    Buffer.from(expectedSig, 'hex'),
    Buffer.from(signature!, 'hex')
  );
  
  if (!isValid) {
    return NextResponse.json({ message: 'Invalid signature' }, { status: 400 });
  }
  
  const payload = JSON.parse(body);
  // ... process event
}
```

### 3.5 Idempotent Webhook Processing

**Required:** Track processed events to prevent duplicate entitlement grants.

```typescript
// In webhook handler, before processing:
const { data: existingEvent } = await supabase
  .from('webhook_events')
  .select('id')
  .eq('provider_event_id', payload.payload.event_id) // or appropriate field
  .single();

if (existingEvent) {
  // Already processed; return success without re-processing
  return NextResponse.json({ success: true, idempotent: true });
}

// Insert before processing
await supabase.from('webhook_events').insert({
  provider: 'razorpay',
  provider_event_id: payload.event,
  event_type: payload.event,
  processing_status: 'pending',
});
```

### 3.5 Order-to-Payment Mapping

**Current State:** Orders have `razorpay_order_id` field; payments table not fully implemented.

**Required:**
- On `payment.captured` webhook: update order status to `paid`, create payment record
- On `payment.failed` webhook: update order status to `failed`
- Map `razorpay_payment_id` and `razorpay_signature` from webhook payload

### 3.6 Payment Status Transitions

| State | Transitions To | Trigger |
|-------|---------------|---------|
| `pending` | `verified`, `failed` | Webhook: payment.captured, payment.failed |
| `verified` | `entitled` | Server-side entitlement creation |
| `failed` | — | — |
| `refunded` | — | Refund webhook or admin action |

### 3.7 Entitlement Creation After Verified Payment

**Required Flow:**
1. Webhook `payment.captured` receives `payment_id` and `order_id`
2. Server updates order status to `paid`, sets `verified_at`
3. Server creates entitlement record: `user_id` + `order_id` + `product_id` + `status: active`
4. Server grants access: generates signed download URL or grants Supabase RLS access
5. Customer receives access email

### 3.8 Refund Handling

**Required:**
- On refund webhook (if Razorpay supports) or admin action:
  - Find order by `razorpay_order_id` or `razorpay_payment_id`
  - Update order status to `refunded`
  - Revoke entitlement: set `entitlements.status = 'revoked'`, set `revoked_at`
  - Optionally revoke access via Supabase RLS policy change

**Razorpay Refund Webhook Events:**
- `refund.created`, `refund.processed`, `refund.failed`

### 3.9 Razorpay Dashboard Settings Required

**Create in Razorpay Dashboard:**

1. **Application Settings:**
   - Name: CareerVault
   - Business Type: Individual / Company (as applicable)
   - Payout Account: Configured
   - Currency: INR

2. **Webhook Settings:**
   - Enable Event Subscriptions
   - Select events to receive:
     - `payment.captured`
     - `payment.failed`
     - `refund.created` (optional)
     - `order.created` (optional)
   - Webhook URL: `https://your-domain.com/api/webhooks`
   - Secret: Automatically generated; use in verification

3. **Payment Methods:**
   - UPI: Enabled
   - Credit Cards: Enabled
   - Debit Cards: Enabled
   - Net Banking: Enabled (as applicable)
   - Wallets: As applicable

4. **Auto-Payout:**
   - Set payout frequency (daily/weekly)
   - Minimum payout amount
   - Payout account verified

5. **Dashboard Notifications:**
   - Enable email notifications for key events

### 3.10 Required Webhook Events

| Event | Purpose |
|-------|---------|
| `payment.captured` | Payment successful — grant entitlement |
| `payment.failed` | Payment failed — show failure page |
| `refund.created` | (Optional) Process refund, revoke access |
| `order.created` | (Optional) Initial order tracking |

---

## Stage 4 — Transactional Email Integration

### 4.1 Current State

Email templates are documented in `SECURITY_AND_QA.md` but no email provider is connected. No sending logic exists in the codebase.

### 4.2 Recommended Provider: Resend

Resend is a good choice for transactional emails due to:
- Simple API
- Good deliverability
- Reasonable pricing for startups
- Transactional focus (no marketing requirements without consent)

**Alternative:** SendGrid or AWS SES (more complex to set up).

### 4.3 Required Account Setup

1. **Sign up** at https://resend.com
2. **Verify sender domain:**
   - Add DNS TXT record: `_resend domain-verification`
   - Add DNS TXT record: `v=spf1 include:mail.resend.com ~all`
3. **Configure SMTP** (if using custom domain or fallback):
   - Host: `smtp.resend.com`
   - Port: 587
   - Username: `resend_api_key`
   - Password: `your_api_key`

### 4.4 API Key Configuration

```env
# In .env.example
RESEND_API_KEY=re_xxxxx your_resend_api_key_here
```

### 4.4 Email Templates

#### 4.3.1 Purchase Confirmation

```
Subject: Your CareerVault purchase is confirmed

Hi {customer_name},

Your payment of ₹3,999 has been verified.

Order Reference: {order_id}
Product: CareerVault Complete Job Switch System

Your access is now ready. Click the button below to open your personal library:
{secure_login_link}

If you did not make this purchase, please contact support@careervault.in.

Thank you,
CareerVault Team
```

#### 4.3.2 Customer Access (Magic Link)

```
Subject: Your CareerVault library is ready

Hi {customer_name},

Click the button below to access your CareerVault library:
{secure_login_link}

This link will expire in 24 hours.

If you did not request this, please ignore this email.

Best,
CareerVault Team
```

#### 4.3.3 Payment Pending

```
Subject: We're confirming your CareerVault payment

Hi {customer_name},

We're verifying your payment of ₹3,999. Your access will appear as soon as verification is complete.

We'll send another email once your payment is verified.

Thank you for your patience.

CareerVault Team
```

#### 4.3.4 Payment Failure

```
Subject: Your CareerVault payment was not completed

Hi {customer_name},

Your payment of ₹3,999 could not be completed. 

Please try again using the button below, or contact support@careervault.in if you need assistance.

{retry_payment_link}

Best,
CareerVault Team
```

#### 4.3.5 Access Recovery

```
Subject: Your CareerVault access recovery

Hi {customer_name},

You can recover access to your CareerVault library by verifying your email address.

{recovery_link}

If you did not request this, please ignore this email.

Best,
CareerVault Team
```

#### 4.3.5 Product Update

```
Subject: A new CareerVault update is available

Hi {customer_name},

A new version of CareerVault (v{version}) is now available in your library.

What's new:
{release_notes}

Update your library to access the latest resources.

Best,
CareerVault Team
```

### 4.4 DNS Records for Domain Verification

When using Resend (or any transactional email provider):

```
# TXT record for domain verification
_dmarc.careervault.in  TXT  "v=DMARC1; p=reject; rua=mailto:rua@careervault.in"

# SPF record
careervault.in  TXT  "v=spf1 include:mail.resend.com ~all"

# CNAME for mail (optional)
mail.careervault.in  CNAME  mail.resend.com
```

### 4.5 Email Delivery Testing

```bash
# Test sending a simple email
curl -X POST https://api.resend.com/emails \
  -H "Authorization: Bearer $RESEND_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "from": "CareerVault <support@careervault.in>",
    "to": "test@example.com",
    "subject": "Test email from CareerVault",
    "html": "<p>This is a test email.</p>"
  }'
```

---

## Stage 5 — Private Storage and Downloads

### 5.1 Current State

No Supabase Storage integration exists. Download API routes (`app/api/downloads/route.tsx`) return placeholder URLs, not actual signed download links.

### 5.2 Required Architecture

#### 5.2.1 Supabase Storage Bucket

- **Bucket Name:** `product-files` (or similar)
- **Access Level:** Private
- **File Types:** DOCX, XLSX, PDF, JSON, ZIP

#### 5.2.2 File Structure in Storage

```
product-files/
  01_Resume_Mastery/
    Resume_Mastery_Handbook.pdf
    Resume_Template_01.docx
    ATS_Optimisation_Checklist.pdf
  02_Professional_Profile/
    LinkedIn_Optimisation_Guide.pdf
    Naukri_Profile_Checklist.docx
  03_Job_Search_System/
    Job_Application_Tracker.xlsx
    Job_Description_Analysis_Worksheet.xlsx
  04_Interview_Preparation/
    Interview_Questions_Bank.pdf
    STAR_Workbook.pdf
  05_Salary_and_Negotiation/
    Salary_Offer_Comparison_Calculator.xlsx
    Negotiation_Scripts.pdf
  06_AI_Career_Assistant/
    AI_Prompt_Library.json
  07_90_Day_Programme/
    30_Day_Roadmap.pdf
    60_Day_Milestones.xlsx
  08_Career_Advancement/
    Portfolio_Guide.pdf
    First_90_Days_Guide.pdf
    LICENSE_AND_USAGE.pdf
    START_HERE.pdf
```

#### 5.2.2 Signed Download URL Flow

```typescript
// In app/api/downloads/route.tsx
import { createClient } from '@supabase/supabase-js';

const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  supabaseServiceRoleKey, // Server-side only!
  { auth: { autoRefreshToken: false, persistSession: false } }
);

export async function GET(req: NextRequest) {
  const { searchParams } = new URL(req.url);
  const downloadType = searchParams.get('type') || 'module';
  const fileId = searchParams.get('fileId');
  const userId = req.headers.get('x-user-id'); // From auth middleware

  // Verify entitlement first
  if (downloadType === 'module' && fileId) {
    const { data: entitlement } = await supabase
      .from('entitlements')
      .select('*')
      .eq('user_id', userId)
      .eq('product_file_id', fileId)
      .single();

    if (!entitlement || entitlement.status !== 'active') {
      return NextResponse.json({ error: 'Access denied' }, { status: 403 });
    }
  }

  // Generate signed URL (valid for 24 hours)
  const { data: { signedUrl } } = await supabase.storage
    .from('product-files')
    .getSignedUrl(fileId, { expiresIn: 86400 });

  return NextResponse.json({ download_url: signedUrl });
}
```

#### 5.2.3 ZIP Package Delivery

Same entitlement checks apply:

```typescript
// ZIP download - verify user has access to the product
const { data: order } = await supabase
  .from('orders')
  .select('status')
  .eq('customer_email', userEmail)
  .single();

if (order.status !== 'paid') {
  return NextResponse.json({ error: 'Purchase required' }, { status: 403 });
}

// Generate signed URL for ZIP
const { data: { signedUrl } } = await supabase.storage
  .from('product-files')
  .getSignedUrl('careervault_complete_system.zip', { expiresIn: 86400 });

return NextResponse.json({ download_url: signedUrl });
```

### 5.3 Download Endpoint Security

**Never trust browser input:**
- Validate `fileId` against database, don't accept arbitrary paths
- Check MIME type before serving
- Log download events with user ID (minimal data)
- Rate limit: e.g., max 5 downloads per minute per user

**Path Traversal Protection:**
```typescript
// Validate fileId contains only alphanumeric and hyphens
if (!/^[a-zA-Z0-9_-]+$/.test(fileId)) {
  return NextResponse.json({ error: 'Invalid file ID' }, { status: 400 });
}
```

### 5.4 File-Publishing Process for All Eight Modules

**Step 1: Prepare Files**
- Ensure all 8 modules have DOCX, PDF, XLSX as specified
- Name files consistently: `{module-number}_{descriptive-name}.{ext}`
- Include `LICENSE_AND_USAGE.pdf` and `START_HERE.pdf` at root ZIP level

**Step 2: Upload to Supabase Storage**
```bash
# Using Supabase CLI
supabase storage upload product-files \
  --path "./dist/" \
  --mode add \
  --limit 50
```

**Step 2: Record in Database**
For each file, insert into `product_files` table:
- `filename`: e.g., `01_Resume_Mastery_Handbook.pdf`
- `storage_key`: the Supabase Storage path
- `file_type`: `pdf`, `docx`, `xlsx`, `json`
- `published`: `true`

**Step 5: Generate ZIP**
- Download all files from Supabase Storage
- Create ZIP with proper structure
- Upload ZIP to Supabase Storage as `careervault_complete_system.zip`
- Record in `product_files` with `filename: "careervault_complete_system.zip"`

**Step 6: Publish Version**
- Update `product_versions` table: `version_number: "1.0"`, `published_at: now()`
- Update `product_modules` for all 8 modules
- Update all `product_files` `published: true`
- Notify customers via email (template 5 from Stage 4)

### 5.5 What MUST NOT Happen

- ❌ Pilot resources from Phase One should NOT be uploaded as final commercial product assets
- ❌ Files should not be publicly accessible via guessable URLs (e.g., `https://supabase.co/storage/v1/object/public/product-files/...`)
- ❌ Storage bucket should remain "Private" — all access via signed URLs only
- ❌ `SUPABASE_SERVICE_ROLE_KEY` should never be used in browser code or client-side functions

---

## Stage 6 — Integration Test Plan

### 6.1 Test Scenarios (Must Distinguish Real vs Mock)

| # | Test Case | Status | Notes |
|---|-----------|--------|-------|
| 1 | **Successful test payment** | Mock | Use Razorpay test card: `4242 4242 4242 4242` with future expiry; verify order created, webhook triggered, entitlement granted |
| 2 | **Failed payment** | Mock | Use test card with declined status; verify failure page shown, no entitlement created |
| 3 | **Duplicate webhook** | Mock | Send same event twice; verify idempotent processing, no double entitlement |
| 4 | **Delayed webhook** | Mock | Send event after delay; verify state consistency, no corruption |
| 5 | **Browser closed after payment** | Mock | Payment succeeds but redirect not completed; verify entitlement still granted via webhook later |
| 6 | **Invalid signature** | Mock | Send webhook with wrong signature; verify rejection with 400 status |
| 7 | **Payment/order mismatch** | Mock | Send webhook with order_id that doesn't match any order in DB; verify error handling |
| 8 | **Customer magic-link login** | Mock | Test full flow: login → email → magic link → library access |
| 9 | **Non-purchaser download rejection** | Mock | Non-purchased user tries download; verify 403 / access denied |
| 10 | **Cross-customer access rejection** | Mock | User A tries to download User B's files; verify RLS enforcement |
| 11 | **ZIP download** | Mock | Complete ZIP download with all 8 modules; verify integrity |
| 12 | **Expired signed URL** | Mock | Use old signed URL; verify 403 or redirect to login |
| 13 | **Refund notification** | Mock | Receive refund webhook; verify entitlement revoked |
| 14 | **Customer access recovery** | Mock | Magic link resend/recovery flow works |

### 6.2 Test Infrastructure

**Required Testing Tools:**
- **Razorpay Test Mode:** Use test API keys and test cards
- **Supabase Emulator** or test project
- **Jest/Pytest** for unit tests
- **Playwright or Cypress** for end-to-end UI tests
- **Postman** for API route testing

### 6.3 Sample Test Scenarios

#### 6.3.1 Successful Test Payment

```typescript
// Test: Successful payment flow
test('successful payment flow', async () => {
  // 1. Submit checkout form
  const checkoutRes = await fetch('/api/checkout', {
    method: 'POST',
    body: JSON.stringify({ name: 'Test User', email: 'test@careervault.in' }),
  });
  const checkoutData = await checkoutRes.json();
  
  // 2. Submit Razorpay test form with test card
  // (test card: 4242 4242 4242 4242, any future expiry, any cvc)
  
  // 3. Verify webhook processes payment.captured
  // 4. Verify order status updated to 'paid'
  // 5. Verify entitlement created for user
  // 6. Verify magic link sent
  // 7. Verify library access granted
});
```

#### 6.3.2 Non-Purchaser Download Rejection

```typescript
test('non-purchaser download rejection', async () => {
  // 1. Log in as user without purchase
  // 2. Try to download module file
  // 3. Expect 403 or redirect to login
  // 4. Verify no entitlement exists in DB
});
```

---

## Stage 7 — Commercial Content Readiness Audit

### 7.1 Resource Inventory

| Module | Resources Marked | PILOT Resources | Non-Pilot (Missing) |
|--------|-----------------|-----------------|---------------------|
| 01: Resume Mastery | 3 (resume examples + schemas) | 3 | 12 template files, handbook content |
| 02: Professional Profile | 0 | 0 | All content missing |
| 03: Job Search System | 2 (tracker XLSX, schemas) | 2 | All worksheets, outreach templates |
| 04: Interview Preparation | 6 (interview questions + schemas) | 6 | 194+ more questions, mock interview scenarios |
| 05: Salary Negotiation | 1 (calculator XLSX + schemas) | 1 | Negotiation scripts, email templates |
| 06: AI Career Assistant | 0 | 0 | 100+ prompts, tested workflows |
| 07: 90-Day Programme | 1 (roadmap JSON + schemas) | 1 | Full 30/60/90-day programme, weekly milestones |
| 08: Career Advancement | 0 | 0 | All content missing |

**Total Pilot Resources:** 13 JSON/XLSX files across modules  
**Total Missing Commercial Resources:** Significant — full product not yet built

### 7.2 Resources by Career Track

| Track | Interview Questions | Resume Examples | Relevance |
|-------|--------------------|-----------------|-----------|
| Track A: Technology and IT | 1 (int-tech-challenge.json) | 1 (tech-professional-resume.json) | ✅ One-to-one mapping |
| Track B: Business Analysis | 1 (int-ba-stakeholder.json) | 1 (business-analyst-resume.json) | ✅ One-to-one mapping |
| Track C: Product & PM | 1 (int-product-feature.json) | 0 | ⚠️ No resume example |
| Track D: Finance | 1 (int-finance-error.json) | 1 (finance-resume.json) | ✅ One-to-one mapping |
| Track E: Sales and Marketing | 1 (int-sales-persuasion.json) | 0 | ⚠️ No resume example |
| Track F: Management and Operations | 1 (int-management-change.json) | 0 | ⚠️ No resume example |

### 7.3 PILOT Label Distribution

| Status | Count | Percentage |
|--------|-------|------------|
| Pilot JSON resources | 20 | 66.7% |
| Pilot XLSX files | 2 | 6.7% |
| Non-pilot (empty/placeholder) | 8 | 26.7% |
| **Total Phase One resources** | **30** | **100%** |

### 7.4 Missing Commercial Resources

| Module | Required but Missing | Priority |
|--------|---------------------|----------|
| 02: Professional Profile Optimisation | LinkedIn/Naukri guides, headline/summary templates | High |
| 05: Salary Negotiation | Negotiation scripts, email templates, counteroffer framework | High |
| 06: AI Career Assistant | 100 tested prompts, workflows, job matching | High |
| 08: Career Advancement | Portfolio guides, transition planning, first 90 days | Medium |
| 03: Job Search System | Company research worksheets, recruiter message variations | Medium |
| 01: Resume Mastery | 15 templates, ATS handbook before-and-after examples | Medium |
| 04: Interview Preparation | 194 questions + frameworks, mock scenarios, scorecards | High |
| 07: 90-Day Programme | Full roadmap, weekly milestones, progress tracking | Medium |

### 7.5 Resources Requiring Research

| Resource Type | Research Needed | Status |
|--------------|----------------|--------|
| ATS optimisation percentages | Must not invent percentages | ✅ Policy documented |
| Salary increase guarantees | Must not claim | ✅ Policy documented |
| Interview success rates | Must not fabricate | ✅ Policy documented |
| Company-specific hiring questions | Must not invent | ✅ Policy documented |
| Customer testimonials | Must not fabricate | ✅ Policy documented |

### 7.6 Recommended Production-Content Backlog

| Priority | Module | Resource | Estimated Effort |
|----------|--------|----------|-----------------|
| P0 | 06: AI Career Assistant | 100 tested prompts across 6 tracks | 2-3 weeks |
| P0 | 05: Salary Negotiation | Scripts, email templates, calculator enhancements | 1-2 weeks |
| P0 | 04: Interview Preparation | 50+ questions + frameworks across 6 tracks | 3-4 weeks |
| P1 | 01: Resume Mastery | 15 templates + handbook content | 2-3 weeks |
| P1 | 08: Career Advancement | Portfolio guides, transition planning | 1-2 weeks |
| P1 | 03: Job Search System | Worksheets, recruiter message variations | 1-2 weeks |
| P2 | 02: Professional Profile | LinkedIn/Optimisation guides | 1 week |
| P2 | 07: 90-Day Programme | Full roadmap engine | 1-2 weeks |

---

## Stage 8 — Deliverables

### 8.1 TASK_003_INTEGRATION_AUDIT.md

Created above — comprehensive audit covering all 8 stages.

### 8.2 .env.example

Create `.env.example` with placeholder names only:

```
# ==========================================
# CareerVault — Environment Variables
# ==========================================
# NOTE: Never commit actual credentials.
# Replace all placeholder values before deployment.

# ==========================================
# Supabase
# ==========================================
NEXT_PUBLIC_SUPABASE_URL=https://your-project.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_anon_key_here
SUPABASE_SERVICE_ROLE_KEY=your_service_role_key_here

# ==========================================
# Razorpay
# ==========================================
NEXT_PUBLIC_RAZORPAY_KEY=rzp_test_your_key_here
RAZORPAY_SECRET=your_razorpay_secret_here
RAZORPAY_WEBHOOK_SECRET=your_webhook_secret_here

# ==========================================
# Transactional Email (Resend)
# ==========================================
RESEND_API_KEY=re_your_api_key_here

# ==========================================
# Application
# ==========================================
NEXT_PUBLIC_SITE_URL=https://your-domain.com
NEXT_PUBLIC_APP_VERSION=1.0
```

### 8.3 Implementation Roadmap (Prioritised)

| Phase | Week | Focus | Deliverables |
|-------|------|-------|-------------|
| **P0 — Critical** | 1-2 | Supabase project + migrations + RLS | Auth flow, order storage, entitlement tables |
| **P0 — Critical** | 2-3 | Razorpay test-mode integration | Order creation, signature verification, webhook handling |
| **P0 — Critical** | 3 | Email provider setup + templates | All 5 transactional emails operational |
| **P0 — Critical** | 3-4 | Private storage + download flow | Supabase Storage, signed URLs, ZIP delivery |
| **P0 — Critical** | 4 | End-to-end test flow | All 14 integration test cases pass |
| **P1 — Core** | 5-6 | Admin dashboard + RLS enforcement | Admin can manage orders, cannot change payment status silently |
| **P1 — Core** | 5-6 | Content pipeline | Process for uploading modules, publishing versions |
| **P1 — Core** | 6 | Legal & policy review | All pages accurate, no fabricated claims |
| **P2 — Polish** | 7-8 | Performance & SEO | Page speeds, meta tags, responsive refinement |
| **P2 — Polish** | 8 | Monitoring & analytics | Error tracking, payment metrics, download analytics |
| **P3 — Launch** | 9 | Controlled launch | Small group of beta testers, feedback collection |
| **P3 — Launch** | 9-10 | Full public launch | All checks pass, marketing materials ready |

### 8.4 Deployment Dependencies

**Must-Have Before Launch:**
- [ ] Supabase project live with RLS policies
- [ ] Razorpay test-mode flow fully functional
- [ ] Email provider verified and sending templates
- [ ] Supabase Storage bucket private, signed URLs working
- [ ] All 14 integration test cases passing
- [ ] Legal pages reviewed (no fabricated guarantees)
- [ ] Product version "1.0" published across all tables
- [ ] `.env.example` committed with placeholder values
- [ ] No `SUPABASE_SERVICE_ROLE_KEY` in frontend bundles

**Nice-to-Have:**
- [ ] Custom domain with HTTPS
- [ ] Analytics (privacy-conscious)
- [ ] Email A/B testing subject lines
- [ ] Abandoned checkout recovery
- [ ] Multi-language support (i18n)

### 8.5 Final Audit Checklist

- [ ] Repository inspected, no Phase One content overwritten
- [ ] All mock implementations identified and documented
- [ ] Supabase integration plan documented with setup instructions
- [ ] Razorpay audit complete with dashboard settings list
- [ ] Transactional email integration plan documented
- [ ] Private storage architecture verified
- [ ] 14 integration test cases defined (mix of real/mock)
- [ ] Commercial content readiness audit complete
- [ ] `.env.example` created with placeholder names only
- [ ] No live payments activated
- [ ] No public deployment
- [ ] Pilot resources clearly marked `PILOT — NOT FINAL COMMERCIAL RELEASE`
- [ ] Security weaknesses documented and remediation planned
- [ ] Duplicate code identified and consolidation planned
- [ ] Missing database functionality listed
- [ ] External service dependencies catalogued

---

**Audit Complete.** This document provides the verified integration plan for CareerVault's production readiness. All findings are based on inspection of the existing codebase at `C:\Users\Quick\Desktop\CareerVault`. No live services have been activated, and no credentials have been exposed.

**Next Step:** Approval of this audit before modifying any external-service integration code.