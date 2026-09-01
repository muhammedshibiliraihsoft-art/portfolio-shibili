const fs = require('fs');

let code = fs.readFileSync('src/components/contact/ContactPageClient.tsx', 'utf8');

const oldUseForm =   const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<ContactValues>({;

const newUseForm =   const {
    register,
    handleSubmit,
    reset,
    setValue,
    formState: { errors, isSubmitting },
  } = useForm<ContactValues>({;

code = code.replace(oldUseForm, newUseForm);

const oldInput = /<span className="text-neutral\/70 mr-2 flex-shrink-0">.*? \+91<\/span>\s*<input\s*\{\.\.\.register\('mobile'\)\}\s*type="tel"/;

const newInput = <span className="text-neutral/70 mr-2 flex-shrink-0">IN +91</span>
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
              type="tel";

code = code.replace(oldInput, newInput);

fs.writeFileSync('src/components/contact/ContactPageClient.tsx', code);
console.log('Fixed JS');
