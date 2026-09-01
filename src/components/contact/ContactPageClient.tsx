'use client';

import { useState } from 'react';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';

const ContactSchema = z.object({
  name: z.string().min(2, "Name must be at least 2 characters").max(200),
  email: z.string().email("Please enter a valid email"),
  mobile: z
    .string()
    .length(10, 'Enter a valid 10-digit mobile number')
    .regex(/^[0-9]+$/, 'Only digits are allowed'),
  message: z.string().min(10, "Message must be at least 10 characters").max(5000),
});

type ContactValues = z.infer<typeof ContactSchema>;

export default function ContactPageClient() {
  const [status, setStatus] = useState<'idle' | 'loading' | 'success' | 'error'>('idle');
  const [errorMessage, setErrorMessage] = useState('');
  const [isLongRequest, setIsLongRequest] = useState(false);

  const {
    register,
    handleSubmit,
    reset,
    setValue,
    formState: { errors, isSubmitting },
  } = useForm<ContactValues>({
    resolver: zodResolver(ContactSchema),
  });

  const onSubmit = async (data: ContactValues) => {
    setStatus('loading');
    setErrorMessage('');
    setIsLongRequest(false);
    
    const timeoutId = setTimeout(() => {
      setIsLongRequest(true);
    }, 4000); // Trigger after 4 seconds
    
    try {
      const res = await fetch('/api/contact', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
      });
      
      clearTimeout(timeoutId);
      const body = await res.json();
      
      if (res.ok) {
        setStatus('success');
        reset();
      } else {
        setStatus('error');
        setErrorMessage(body.error || 'Something went wrong. Please try again.');
      }
    } catch {
      clearTimeout(timeoutId);
      setStatus('error');
      setErrorMessage('Network error. Please try again later.');
    }
  };

  return (
    <form className="space-y-6" onSubmit={handleSubmit(onSubmit)}>
      {status === 'success' && (
        <div className="relative bg-[#0c1218] border border-primary/30 p-6 rounded-md mb-6 flex items-start gap-4 shadow-[0_0_20px_rgba(4,83,216,0.15)]">
          <span className="material-symbols-outlined text-primary text-[24px]">check_circle</span>
          <div>
            <h3 className="text-white font-bold mb-1">Message Sent</h3>
            <p className="text-neutral text-sm opacity-80">Thank you! Your message has been sent successfully. I will get back to you soon.</p>
          </div>
        </div>
      )}
      
      {status === 'error' && (
        <div className="relative bg-[#0c1218] border border-red-500/30 p-6 rounded-md mb-6 flex items-start gap-4">
          <span className="material-symbols-outlined text-red-400 text-[24px]">error</span>
          <div>
            <h3 className="text-white font-bold mb-1">Something went wrong</h3>
            <p className="text-neutral text-sm opacity-80">{errorMessage}</p>
          </div>
        </div>
      )}

      <div className="flex flex-col md:flex-row gap-6">
        {/* Name Input */}
        <div className="flex-1 relative group">
          <div className="relative bg-[#0c1218] border border-outline-variant rounded-md p-4 transition-colors">
            <div className="flex items-center gap-2 text-sm text-neutral mb-2 font-medium">
              <span className="material-symbols-outlined text-[18px]">person</span> Your Name
            </div>
            <input 
              {...register('name')}
              type="text" 
              placeholder="Enter your name" 
              className="w-full bg-transparent border-none text-white focus:outline-none focus:ring-0 placeholder-neutral/50 font-poppins" 
            />
          </div>
          {errors.name && <p className="text-red-500 text-xs mt-1 absolute">{errors.name.message}</p>}
        </div>
        {/* Email Input */}
        <div className="flex-1 relative group">
          <div className="relative bg-[#0c1218] border border-outline-variant rounded-md p-4 transition-colors">
            <div className="flex items-center gap-2 text-sm text-neutral mb-2 font-medium">
              <span className="material-symbols-outlined text-[18px]">mail</span> Your Email
            </div>
            <input 
              {...register('email')}
              type="email" 
              placeholder="Enter your email" 
              className="w-full bg-transparent border-none text-white focus:outline-none focus:ring-0 placeholder-neutral/50 font-poppins" 
            />
          </div>
          {errors.email && <p className="text-red-500 text-xs mt-1 absolute">{errors.email.message}</p>}
        </div>
      </div>

      {/* Mobile Input */}
      <div className="relative group mt-8 md:mt-6">
        <div className="relative bg-[#0c1218] border border-outline-variant rounded-md p-4 transition-colors">
          <div className="flex items-center gap-2 text-sm text-neutral mb-2 font-medium">
            <span className="material-symbols-outlined text-[18px]">call</span> Mobile Number
          </div>
          <div className="flex items-center">
            <span className="text-neutral/70 mr-2 flex-shrink-0">IN +91</span>
            <input 
              {...register('mobile')}
              onInput={(e) => {
                let val = e.currentTarget.value;
                if (val.startsWith('+91')) {
                    val = val.substring(3);
                } else if (val.startsWith('91') && val.length > 10) {
                    val = val.substring(2);
                }
                val = val.replace(/\D/g, '');
                if (val !== e.currentTarget.value) {
                    e.currentTarget.value = val;
                    setValue('mobile', val, { shouldValidate: true });
                }
              }}
              type="tel" 
              placeholder="Enter 10 digit number" 
              className="w-full bg-transparent border-none text-white focus:outline-none focus:ring-0 placeholder-neutral/50 font-poppins" 
            />
          </div>
        </div>
        {errors.mobile && <p className="text-red-500 text-xs mt-1 absolute">{errors.mobile.message}</p>}
      </div>

      {/* Message Input */}
      <div className="relative group mt-8 md:mt-6">
        <div className="relative bg-[#0c1218] border border-outline-variant rounded-md p-4 transition-colors">
          <div className="flex items-center gap-2 text-sm text-neutral mb-2 font-medium">
            <span className="material-symbols-outlined text-[18px]">chat_bubble</span> Your Message
          </div>
          <textarea 
            {...register('message')}
            rows={4} 
            placeholder="Tell me about your project..." 
            className="w-full bg-transparent border-none text-white focus:outline-none focus:ring-0 placeholder-neutral/50 font-poppins resize-none"
          ></textarea>
        </div>
        {errors.message && <p className="text-red-500 text-xs mt-1 absolute">{errors.message.message}</p>}
      </div>

      {/* Submit Row */}
      <div className="flex flex-col sm:flex-row items-start sm:items-center gap-6 pt-6">
        <button 
          type="submit" 
          disabled={isSubmitting}
          className="relative group overflow-hidden bg-surface-container-high border border-outline-variant hover:border-primary text-white px-8 py-4 rounded-md font-bold flex items-center gap-4 transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed"
        >
          <div className="absolute inset-0 bg-primary/10 translate-y-full group-hover:translate-y-0 transition-transform duration-300"></div>
          <span className="relative z-10 tracking-widest text-sm">
            {isSubmitting ? (isLongRequest ? 'WAKING UP SERVER...' : 'SENDING...') : 'SEND MESSAGE'}
          </span>
          {!isSubmitting && <span className="material-symbols-outlined relative z-10 text-[18px] group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform">north_east</span>}
        </button>
        <div className="flex items-center gap-3 text-neutral text-sm opacity-80">
          <span className="material-symbols-outlined text-[20px]">lock</span>
          <p>Your information is safe<br/>and will never be shared.</p>
        </div>
      </div>
    </form>
  );
}
