import { create } from "zustand";

export const useAuthStore = create((set) => ({
  user: null,
  accessToken: null,
  refreshToken: null,

  setAuth: (data) =>
    set({
      user: data.user || null,
      accessToken: data.access,
      refreshToken: data.refresh,
    }),

  logout: () =>
    set({
      user: null,
      accessToken: null,
      refreshToken: null,
    }),
}));
