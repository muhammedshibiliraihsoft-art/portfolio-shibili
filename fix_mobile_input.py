import re

with open('src/components/contact/ContactPageClient.tsx', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Extract setValue from useForm
old_useform = '''  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<ContactValues>({'''

new_useform = '''  const {
    register,
    handleSubmit,
    reset,
    setValue,
    formState: { errors, isSubmitting },
  } = useForm<ContactValues>({'''
code = code.replace(old_useform, new_useform)


# 2. Fix corrupted country prefix and add onInput handler
old_input_block = r'<span className="text-neutral/70 mr-2 flex-shrink-0">.*? \+91</span>\s*<input\s*\{\.\.\.register\(\'mobile\'\)\}\s*type="tel"'

new_input_block = '''<span className="text-neutral/70 mr-2 flex-shrink-0">IN +91</span>
            <input 
              {...register('mobile')}
              onInput={(e) => {
                let val = e.currentTarget.value;
                if (val.startswith('+91')) {
                    val = val.replace('+91', '');
                } else if (val.startswith('91') && val.length > 10) {
                    val = val.replace('91', '');
                }
                val = val.replace(/\D/g, '');
                
                if (val !== e.currentTarget.value) {
                    e.currentTarget.value = val;
                    setValue('mobile', val, { shouldValidate: true });
                }
              }}
              type="tel"'''

code = re.sub(old_input_block, new_input_block, code)

with open('src/components/contact/ContactPageClient.tsx', 'w', encoding='utf-8') as f:
    f.write(code)

print("Fixed mobile input filtering.")
