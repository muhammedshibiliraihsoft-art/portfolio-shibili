import './globals.css';
import type { Metadata } from 'next';
import { Gabarito, Be_Vietnam_Pro, Poppins, JetBrains_Mono } from 'next/font/google';

const gabarito = Gabarito({ subsets: ['latin'], variable: '--font-gabarito' });
const beVietnamPro = Be_Vietnam_Pro({ weight: ['400', '500', '600', '700', '800'], subsets: ['latin'], variable: '--font-be-vietnam-pro' });
const poppins = Poppins({ weight: ['400', '500', '600', '700'], subsets: ['latin'], variable: '--font-poppins' });
const jetbrainsMono = JetBrains_Mono({ weight: ['500'], subsets: ['latin'], variable: '--font-jetbrains-mono' });


export const metadata: Metadata = {
  title: 'Muhammed Shibili | Portfolio',
  description: 'Reusable starter template for multi-tenant Raisuite client sites.'
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className={`dark scroll-smooth scroll-pt-32 ${gabarito.variable} ${beVietnamPro.variable} ${poppins.variable} ${jetbrainsMono.variable}`}>
      
      <head>
        <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet" />
        
        
      </head>
      <body>
        
        <main>{children}</main>
        
      </body>
    </html>
  );
}