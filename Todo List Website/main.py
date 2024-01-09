import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        tasks.pop(selected_task_index[0])
        update_listbox()
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# Configure the main window
root = tk.Tk()
root.title("ToDo List App")
root.geometry("400x400")
root.configure(bg="#f2f2f2")

tasks = []

# Configure and style UI elements
font_style = ("Helvetica", 12)
bg_color = "#f2f2f2"
accent_color = "#3498db"

label = tk.Label(root, text="Enter Task:", font=font_style, bg=bg_color)
label.pack(pady=10)

entry = tk.Entry(root, width=40, font=font_style, bg="white", fg="black")
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task, font=font_style, bg=accent_color, fg="white")
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task, font=font_style, bg=accent_color, fg="white")
delete_button.pack(pady=5)

listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=10, font=font_style, bg="white", fg="black", selectbackground=accent_color)
listbox.pack(pady=10)

# Start the main loop
root.mainloop()