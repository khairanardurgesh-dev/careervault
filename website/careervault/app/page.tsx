import { Hero } from "@/components/landing/hero";
import { TrustBadges } from "@/components/landing/trust-badges";
import { Testimonials } from "@/components/landing/testimonials";
import { Comparison } from "@/components/landing/comparison";
import { CTA } from "@/components/landing/cta";
import { FAQ } from "@/components/landing/faq";

export default function HomePage() {
  return (
    <>
      <Hero variant="home" />
      <TrustBadges />
      <Testimonials />
      <Comparison />
      <FAQ />
      <CTA />
    </>
  );
}