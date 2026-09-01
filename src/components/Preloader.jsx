"use client";
import React, { useEffect, useState } from "react";
import { useProgress } from "@react-three/drei";
import gsap from "gsap";

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
    if (progress >= 100 && imagesLoaded) {
      setTimeout(() => {
        gsap.to(".preloader-overlay", {
          yPercent: -100,
          duration: 1.2,
          ease: "power3.inOut",
          onComplete: () => setLoading(false)
        });
      }, 1000); // 1s buffer for rendering
    }
  }, [progress, imagesLoaded]);

  if (!mounted || !loading) return null;

  // Calculate overall percentage (50% from 3D, 50% from images - but we'll just show 3D progress for now as it's the heaviest, or fake a 99% until images load)
  const displayProgress = (!imagesLoaded && progress >= 100) ? 99 : Math.round(progress);

  return (
    <div className="preloader-overlay fixed inset-0 z-[99999] bg-[#050505] flex flex-col items-center justify-center">
      <div className="flex flex-col items-center justify-center gap-6">
        <div className="w-16 h-16 border-4 border-white-50/20 border-t-primary rounded-full animate-spin"></div>
        
        <div className="text-white text-3xl md:text-5xl font-extrabold font-serif tracking-widest">
          {displayProgress}%
        </div>
        
        <p className="text-neutral text-sm uppercase tracking-widest opacity-60 font-poppins mt-2">
          {imagesLoaded && progress >= 100 ? "Ready!" : "Preloading Assets..."}
        </p>
      </div>
    </div>
  );
}
