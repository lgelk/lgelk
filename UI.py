import tkinter as tk
from tkinter import ttk
import threading
import time

def iniciar_tarefa():
    # Defina a tarefa que deseja realizar aqui. Por exemplo, um loop com atualizações de texto.
    for i in range(11):
        time.sleep(1)  # Simulação de uma tarefa que leva 1 segundo para ser concluída.
        texto_atual.set(f"Progresso: {i * 10}%")
        progresso["value"] = i * 10
        root.update()

def sair():
    root.destroy()

# Configuração da janela principal
root = tk.Tk()
root.title("Projeto Automatização Financeiro")
root.geometry("640x480")  # Tamanho da janela definido para 640x480 pixels
# Definindo o ícone personalizado
root.iconbitmap("C:\icon.ico")  # Substitua "icone.ico" pelo nome do seu arquivo .ico ou .png

# Frame para a área de texto
frame_texto = tk.Frame(root, padx=10, pady=10)
frame_texto.pack(side=tk.BOTTOM)

texto_atual = tk.StringVar()
label_texto = tk.Label(frame_texto, textvariable=texto_atual, font=("Arial", 12))
label_texto.pack()

# Frame para os botões
frame_botoes = tk.Frame(root, padx=10, pady=10)
frame_botoes.pack(side=tk.BOTTOM)  # Colocando os botões na parte inferior da janela

# Barra de Progresso
progresso = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progresso.pack(side=tk.BOTTOM, pady=10)  # Colocando a barra de progresso acima dos botões

# Botão "Iniciar Tarefa"
botao_iniciar = tk.Button(frame_botoes, text="Iniciar Tarefa", command=lambda: threading.Thread(target=iniciar_tarefa).start())
botao_iniciar.pack(side=tk.LEFT, padx=5)

# Botão "Sair"
botao_sair = tk.Button(frame_botoes, text="Sair", command=sair)
botao_sair.pack(side=tk.LEFT, padx=5)

# Inicialização da janela principal
root.mainloop()
