"""A small Tkinter desktop GUI that runs locally on Windows."""

import tkinter as tk
from tkinter import messagebox


def update_message() -> None:
    name = name_input.get().strip()
    message = f"Hello, {name}! Your Tkinter application is running locally." if name else "Hello! Your Tkinter application is running locally."
    status_label.config(text=message)


def show_help() -> None:
    messagebox.showinfo("About", "This is a local Tkinter GUI demo. It does not need a browser or a cloud server.")


window = tk.Tk()
window.title("Tkinter Local GUI Demo")
window.geometry("500x300")
window.configure(bg="#f3f7fc")

tk.Label(window, text="Tkinter Local GUI Demo", font=("Segoe UI", 18, "bold"), bg="#f3f7fc", fg="#1d4ed8").pack(pady=(35, 8))
tk.Label(window, text="Enter your name and select the button.", font=("Segoe UI", 10), bg="#f3f7fc").pack(pady=4)

name_input = tk.Entry(window, width=34, font=("Segoe UI", 11))
name_input.pack(pady=10)
name_input.focus()

tk.Button(window, text="Show message", command=update_message, bg="#1d4ed8", fg="white", font=("Segoe UI", 10, "bold"), padx=14, pady=6).pack(pady=5)
status_label = tk.Label(window, text="Ready.", wraplength=430, font=("Segoe UI", 10), bg="#f3f7fc")
status_label.pack(pady=14)
tk.Button(window, text="About", command=show_help).pack()

window.mainloop()
