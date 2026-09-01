import { z } from 'zod';
import { rateLimitCheck } from '@/lib/rateLimit';
import { NextResponse } from 'next/server';
import { getRaihsuiteConfig, createEnquiry } from '@/lib/raihsuite/enquiries';

export const runtime = 'edge';

const ContactSchema = z.object({
  name: z.string().min(2).max(200),
  email: z.string().email(),
  mobile: z
    .string()
    .length(10, 'Enter a valid 10-digit mobile number')
    .regex(/^[0-9]+$/, 'Only digits are allowed'),
  message: z.string().min(10).max(5000),
});

async function verifyTurnstile(): Promise<boolean> {
  // TODO: Integrate Cloudflare Turnstile once TURNSTILE_SECRET is configured.
  return true;
}

export async function POST(req: Request) {
  let body: unknown;

  try {
    body = await req.json();
  } catch {
    return NextResponse.json({ error: 'Invalid JSON body' }, { status: 400 });
  }

  const parsed = ContactSchema.safeParse(body);
  if (!parsed.success) {
    return NextResponse.json(
      { error: 'Validation failed', issues: parsed.error.issues.map((i) => i.message) },
      { status: 400 },
    );
  }

  const ip = req.headers.get('x-forwarded-for') || 'unknown';
  const limited = rateLimitCheck(ip);
  if (limited) {
    return NextResponse.json({ error: 'Too many requests' }, { status: 429 });
  }

  const captchaOk = await verifyTurnstile();
  if (!captchaOk) {
    return NextResponse.json({ error: 'Captcha failed' }, { status: 403 });
  }

  let config;
  try {
    config = getRaihsuiteConfig();
  } catch {
    return NextResponse.json(
      { error: 'Server configuration error. Please try again later.' },
      { status: 500 },
    );
  }

  const result = await createEnquiry(config, parsed.data);

  if (!result.ok) {
    return NextResponse.json(
      { error: 'Unable to send your enquiry right now. Please try again later.' },
      { status: 502 },
    );
  }

  return NextResponse.json({ status: 'ok' }, { status: 200 });
}