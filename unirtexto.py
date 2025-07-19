import tkinter as tk
from tkinter import ttk
import re

def mostrar_frame(frame):
    frame.tkraise()

# Tela principal do menu
def criar_menu():
    menu_frame = tk.Frame(janela, bg="#2b2b2b")
    menu_frame.place(relwidth=1, relheight=1)

    label = ttk.Label(menu_frame, text="O que deseja fazer?", font=("Arial", 20))
    label.pack(pady=50)

    btn_unir = ttk.Button(menu_frame, text="Unir texto", style="Grande.TButton",
                         command=lambda: mostrar_frame(unir_frame))
    btn_unir.pack(pady=20, ipadx=20, ipady=10)

    btn_procurar = ttk.Button(menu_frame, text="Procurar ordens", style="Grande.TButton",
                             command=lambda: mostrar_frame(procurar_frame))
    btn_procurar.pack(pady=20, ipadx=20, ipady=10)

    return menu_frame

# Tela unir texto sem scroll
def criar_unir_texto():
    frame = tk.Frame(janela, bg="#2b2b2b")
    frame.place(relwidth=1, relheight=1)

    label_entrada = ttk.Label(frame, text="Digite o texto:")
    label_entrada.pack(padx=10, pady=10)

    global entrada_texto
    entrada_texto = tk.Text(frame, height=8, width=80, bg="#3c3f41", fg="#ffffff",
                        insertbackground="white", font=("Consolas", 12), wrap="word")
    entrada_texto.pack(padx=10, pady=10)

    label_sep = ttk.Label(frame, text="Separador (deixe vazio para ','):")
    label_sep.pack(padx=10, pady=(5, 0))

    global entrada_separador
    entrada_separador = ttk.Entry(frame, width=10)
    entrada_separador.pack(padx=10, pady=5)

    botao = ttk.Button(frame, text="🔄 Processar", command=processar_ordens)
    botao.pack(pady=10)

    label_saida = ttk.Label(frame, text="Texto processado:")
    label_saida.pack(padx=10, pady=10)

    global texto_saida
    texto_saida = tk.Text(frame, height=8, width=80, bg="#3c3f41", fg="#00ff00",
                          insertbackground="white", font=("Consolas", 12), wrap="word")
    texto_saida.pack(padx=10, pady=10)

    botao_copiar = ttk.Button(frame, text="📋 Copiar texto processado",
                              command=copiar_saida,
                              style="Grande.TButton")
    botao_copiar.pack(pady=20)

    btn_voltar = ttk.Button(frame, text="⬅ Voltar ao menu",
                           command=lambda: mostrar_frame(menu_frame))
    btn_voltar.pack(pady=10)

    return frame

# Tela procurar ordens com saída única formatada
def criar_procurar_ordens():
    frame = tk.Frame(janela, bg="#2b2b2b")
    frame.place(relwidth=1, relheight=1)

    label_info = ttk.Label(frame, text="Joga o textão confuso ai:")
    label_info.pack(padx=10, pady=10)

    global entrada_procurar
    entrada_procurar = tk.Text(frame, height=10, width=100, bg="#3c3f41", fg="#ffffff",
                              insertbackground="white", font=("Consolas", 12), wrap="word")
    entrada_procurar.pack(padx=10, pady=10)

    botao_procurar = ttk.Button(frame, text="🔍 Encontrar ordens", command=procurar_ordens)
    botao_procurar.pack(pady=10)

    label_saida_procurar = ttk.Label(frame, text="Ordens encontradas:")
    label_saida_procurar.pack(padx=10, pady=10)

    global texto_saida_procurar
    texto_saida_procurar = tk.Text(frame, height=10, width=100, bg="#3c3f41", fg="#00ff00",
                                  insertbackground="white", font=("Consolas", 12), wrap="word")
    texto_saida_procurar.pack(padx=10, pady=10)

    botao_copiar_procurar = ttk.Button(frame, text="📋 Copiar ordens encontradas",
                                       command=copiar_saida_procurar,
                                       style="Grande.TButton")
    botao_copiar_procurar.pack(pady=10)

    btn_voltar = ttk.Button(frame, text="⬅ Voltar ao menu",
                           command=lambda: mostrar_frame(menu_frame))
    btn_voltar.pack(pady=10)

    return frame

def processar_ordens():
    ordens = entrada_texto.get("1.0", tk.END)
    ordens = "".join(ordens.split())  # remove todos espaços e quebras

    separador = entrada_separador.get().strip()
    if separador == "":
        separador = ","

    cont = 0
    novas_ordens = ""
    for c in ordens:
        if cont < 8:
            novas_ordens += c
            cont += 1
        else:
            novas_ordens += f"{separador}{c}"
            cont = 1

    texto_saida.delete("1.0", tk.END)
    texto_saida.insert(tk.END, novas_ordens)

def copiar_saida():
    texto = texto_saida.get("1.0", tk.END).strip()
    if texto:
        janela.clipboard_clear()
        janela.clipboard_append(texto)
        janela.update()
        print("Texto copiado!")
    else:
        print("Nada pra copiar, fi!")

def procurar_ordens():
    texto = entrada_procurar.get("1.0", tk.END).replace("\n", "")
    padrao = r"\b621\d{5}\b"
    encontrados = re.findall(padrao, texto)

    texto_saida_procurar.delete("1.0", tk.END)

    if encontrados:
        resultado = " ".join(encontrados)
        texto_saida_procurar.insert(tk.END, resultado)
    else:
        texto_saida_procurar.insert(tk.END, "Nenhuma ordem encontrada.")

def copiar_saida_procurar():
    texto = texto_saida_procurar.get("1.0", tk.END).strip()
    if texto:
        janela.clipboard_clear()
        janela.clipboard_append(texto)
        janela.update()
        print("Ordens copiadas!")
    else:
        print("Nada pra copiar aí não, parceiro!")

# Config janela
janela = tk.Tk()
janela.title("Toolkit do aprendiz")
janela.geometry("900x750")
janela.config(bg="#2b2b2b")

style = ttk.Style(janela)
style.theme_use("clam")
style.configure("TLabel", background="#2b2b2b", foreground="#ffffff", font=("Arial", 12))
style.configure("TButton", background="#4caf50", foreground="#ffffff", font=("Arial", 12), padding=10)
style.configure("Grande.TButton", font=("Arial", 16), padding=(20, 15))
style.map("TButton", background=[("active", "#45a049")])

menu_frame = criar_menu()
unir_frame = criar_unir_texto()
procurar_frame = criar_procurar_ordens()

menu_frame.tkraise()

janela.mainloop()