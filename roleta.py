import tkinter as tk
import random
import math
import threading
import time

class RoletaComica:
    def __init__(self, root):
        self.root = root
        self.root.title("Roleta Cômica: Quem Vai Apresentar Primeiro? 😂")
        self.itens = []
        self.angulo_atual = 0

        # Parte de cima
        frame_top = tk.Frame(root)
        frame_top.pack(pady=10)

        self.entry_item = tk.Entry(frame_top, width=30)
        self.entry_item.pack(side=tk.LEFT, padx=5)

        btn_add = tk.Button(frame_top, text="Adicionar Vítima", command=self.adicionar_item)
        btn_add.pack(side=tk.LEFT)

        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack(pady=10)

        self.btn_sortear = tk.Button(root, text="🎯 Rodar Roleta", command=self.rodar_roleta, bg="purple", fg="white", font=("Arial", 14, "bold"))
        self.btn_sortear.pack(pady=10)

        self.lbl_resultado = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="blue")
        self.lbl_resultado.pack()

    def adicionar_item(self):
        nome = self.entry_item.get().strip()
        if nome:
            self.itens.append(nome)
            self.entry_item.delete(0, tk.END)
            self.desenhar_roleta()
        else:
            tk.messagebox.showwarning("Campo vazio", "Digite o nome de um(a) azarado(a)!")

    def desenhar_roleta(self):
        self.canvas.delete("all")
        total = len(self.itens)
        if total == 0:
            return

        angulo_por_setor = 360 / total
        cores = ["#ff9999", "#99ff99", "#9999ff", "#ffff99", "#ffcc99", "#cc99ff"]

        for i, nome in enumerate(self.itens):
            cor = cores[i % len(cores)]
            start = (i * angulo_por_setor + self.angulo_atual) % 360
            self.canvas.create_arc(50, 50, 350, 350, start=start, extent=angulo_por_setor,fill=cor, outline="black")

            # Texto
            meio_angulo = math.radians(start + angulo_por_setor / 2)
            x = 200 + 120 * math.cos(meio_angulo)
            y = 200 - 120 * math.sin(meio_angulo)
            self.canvas.create_text(x, y, text=nome, angle=0, font=("Arial", 10, "bold"))

        # Ponta da seta
        self.canvas.create_polygon(195, 10, 205, 10, 200, 30, fill="red")

    def rodar_roleta(self):
        if not self.itens:
            tk.messagebox.showwarning("Sem nomes", "Adicione os nomes dos sortudos antes.")
            return

        self.btn_sortear.config(state=tk.DISABLED)
        threading.Thread(target=self.animar_roleta).start()

    def animar_roleta(self):
        voltas = random.randint(5, 8)
        duracao = 3.5
        passos = 60
        angulo_total = 360 * voltas + random.randint(0, 359)
        incremento = angulo_total / passos

        for _ in range(passos):
            self.angulo_atual = (self.angulo_atual + incremento) % 360
            self.root.after(0, self.desenhar_roleta)
            self.root.update()  # <- Atualiza a interface em tempo real
            time.sleep(duracao / passos)

        escolhido = self.obter_nome_escolhido()
        self.lbl_resultado.config(text=f"😂 Vai apresentar primeiro: {escolhido}!")
        self.btn_sortear.config(state=tk.NORMAL)

    def obter_nome_escolhido(self):
        angulo_por_setor = 360 / len(self.itens)
        angulo_normalizado = (360 - self.angulo_atual + angulo_por_setor / 2) % 360
        index = int(angulo_normalizado // angulo_por_setor)
        return self.itens[index]

if __name__ == "__main__":
    root = tk.Tk()
    app = RoletaComica(root)
    root.mainloop()