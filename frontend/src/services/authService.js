import axios from "axios";

const API_URL = "http://localhost:8000/api"; // Ajusta tu backend

export const login = async (email, password) => {
  const response = await axios.post(`${API_URL}/token/`, {
    email,
    password,
  });
  return response.data;
};
