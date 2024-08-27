import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def submit_data():
    root.nome_proponente = entry_nome_proponente.get()
    root.objeto_servico = entry_objeto_servico.get()
    root.atividade = entry_atividade.get()

    imovel_selecionado = []
    if var_imovel_rural.get():
        imovel_selecionado.append("Rural")
    if var_imovel_urbano.get():
        imovel_selecionado.append("Urbano")
    root.imovel = ", ".join(imovel_selecionado)

    root.denominacao_imovel = entry_denominacao_imovel.get()

    genero_selecionado = []
    if var_genero_sr.get():
        genero_selecionado.append("Sr")
    if var_genero_sra.get():
        genero_selecionado.append("Sra")
    root.genero = ", ".join(genero_selecionado)

    root.cpf = entry_cpf.get()
    root.orgao_ambiental = combo_orgao_ambiental.get()
    root.prazo_dias = entry_prazo_dias.get()

    root.municipio = combo_municipio.get() if label_municipio.winfo_ismapped() else ""
    root.estado = entry_estado.get() if "Estadual" in combo_orgao_ambiental.get() else ""
    root.federal = entry_federal.get() if "Federal" in combo_orgao_ambiental.get() else ""

    root.destroy()

def on_orgao_ambiental_change(event):
    selection = combo_orgao_ambiental.get()
    if selection == "Municipal":
        label_municipio.grid(row=10, column=0, padx=2, pady=1, sticky='w')
        combo_municipio.grid(row=10, column=1, padx=2, pady=1)
        label_estado.grid_remove()
        entry_estado.grid_remove()
        label_federal.grid_remove()
        entry_federal.grid_remove()
    elif selection == "Estadual":
        label_estado.grid(row=10, column=0, padx=2, pady=1, sticky='w')
        entry_estado.grid(row=10, column=1, padx=2, pady=1)
        label_municipio.grid(row=11, column=0, padx=2, pady=1, sticky='w')
        combo_municipio.grid(row=11, column=1, padx=2, pady=1)
        label_federal.grid_remove()
        entry_federal.grid_remove()
    elif selection == "Municipal e Estadual":
        label_municipio.grid(row=10, column=0, padx=2, pady=1, sticky='w')
        combo_municipio.grid(row=10, column=1, padx=2, pady=1)
        label_estado.grid(row=11, column=0, padx=2, pady=1, sticky='w')
        entry_estado.grid(row=11, column=1, padx=2, pady=1)
        label_federal.grid_remove()
        entry_federal.grid_remove()
    elif selection == "Federal":
        label_federal.grid(row=10, column=0, padx=2, pady=1, sticky='w')
        entry_federal.grid(row=10, column=1, padx=2, pady=1)
        entry_federal.delete(0, tk.END)
        entry_federal.insert(0, "IBAMA")
        label_municipio.grid(row=11, column=0, padx=2, pady=1, sticky='w')
        combo_municipio.grid(row=11, column=1, padx=2, pady=1)
        label_estado.grid_remove()
        entry_estado.grid_remove()
    elif selection == "Federal e Municipal":
        label_federal.grid(row=10, column=0, padx=2, pady=1, sticky='w')
        entry_federal.grid(row=10, column=1, padx=2, pady=1)
        entry_federal.delete(0, tk.END)
        entry_federal.insert(0, "IBAMA")
        label_municipio.grid(row=11, column=0, padx=2, pady=1, sticky='w')
        combo_municipio.grid(row=11, column=1, padx=2, pady=1)
        label_estado.grid_remove()
        entry_estado.grid_remove()
    else:
        label_municipio.grid_remove()
        combo_municipio.grid_remove()
        label_estado.grid_remove()
        entry_estado.grid_remove()
        label_federal.grid_remove()
        entry_federal.grid_remove()

# Criando a janela principal
root = tk.Tk()
root.title("Formulário de Entrada")
root.configure(bg="#f0f0f0")

# Labels e Entradas de Texto
tk.Label(root, text="Nome do Cliente:", bg="#f0f0f0", font=('Arial', 12)).grid(row=0, column=0, padx=2, pady=5, sticky='w')
entry_nome_proponente = tk.Entry(root, width=40, font=('Arial', 12), highlightbackground="#cccccc", highlightthickness=1)
entry_nome_proponente.grid(row=0, column=1, padx=2, pady=5)

tk.Label(root, text="CPF:", bg="#f0f0f0", font=('Arial', 12)).grid(row=1, column=0, padx=2, pady=5, sticky='w')
entry_cpf = tk.Entry(root, width=40, font=('Arial', 12), highlightbackground="#cccccc", highlightthickness=1)
entry_cpf.grid(row=1, column=1, padx=2, pady=5)

tk.Label(root, text="Objeto de Proposta:", bg="#f0f0f0", font=('Arial', 12)).grid(row=6, column=0, padx=2, pady=5, sticky='w')
entry_objeto_servico = tk.Entry(root, width=40, font=('Arial', 12), highlightbackground="#cccccc", highlightthickness=1)
entry_objeto_servico.grid(row=6, column=1, padx=2, pady=5)

tk.Label(root, text="Gênero:", bg="#f0f0f0", font=('Arial', 12)).grid(row=2, column=0, padx=2, pady=5, sticky='w')
var_genero_sr = tk.BooleanVar()
var_genero_sra = tk.BooleanVar()
tk.Checkbutton(root, text="Sr", variable=var_genero_sr, bg="#f0f0f0", font=('Arial', 12)).grid(row=2, column=1, padx=2, pady=5, sticky='w')
tk.Checkbutton(root, text="Sra", variable=var_genero_sra, bg="#f0f0f0", font=('Arial', 12)).grid(row=2, column=1, padx=2, pady=20, sticky='s')

tk.Label(root, text="Atividade:", bg="#f0f0f0", font=('Arial', 12)).grid(row=7, column=0, padx=2, pady=5, sticky='w')
entry_atividade = tk.Entry(root, width=40, font=('Arial', 12), highlightbackground="#cccccc", highlightthickness=1)
entry_atividade.grid(row=7, column=1, padx=2, pady=5)

tk.Label(root, text="Imóvel:", bg="#f0f0f0", font=('Arial', 12)).grid(row=3, column=0, padx=2, pady=5, sticky='w')
var_imovel_rural = tk.BooleanVar()
var_imovel_urbano = tk.BooleanVar()
tk.Checkbutton(root, text="Rural", variable=var_imovel_rural, bg="#f0f0f0", font=('Arial', 12)).grid(row=3, column=1, padx=2, pady=5, sticky='w')
tk.Checkbutton(root, text="Urbano", variable=var_imovel_urbano, bg="#f0f0f0", font=('Arial', 12)).grid(row=3, column=1, padx=2, pady=20, sticky='s')

tk.Label(root, text="Nome do Imóvel:", bg="#f0f0f0", font=('Arial', 12)).grid(row=4, column=0, padx=2, pady=5, sticky='w')
entry_denominacao_imovel = tk.Entry(root, width=40, font=('Arial', 12), highlightbackground="#cccccc", highlightthickness=1)
entry_denominacao_imovel.grid(row=4, column=1, padx=2, pady=5)

tk.Label(root, text="Prazo (dias):", bg="#f0f0f0", font=('Arial', 12)).grid(row=8, column=0, padx=2, pady=5, sticky='w')
entry_prazo_dias = tk.Entry(root, width=40, font=('Arial', 12), highlightbackground="#cccccc", highlightthickness=1)
entry_prazo_dias.grid(row=8, column=1, padx=2, pady=5)

tk.Label(root, text="Esfera:", bg="#f0f0f0", font=('Arial', 12)).grid(row=9, column=0, padx=2, pady=5, sticky='w')
combo_orgao_ambiental = ttk.Combobox(root, values=["Municipal", "Estadual", "Municipal e Estadual", "Federal", "Federal e Municipal"], state="readonly", width=37, font=('Arial', 12))
combo_orgao_ambiental.grid(row=9, column=1, padx=2, pady=5)
combo_orgao_ambiental.bind("<<ComboboxSelected>>", on_orgao_ambiental_change)

# Campos adicionais (inicialmente ocultos)
label_municipio = tk.Label(root, text="Município:", bg="#f0f0f0", font=('Arial', 12))
combo_municipio = ttk.Combobox(root, values=["Palmas - TO", "Porto Nacional - TO", "Araguaina - TO", "Gurupi - TO"], width=37, font=('Arial', 12))
combo_municipio.set("Palmas - TO")  # Define um valor padrão
combo_municipio['state'] = 'normal'  # Permite a edição dos valores

label_estado = tk.Label(root, text="Orgão estadual:", bg="#f0f0f0", font=('Arial', 12))
entry_estado = tk.Entry(root, width=40, font=('Arial', 12), highlightbackground="#cccccc", highlightthickness=1)

label_federal = tk.Label(root, text="Federal:", bg="#f0f0f0", font=('Arial', 12))
entry_federal = tk.Entry(root, width=40, font=('Arial', 12), highlightbackground="#cccccc", highlightthickness=1)

# Botão de Envio
submit_button = tk.Button(root, text="Enviar", command=submit_data, bg="#4CAF50", fg="white", font=('Arial', 12), padx=10, pady=5)
submit_button.grid(row=12, column=0, columnspan=2, pady=20)

# Executando a janela
root.mainloop()

# Aqui você pode acessar as variáveis e usá-las
print("Nome do Proponente:", root.nome_proponente)
print("Objeto Serviço:", root.objeto_servico)
print("Atividade:", root.atividade)
print("Imóvel:", root.imovel)
print("Denominação Imóvel:", root.denominacao_imovel)

print("Gênero:", root.genero)
print("CPF:", root.cpf)
print("Órgão Ambiental:", root.orgao_ambiental)
print("Município:", root.municipio)
print("Estado:", root.estado)
print("Federal:", root.federal)
print("Prazo (dias):", root.prazo_dias)
