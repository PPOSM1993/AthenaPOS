import React from "react";
import clsx from "clsx";

const Label = ({
    children,
    htmlFor,
    size = "md",
    variant = "default",
    required = false,
    disabled = false,
    className = "",
}) => {
    const baseStyles = "block font-medium";

    const sizeStyles = {
        sm: "text-xs",
        md: "text-sm",
        lg: "text-base",
    };

    const variantStyles = {
        default: "text-gray-700",
        error: "text-red-600",
        success: "text-green-600",
        disabled: "text-gray-400 cursor-not-allowed",
    };

    return (
        <label
            htmlFor={htmlFor}
            className={clsx(
                baseStyles,
                sizeStyles[size],
                disabled ? variantStyles.disabled : variantStyles[variant],
                className
            )}
        >
            {children}
            {required && <span className="text-red-500 ml-0.5">*</span>}
        </label>
    );
};

export default Label;
