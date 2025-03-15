import tkinter as tk
from tkinter import messagebox
import random
import spacy

nlp = spacy.load("en_core_web_sm")

# Função que calcula a similaridade entre as palavras
def calcular_similaridade(palavra1, palavra2):
    doc1 = nlp(palavra1)
    doc2 = nlp(palavra2)

    return doc1.similarity(doc2)

def iniciar_jogo():
    palavras = ["python", "java", "javascript", "html", "css", "ruby", "swift", "kotlin", "go"]
    
    palavra_sorteada.set(random.choice(palavras))
    palavra_digitada.set("")

# Função que verifica a similaridade e o progresso no jogo
def verificar_palavra():
    palavra_original = palavra_sorteada.get()
    palavra_input = palavra_digitada.get()
    limiar = 0.60  # Limiar de similaridade (60%)

    similaridade = calcular_similaridade(palavra_original, palavra_input)

    if similaridade >= limiar:
        resultado.set(f"Você acertou! Similaridade: {similaridade*100:.2f}%")
    else:
        resultado.set(f"Jogo encerrado! Similaridade abaixo do limiar. Similaridade: {similaridade*100:.2f}%")
        messagebox.showinfo("Fim do Jogo", f"Jogo encerrado! A similaridade foi de {similaridade*100:.2f}%")
        botao_verificar.config(state=tk.NORMAL)  

# Configuração da interface gráfica
root = tk.Tk()
root.title("Jogo de Similaridade de Palavras")

palavra_sorteada = tk.StringVar()
palavra_digitada = tk.StringVar()
resultado = tk.StringVar()

tk.Label(root, text="Palavra sorteada:").pack(pady=10)
tk.Label(root, textvariable=palavra_sorteada, font=("Arial", 14)).pack(pady=10)

tk.Label(root, text="Digite uma palavra similar:").pack(pady=10)
tk.Entry(root, textvariable=palavra_digitada, font=("Arial", 14)).pack(pady=10)

botao_verificar = tk.Button(root, text="Verificar", command=verificar_palavra, font=("Arial", 14))
botao_verificar.pack(pady=10)

tk.Label(root, textvariable=resultado, font=("Arial", 14)).pack(pady=20)

tk.Button(root, text="Iniciar Jogo", command=iniciar_jogo, font=("Arial", 14)).pack(pady=10)

iniciar_jogo()
root.mainloop()