import re

with open('src/components/contact/ContactPageClient.tsx', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Add state variable
old_states = "  const [errorMessage, setErrorMessage] = useState('');"
new_states = "  const [errorMessage, setErrorMessage] = useState('');\n  const [isLongRequest, setIsLongRequest] = useState(false);"
code = code.replace(old_states, new_states)

# 2. Update onSubmit function to handle timeout logic
old_onsubmit = '''  const onSubmit = async (data: ContactValues) => {
    setStatus('loading');
    setErrorMessage('');
    
    try {
      const res = await fetch('/api/contact', {'''

new_onsubmit = '''  const onSubmit = async (data: ContactValues) => {
    setStatus('loading');
    setErrorMessage('');
    setIsLongRequest(false);
    
    const timeoutId = setTimeout(() => {
      setIsLongRequest(true);
    }, 4000); // Trigger after 4 seconds
    
    try {
      const res = await fetch('/api/contact', {'''
code = code.replace(old_onsubmit, new_onsubmit)

old_clear1 = '''      const body = await res.json();
      
      if (res.ok) {'''
new_clear1 = '''      clearTimeout(timeoutId);
      const body = await res.json();
      
      if (res.ok) {'''
code = code.replace(old_clear1, new_clear1)

old_clear2 = '''    } catch {
      setStatus('error');
      setErrorMessage('Network error. Please try again later.');
    }
  };'''
new_clear2 = '''    } catch {
      clearTimeout(timeoutId);
      setStatus('error');
      setErrorMessage('Network error. Please try again later.');
    }
  };'''
code = code.replace(old_clear2, new_clear2)

# 3. Update the button text logic
old_button_text = "{isSubmitting ? 'SENDING...' : 'SEND MESSAGE'}"
new_button_text = "{isSubmitting ? (isLongRequest ? 'WAKING UP SERVER...' : 'SENDING...') : 'SEND MESSAGE'}"
code = code.replace(old_button_text, new_button_text)

with open('src/components/contact/ContactPageClient.tsx', 'w', encoding='utf-8') as f:
    f.write(code)

print("Wait and Inform UX applied.")
