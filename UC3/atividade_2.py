import random
import tkinter as tk
from tkinter import ttk, messagebox

class JogoForcaGUI:
    def __init__(self, master):
        self.master = master
        master.title("Jogo da Forca")

        self.palavras = ["python", "programacao", "computador", "algoritmo", "desenvolvimento", "inteligencia", "artificial", "ciencia", "dados", "inovacao"]
        self.palavra_secreta = random.choice(self.palavras).lower()
        self.letras_corretas = set()
        self.letras_erradas = set()
        self.tentativas_maximas = 7
        self.erros = 0

        self.forca_estados = [
            """
              -----
              |
              |
              |
              -
            """,
            """
              -----
              |   |
              |
              |
              -
            """,
            """
              -----
              |   |
              |   O
              |
              -
            """,
            """
              -----
              |   |
              |   O
              |   |
              -
            """,
            """
              -----
              |   |
              |   O
              |  /|
              -
            """,
            """
              -----
              |   |
              |   O
              |  /|\
              -
            """,
            """
              -----
              |   |
              |   O
              |  /|\
              -  /
            """,
            """
              -----
              |   |
              |   O
              |  /|\
              -  / \\
            """
        ]

        self.forca_label = ttk.Label(master, text=self.forca_estados[0], font=("Consolas", 16))
        self.forca_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.palavra_label = ttk.Label(master, text=self.exibir_palavra(), font=("Arial", 24))
        self.palavra_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.letras_erradas_label = ttk.Label(master, text="Letras Erradas: ", font=("Arial", 12))
        self.letras_erradas_label.grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)

        self.tentativas_label = ttk.Label(master, text=f"Tentativas Restantes: {self.tentativas_maximas}", font=("Arial", 12))
        self.tentativas_label.grid(row=2, column=1, sticky=tk.E, padx=10, pady=5)

        self.palpite_entry = ttk.Entry(master, width=3)
        self.palpite_entry.grid(row=3, column=0, padx=10, pady=10)
        self.palpite_entry.focus()

        self.palpite_button = ttk.Button(master, text="Palpitar", command=self.tentar_palpite)
        self.palpite_button.grid(row=3, column=1, padx=10, pady=10)

        self.master.bind('<Return>', lambda event=None: self.palpite_button.invoke()) # Ativar botão com Enter

    def exibir_palavra(self):
        display = ""
        for letra in self.palavra_secreta:
            if letra in self.letras_corretas:
                display += letra + " "
            else:
                display += "_ "
        return display.strip()

    def atualizar_jogo(self):
        self.forca_label.config(text=self.forca_estados[self.erros])
        self.palavra_label.config(text=self.exibir_palavra())
        self.letras_erradas_label.config(text=f"Letras Erradas: {', '.join(sorted(list(self.letras_erradas)))}")
        self.tentativas_label.config(text=f"Tentativas Restantes: {self.tentativas_maximas - self.erros}")

        if set(self.palavra_secreta) == self.letras_corretas:
            messagebox.showinfo("Parabéns!", f"Você venceu! A palavra era: {self.palavra_secreta}")
            self.master.destroy()
        elif self.erros >= self.tentativas_maximas:
            messagebox.showinfo("Game Over!", f"Você perdeu! A palavra era: {self.palavra_secreta}")
            self.master.destroy()

    def tentar_palpite(self):
        palpite = self.palpite_entry.get().lower()
        self.palpite_entry.delete(0, tk.END)

        if not palpite.isalpha() or len(palpite) != 1:
            messagebox.showerror("Erro", "Por favor, digite uma única letra válida.")
            return
        elif palpite in self.letras_corretas or palpite in self.letras_erradas:
            messagebox.showinfo("Aviso", "Você já tentou essa letra.")
            return
        elif palpite in self.palavra_secreta:
            self.letras_corretas.add(palpite)
        else:
            self.letras_erradas.add(palpite)
            self.erros += 1

        self.atualizar_jogo()

if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoForcaGUI(root)
    root.mainloop()