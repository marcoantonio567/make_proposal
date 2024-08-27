from datetime import datetime
import re
import pyautogui

def obter_mes_atual():
    # Obtém o mês atual
    mes_atual = datetime.now().month

    # Lista de meses em português
    meses = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]

    # Retorna o nome do mês atual
    return meses[mes_atual - 1]

dia_atual = datetime.now().day

def calcular_percentual(parcela, total):
    return (parcela / total) * 100
ano_atual = datetime.now().year

def formatar_cpf(cpf: str) -> str:
    # Remove qualquer caractere que não seja dígito
    cpf_numeros = re.sub(r'\D', '', cpf)
    
    # Verifica se o CPF tem 11 dígitos
    if len(cpf_numeros) != 11:
        pyautogui.alert('Erro: O CPF deve conter exatamente 11 dígitos numéricos.', 'Erro de Formatação')
        return ''
    
    # Verifica se todos os caracteres são números
    if not cpf_numeros.isdigit():
        pyautogui.alert('Erro: O CPF deve conter apenas dígitos.', 'Erro de Formatação')
        return ''
    
    # Formata o CPF
    cpf_formatado = f'{cpf_numeros[:3]}.{cpf_numeros[3:6]}.{cpf_numeros[6:9]}-{cpf_numeros[9:]}'
    
    return cpf_formatado
    


mes_atual = obter_mes_atual()