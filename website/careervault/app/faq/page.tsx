import { Hero } from "@/components/landing/hero";
import { FAQ } from "@/components/landing/faq";
import { CTA } from "@/components/landing/cta";

export default function FaqPage() {
  return (
    <>
      <Hero variant="product" />
      <FAQ />
      <CTA />
    </>
  );
}