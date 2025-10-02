import { create } from "zustand";
import {jwtDecode} from "jwt-decode";


interface TokenPayload {
  sub: string; // email
  role: string;
  exp: number;
}

export function getUserFromToken(token: string) {
  const decoded: TokenPayload = jwtDecode(token);
  return {
    email: decoded.sub,
    role: decoded.role
  };
}

interface AuthState {
  token: string | null;
  user: { email: string; role: string } | null;
  login: (token: string) => void;
  logout: () => void;
}

export const useAuthStore = create<AuthState>((set) => ({
  token: localStorage.getItem("access_token"),
  user: localStorage.getItem("access_token")
    ? getUserFromToken(localStorage.getItem("access_token")!)
    : null,
  login: (token) => {
    const user = getUserFromToken(token);
    localStorage.setItem("access_token", token);
    set({ token, user });
  },
  logout: () => {
    localStorage.removeItem("access_token");
    set({ token: null, user: null });
  },
}));
