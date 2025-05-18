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

        tk.Label(root, text="Ambulance Routing System - RapidRoute",font=("Helvetica", 20, "bold"), bg="#f0f2f5", fg="#1a237e").pack(pady=10)
        self.canvas = tk.Canvas(root, width=700, height=500, bg="white", bd=2, relief=tk.SOLID)

       # self.canvas = tk.Canvas(root, width=1000, height=550, bg="white", bd=2, relief=tk.SOLID)
        self.canvas.pack(pady=10)

        self.start_var = tk.StringVar()
        self.end_var = tk.StringVar()

        # location_names = [n for n in nodes if nodes[n]['type'] == 'location']
        #  hospital_names = [n for n in nodes if nodes[n]['type'] == 'hospital']


        location_names = []
        for n in nodes:
            if nodes[n]['type'] == 'location':
                location_names.append(n)

        hospital_names = []
        for n in nodes:
            if nodes[n]['type'] == 'hospital':
                    hospital_names.append(n)


        frame = tk.Frame(root, bg="#f0f2f5")
        frame.pack(pady=10)

        # Start Location dropdown
        ttk.Label(frame, text="Start Location:").grid(row=0, column=0, padx=5)
        ttk.Combobox(frame, textvariable=self.start_var, values=location_names, width=30).grid(row=0, column=1, padx=5)

        # Hospital dropdown
        ttk.Label(frame, text="Hospital:").grid(row=0, column=2, padx=5)
        ttk.Combobox(frame, textvariable=self.end_var, values=hospital_names, width=30).grid(row=0, column=3, padx=5)

        # Button
        ttk.Button(frame, text="Find Shortest Path", command=self.find_path).grid(row=0, column=4, padx=10)

        # Result Label
        self.result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f2f5", fg="#2e7d32", wraplength=1000)
        self.result_label.pack(pady=5)

        # Footer
        self.footer = tk.Label(root, text="Made by Team PathPulse | Team ID: DAA-IV-T159",font=("Arial", 10), bg="#f0f2f5", fg="gray")
        self.footer.pack(side=tk.BOTTOM, pady=5)

        self.draw_graph()

    def draw_graph(self):
        self.canvas.delete("all")

        # Draw all edges first
        for src, neighbors in backend.edges.items():
            x1, y1 = nodes[src]['coords']
            for dest in neighbors:
                x2, y2 = nodes[dest]['coords']
                self.canvas.create_line(x1, y1, x2, y2, fill="#9e9e9e")

        # Draw nodes
        for node, data in nodes.items():
            x, y = data['coords']
            color = "red" if data['type'] == "hospital" else "blue"
            self.canvas.create_oval(x-6, y-6, x+6, y+6, fill=color, outline="black")
            self.canvas.create_text(x + 10, y - 10, text=node, font=("Arial", 8), anchor="w")

    def find_path(self):
        start = self.start_var.get()
        end = self.end_var.get()
        if not start or not end:
            messagebox.showerror("Input Error", "Please select both a start location and a hospital.")
            return

        distance, path = dijkstra(start, end)
        if distance == float("inf") or not path:
            self.result_label.config(text="No path found.", fg="red")
            return

        self.draw_graph()

        # Draw shortest path
        for i in range(len(path) - 1):
            x1, y1 = nodes[path[i]]["coords"]
            x2, y2 = nodes[path[i + 1]]["coords"]
            self.canvas.create_line(x1, y1, x2, y2, fill="green", width=3)

        self.result_label.config(
            text=f"Shortest path: {' ➝ '.join(path)}\n\n Total Distance: {distance} km", fg="#2e7d32"
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = AmbulanceRoutingApp(root)
    root.mainloop()
