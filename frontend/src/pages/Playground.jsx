import { Plus, Trash2, Check, ArrowRight, Edit } from "lucide-react";
import {Button} from "../index";

export default function Playground() {
  return (
    <div className="p-8 space-y-10">
      {/* Variantes */}
      <section>
        <h2 className="text-xl font-bold mb-4">Variantes</h2>
        <div className="flex flex-wrap gap-4">
          <Button variant="primary">Primary</Button>
          <Button variant="secondary">Secondary</Button>
          <Button variant="success">Success</Button>
          <Button variant="danger">Danger</Button>
          <Button variant="accent">Accent</Button>
          <Button variant="outline">Outline</Button>
          <Button variant="ghost">Ghost</Button>
        </div>
      </section>

      {/* Tamaños */}
      <section>
        <h2 className="text-xl font-bold mb-4">Tamaños</h2>
        <div className="flex flex-wrap gap-4 items-center">
          <Button size="sm" variant="primary">Small</Button>
          <Button size="md" variant="primary">Medium</Button>
          <Button size="lg" variant="primary">Large</Button>
        </div>
      </section>

      {/* Con Iconos */}
      <section>
        <h2 className="text-xl font-bold mb-4">Con Iconos</h2>
        <div className="flex flex-wrap gap-4">
          <Button variant="primary" iconLeft={Plus}>Nuevo</Button>
          <Button variant="success" iconRight={Check}>Guardar</Button>
          <Button variant="danger" iconLeft={Trash2}>Eliminar</Button>
          <Button variant="secondary" iconLeft={Edit} iconRight={ArrowRight}>Editar</Button>
          <Button variant="ghost" iconRight={ArrowRight}>Ver más</Button>
        </div>
      </section>

      {/* Deshabilitados */}
      <section>
        <h2 className="text-xl font-bold mb-4">Deshabilitados</h2>
        <div className="flex flex-wrap gap-4">
          <Button variant="primary" disabled>Primary</Button>
          <Button variant="success" disabled iconRight={Check}>Guardar</Button>
          <Button variant="danger" disabled iconLeft={Trash2}>Eliminar</Button>
        </div>
      </section>
    </div>
  );
}
