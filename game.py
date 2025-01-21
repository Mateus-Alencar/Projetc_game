import threading
from tkinter import messagebox

class Logica:
    def __init__(self, instancia):
        self.instancia = instancia

        # Inserir texto na caixa de texto
        sample_text = """
        Bem-vindo ao Jogo!
        Aqui estão algumas instruções:
        
        1. Use as setas do teclado para se mover.
        2. Colete todas as moedas para ganhar pontos.
        3. Evite os inimigos a todo custo!

        Boa sorte!
        """
        instancia.text_box.insert("1.0", sample_text) 

        cronometro = threading.Timer(3.0, self.teste())
        cronometro.start()

    def teste(self):
        sample_text2 = """
        Bem-vindo ao Jogo!
        Aqui estão algumas instruções:
        
        1. Use as setas do teclado para se mover.
        2. Colete todas as moedas para ganhar pontos.
        3. Evite os inimigos a todo custo!

        Boa sorte!
        """
        self.instancia.text_box.insert("1.0", sample_text2) 
