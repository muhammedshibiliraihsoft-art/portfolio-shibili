# Raihsuite Enquiry Integration Guide

This document explains how the **Contact Form** connects to the **Raihsoft Raihsuite CRM backend** and how to plug this integration into any future project.

---

## How It Works — Full Flow

```
User submits form
      ↓
ContactPageClient.tsx  (validates input with Zod)
      ↓
POST /api/contact       (Next.js Edge API Route)
      ↓
Rate limit check        (20 req/IP/min)
      ↓
Captcha check           (Cloudflare Turnstile — optional)
      ↓
getRaihsuiteConfig()    (reads env vars)
      ↓
createEnquiry()         (POST to Raihsuite CRM API)
      ↓
POST https://{RAIHSUITE_API_BASE_URL}/crm/enquiries/
Body: { name, email, mobile, message, tenant: TENANT_ID }
      ↓
Response → User sees success / error
```

---

## Files Involved

| File | Purpose |
|---|---|
| `src/components/contact/ContactPageClient.tsx` | Frontend form (React, Zod validation) |
| `src/app/api/contact/route.ts` | Next.js API Route (Edge runtime) |
| `src/lib/raihsuite/enquiries.ts` | Raihsuite integration module |
| `src/lib/rateLimit.ts` | In-memory IP rate limiter |
| `.env.local` | Secret environment variables (never commit) |

---

## Environment Variables (.env.local)

```env
# Required — Raihsuite Tenant ID (unique per client project)
RAIHSUITE_TENANT_ID=115

# Required — Raihsuite backend base URL
RAIHSUITE_API_BASE_URL=https://staging-api.raihsuite.com/v1

# Optional — same value, exposed to client if needed
NEXT_PUBLIC_RAIHSUITE_API_BASE_URL=https://staging-api.raihsuite.com/v1

# Optional — Cloudflare Turnstile CAPTCHA secret
TURNSTILE_SECRET=
```

> IMPORTANT: Never commit .env.local to Git. Keep secrets only on the server / hosting platform.

---

## The API Endpoint

**URL:**
```
POST {RAIHSUITE_API_BASE_URL}/crm/enquiries/
```

**Example:**
```
POST https://staging-api.raihsuite.com/v1/crm/enquiries/
```

**Request Body (JSON):**
```json
{
  "name": "Shibili K",
  "email": "shibili@example.com",
  "mobile": "9876543210",
  "message": "I need a custom web app for my business.",
  "tenant": "115"
}
```

**Success Response (200):**
```json
{ "status": "ok" }
```

---

## Field Validation Rules

| Field | Validation |
|---|---|
| `name` | Min 2 chars, max 200 chars |
| `email` | Valid email format |
| `mobile` | Exactly 10 digits, numbers only |
| `message` | Min 10 chars, max 5000 chars |
| `tenant` | Auto-injected from RAIHSUITE_TENANT_ID env var |

---

## Authentication (To Be Confirmed with Backend Team)

Current integration sends requests without an auth header.
When confirmed, update `src/lib/raihsuite/enquiries.ts`:

```ts
headers: {
  'Content-Type': 'application/json',
  // Add auth here, e.g.:
  // 'Authorization': `Bearer ${process.env.RAIHSUITE_API_KEY}`,
  // 'X-API-Key': process.env.RAIHSUITE_API_KEY,
},
```

---

## How to Add to a New Project

### Step 1 — Copy these files
```
src/lib/raihsuite/enquiries.ts
src/lib/rateLimit.ts
src/app/api/contact/route.ts
src/components/contact/ContactPageClient.tsx
```

### Step 2 — Install packages
```bash
pnpm add zod react-hook-form @hookform/resolvers
```

### Step 3 — Set environment variables
```env
RAIHSUITE_TENANT_ID=<client-specific-id>
RAIHSUITE_API_BASE_URL=https://api.raihsuite.com/v1
```
> Each client project gets a unique RAIHSUITE_TENANT_ID from Raihsoft.

### Step 4 — Render the form
```tsx
import ContactPageClient from '@/components/contact/ContactPageClient';

export default function ContactPage() {
  return <ContactPageClient />;
}
```

---

## Rate Limiting

- Window: 60 seconds
- Limit: 20 requests per IP per window
- Returns HTTP 429 if exceeded

---

## Staging vs Production

| Environment | API Base URL |
|---|---|
| Staging | `https://staging-api.raihsuite.com/v1` |
| Production | `https://api.raihsuite.com/v1` |

---

## Quick Test (curl)

```bash
curl -X POST https://your-domain.com/api/contact \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test User",
    "email": "test@example.com",
    "mobile": "9876543210",
    "message": "This is a test enquiry message."
  }'
```

Expected: `{ "status": "ok" }`

---

## Troubleshooting

| Error | Cause | Fix |
|---|---|---|
| 502 Bad Gateway | Raihsuite API unreachable | Check RAIHSUITE_API_BASE_URL |
| 500 Server Error | Missing env vars | Add RAIHSUITE_TENANT_ID and RAIHSUITE_API_BASE_URL |
| 429 Too Many Requests | Rate limit hit | Wait 60 seconds and retry |
| 400 Validation failed | Invalid form data | Check field rules above |

---

Last updated: 2026-08-28 | Raihsoft Internal Integration Docs
