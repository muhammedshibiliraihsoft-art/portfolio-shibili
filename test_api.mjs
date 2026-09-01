const res = await fetch('https://staging-api.raihsuite.com/v1/crm/enquiries/', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    name: 'Test User',
    mobile: '9876543210',
    email: 'test@test.com',
    message: 'Test message here please',
    tenant: 67
  })
});
const body = await res.json().catch(() => res.text());
console.log('Status:', res.status);
console.log('Body:', JSON.stringify(body, null, 2));
