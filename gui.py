import tkinter as tk
import star
from tkinter import ttk
from PIL import Image, ImageTk

def get_selec(ini,fim,cor):
    global lista, label_texto1
    if cor == "Azul":
        cor = 1
    elif cor == "Amarela":
        cor = 2
    elif cor == "Verde":
        cor = 3
    else:
        cor = 4
    lista = star.inicio(ini,fim,cor)
    texto = f'Caminho percorrido: {lista[1]}; tempo gasto: {lista[0]} minutos'
    label_texto1.config(text=texto)

def criar_interface():
    # Criar a janela principal
    janela = tk.Tk()
    janela.geometry("800x600")
    janela.title("Heuristica do metrô")

    # Configurar o layout do grid
    janela.grid_columnconfigure(0, weight=1)  # Uma coluna que ocupa

    # Criar as cinco linhas
    for i in range(5):
        janela.grid_rowconfigure(i, weight=1)  # Linhas com peso 1, tamanho igual
        frame = tk.Frame(janela, bg='white')  # Pode alterar a cor de fundo conforme necessário
        frame.grid(row=i, column=0, sticky='nsew')

        # Adicionar texto ao Frame na primeira linha
        if i == 0:
            texto = "Problema do metrô de Paris"
            label_texto = tk.Label(frame, text=texto, fg='white', bg='blue')  # Cores de texto e fundo
            label_texto.pack(expand=True)
        if i == 1:
            texto = "Calcule o tempo do trajeto mais rápido entre duas estações e escolhendo a cor da linha inicial"
            label_texto = tk.Label(frame, text=texto, fg='white', bg='blue')  # Cores de texto e fundo
            label_texto.pack(expand=True)
        if i == 2:
            texto = "*Lembrando que a velocidade média é de 30km/h e o tempo de baldeação é de 4 minutos"
            label_texto = tk.Label(frame, text=texto, fg='white', bg='blue')  # Cores de texto e fundo
            label_texto.pack(expand=True)
        if i == 4 :
            global label_texto1
            texto =''
            label_texto1 = tk.Label(frame, text=texto, fg='white', bg='blue')  # Cores de texto e fundo
            label_texto1.pack(expand=True)

        if i == 3:
            # Variáveis de controle para armazenar as seleções
            var_1 = tk.StringVar()
            var_2 = tk.StringVar()
            var_3 = tk.StringVar()

            opcoes = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
            seletor = ttk.Combobox(frame, values=opcoes, textvariable=var_1)
            seletorf = ttk.Combobox(frame, values=opcoes, textvariable=var_2)

            opcoesLinha = ["Azul","Amarela","Verde","Vermelha"]
            seletorLinha = ttk.Combobox(frame, values=opcoesLinha, textvariable=var_3)

            texto = "Estação de inicio: "
            label_texto = tk.Label(frame, text=texto, fg='white', bg='blue', anchor='w')  # Cores de texto e fundo
            label_texto.pack(side='left', padx=5, pady=5)

            seletor.pack(side='left')

            texto = "Linha inicial: "
            label_texto = tk.Label(frame, text=texto, fg='white', bg='blue', anchor='w')  # Cores de texto e fundo
            label_texto.pack(side='left', padx=5, pady=5)

            seletorLinha.pack(side='left')

            texto = "Estação final: "
            label_texto = tk.Label(frame, text=texto, fg='white', bg='blue', anchor='w')  # Cores de texto e fundo
            label_texto.pack(side='left', padx=5, pady=5)

            seletorf.pack(side='left')

            # Adicionar um botão ao Frame na terceira linha
            botao = ttk.Button(frame, text="Calcular", command=lambda: get_selec(var_1.get(),var_2.get(),var_3.get()))
            botao.pack(side='left', padx=5)

    # Criar a quinta linha com altura de 500 pixels
    janela.grid_rowconfigure(5, minsize=500)  # Linha com altura mínima de 500 pixels
    frame = tk.Frame(janela, bg='white')  # Pode alterar a cor de fundo conforme necessário
    frame.grid(row=5, column=0, sticky='nsew')

    # Adicionar uma imagem no meio do Frame na quarta linha
    imagem = Image.open("metro.png")  # Substitua pelo caminho real da sua imagem
    imagem = imagem.resize((450, 450), Image.ANTIALIAS)  # Ajuste o tamanho conforme necessário

    imagem_tk = ImageTk.PhotoImage(imagem)
    label_imagem = tk.Label(frame, image=imagem_tk)
    label_imagem.place(relx=0.5, rely=0.5, anchor='center')

    # Iniciar o loop principal da interface gráfica
    janela.mainloop()

# Chamar a função para criar a interface
criar_interface()
