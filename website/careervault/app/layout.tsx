import "./globals.css";
import type { Metadata } from "next";
import type { ReactNode } from "react";

export const metadata: Metadata = {
  title: "CareerVault - Your Complete Job Switch System",
  description:
    "Premium digital toolkit for working professionals switching jobs in India. Eight modules, six career tracks, organised career transition system.",
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}