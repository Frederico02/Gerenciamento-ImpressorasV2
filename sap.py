from tkinter import messagebox
import subprocess

def para_sap():
    subprocess.run(["net", "stop", "SAPSprint"],stdout=subprocess.DEVNULL, creationflags=subprocess.CREATE_NO_WINDOW)

def volta_sap():
    subprocess.run(["net", "start", "SAPSprint"], stdout=subprocess.DEVNULL, creationflags=subprocess.CREATE_NO_WINDOW)

def reinicia_sap():
    messagebox.showinfo("status", "Reiniciando SAPSprint")
    subprocess.run(["net", "stop", "SAPSprint"],stdout=subprocess.DEVNULL, creationflags=subprocess.CREATE_NO_WINDOW)
    subprocess.run(["net", "start", "SAPSprint"],stdout=subprocess.DEVNULL, creationflags=subprocess.CREATE_NO_WINDOW)
    messagebox.showinfo("status", "SAPSprint Reinciado")
