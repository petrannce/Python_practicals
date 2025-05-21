import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")

clock_label = tk.Label(root, font=("calibri", 48, "bold"), background="black", foreground="cyan")
clock_label.pack(anchor="center", fill="both", expand=True)

# Function to update the time
def update_time():
    current_time = strftime("%H:%M:%S %p")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)  # Update every second

# Start updating the time
update_time()

root.mainloop()