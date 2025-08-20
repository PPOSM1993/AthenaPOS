import axios from "axios";

const API_URL = "http://localhost:8000/api/authentication"; // Ajusta al prefijo correcto

export const login = async (username, password) => {
  const response = await axios.post(`${API_URL}/login/`, {
    username,
    password,
  });
  return response.data;
};