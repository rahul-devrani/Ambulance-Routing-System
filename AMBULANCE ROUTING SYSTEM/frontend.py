# frontend.py
import backend
import tkinter as tk
from tkinter import ttk, messagebox
from backend import nodes, dijkstra

class AmbulanceRoutingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🚑 Ambulance Routing System - RapidRoute")
        self.root.geometry("1100x750")
        self.root.configure(bg="#9bb8e4")

        tk.Label(root, text="Ambulance Routing System - RapidRoute", 
                 font=("Helvetica", 20, "bold"), bg="#f0f2f5", fg="#1a237e").pack(pady=10)
        
        self.canvas = tk.Canvas(root, width=740, height=440, bg="white", bd=2, relief=tk.SOLID)
        self.canvas.pack(pady=10)

        self.start_var = tk.StringVar()
        self.end_var = tk.StringVar()
        self.stop_at_first_var = tk.BooleanVar()

        location_names = [n for n in nodes if nodes[n]['type'] == 'location']
        hospital_names = [n for n in nodes if nodes[n]['type'] == 'hospital']

        frame = tk.Frame(root, bg="#f0f2f5")
        frame.pack(pady=10)

        ttk.Label(frame, text="Start Location:").grid(row=0, column=0, padx=5)
        ttk.Combobox(frame, textvariable=self.start_var, values=location_names, width=30).grid(row=0, column=1, padx=5)

        ttk.Label(frame, text="Hospital:").grid(row=0, column=2, padx=5)
        ttk.Combobox(frame, textvariable=self.end_var, values=hospital_names, width=30).grid(row=0, column=3, padx=5)

        ttk.Checkbutton(frame, text="Stop at First Hospital Encountered", variable=self.stop_at_first_var).grid(row=0, column=4, padx=10)

        ttk.Button(frame, text="Find Shortest Path", command=self.find_path).grid(row=0, column=5, padx=10)
        ttk.Button(frame, text="Find Nearest Hospital", command=self.find_nearest).grid(row=0, column=6, padx=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f2f5", fg="#2e7d32", wraplength=1000)
        self.result_label.pack(pady=5)

        self.footer = tk.Label(root, text="Made by Team PathPulse | Team ID: DAA-IV-T159",font=("Arial", 10), bg="#f0f2f5", fg="gray")
        self.footer.pack(side=tk.BOTTOM, pady=5)

        self.draw_graph()

    def draw_graph(self):
        self.canvas.delete("all")

        for src, neighbors in backend.edges.items():
            x1, y1 = nodes[src]['coords']
            for dest, dist in neighbors.items():
                x2, y2 = nodes[dest]['coords']
                self.canvas.create_line(x1, y1, x2, y2, fill="#9e9e9e")
                mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
                self.canvas.create_text(mid_x, mid_y, text=str(dist), fill="gray", font=("Arial", 7))

        for node, data in nodes.items():
            x, y = data['coords']
            color = "red" if data['type'] == "hospital" else "blue"
            self.canvas.create_oval(x-6, y-6, x+6, y+6, fill=color, outline="black")
            self.canvas.create_text(x + 10, y - 10, text=node, font=("Arial", 8), anchor="w")

    def highlight_path(self, path):
        for i in range(len(path) - 1):
            x1, y1 = nodes[path[i]]["coords"]
            x2, y2 = nodes[path[i + 1]]["coords"]
            self.canvas.create_line(x1, y1, x2, y2, fill="green", width=3)

    def find_path(self):
        start = self.start_var.get()
        end = self.end_var.get()
        stop_at_first = self.stop_at_first_var.get()

        if not start:
            messagebox.showerror("Input Error", "Please select a start location.")
            return
        if not end:
            messagebox.showerror("Input Error", "Please select a hospital.")
            return

        self.draw_graph()

        total_distance, full_path = dijkstra(start, end)

        if total_distance == float("inf") or not full_path:
            self.result_label.config(text="No path found.", fg="red")
            return

        if stop_at_first:
            for i in range(1, len(full_path)):
                if nodes[full_path[i]]["type"] == "hospital":
                    truncated_path = full_path[:i+1]
                    truncated_distance = 0
                    for j in range(len(truncated_path) - 1):
                        truncated_distance += backend.edges[truncated_path[j]][truncated_path[j + 1]]
                    self.highlight_path(truncated_path)
                    self.result_label.config(
                        text=f"Stopped at first hospital: {full_path[i]}\n\n"
                             f"Path: {' ➝ '.join(truncated_path)}\n\n"
                             f"Distance: {truncated_distance} km",
                        fg="#2e7d32"
                    )
                    return
            self.result_label.config(text="No hospital found on the path.", fg="red")
        else:
            self.highlight_path(full_path)
            self.result_label.config(
                text=f"Shortest path to {end}:\n\n {' ➝ '.join(full_path)}\n\nTotal Distance: {total_distance} km",
                fg="#2e7d32"
            )

    def find_nearest(self):
        start = self.start_var.get()
        if not start:
            messagebox.showerror("Input Error", "Please select a start location.")
            return

        hospital, distance, path = backend.find_nearest_hospital(start)
        if hospital is None:
            messagebox.showinfo("No Hospital Found", "No hospital found reachable from this location.")
            return

        self.draw_graph()
        self.highlight_path(path)

        self.result_label.config(
            text=f"Nearest hospital from {start} is {hospital}\n"
                 f"\nPath: {' ➝ '.join(path)}\n\nTotal Distance: {distance} km",
            fg="#2e7d32"
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = AmbulanceRoutingApp(root)
    root.mainloop()
