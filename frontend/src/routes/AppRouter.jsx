// AppRouter.jsx
import { Routes, Route, Navigate } from "react-router-dom"
import { useAuthStore } from "../index"
import {
  PrivateRoute,
  Login,
  Dashboard
} from "../index"

export default function AppRouter() {
  const isAuthenticated = useAuthStore((state) => state.isAuthenticated)

  return (
    <Routes>
      {/* 🔓 Rutas públicas */}
      <Route
        path="/login"
        element={isAuthenticated ? <Navigate to="/home" /> : <Login />}
      />
      <Route element={<PrivateRoute />}>
        <Route
          path="/dashboard" element={<Dashboard />}
        />
      </Route>

    </Routes>
  )
}