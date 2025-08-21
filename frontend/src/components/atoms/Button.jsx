// src/components/atoms/Button.jsx
import React from "react";
import clsx from "clsx";

const variants = {
  primary:
    "bg-indigo-600 text-white hover:bg-indigo-700 focus:ring-indigo-500",
  secondary:
    "bg-gray-200 text-gray-800 hover:bg-gray-300 focus:ring-gray-400",
  success:
    "bg-emerald-600 text-white hover:bg-emerald-700 focus:ring-emerald-500",
  danger: "bg-red-600 text-white hover:bg-red-700 focus:ring-red-500",
  accent:
    "bg-yellow-500 text-white hover:bg-yellow-600 focus:ring-yellow-400",

  // Nuevos estilos
  outline:
    "border border-gray-300 bg-transparent text-gray-800 hover:bg-gray-100 focus:ring-gray-400",
  ghost:
    "bg-transparent text-indigo-600 hover:bg-indigo-50 focus:ring-indigo-400",
};

const sizes = {
  sm: "px-3 py-1.5 text-sm",
  md: "px-4 py-2 text-base",
  lg: "px-5 py-3 text-lg",
};

const Button = ({
  children,
  variant = "primary",
  size = "md",
  fullWidth = false,
  disabled = false,
  iconLeft: IconLeft,
  iconRight: IconRight,
  ...props
}) => {
  return (
    <button
      className={clsx(
        "inline-flex items-center justify-center gap-2 rounded-xl font-medium shadow-sm transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed",
        variants[variant],
        sizes[size],
        fullWidth && "w-full"
      )}
      disabled={disabled}
      {...props}
    >
      {IconLeft && <IconLeft className="w-5 h-5" />}
      {children}
      {IconRight && <IconRight className="w-5 h-5" />}
    </button>
  );
};

export default Button;
