from SelecionarTextos import *
import time
import tkinter as tk

class Logica:
    def __init__(self, instancia):
        self.instancia = instancia

        # Inserir texto inicial
        self.inserir_texto_inicial()
        
        # Configurar progresso
        self.progresso_atual = 0
        self.progresso_total = 68 
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
        self.instancia.text_box.insert("end", "\nDigite sua escolha: "+ "\n")
        self.etapa = "dificuldade"
        self.instancia.text_box.mark_set("insert", "end")  # Move o cursor para o final
        self.instancia.text_box.see("end")
        self.instancia.text_box.bind("<Return>", self.pegar_entrada)
        
        
        

    def selecionar_tx(self):
        textos = SelecionarTextos()
        textos_filtrados = textos.selecionarDificuldade(int(self.ultima_linha))
 
        # Criar as opções numeradas dinamicamente
        opcoes = "\n".join(
            [f"""   {chr(97 + i)} - {texto}""" for i, texto in enumerate(textos_filtrados)]
        )

        #opcoes = ""
        #for i, texto in enumerate(textos_filtrados):
        #    letra = chr(97 + i)  # 97 é o código ASCII de 'a'
        #    opcoes += f"{letra} - {texto}\n"

        # Construir a string final
        op_text_texto = f"""
        Escolha um texto:
        {opcoes.strip()} 
        Digite sua escolha:
        """

        self.instancia.text_box.insert("end", "\n" + op_text_texto.strip())
        self.instancia.text_box.insert("end", "\nDigite sua escolha: " + "\n")
        self.etapa = "texto"
        self.instancia.text_box.mark_set("insert", "end")  # Move o cursor para o final
        self.instancia.text_box.see("end")
        self.instancia.text_box.bind("<Return>", self.pegar_entrada)


    def pegar_entrada(self, event):
        conteudo = self.instancia.text_box.get("1.0", "end").strip()
        self.ultima_linha = conteudo.split("\n")[-1].strip()

        if self.etapa == "dificuldade":
            if self.ultima_linha in {"1", "2", "3", "4"}:
                self.instancia.text_box.insert("end", f"\nVocê escolheu a dificuldade: {self.ultima_linha}\n")
                self.selecionar_tx() 
            else:
                self.instancia.text_box.insert("end", "\nOpção inválida! Tente novamente.\n")

        elif self.etapa == "texto":
            if self.ultima_linha in {"a", "b", "c", "d"}:
                self.instancia.text_box.insert("end", f"\nVocê escolheu o texto: {self.ultima_linha}\n")
                #self.instancia.text_box.insert("end", "\nProcesso concluído!\n")
                Play(self.instancia, self.ultima_linha)
                self.instancia.text_box.unbind("<Return>") 
            else:
                self.instancia.text_box.insert("end", "\nOpção inválida! Tente novamente.\n")

        self.instancia.text_box.see("end")
        self.instancia.text_box.bind("<Return>", self.pegar_entrada)

        return "break" 

class Play:
    def __init__(self, instancia, texto):
        self.instancia = instancia
        self.texto = texto.strip()
        self.start_time = None
        self.acertos = 0
        self.erros = 0

        # Configuração da interface
        self.instancia.text_box.delete("1.0", tk.END)
        self.instancia.text_box.insert("1.0", self.texto)
        self.instancia.text_box.config(state=tk.DISABLED)  # Impede edição do texto original

        # Entrada do usuário
        self.input_box = tk.Text(self.instancia.root, height=5, wrap=tk.WORD)
        self.input_box.pack()
        self.input_box.bind("<KeyRelease>", self.verificar_texto)
        self.input_box.focus()
    
    def verificar_texto(self, event):
        if self.start_time is None:
            self.start_time = time.time()

        digitado = self.input_box.get("1.0", tk.END).strip()
        correto = self.texto[:len(digitado)]

        if digitado == correto:
            self.acertos = len(digitado)
        else:
            self.erros += 1

        if digitado == self.texto:
            self.finalizar()
    
    def finalizar(self):
        tempo_total = time.time() - self.start_time
        palavras = len(self.texto.split())
        wpm = (palavras / tempo_total) * 60

        self.instancia.text_box.config(state=tk.NORMAL)
        self.instancia.text_box.insert("end", f"\n\nFim! Você digitou {self.acertos} caracteres corretamente com {self.erros} erros.")
        self.instancia.text_box.insert("end", f"\nSua velocidade: {wpm:.2f} palavras por minuto.")
        self.instancia.text_box.config(state=tk.DISABLED)

        self.input_box.config(state=tk.DISABLED)
