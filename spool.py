from tkinter import messagebox
import subprocess
from sap import para_sap, volta_sap


def reiniciar_spool():
    para_sap()
    messagebox.showinfo("status", "Reiniciando fila de impressão")
    subprocess.run(["net", "stop", "spooler"], stdout=subprocess.DEVNULL, creationflags=subprocess.CREATE_NO_WINDOW)
    subprocess.run(["net", "start", "spooler"], stdout=subprocess.DEVNULL, creationflags=subprocess.CREATE_NO_WINDOW)
    volta_sap()
    messagebox.showinfo("status", "Fila de impressão Reiniciada!")

def limpar_spool():
    messagebox.showinfo("status", "Limpando fila de impressão")
    subprocess.run(["cmd", "/c", "net stop spooler && del /F /Q %systemroot%\\System32\\spool\\PRINTERS\\* && net start spooler"],stdout=subprocess.DEVNULL, creationflags=subprocess.CREATE_NO_WINDOW)
    messagebox.showinfo("status", "Fila de impressão LIMPA!")
