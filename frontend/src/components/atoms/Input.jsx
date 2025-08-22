// src/components/atoms/Input.jsx
import React from "react";
import clsx from "clsx";

const Input = ({
  label,
  type = "text",
  placeholder = "",
  value,
  onChange,
  variant = "default", // default | error | success
  size = "md", // sm | md | lg
  disabled = false,
  readOnly = false,
  leftIcon,
  rightIcon,
  fullWidth = false,
  error, // mensaje de error
  success, // mensaje de éxito
  className,
  ...props
}) => {
  const baseStyles =
    "rounded-lg border shadow-sm transition-all focus:outline-none placeholder-gray-400";

  const variantStyles = {
    default:
      "border-neutral-light bg-white text-neutral focus:border-primary-light focus:ring-2 focus:ring-primary-light/30",
    error:
      "border-danger bg-white text-danger placeholder-danger/70 focus:border-danger focus:ring-2 focus:ring-danger/30",
    success:
      "border-green-500 bg-white text-green-700 placeholder-green-400 focus:border-green-500 focus:ring-2 focus:ring-green-400/30",
  };

  const sizeStyles = {
    sm: "px-2 py-1 text-sm h-8",
    md: "px-3 py-2 text-base h-10",
    lg: "px-4 py-2 text-lg h-12",
  };

  const wrapperStyles = clsx(
    "flex flex-col gap-1",
    fullWidth ? "w-full" : "w-auto"
  );

  const inputWrapperStyles = clsx(
    "flex items-center relative",
    fullWidth ? "w-full" : "w-auto"
  );

  const inputStyles = clsx(
    baseStyles,
    variantStyles[variant],
    sizeStyles[size],
    disabled && "bg-gray-100 cursor-not-allowed opacity-70",
    readOnly && "bg-gray-50 text-gray-500",
    fullWidth ? "w-full" : "w-auto",
    leftIcon ? "pl-10" : "pl-3",
    rightIcon ? "pr-10" : "pr-3",
    className
  );

  return (
    <div className={wrapperStyles}>
      {label && (
        <label className="text-sm font-medium text-neutral-dark">
          {label}
        </label>
      )}

      <div className={inputWrapperStyles}>
        {leftIcon && (
          <span className="absolute left-3 text-gray-400">{leftIcon}</span>
        )}
        <input
          type={type}
          value={value}
          placeholder={placeholder}
          onChange={onChange}
          disabled={disabled}
          readOnly={readOnly}
          className={inputStyles}
          {...props}
        />
        {rightIcon && (
          <span className="absolute right-3 text-gray-400">{rightIcon}</span>
        )}
      </div>

      {error && <span className="text-xs text-danger">{error}</span>}
      {success && !error && (
        <span className="text-xs text-green-600">{success}</span>
      )}
    </div>
  );
};

export default Input;
