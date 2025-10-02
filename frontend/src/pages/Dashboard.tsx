import { useEffect, useState } from "react";
import api from "@/lib/axios";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { toast } from "sonner";

export default function Dashboard() {
  const [tasks, setTasks] = useState<any[]>([]);
  const [title, setTitle] = useState("");
  const [desc, setDesc] = useState("");

  async function fetchTasks() {
    try {
      const res = await api.get("/tasks/");
      setTasks(res.data);
    } catch {
      toast.error("Failed to load tasks");
    }
  }

  async function addTask() {
    try {
      await api.post("/tasks/", { title, description: desc, status: "pending" });
      toast.success("Task added!");
      setTitle("");
      setDesc("");
      fetchTasks();
    } catch {
      toast.error("Could not add task");
    }
  }

  async function toggleStatus(id: string, title: string, description: string, status: string) {
    try {
      await api.put(`/tasks/${id}`, { title, description, status });
      toast.success("Task updated!");
      fetchTasks();
    } catch {
      toast.error("Failed to update task");
    }
  }

  async function deleteTask(id: string) {
    try {
      await api.delete(`/tasks/${id}`);
      toast.success("Task deleted!");
      fetchTasks();
    } catch {
      toast.error("Failed to delete task");
    }
  }

  useEffect(() => {
    fetchTasks();
  }, []);

  return (
    <div className="p-6 max-w-2xl mx-auto space-y-4">
      <Card>
        <CardHeader>
          <CardTitle>Add Task</CardTitle>
        </CardHeader>
        <CardContent className="flex gap-2">
          <Input
            placeholder="Title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
          />
          <Input
            placeholder="Description"
            value={desc}
            onChange={(e) => setDesc(e.target.value)}
          />
          <Button onClick={addTask}>Add</Button>
        </CardContent>
      </Card>

      <Card>
        <CardHeader>
          <CardTitle>Tasks</CardTitle>
        </CardHeader>
        <CardContent>
          <ul className="space-y-2">
            {tasks.map((t) => (
              <li
                key={t.id}
                className="flex justify-between items-center border rounded p-2"
              >
                <span>
                  {t.title} -{" "}
                  <span className="text-sm text-gray-500">{t.status}</span>
                </span>
                <div className="flex gap-2">
                  <Button
                    size="sm"
                    variant="secondary"
                    onClick={() =>
                      toggleStatus(t.id, t.title, t.description, t.status === "pending" ? "completed" : "pending")
                    }
                  >
                    Toggle
                  </Button>
                  <Button
                    size="sm"
                    variant="destructive"
                    onClick={() => deleteTask(t.id)}
                  >
                    Delete
                  </Button>
                </div>
              </li>
            ))}
          </ul>
        </CardContent>
      </Card>
    </div>
  );
}
