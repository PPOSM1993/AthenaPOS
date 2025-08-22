// src/playground/Playground.jsx
import {
  ButtonShowcase,
  InputShowcase,
  LabelShowcase
} from "../index";

export default function Playground() {
  return (
    <div className="p-8 space-y-10">
      <h1 className="text-3xl font-bold">Playground</h1>
      <ButtonShowcase />
      <InputShowcase />
      <LabelShowcase />
    </div>
  );
}
