import subprocess

def geral():

    # Para SapsPrint
    subprocess.run(["net", "stop", "SAPSprint"], stdout=subprocess.DEVNULL, creationflags=subprocess.CREATE_NO_WINDOW)

    # Limpa fila
    subprocess.run(["cmd", "/c", "net stop spooler && del /F /Q %systemroot%\\System32\\spool\\PRINTERS\\* && net start spooler"],
                   stdout=subprocess.DEVNULL, creationflags=subprocess.CREATE_NO_WINDOW)
    # Para Spool
    subprocess.run(["net", "stop", "spooler"], stdout=subprocess.DEVNULL, creationflags=subprocess.CREATE_NO_WINDOW)

    # Inicia Spool
    subprocess.run(["net", "start", "spooler"], stdout=subprocess.DEVNULL, creationflags=subprocess.CREATE_NO_WINDOW)


    # Inicia SapsPrint
    subprocess.run(["net", "start", "SAPSprint"], stdout=subprocess.DEVNULL, creationflags=subprocess.CREATE_NO_WINDOW)