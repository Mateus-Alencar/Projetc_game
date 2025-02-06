class Logica:
    def __init__(self, instancia):
        self.instancia = instancia

        # Inserir texto inicial
        self.inserir_texto_inicial()
        
        # Configurar progresso
        self.progresso_atual = 0
        self.progresso_total = 70  
        self.iniciar_barra()

    def inserir_texto_inicial(self):
        texto_inicial = """
        Bem-vindo ao Jogo!
        Aqui estão algumas instruções:
        
        1. Use as setas do teclado para digitar.
        2. Seja rápido e não cometa erros!

                                                                    Boa sorte!
        """
        self.instancia.text_box.insert("1.0", texto_inicial)
        self.instancia.text_box.insert("end", "\n" + " " * 61 + "Carregando Textos\n")

    def iniciar_barra(self): 
        if self.progresso_atual < self.progresso_total:
            self.instancia.text_box.insert("end", "=")
            self.progresso_atual += 1
            self.instancia.root.after(10, self.iniciar_barra)
        else:
            self.selecionar_op()


    def selecionar_op(self):
        op_text_dificuldade = """
        Selecione uma opção:
        Dificuldade:
        1 - Fácil
        2 - Médio
        3 - Difícil
        4 - Avançado
        """
        self.instancia.text_box.insert("end", "\n" + op_text_dificuldade)
        self.instancia.text_box.insert("end", "\nDigite sua escolha: ")
        self.etapa = "dificuldade"
        self.instancia.text_box.bind("<Return>", self.pegar_entrada)

    def selecionar_tx(self):
        op_text_texto = """
        Escolha um texto:
        a - Texto A
        b - Texto B
        c - Texto C
        d - Texto D
        """
        self.instancia.text_box.insert("end", "\n" + op_text_texto)
        self.instancia.text_box.insert("end", "\nDigite sua escolha: ")
        self.etapa = "texto"
        self.instancia.text_box.bind("<Return>", self.pegar_entrada)

    def pegar_entrada(self, event):
        conteudo = self.instancia.text_box.get("1.0", "end").strip()
        ultima_linha = conteudo.split("\n")[-1].strip()

        if self.etapa == "dificuldade":
            if ultima_linha in {"1", "2", "3", "4"}:
                self.instancia.text_box.insert("end", f"\nVocê escolheu a dificuldade: {ultima_linha}\n")
                self.selecionar_tx() 
            else:
                self.instancia.text_box.insert("end", "\nOpção inválida! Tente novamente.\n")

        elif self.etapa == "texto":
            if ultima_linha in {"a", "b", "c", "d"}:
                self.instancia.text_box.insert("end", f"\nVocê escolheu o texto: {ultima_linha}\n")
                self.instancia.text_box.insert("end", "\nProcesso concluído!\n")
                self.instancia.text_box.unbind("<Return>") 
            else:
                self.instancia.text_box.insert("end", "\nOpção inválida! Tente novamente.\n")

        return "break" 

