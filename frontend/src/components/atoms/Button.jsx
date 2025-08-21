import clsx from "clsx";

const Button = ({
  children,
  variant = "primary", // primary | secondary | danger | neutral
  size = "md", // sm | md | lg
  fullWidth = false,
  disabled = false,
  onClick,
  type = "button",
}) => {
  const baseStyles =
    "inline-flex items-center justify-center font-medium rounded-lg focus:outline-none transition-colors duration-200";

  const variants = {
    primary:
      "bg-primary text-white hover:bg-primary-dark disabled:bg-primary-light",
    secondary:
      "bg-secondary text-white hover:bg-secondary-dark disabled:bg-secondary-light",
    danger:
      "bg-danger text-white hover:bg-danger-dark disabled:bg-danger-light",
    neutral:
      "bg-neutral text-white hover:bg-neutral-dark disabled:bg-neutral-light",
  };

  const sizes = {
    sm: "px-3 py-1.5 text-sm",
    md: "px-4 py-2 text-base",
    lg: "px-6 py-3 text-lg",
  };

  const classes = clsx(
    baseStyles,
    variants[variant],
    sizes[size],
    fullWidth && "w-full",
    disabled && "opacity-50 cursor-not-allowed"
  );

  return (
    <button type={type} className={classes} disabled={disabled} onClick={onClick}>
      {children}
    </button>
  );
};

export default Button;
