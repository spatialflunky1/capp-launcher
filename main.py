import parse_files
import tkinter as tk
import os

apps = parse_files.get_apps()
root = tk.Tk()
root.geometry("640x480")
root.title("Cool Application Launcher")

app_buttons = []

for app in apps:
    if app["Type"] == "Application" and "Exec" in app:
        app_name = tk.Button(text=app["Name"], command=lambda run = app["Exec"]: os.system(run))
        app_name.pack(anchor="w")
        app_buttons.append(app_name)
root.mainloop()