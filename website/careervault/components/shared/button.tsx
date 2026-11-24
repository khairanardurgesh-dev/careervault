import { cn } from "@/lib/utils";

export { cn } from "@/lib/utils";

export function Button({
  className,
  asChild = false,
  variant = "primary",
  ...props
}: {
  className?: string;
  asChild?: boolean;
  variant?: "primary" | "outline";
  [key: string]: any;
}) {
  const VariantClass =
    variant === "primary"
      ? "btn-primary"
      : "btn-outline";

  if (asChild) {
    const Component = props.asChild;
    const { childProps, ...rest } = props;
    return <Component className={cn(VariantClass, className)} {...rest} />;
  }

  return (
    <button className={cn("btn", VariantClass, className)} {...props} />
  );
}