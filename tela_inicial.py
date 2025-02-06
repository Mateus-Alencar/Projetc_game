import tkinter as tk
from tkinter import messagebox
from game import Logica


class Game:
    def __init__(self):
        # Criação da janela principal
        self.root = tk.Tk()
        self.root.title("Menu do Jogo")
        self.root.geometry("800x500")
        self.root.resizable(False, False)

        # Simulação de gradiente de fundo
        self.canvas = tk.Canvas(self.root, width=820, height=500)
        self.canvas.pack(fill="both", expand=True)
        self.create_gradient_background()

        # Título
        self.title = tk.Label(
            self.root,
            text="Meu Jogo Fantástico",
            font=("Arial", 36, "bold"),
            fg="white",
            bg="#34495e"
        )
        self.canvas.create_window(400, 80, window=self.title)

        # Botões estilizados
        self.create_button("Iniciar Jogo", self.start_game, 200)
        self.create_button("Configurações", self.settings, 280)
        self.create_button("Sair do Jogo", self.quit_game, 360)

    def create_gradient_background(self):
        for i in range(100):
            color = f"#{int(44 + i * 1.3):02x}{int(62 + i * 1.5):02x}{int(80 + i * 1.7):02x}"
            self.canvas.create_rectangle(0, i * 5, 800, (i + 1) * 5, outline=color, fill=color)

    def create_button(self, text, command, y_position):
        btn = tk.Button(
            self.root,
            text=text,
            command=command,
            font=("Arial", 18, "bold"),
            fg="#ffffff",
            bg="#2980b9",
            activeforeground="#ffffff",
            activebackground="#3498db",
            bd=0,
            relief="flat",
            width=20,
            height=2,
            cursor="hand2",
            highlightthickness=0
        )
        btn.place(x=300, y=y_position, width=200, height=50)




    def start_game(self):
        self.clear_root()


        # Criar a caixa de texto com estilo aprimorado
        self.text_box = tk.Text(
        self.root,
        font=("Arial", 14),      # Fonte maior para melhor leitura
        wrap="word",             # Quebra de linha por palavra
        bg="#000",               # Fundo preto (estilo terminal)
        fg="#FFF",               # Texto branco
        insertbackground="#FFF", # Cursor branco
        padx=10,                 # Espaçamento interno (esquerda/direita)
        pady=10,                 # Espaçamento interno (topo/baixo)
        spacing1=5,              # Espaçamento antes de cada linha
        spacing3=5               # Espaçamento após cada linha
            )
        self.text_box.pack(fill="both", expand=True, padx=10, pady=10)  # Margens externas para um layout mais limpo

        # Criar e configurar a barra de rolagem
        scrollbar = tk.Scrollbar(self.root, command=self.text_box.yview)
        scrollbar.pack(side="right", fill="y")
        self.text_box.config(yscrollcommand=scrollbar.set)

        Logica(self)


    def settings(self):
        messagebox.showinfo("Configurações", "Abrindo configurações!")

    def quit_game(self):
        self.root.destroy()

    def clear_root(self):
        # Itera sobre todos os widgets filhos do root e os destrói
        for widget in self.root.winfo_children():
            widget.destroy()

    def run(self):
        # Rodar a aplicação
        self.root.mainloop()


# Executar o aplicativo
if __name__ == "__main__":
    app = Game()
    app.run()
 