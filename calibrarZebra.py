import tkinter as tk
from calibracao import calibracao


class TelaSecundaria:
    def __init__(self, janela):
        self.janela = janela
        janela.geometry("310x300")
        janela.title("Calibração Zebras")

        # Cria uma etiqueta para exibir a impressora selecionada
        self.impressora_selecionada = tk.Label(janela, text="Nenhuma impressora selecionada")
        self.impressora_selecionada.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Cria uma etiqueta para exibir o item selecionado
        self.etiqueta = tk.Label(janela, text="Nenhum item selecionado")
        self.etiqueta.grid(row=0, column=0, columnspan=2, padx=10, pady=10)


        # Variável de controle para o item selecionado
        self.selecionado = tk.IntVar()

        # Variável de controle para a impressora selecionada
        self.impressora = tk.IntVar()

        def selecionar_item():
            item_selecionado = self.selecionado.get()
            if item_selecionado == 1:
                self.etiqueta.config(text="Zebra GC420t selecionada")
            elif item_selecionado == 2:
                self.etiqueta.config(text="Zebra ZD220 selecionada")

        def selecionar_impressora():
            impressora_selecionada = self.impressora.get()
            if impressora_selecionada == 1:
                self.impressora_selecionada.config(text="Zebra MASTER")
            elif impressora_selecionada == 2:
                self.impressora_selecionada.config(text="Zebra UNITARIA")

        # Cria os radio buttons para os itens
        rb_gc420t = tk.Radiobutton(janela, text="Zebra GC420t (Branca)", variable=self.selecionado, value=1,
                                   command=selecionar_item)
        rb_zd220 = tk.Radiobutton(janela, text="Zebra ZD220 (Preta)", variable=self.selecionado, value=2,
                                  command=selecionar_item)

        # Cria os radio buttons para os itens
        rb_master = tk.Radiobutton(janela, text="Zebra MASTER", variable=self.impressora, value=1,
                                   command=selecionar_impressora)
        rb_unitaria = tk.Radiobutton(janela, text="Zebra UNITARIA", variable=self.impressora, value=2,
                                  command=selecionar_impressora)


        # Posiciona os radio buttons na janela usando grid
        rb_gc420t.grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        rb_zd220.grid(row=2, column=1, sticky=tk.W, padx=10, pady=5)

        rb_master.grid(row=4, column=0, sticky=tk.W, padx=10, pady=5)
        rb_unitaria.grid(row=4, column=1, sticky=tk.W, padx=10, pady=5)


        botao_calibrar = tk.Button(janela, text="Calibrar", command=calibracao)
        botao_calibrar.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

        botao_voltar = tk.Button(janela, text="Voltar para a tela principal", command=self.voltar_tela_principal)
        botao_voltar.grid(row=7, column=0, columnspan=2, padx=10, pady=5)


    def voltar_tela_principal(self):
        self.janela.destroy()