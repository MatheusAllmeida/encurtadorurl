import requests
import tkinter as tk
from tkinter import messagebox

def encurtar_url():
    url = entrada.get()
    if not url:
        messagebox.showwarning("Aviso", "Digite uma URL primeiro!")
        return
    
    api_url = f"http://tinyurl.com/api-create.php?url={url}"
    try:
        response = requests.get(api_url)
        link_curto = response.text
        saida.delete(0, tk.END)  # limpa campo anterior
        saida.insert(0, link_curto)
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível encurtar: {e}")

def copiar_link():
    link = saida.get()
    if link:
        janela.clipboard_clear()
        janela.clipboard_append(link)
        janela.update()  # garante que fica na área de transferência
        messagebox.showinfo("Copiado", "Link copiado para a área de transferência!")
    else:
        messagebox.showwarning("Aviso", "Nenhum link para copiar.")

# Criando a janela
janela = tk.Tk()
janela.title("Encurtador de Links")
janela.geometry("400x220")

# Entrada
tk.Label(janela, text="Digite a URL:").pack(pady=5)
entrada = tk.Entry(janela, width=50)
entrada.pack(pady=5)

# Botão Encurtar
btn = tk.Button(janela, text="Encurtar", command=encurtar_url)
btn.pack(pady=10)

# Saída
tk.Label(janela, text="Link encurtado:").pack(pady=5)
saida = tk.Entry(janela, width=50)
saida.pack(pady=5)

# Botão Copiar
btn_copiar = tk.Button(janela, text="Copiar", command=copiar_link)
btn_copiar.pack(pady=10)

# Loop
janela.mainloop()
