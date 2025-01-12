import pandas
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

relatorio = pandas.read_csv("Sara_planilia.csv")

def calculo():
    sele = listbox.curselection()
    indice = 0
    valor = 0
    if sele:
        lista = relatorio.loc[:, ["Data", "Valor"]]
        for i in lista["Data"]:
            if "/" in i:
                a = i.split("/")[1]
                if a.count(str(sele[0]+1)):
                    try:
                        valor += int(relatorio.loc[indice, 'Valor'])
                    except:
                        pass
            indice += 1
        if valor:
            resultado.configure(text=f"R${valor}")
        else:
            resultado.configure(text="Não existe valor \n"
                                     "neste mês")
def carregar_decoraçoes():
    global relatorio
    for item in tree.get_children():
        tree.delete(item)


    for linha in range(int(relatorio.shape[0])):
        ad = []
        for item in relatorio.loc[linha]:
            ad.append(item)
        tree.insert("", "end", values=ad)

def adicionar():
    Data = entry_data.get()
    Cliente = entry_nome.get()
    Valor = entry_valor.get()
    Tema = entry_tema.get()
    Telefone = entry_tele.get()

    if not Data or not Cliente or not Valor or not Tema or not Telefone:
        messagebox.showerror("erro", "Todos campos obrigatorios mae")
        return
    entry_data.delete(0, tk.END)
    entry_tema.delete(0, tk.END)
    entry_valor.delete(0, tk.END)
    entry_nome.delete(0, tk.END)
    entry_tele.delete(0, tk.END)

    new_disc = {
        "Data": [Data],
        "Cliente": [Cliente],
        "Valor": [Valor],
        "Tema": [Tema],
        "Telefone": [Telefone]
    }
    new_csv = pandas.DataFrame(new_disc)
    global relatorio
    relatorio = pandas.concat([relatorio, new_csv], ignore_index=True)
    carregar_decoraçoes()
def apagar():
    item_selecionado = tree.selection()[0]
    valores = tree.item(item_selecionado, "values")
    produto_id = valores[1]
    global relatorio
    relatorio = relatorio[relatorio['Cliente'] != produto_id]
    relatorio = relatorio.reset_index(drop=True)
    carregar_decoraçoes()
def salvar():
    global relatorio
    relatorio.to_csv("Sara_planilia.csv", index=0)
    messagebox.showinfo("concluido", "salvo com sucesso")
def alterar():
    Data = entry_data.get()
    Cliente = entry_nome.get()
    Valor = entry_valor.get()
    Tema = entry_tema.get()
    Telefone = entry_tele.get()

    if not Data or not Cliente or not Valor or not Tema or not Telefone:
        messagebox.showerror("erro", "Todos campos obrigatorios mae")
        return
    entry_data.delete(0, tk.END)
    entry_tema.delete(0, tk.END)
    entry_valor.delete(0, tk.END)
    entry_nome.delete(0, tk.END)
    entry_tele.delete(0, tk.END)

    item_selecionado = tree.selection()[0]
    valores = tree.item(item_selecionado, "values")
    produto_id = valores[1]

    relatorio.loc[relatorio["Cliente"] == produto_id, ["Data", "Cliente", "Valor", "Tema", "Telefone"]] = [Data, Cliente, Valor, Tema, Telefone]
    carregar_decoraçoes()

#janela
janela = tk.Tk()
janela.title("Gerenciador")
janela.geometry("800x600")
janela.config()

estilo = ttk.Style()
estilo.theme_use("clam")

#titulo
frame_titulo = tk.Frame(janela)
frame_titulo.pack(pady=10)
titulo = tk.Label(janela ,bg="#cfcedb", text="Gerenciador de Decoração",fg="#000000", font=('Helvetica', 25, "bold")).pack(side="top", fill="x")



#frame entradas
frame_entradas = tk.Frame(janela)
frame_entradas.pack(fill="x")

tk.Label(frame_entradas, text="Data", font=("Tahoma", 14, "bold")).grid(row=0, column=1,padx=20, pady=10)
entry_data = tk.Entry(frame_entradas)
entry_data.grid(row=0, column=2, padx=0, pady=0)

tk.Label(frame_entradas, text="Nome", font=("Tahoma", 14, "bold")).grid(row=1, column=1,padx=20, pady=10)
entry_nome = tk.Entry(frame_entradas)
entry_nome.grid(row=1, column=2, padx=0, pady=0)

tk.Label(frame_entradas, text="Valor", font=("Tahoma", 14, "bold")).grid(row=2, column=1,padx=20, pady=0)
entry_valor = tk.Entry(frame_entradas)
entry_valor.grid(row=2, column=2, padx=0, pady=0)

tk.Label(frame_entradas, text="Tema", font=("Tahoma", 14, "bold")).grid(row=3, column=1,padx=20, pady=10)
entry_tema = tk.Entry(frame_entradas)
entry_tema.grid(row=3, column=2, padx=0, pady=0)

tk.Label(frame_entradas, text="Telefone", font=("Tahoma", 14, "bold")).grid(row=4, column=1,padx=20, pady=10)
entry_tele = tk.Entry(frame_entradas)
entry_tele.grid(row=4, column=2, padx=0, pady=0)

botao_adicionar = tk.Button(frame_entradas, text="adicionar", font=("arial", 15), bg="#30c755", command=adicionar)
botao_adicionar.grid(row= 0, column=3, padx=30)

botao_apagar = tk.Button(frame_entradas, text="apagar", font=("arial", 15), bg="#c73030", command=apagar)
botao_apagar.grid(row= 1, column=3, padx=30)

botao_salvar = tk.Button(frame_entradas, text="salvar", font=("arial", 15), bg="#ffee00", command=salvar)
botao_salvar.grid(row= 2, column=3, padx=30)

botao_alte = tk.Button(frame_entradas, text="alterar", font=("arial", 15), bg="#ffee00", command=alterar)
botao_alte .grid(row= 3, column=3, padx=30)

listbox = tk.Listbox(frame_entradas, selectmode=tk.SINGLE, height=5)
opcoes = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezenbro"]
for opcao in opcoes:
    listbox.insert(tk.END, opcao)  # Adiciona as opções na lista
listbox.grid(row=2, column=4)

botao_calcular = tk.Button(frame_entradas, text="Calcular o ganho total do mes: ", command=calculo)
botao_calcular.grid(row=1, column=4)

resultado = tk.Label(frame_entradas, text="Clique no botao:", font=("arial", 15, "bold"))
resultado.grid(row=2, column=5)

#criaçao do tree
frame_tabela = tk.Frame(janela).pack(fill="both", expand=True)

colunas = ("Data", "Cliente", "Valor", "Tema", "Telefone")
tree = ttk.Treeview(frame_tabela, columns=colunas, show="headings", selectmode="browse")

tree.heading("#0", text="", anchor=tk.W)
tree.heading("Data", text="Data", anchor=tk.W)
tree.heading("Cliente", text="Cliente", anchor=tk.W)
tree.heading("Valor", text="Valor", anchor=tk.W)
tree.heading("Tema", text="Tema", anchor=tk.W)
tree.heading("Telefone", text="Telefone", anchor=tk.W)

tree.column("#0", width=0, stretch=tk.NO)
tree.column("Data", width=100)
tree.column("Cliente", width=100)
tree.column("Valor", width=80)
tree.column("Tema", width=100)
tree.column("Telefone", width=120)

scrol = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrol.set)
scrol.pack(side="right", fill="y")
tree.pack(pady=20, fill="both", expand=True)
carregar_decoraçoes()
janela.mainloop()