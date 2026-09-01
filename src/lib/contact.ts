export interface ContactPayload {
  name: string;
  mobile: string;
  email: string;
  message: string;
}

export async function submitContact(data: ContactPayload): Promise<Response> {
  const apiBase =
    process.env.NEXT_PUBLIC_RAIHSUITE_API_BASE_URL ||
    'https://staging-api.raihsuite.com/v1';

  return fetch(`${apiBase}/crm/enquiries/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ ...data, tenant: Number(process.env.NEXT_PUBLIC_RAIHSUITE_TENANT_ID) || 8 }),
  });
}