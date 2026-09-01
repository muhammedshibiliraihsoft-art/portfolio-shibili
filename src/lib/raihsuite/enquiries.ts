/**
 * Raihsuite CRM — Enquiry integration boundary.
 *
 * TODO: Confirm authentication scheme, tenant contract, and exact payload
 * schema with the backend team before enabling upstream submission.
 */

export interface RaihsuiteEnquiryPayload {
  name: string;
  mobile: string;
  email: string;
  message: string;
}

export interface RaihsuiteConfig {
  apiBase: string;
  tenantId: string;
}

export interface RaihsuiteResult {
  ok: boolean;
  status: number;
  body?: unknown;
  error?: string;
}

/**
 * Build the upstream Raihsuite configuration from server-only environment
 * variables. Throws if required config is missing so the route can return 500.
 */
export function getRaihsuiteConfig(): RaihsuiteConfig {
  // Support both current and legacy env variable names during migration.
  const configuredBase =
    process.env.RAIHSUITE_API_BASE_URL || process.env.RAISUITE_API_BASE;
  const tenantId = process.env.RAIHSUITE_TENANT_ID || process.env.TENANT_ID;

  if (!configuredBase || !tenantId) {
    throw new Error(
      'Raihsuite integration not configured: API base URL and tenant ID are required.',
    );
  }

  // Normalise: ensure base ends with /v1 exactly once
  const apiBase = configuredBase.replace(/\/+$/, '').endsWith('/v1')
    ? configuredBase.replace(/\/+$/, '')
    : `${configuredBase.replace(/\/+$/, '')}/v1`;

  return { apiBase, tenantId };
}

/**
 * Create an enquiry in the Raihsuite CRM.
 *
 * Authentication method is TBD — update the headers here once the
 * backend team confirms the exact scheme (Bearer, Token, X-API-Key, etc.).
 */
export async function createEnquiry(
  config: RaihsuiteConfig,
  data: RaihsuiteEnquiryPayload,
): Promise<RaihsuiteResult> {
  try {
    const upstream = await fetch(`${config.apiBase}/crm/enquiries/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ ...data, tenant: parseInt(config.tenantId, 10) }),
    });

    const body = await upstream.json().catch(() => null);

    if (!upstream.ok) {
      console.error('[Raihsuite] Upstream error:', upstream.status, JSON.stringify(body));
      return {
        ok: false,
        status: upstream.status,
        body,
        error: `Upstream returned ${upstream.status}`,
      };
    }

    return { ok: true, status: upstream.status, body };
  } catch (err) {
    return {
      ok: false,
      status: 502,
      error: err instanceof Error ? err.message : 'Network error contacting Raihsuite',
    };
  }
}
