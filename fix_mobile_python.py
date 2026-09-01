with open('src/components/contact/ContactPageClient.tsx', 'r', encoding='utf-8') as f:
    code = f.read()

# 1
old1 = '''  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<ContactValues>({'''

new1 = '''  const {
    register,
    handleSubmit,
    reset,
    setValue,
    formState: { errors, isSubmitting },
  } = useForm<ContactValues>({'''

code = code.replace(old1, new1)

# 2
import re
old2_regex = r'<span className="text-neutral/70 mr-2 flex-shrink-0">.*? \+91</span>\s*<input\s*\{\.\.\.register\(\'mobile\'\)\}\s*type="tel"'

new2 = '''<span className="text-neutral/70 mr-2 flex-shrink-0">IN +91</span>
            <input 
              {...register('mobile')}
              onInput={(e) => {
                let val = e.currentTarget.value;
                if (val.startsWith('+91')) {
                    val = val.substring(3);
                } else if (val.startsWith('91') && val.length > 10) {
                    val = val.substring(2);
                }
                val = val.replace(/\\D/g, '');
                if (val !== e.currentTarget.value) {
                    e.currentTarget.value = val;
                    setValue('mobile', val, { shouldValidate: true });
                }
              }}
              type="tel"'''

# Using a lambda allows us to bypass regex escape parsing on the replacement string
code = re.sub(old2_regex, lambda match: new2, code)

with open('src/components/contact/ContactPageClient.tsx', 'w', encoding='utf-8') as f:
    f.write(code)

print("done")
