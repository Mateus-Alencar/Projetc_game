import tkinter as tk
import time

class Logica:
    def __init__(self, instancia):
        self.instancia = instancia

        # Inserir texto na caixa de texto existente
        sample_text = """
        Bem-vindo ao Jogo!
        Aqui estão algumas instruções:
        
        1. Use as setas do teclado para digitar.
        2. Seja rápido e não cometa erros!

                                                                    Boa sorte!
        """
        self.instancia.text_box.insert("1.0", sample_text)
        self.instancia.text_box.insert("end", "\n")
        # Iniciar a barra de carregamento
        self.instancia.text_box.insert("end","                                                           Carregando Textos")
        self.instancia.text_box.insert("end", "\n")
        self.progresso_atual = 0 
        self.iniciar_barra()
    
    def iniciar_barra(self): 
        if self.progresso_atual < 72:
            self.instancia.text_box.insert("end","=")
            self.progresso_atual += 1
            self.instancia.root.after(100, self.iniciar_barra)
