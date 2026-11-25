import * as React from "react";
import { cn } from "@/lib/utils";

type ButtonVariant = "primary" | "outline";

export interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: ButtonVariant;
  asChild?: boolean;
  loading?: boolean;
}

const variantClasses: Record<ButtonVariant, string> = {
  primary: "btn-primary",
  outline: "btn-outline",
};

export function Button({
  className,
  variant = "primary",
  asChild = false,
  loading = false,
  disabled,
  children,
  type,
  ...props
}: ButtonProps) {
  const classes = cn("btn", variantClasses[variant], className);
  const isDisabled = Boolean(disabled) || loading;

  if (asChild) {
    if (!React.isValidElement(children)) {
      throw new Error("Button asChild requires a single React element child");
    }
    const child = children as React.ReactElement<Record<string, unknown>>;
    return React.cloneElement(child, {
      className: cn(child.props.className as string | undefined, classes),
      "aria-disabled": isDisabled || undefined,
    });
  }

  return (
    <button
      type={type ?? "button"}
      className={classes}
      disabled={isDisabled}
      aria-busy={loading || undefined}
      {...props}
    >
      {children}
    </button>
  );
}
