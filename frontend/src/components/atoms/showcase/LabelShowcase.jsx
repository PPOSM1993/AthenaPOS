import React from "react";
import {Label} from "../../../index";

const LabelShowcase = () => {
  return (
    <div className="p-8 space-y-10 bg-gray-50 min-h-screen">
      <h1 className="text-2xl font-bold text-gray-800">Label Showcase</h1>

      {/* Variants */}
      <section className="space-y-4">
        <h2 className="text-lg font-semibold text-gray-700">Variants</h2>
        <div className="space-y-2">
          <Label htmlFor="default">Default Label</Label>
          <Label htmlFor="error" variant="error">Error Label</Label>
          <Label htmlFor="success" variant="success">Success Label</Label>
          <Label htmlFor="disabled" variant="disabled">Disabled Label</Label>
        </div>
      </section>

      {/* Sizes */}
      <section className="space-y-4">
        <h2 className="text-lg font-semibold text-gray-700">Sizes</h2>
        <div className="space-y-2">
          <Label size="sm">Small Label</Label>
          <Label size="md">Medium Label</Label>
          <Label size="lg">Large Label</Label>
        </div>
      </section>

      {/* Required */}
      <section className="space-y-4">
        <h2 className="text-lg font-semibold text-gray-700">Required</h2>
        <Label required htmlFor="email">Email</Label>
      </section>
    </div>
  );
};

export default LabelShowcase;
