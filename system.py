# import tkinter as tk
# from tkinter import messagebox
# from PIL import Image, ImageTk
# import random

# class RoverControlSystem:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Rover Control System")
#         self.root.geometry("900x650")
#         self.root.configure(bg="black")

#         # Frames
#         self.control_frame = tk.Frame(self.root, bg="gray20", width=200, height=650)
#         self.control_frame.pack(side="left", fill="y")

#         self.display_frame = tk.Frame(self.root, bg="black")
#         self.display_frame.pack(side="right", expand=True, fill="both")

#         # Canvas for display
#         self.canvas = tk.Canvas(self.display_frame, bg="white")
#         self.canvas.pack(fill="both", expand=True)

#         # Load background image
#         self.bg_img = Image.open("C:/Users/Lenovo/OneDrive/Desktop/Anant_Photo/Obstacle_BK.jpg").resize((700, 650))
#         self.bg_img = ImageTk.PhotoImage(self.bg_img)
#         self.bg_id = self.canvas.create_image(0, 0, image=self.bg_img, anchor="nw")

#         # Load rover image
#         self.rover_img = Image.open("C:/Users/Lenovo/OneDrive/Desktop/Anant_Photo/Rover_image.jpg").resize((60, 60))
#         self.rover_img = ImageTk.PhotoImage(self.rover_img)

#         self.rover_x = 350
#         self.rover_y = 560
#         self.rover = self.canvas.create_image(self.rover_x, self.rover_y, image=self.rover_img)

#         self.obstacles = []
#         self.throttle_on = False
#         self.ca_on = False

#         # Control panel
#         tk.Label(self.control_frame, text="CONTROL PANEL", fg="white", bg="gray20", font=("Arial", 12, "bold")).pack(pady=10)

#         # Throttle
#         tk.Label(self.control_frame, text="Throttle", fg="white", bg="gray20", font=("Arial", 11, "bold")).pack(pady=5)
#         tk.Button(self.control_frame, text="ON", width=12, command=self.start_throttle).pack(pady=2)
#         tk.Button(self.control_frame, text="OFF", width=12, command=self.stop_throttle).pack(pady=2)

#         # Rudder
#         tk.Label(self.control_frame, text="Rudder", fg="white", bg="gray20", font=("Arial", 11, "bold")).pack(pady=5)
#         self.rudder_angle = tk.Entry(self.control_frame, width=12)
#         self.rudder_angle.pack(pady=2)
#         tk.Button(self.control_frame, text="Set Angle", width=12, command=self.set_rudder).pack(pady=2)

#         # Collision Avoidance
#         tk.Label(self.control_frame, text="Collision Avoidance", fg="white", bg="gray20", font=("Arial", 11, "bold")).pack(pady=10)
#         tk.Button(self.control_frame, text="CA-ON", width=12, command=self.ca_enable).pack(pady=2)
#         tk.Button(self.control_frame, text="CA-OFF", width=12, command=self.ca_disable).pack(pady=2)

#     def start_throttle(self):
#         self.throttle_on = True
#         self.generate_obstacle()

#     def stop_throttle(self):
#         self.throttle_on = False

#     def set_rudder(self):
#         try:
#             angle = int(self.rudder_angle.get())
#             messagebox.showinfo("Rudder", f"Rudder set to {angle}°")
#         except ValueError:
#             messagebox.showwarning("Invalid Input", "Please enter a valid angle.")

#     def ca_enable(self):
#         self.ca_on = True
#         messagebox.showinfo("CA", "Collision Avoidance Activated")

#     def ca_disable(self):
#         self.ca_on = False
#         messagebox.showinfo("CA", "Collision Avoidance Deactivated")

#     def generate_obstacle(self):
#         if self.throttle_on:
#             x = random.randint(50, 650)
#             obs = self.canvas.create_oval(x, 0, x+40, 40, fill="red")
#             self.obstacles.append(obs)
#             self.move_obstacle(obs)
#             self.root.after(2000, self.generate_obstacle)

#     def move_obstacle(self, obs):
#         def step():
#             if obs not in self.obstacles:
#                 return
#             self.canvas.move(obs, 0, 5)
#             pos = self.canvas.coords(obs)
#             if pos[3] >= 650:
#                 self.canvas.delete(obs)
#                 self.obstacles.remove(obs)
#                 return
#             # Collision check
#             rover_coords = self.canvas.coords(self.rover)
#             rx, ry = rover_coords
#             if abs(pos[0] - rx) < 40 and abs(pos[1] - ry) < 40:
#                 if self.ca_on:
#                     self.avoid_collision()
#                 else:
#                     messagebox.showwarning("Collision!", "Rover Hit an Obstacle!")
#                     self.stop_throttle()
#                     return
#             self.root.after(30, step)
#         step()

#     def avoid_collision(self):
#         shift = random.choice([-60, 60])  # left or right move
#         new_x = self.rover_x + shift
#         if 50 < new_x < 650:  # stay inside canvas
#             self.rover_x = new_x
#             self.canvas.coords(self.rover, self.rover_x, self.rover_y)

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = RoverControlSystem(root)
#     root.mainloop()


import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import random

# --- Config ---
WINDOW_W, WINDOW_H = 900, 600
OBSTACLE_SIZE = 50
ROVER_SIZE = 70

class RoverSim:
    def __init__(self, root):
        self.root = root
        self.root.title("🚀 Rover Simulation")
        self.root.geometry(f"{WINDOW_W}x{WINDOW_H}")
        self.root.configure(bg="#1e1e2f")

        # --- Canvas Simulation Area ---
        self.canvas = tk.Canvas(root, width=650, height=WINDOW_H, bg="black", highlightthickness=0)
        self.canvas.pack(side="right", fill="both", expand=True)

        # Background image
        bg_img = Image.open("C:/Users/Lenovo/OneDrive/Desktop/Anant_Photo/Obstacle_BK.jpg")
        bg_img = bg_img.resize((650, WINDOW_H))
        self.bg_img = ImageTk.PhotoImage(bg_img)
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg_img)

        # Rover image
        rover_img = Image.open("C:/Users/Lenovo/OneDrive/Desktop/Anant_Photo/Rover_image.jpg")
        rover_img = rover_img.resize((ROVER_SIZE, ROVER_SIZE))
        self.rover_img = ImageTk.PhotoImage(rover_img)
        self.rover_x = 325
        self.rover_y = WINDOW_H - 100
        self.rover = self.canvas.create_image(self.rover_x, self.rover_y, image=self.rover_img)

        # Control variables
        self.throttle_on = False
        self.ca_on = False
        self.obstacles = []

        # --- Left Control Panel ---
        control_frame = tk.Frame(root, bg="#252540", padx=15, pady=15)
        control_frame.pack(side="left", fill="y")

        tk.Label(control_frame, text="🎛️ Controls", fg="white", bg="#252540",
                 font=("Arial", 16, "bold")).pack(pady=10)

        # Throttle Buttons
        self.throttle_on_btn = ttk.Button(control_frame, text="Throttle ON", command=self.throttle_on_func)
        self.throttle_on_btn.pack(pady=10, ipadx=10, ipady=5)
        self.throttle_off_btn = ttk.Button(control_frame, text="Throttle OFF", command=self.throttle_off_func)
        self.throttle_off_btn.pack(pady=10, ipadx=10, ipady=5)

        # Rudder Controls
        tk.Label(control_frame, text="Rudder Angle", fg="white", bg="#252540").pack(pady=5)
        self.rudder_entry = ttk.Entry(control_frame, width=10)
        self.rudder_entry.pack(pady=5)
        ttk.Button(control_frame, text="Set Angle", command=self.set_rudder).pack(pady=5)

        # --- Bottom Collision Avoidance (Remote-like) ---
        ca_frame = tk.Frame(root, bg="#1e1e2f")
        ca_frame.place(relx=0.5, rely=0.92, anchor="center")

        self.ca_on_btn = ttk.Button(ca_frame, text="CA-ON", command=self.ca_on_func)
        self.ca_on_btn.grid(row=0, column=0, padx=20, ipadx=15, ipady=10)

        self.ca_off_btn = ttk.Button(ca_frame, text="CA-OFF", command=self.ca_off_func)
        self.ca_off_btn.grid(row=0, column=1, padx=20, ipadx=15, ipady=10)

        # Start game loop
        self.update_game()

    # --- Throttle Functions ---
    def throttle_on_func(self):
        self.throttle_on = True

    def throttle_off_func(self):
        self.throttle_on = False

    # --- Rudder Function ---
    def set_rudder(self):
        try:
            angle = int(self.rudder_entry.get())
            self.rover_x += angle
            if self.rover_x < 0: self.rover_x = 0
            if self.rover_x > 650: self.rover_x = 650
            self.canvas.coords(self.rover, self.rover_x, self.rover_y)
        except:
            messagebox.showerror("Error", "Enter a valid integer angle")

    # --- Collision Avoidance ---
    def ca_on_func(self):
        self.ca_on = True

    def ca_off_func(self):
        self.ca_on = False

    # --- Obstacles ---
    def spawn_obstacle(self):
        x = random.randint(50, 600)
        obs = self.canvas.create_rectangle(x, 0, x + OBSTACLE_SIZE, OBSTACLE_SIZE, fill="red", outline="")
        self.obstacles.append(obs)

    def move_obstacles(self):
        for obs in self.obstacles[:]:
            self.canvas.move(obs, 0, 10)
            ox1, oy1, ox2, oy2 = self.canvas.coords(obs)
            rx1, ry1, rx2, ry2 = self.rover_x - ROVER_SIZE//2, self.rover_y - ROVER_SIZE//2, self.rover_x + ROVER_SIZE//2, self.rover_y + ROVER_SIZE//2

            # Collision check
            if oy2 >= self.rover_y - ROVER_SIZE//2:
                if self.ca_on:
                    # Auto-avoid
                    shift = 100 if self.rover_x < 325 else -100
                    self.rover_x += shift
                    if self.rover_x < 0: self.rover_x = 0
                    if self.rover_x > 650: self.rover_x = 650
                    self.canvas.coords(self.rover, self.rover_x, self.rover_y)
                    self.canvas.delete(obs)
                    self.obstacles.remove(obs)
                    continue
                else:
                    self.canvas.itemconfig(obs, fill="yellow")  # mark collision

            # Remove if passed
            if oy1 > WINDOW_H:
                self.canvas.delete(obs)
                self.obstacles.remove(obs)

    # --- Game Loop ---
    def update_game(self):
        if self.throttle_on and len(self.obstacles) < 5:
            if random.randint(1, 10) == 1:
                self.spawn_obstacle()
        self.move_obstacles()
        self.root.after(100, self.update_game)

# --- Run App ---
root = tk.Tk()
style = ttk.Style()
style.configure("TButton", font=("Arial", 12, "bold"), padding=6)
app = RoverSim(root)
root.mainloop()
