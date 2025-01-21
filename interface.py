import tkinter as tk
from tkinter import messagebox

# Funções para cada botão
def start_game():
    messagebox.showinfo("Iniciar Jogo", "O jogo está iniciando!")

def settings():
    messagebox.showinfo("Configurações", "Abrindo configurações!")

def quit_game():
    root.destroy()

# Criação da janela principal
root = tk.Tk()
root.title("Menu do Jogo")
root.geometry("800x500")
root.resizable(False, False)

# Simulação de gradiente de fundo
canvas = tk.Canvas(root, width=800, height=500)
canvas.pack(fill="both", expand=True)

for i in range(100):
    color = f"#{int(44 + i * 1.3):02x}{int(62 + i * 1.5):02x}{int(80 + i * 1.7):02x}"
    canvas.create_rectangle(0, i * 5, 800, (i + 1) * 5, outline=color, fill=color)

# Título do Menu
title = tk.Label(
    root,
    text="Meu Jogo Fantástico",
    font=("Arial", 36, "bold"),
    fg="white",
    bg="#34495e"
)
canvas.create_window(400, 80, window=title)

# Botões estilizados
def create_button(text, command, y_position):
    btn = tk.Button(
        root,
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
    # Borda arredondada (simulação)
    canvas.create_oval(280, y_position, 300, y_position + 50, fill="#2980b9", outline="")
    canvas.create_oval(500, y_position, 520, y_position + 50, fill="#2980b9", outline="")
    return btn

# Criação dos botões
btn_start = create_button("Iniciar Jogo", start_game, 200)
btn_settings = create_button("Configurações", settings, 280)
btn_quit = create_button("Sair do Jogo", quit_game, 360)

# Rodar a aplicação
root.mainloop()
