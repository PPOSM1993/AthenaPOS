// src/components/atoms/ButtonShowcase.jsx
import React from "react";
import { Button } from "../../../index";
const ButtonShowcase = () => {
  return (
    <div className="p-6 space-y-6">
      {/* Variants */}
      <div>
        <h2 className="text-lg font-semibold mb-2">Variants</h2>
        <div className="flex gap-4 flex-wrap">
          <Button variant="primary">Primary</Button>
          <Button variant="secondary">Secondary</Button>
          <Button variant="danger">Danger</Button>
          <Button variant="neutral">Neutral</Button>
        </div>
      </div>

      {/* Sizes */}
      <div>
        <h2 className="text-lg font-semibold mb-2">Sizes</h2>
        <div className="flex gap-4 items-center">
          <Button size="sm">Small</Button>
          <Button size="md">Medium</Button>
          <Button size="lg">Large</Button>
        </div>
      </div>

      {/* Disabled */}
      <div>
        <h2 className="text-lg font-semibold mb-2">Disabled</h2>
        <div className="flex gap-4 flex-wrap">
          <Button variant="primary" disabled>
            Primary Disabled
          </Button>
          <Button variant="secondary" disabled>
            Secondary Disabled
          </Button>
          <Button variant="danger" disabled>
            Danger Disabled
          </Button>
          <Button variant="neutral" disabled>
            Neutral Disabled
          </Button>
        </div>
      </div>

      {/* Full Width */}
      <div>
        <h2 className="text-lg font-semibold mb-2">Full Width</h2>
        <Button variant="primary" fullWidth>
          Full Width Button
        </Button>
      </div>
    </div>
  );
};

export default ButtonShowcase;
