// src/components/atoms/InputShowcase.jsx
import React from "react";
import Input from "../Input";
import { Search, Mail, Lock } from "lucide-react";

const InputShowcase = () => {
  return (
    <div className="p-8 space-y-10 bg-gray-50 min-h-screen">
      <h1 className="text-2xl font-bold text-gray-800">Input Showcase</h1>

      {/* Variants */}
      <section className="space-y-4">
        <h2 className="text-lg font-semibold text-gray-700">Variants</h2>
        <div className="flex flex-col gap-4 max-w-md">
          <Input placeholder="Default input" />
          <Input placeholder="Danger input" variant="danger" />
          <Input placeholder="Success input" variant="success" />
          <Input placeholder="Primary input" variant="primary" />
          <Input placeholder="Neutral input" variant="neutral" />
        </div>
      </section>

      {/* Sizes */}
      <section className="space-y-4">
        <h2 className="text-lg font-semibold text-gray-700">Sizes</h2>
        <div className="flex flex-col gap-4 max-w-md">
          <Input placeholder="Small input" size="sm" />
          <Input placeholder="Medium input" size="md" />
          <Input placeholder="Large input" size="lg" />
        </div>
      </section>

      {/* With Icons */}
      <section className="space-y-4">
        <h2 className="text-lg font-semibold text-gray-700">With Icons</h2>
        <div className="flex flex-col gap-4 max-w-md">
          <Input placeholder="Search..." leftIcon={<Search size={16} />} />
          <Input placeholder="Email" leftIcon={<Mail size={16} />} />
          <Input
            type="password"
            placeholder="Password"
            leftIcon={<Lock size={16} />}
            rightIcon={
              <span className="text-xs cursor-pointer text-gray-500 hover:text-gray-700">
                👁
              </span>
            }
          />
        </div>
      </section>

      {/* Disabled */}
      <section className="space-y-4">
        <h2 className="text-lg font-semibold text-gray-700">Disabled</h2>
        <div className="max-w-md">
          <Input placeholder="Disabled input" disabled fullWidth />
        </div>
      </section>
    </div>
  );
};

export default InputShowcase;
