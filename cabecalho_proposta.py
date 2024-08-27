from raiz_cabecalho import *

# Solicitação de informações do serviço
objeto_serviço =  root.objeto_servico
atividade = root.atividade
imovel =  root.imovel
denominacao_imovel = root.denominacao_imovel
federal =  root.federal
# Seleção de gênero
select_genero = root.genero

ultima_letra_inscricao = 'o' if select_genero == 'Sr' else 'a'

# Solicitação de CPF
cpf =  root.cpf

# Seleção de órgão ambiental e solicitações adicionais
orgao_ambiental = root.orgao_ambiental

nome_proponente = root.nome_proponente

municipio = root.municipio
estado = root.estado
prazo = root.prazo_dias
orgao_ambiental = root.orgao_ambiental
#verificação rapida de senhor ou senhora
if ultima_letra_inscricao == 'o':
    ele_ou_ela = 'Sr'
else:
    ele_ou_ela = 'Sra'
#verificação rapida sobre o escopo 2
cidade_atendentes = ["Palmas - TO", "Porto nacional - TO", "Araguaina - TO", "Gurupi - TO"]
if municipio in cidade_atendentes:
    texto_escopo_opcional = ""
else: 
    texto_escopo_opcional = f'junto ao orgão ambiental {orgao_ambiental}'