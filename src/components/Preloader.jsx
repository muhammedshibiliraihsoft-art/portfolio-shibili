"use client";
import React, { useEffect, useState } from "react";
import { useProgress } from "@react-three/drei";
import gsap from "gsap";

function ConcentricRing({ className = "", ...props }) {
  return (
    <>
      <style>{`
        @keyframes loading-ui-concentric-ring-rotation {
          0% {
            transform: rotate(0deg);
          }
          100% {
            transform: rotate(360deg);
          }
        }
      `}</style>
      <span
        role="status"
        className={`relative inline-block ${className}`}
        style={{
          animation:
            "loading-ui-concentric-ring-rotation var(--duration, 1s) linear infinite",
        }}
        {...props}
      >
        <span
          aria-hidden="true"
          className="absolute inset-0 rounded-full border-2 border-current"
          style={{ opacity: 0.25 }}
        />
        <span
          aria-hidden="true"
          className="absolute top-1/2 left-1/2 rounded-full border-2 border-transparent border-b-current"
          style={{
            width: "83.333%",
            height: "83.333%",
            transform: "translate(-50%, -50%)",
          }}
        />
        <span className="sr-only">Loading</span>
      </span>
    </>
  );
}

export default function Preloader() {
  const { progress } = useProgress();
  const [loading, setLoading] = useState(true);
  const [mounted, setMounted] = useState(false);
  const [imagesLoaded, setImagesLoaded] = useState(false);

  useEffect(() => {
    setMounted(true);
  }, []);

  useEffect(() => {
    // We must ensure ALL images in the document are fully loaded.
    const images = Array.from(document.images);
    
    if (images.length === 0) {
      setImagesLoaded(true);
      return;
    }

    let loadedCount = 0;
    const checkAllImagesLoaded = () => {
      loadedCount++;
      if (loadedCount >= images.length) {
        setImagesLoaded(true);
      }
    };

    images.forEach(img => {
      if (img.complete) {
        checkAllImagesLoaded();
      } else {
        img.addEventListener('load', checkAllImagesLoaded);
        img.addEventListener('error', checkAllImagesLoaded); // even if error, we shouldn't block forever
      }
    });

    return () => {
      images.forEach(img => {
        img.removeEventListener('load', checkAllImagesLoaded);
        img.removeEventListener('error', checkAllImagesLoaded);
      });
    };
  }, []);

  useEffect(() => {
    // Wait until both 3D models and DOM images are fully loaded
    if (mounted && progress >= 100 && imagesLoaded) {
      setTimeout(() => {
        gsap.to(".preloader-overlay", {
          yPercent: -100,
          duration: 1.2,
          ease: "power3.inOut",
          onComplete: () => setLoading(false)
        });
      }, 1000); // 1s buffer for rendering
    }
  }, [progress, imagesLoaded, mounted]);

  // If loading is finished, unmount completely
  if (!loading) return null;

  // Show 0% during SSR to avoid hydration mismatch, then show actual progress
  const displayProgress = !mounted ? 0 : (!imagesLoaded && progress >= 100) ? 99 : Math.round(progress);

  // We return the overlay even when !mounted so it renders on the server and covers the screen instantly!
  return (
    <div className="preloader-overlay fixed inset-0 z-[99999] bg-[#050505] flex flex-col items-center justify-center">
      <div className="flex flex-col items-center justify-center gap-6">
        <ConcentricRing className="w-16 h-16 text-primary" style={{ "--duration": "1.5s" }} />
        
        <div suppressHydrationWarning className="text-white text-3xl md:text-5xl font-extrabold font-serif tracking-widest tabular-nums">
          {displayProgress}%
        </div>
        
        <p suppressHydrationWarning className="text-neutral text-sm uppercase tracking-widest opacity-60 font-poppins mt-2">
          {(!mounted) ? "Preloading Assets..." : (imagesLoaded && progress >= 100 ? "Ready!" : "Preloading Assets...")}
        </p>
      </div>
    </div>
  );
}
