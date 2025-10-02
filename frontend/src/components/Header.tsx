import { useState } from "react";
import { useAuthStore } from "@/store/authStore";
import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { toast } from "sonner";

export default function Header() {
  const { user, token, logout } = useAuthStore();
  const [showMenu, setShowMenu] = useState(false);

  function handleLogout() {
    logout();
    toast.success("Logged out successfully");
  }

  return (
    <header className="bg-gray-100 p-4 flex justify-between items-center shadow-md">
      <h1 className="text-xl font-bold">Task Manager</h1>
      {token && user && (
        <div className="relative">
          <Button
            variant="outline"
            onClick={() => setShowMenu((prev) => !prev)}
          >
            {user.email}
          </Button>
          {showMenu && (
            <Card className="absolute right-0 mt-2 w-48 p-3 shadow-lg">
              <p className="text-sm font-semibold">{user.email}</p>
              <p className="text-xs text-gray-500">{user.role}</p>
              <Button
                variant="destructive"
                size="sm"
                className="mt-2 w-full"
                onClick={handleLogout}
              >
                Logout
              </Button>
            </Card>
          )}
        </div>
      )}
    </header>
  );
}
