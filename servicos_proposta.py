import tkinter as tk
from tkinter import messagebox
import pandas as pd

# Carregar a planilha
file_path = 'servicos_ambientais_corrigido.xlsx' #TODO : aqui tambem
df = pd.read_excel(file_path)

# Extrair os serviços da primeira coluna e as descrições da segunda
services = df.iloc[:, 0].tolist()
descriptions = df.iloc[:, 1].tolist()

# Variáveis para armazenar os serviços e descrições finais
final_services = []
final_descriptions = []

# Funções de animação para transições de cor suave
def on_enter(e, button, color):
    button['background'] = color

def on_leave(e, button, color):
    button['background'] = color

def animate_button(button, initial_color, hover_color):
    button.bind("<Enter>", lambda e: on_enter(e, button, hover_color))
    button.bind("<Leave>", lambda e: on_leave(e, button, initial_color))

def confirm_services():
    selected_indices = service_list.curselection()
    if selected_indices:
        selected_services = [services[idx] for idx in selected_indices]
        selected_descriptions = [descriptions[idx] for idx in selected_indices]
        
        # Criação de uma janela de confirmação mais detalhada
        confirmation_window = tk.Toplevel(root)
        confirmation_window.title("Confirmar Serviços Selecionados")
        confirmation_window.configure(bg='#f8f9fa')

        tk.Label(confirmation_window, text="Você selecionou os seguintes serviços:", font=('Arial', 16, 'bold'), bg='#f8f9fa', fg='#343a40').pack(pady=10)

        confirmation_frame = tk.Frame(confirmation_window, bg='#f8f9fa')
        confirmation_frame.pack(padx=20, pady=10)

        # Adicionando uma barra de rolagem para o texto de confirmação
        confirmation_scrollbar = tk.Scrollbar(confirmation_frame)
        confirmation_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        confirmation_text = tk.Text(
            confirmation_frame, 
            font=('Arial', 12), 
            wrap=tk.WORD, 
            width=80, 
            height=20, 
            bg='#ffffff', 
            fg='#333333', 
            yscrollcommand=confirmation_scrollbar.set,
            selectbackground='#d6e9f8',  # Cor de fundo mais clara ao selecionar texto
            selectforeground='#003366'   # Cor do texto ao selecionar
        )
        confirmation_text.pack(side=tk.LEFT)
        confirmation_scrollbar.config(command=confirmation_text.yview)
        
        # Inserindo os serviços e suas descrições
        for idx, (service, description) in enumerate(zip(selected_services, selected_descriptions)):
            confirmation_text.insert(tk.END, f"Serviço: {service}\n", 'service')
            confirmation_text.insert(tk.END, f"Descrição:\n{description}\n\n", 'description')

        # Aplicando cores diferentes para serviços e descrições
        confirmation_text.tag_config('service', foreground='#007bff', font=('Arial', 12, 'bold'))
        confirmation_text.tag_config('description', foreground='#6c757d', font=('Arial', 12))

        def proceed():
            global final_services, final_descriptions
            # Salvando as descrições editadas
            updated_text = confirmation_text.get("1.0", tk.END).strip().split("\n\n")
            for i, text in enumerate(updated_text):
                if "Descrição:\n" in text:
                    description = text.split("Descrição:\n")[1]
                    descriptions[selected_indices[i]] = description.strip()
            
            final_services = selected_services
            final_descriptions = [descriptions[idx] for idx in selected_indices]
            confirmation_window.destroy()
            root.destroy()

        # Botão Confirmar com animação de cor
        confirm_button = tk.Button(confirmation_window, text="Confirmar e Prosseguir", command=proceed, font=('Arial', 14), bg='#28a745', fg='white', activebackground='#218838', activeforeground='white')
        confirm_button.pack(pady=10)
        animate_button(confirm_button, '#28a745', '#218838')

        # Botão Cancelar com animação de cor
        cancel_button = tk.Button(confirmation_window, text="Cancelar", command=confirmation_window.destroy, font=('Arial', 14), bg='#dc3545', fg='white', activebackground='#c82333', activeforeground='white')
        cancel_button.pack(pady=5)
        animate_button(cancel_button, '#dc3545', '#c82333')

    else:
        messagebox.showinfo("Serviços Selecionados", "Nenhum serviço selecionado.")

# Criação da janela principal com mais cores e animações
root = tk.Tk()
root.title("Seleção de Serviços")
root.configure(bg='#f2f2f2')

# Configuração do Listbox com cores mais vivas e animação de seleção
service_list = tk.Listbox(root, selectmode=tk.MULTIPLE, width=80, height=20, font=('Arial', 12), bg='#e6f7ff', fg='#003366', selectbackground='#b3d9ff', selectforeground='#001a33')
service_list.pack(padx=20, pady=20)

for service in services:
    service_list.insert(tk.END, service)

# Botão de Confirmar Serviços com animação de cor
confirm_button = tk.Button(root, text="Confirmar Serviços", command=confirm_services, font=('Arial', 14), bg='#007acc', fg='white', activebackground='#005f99', activeforeground='white')
confirm_button.pack(pady=10)
animate_button(confirm_button, '#007acc', '#005f99')

root.mainloop()

# Exemplo de uso das variáveis após a seleção e confirmação
# print("Serviços selecionados:", final_services)
# print("Descrições selecionadas:", final_descriptions)
