import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

label = tk.Label(font=("Arial", 14, "bold"), text="Insira o primeiro numero:")
entry = tk.Entry(width=50)
label2 = tk.Label(font=("Arial", 14, "bold"), text="Insira o segundo numero:")
entry2 = tk.Entry(width=50)

def soma():
    numero1 = entry.get()
    numero2 = entry2.get()
    resultado = int(numero1) + int(numero2)
    messagebox.showinfo("Resultado", f"A soma é: {resultado}")

def subtracao():
    numero1 = entry.get()
    numero2 = entry2.get()
    resultado = int(numero1) - int(numero2)
    messagebox.showinfo("Resultado", f"A subtração é: {resultado}")
    
def multiplicacao():
    numero1 = entry.get()
    numero2 = entry2.get()
    resultado = int(numero1) * int(numero2)
    messagebox.showinfo("Resultado", f"A multiplicação é: {resultado}")
    
def divisao():
    numero1 = entry.get()
    numero2 = entry2.get()
    if int(numero2) == 0:
        messagebox.showerror("Erro", "Divisão por zero não é permitida!")
        return
    resultado = int(numero1) / int(numero2)
    messagebox.showinfo("Resultado", f"A divisão é: {resultado}")

button_soma = tk.Button(text="Soma", command=soma, bg="green", fg="white", font=("Arial", 14, "bold"))
button_subtracao = tk.Button(text="Subtração", command=subtracao, bg="blue", fg="white", font=("Arial", 14, "bold"))
button_multiplicacao = tk.Button(text="Multiplicação", command=multiplicacao, bg="orange", fg="white", font=("Arial", 14, "bold"))
button_divisao = tk.Button(text="Divisão", command=divisao, bg="red", fg="white", font=("Arial", 14, "bold"))

label.pack()
entry.pack()
label2.pack()
entry2.pack()
button_soma.pack()
button_subtracao.pack()
button_multiplicacao.pack()
button_divisao.pack()

root.mainloop()