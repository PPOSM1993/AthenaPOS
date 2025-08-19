# AthenaPOS 📚💳  
**Point of Sale para Librerías y Papelerías**  

AthenaPOS es un sistema de **punto de venta (POS)** diseñado especialmente para **librerías y papelerías**, permitiendo la gestión integral de productos como libros, agendas, marcadores, plumas, juegos de mesa y mucho más.  

El sistema está dividido en **backend (Django Rest Framework)** y **frontend (React + Vite)**, integrando un stack moderno y escalable para cubrir procesos de **inventario, facturación, clientes, ventas y reportes**.  

---

## 🚀 Tecnologías utilizadas  

### Backend
- **Python 3**
- **Django 5 + Django Rest Framework**
- **PostgreSQL**
- **JWT Authentication**
- **Swagger / Redoc** (documentación de API)
- **Docker & Docker Compose**

### Frontend
- **JavaScript (ESNext)**
- **React + Vite**
- **TailwindCSS / Material UI**
- **TanStack Query**
- **Zustand (state management)**
- **Atomic Design Pattern**

### DevOps & Herramientas
- **Docker**
- **Git & GitHub**
- **Prettier / ESLint**
- **Conventional Commits**
- **CI/CD (GitHub Actions – futuro)**

---

## 🎯 Objetivos del proyecto  

### Objetivo General
Desarrollar un sistema de punto de venta especializado en librerías y papelerías, que permita la gestión integral de productos, clientes y ventas, optimizando los procesos internos y mejorando la experiencia de compra.  

### Objetivos Específicos
- Gestionar inventario de productos (libros, papelería, juegos de mesa, etc.).  
- Permitir operaciones de venta rápidas con carrito de compras.  
- Administrar clientes y facturación.  
- Generar reportes de ventas e inventario.  
- Contar con un sistema seguro de autenticación y roles.  
- Implementar un frontend moderno, rápido y responsive.  

---

📌 Roadmap

 - Configuración inicial del backend con Django + DRF.
 - Modelo de usuarios y roles.
 - CRUD de productos.
 - Carrito de ventas y facturación.
 - Integración frontend-backend.
 - Reportes de ventas.
 - Despliegue en producción con Docker.

---

## 📂 Estructura del Proyecto


athenapos/
│── backend/ # API REST con Django + DRF
│ ├── accounts/ # Usuarios, roles, permisos
│ ├── products/ # Libros, agendas, accesorios
│ ├── sales/ # Carrito, facturación y ventas
│ ├── settings/ # Configuración modular (dev/prod)
│ └── ...
│
│── frontend/ # Interfaz en React + Vite
│ ├── src/
│ │ ├── assets/ # Estilos, imágenes, íconos
│ │ ├── components/ # Atomic design components
│ │ ├── features/ # Funcionalidades por dominio
│ │ └── pages/ # Vistas principales
│
│── docs/ # Documentación del proyecto
│── docker-compose.yml
│── README.md


---

## ⚙️ Instalación y Configuración  

### Clonar el repositorio
```bash
git clone https://github.com/tuusuario/athenapos.git
cd athenapos

Backend
cd backend
docker-compose up --build


Frontend
cd frontend
npm install
npm run dev
