from tkinter import messagebox

def calibracao():
    # Configuração da porta da impressora
    port = "LPT2"  # Altere para a porta correta da sua impressora

    # Etiqueta
    zpl_command = '''
        ^XA^JUS^XZ
    '''

    # Abre o arquivo de porta da impressora e envia o comando ZPL
    with open(port, "wb") as printer:
        printer.write(zpl_command.encode("utf-8"))


    messagebox.showinfo("Mensagem", "Processo concluído!")
