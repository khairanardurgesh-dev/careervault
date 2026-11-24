import "./globals.css";
import { children, Metadata } from "next";

export const metadata: Metadata = {
  title: "CareerVault - Your Complete Job Switch System",
  description:
    "Premium digital toolkit for working professionals switching jobs in India. Eight modules, six career tracks, organised career transition system.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}