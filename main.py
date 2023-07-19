from tkinter import messagebox
import tkinter as tk

from gets import get_ip_address, get_mac_address, get_hostname
from spool import reiniciar_spool, limpar_spool
from sap import reinicia_sap
from geral import geral
from calibrarZebra import TelaSecundaria

# Cria uma janela Principal
class TelaPrincipal:
    def __init__(self, janela):
        self.janela = janela
        janela.geometry("250x450")  # aumenta a altura da janela para 400 pixels
        janela.title("Destrava de Impressoras")

        ipv4 = get_ip_address()
        mac = get_mac_address()
        hostname = get_hostname()

        frame_botoes = tk.Frame(self.janela)
        frame_botoes.pack()

        botao_reiniciar_spool = tk.Button(frame_botoes, text="Reiniciar Spooler", command=reiniciar_spool)
        botao_reiniciar_spool.pack(pady=5, padx=10, fill=tk.X)

        botao_reinicia_sap = tk.Button(frame_botoes, text="Reiniciar SAPSprint", command=reinicia_sap)
        botao_reinicia_sap.pack(pady=5, padx=10, fill=tk.X)

        botao_limpar_spool = tk.Button(frame_botoes, text="Limpar Fila", command= limpar_spool)
        botao_limpar_spool.pack(pady=5, padx=10, fill=tk.X)

        botao_geral = tk.Button(frame_botoes, text="Execultar Todas opções", command=executar_todas_opcoes)
        botao_geral.pack(pady=5, padx=10, fill=tk.X)

        botao_outra_tela = tk.Button(frame_botoes, text="Calibrar Zebra", command=abrir_outra_tela)
        botao_outra_tela.pack(pady=5, padx=10, fill=tk.X)

        botao_sair = tk.Button(self.janela, text="Encerrar programa", command= self.janela.quit)
        botao_sair.pack(side=tk.BOTTOM, pady=5)

        label_ip = tk.Label(self.janela, text="IP: {}".format(ipv4))
        label_ip.pack(pady=5)

        label_mac = tk.Label(self.janela, text="MAC: {}".format(mac))
        label_mac.pack(pady=5)

        label_hostname = tk.Label(self.janela, text="Hostname: {}".format(hostname))
        label_hostname.pack(pady=5)

        canvas = tk.Canvas(self.janela, width=200, height=100)
        canvas.pack(pady=5)

        copyright = canvas.create_text(100, 90, text="© DEV Frederico- MULTITECH 2023")


def encerrar():
    TelaPrincipal.janela.destroy()
def mostrar_mensagem_conclusao():
    messagebox.showinfo("Mensagem", "Processo concluído!")

def executar_todas_opcoes():
    geral()
    janela_principal.after(100, mostrar_mensagem_conclusao)

def abrir_outra_tela():
    outra_janela = tk.Toplevel(janela_principal)  # Cria uma nova janela secundária
    tela_secundaria = TelaSecundaria(outra_janela)  # Instancia a classe da outra tela


# Cria uma janela Principal
janela_principal = tk.Tk()
tela_principal = TelaPrincipal(janela_principal)
janela_principal.mainloop()
