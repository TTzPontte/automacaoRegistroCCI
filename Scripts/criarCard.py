import requests
import json
from unidecode import unidecode

def createCardPipefy(dadosPipefy, dadosC, dadosI, nomeTitular, dataNascimentoTitular, cpfTitular, idPipefy, pularMes, idAztronic, participacaoTitular, produto):
    
    try:
        print(f'Caso de erro, segue algumas informações úteis para teste:\nDadosPipefy: {dadosPipefy}\n\n\nDados do contrato: {dadosC}\n\n\nDados Imóvel: {dadosI}\n\n\n')
    except:
        print("Não foi possível apresentar os dados úteis em caso de erro.")
    
    nomeTitular = unidecode(str(nomeTitular))
    idAztronic = idAztronic
    idPipefy = idPipefy
    produto = str(produto)
    operação = str(dadosC['operação'])
    cpfTitular = str(cpfTitular).replace(".","").replace("-","").replace("/", "")
    dataNascimentoTitular = str(dataNascimentoTitular)
    participacaoTitular = str(participacaoTitular)
    valorBruto = str(dadosC['valorBruto']).replace(",",".")
    taxaAoAno = str(dadosC['taxaAoAno'])
    tabela = str(dadosC['tabela'])
    indice = str(dadosC['indice'])
    pularMes = str(pularMes)
    prazoOps = str(dadosPipefy['prazoOps'])
    numeroParcelas = str(dadosPipefy['numeroParcelas'])
    dataDesembolso = str(dadosPipefy['dataDesembolso'])
    dataUltimaParcela = str(dadosPipefy['dataUltimaParcela'])
    valorPriParcela = str(dadosPipefy['valorPriParcela']).replace(",",".")
    valorTotalPriParcela = str(dadosPipefy['valorTotalPriParcela']).replace(",",".")
    dataContrato = str(dadosC['dataContrato'])
    enderecoImovel = unidecode(str(dadosI['enderecoImovel']))
    numeroImovel = str(dadosI['numeroImovel'])
    complementoImovel = unidecode(str(dadosI['complementoImovel']))
    bairroImovel = unidecode(str(dadosI['bairroImovel']))
    cidadeImovel = unidecode(str(dadosI['cidadeImovel']))
    estadoImovel = unidecode(str(dadosI['estadoImovel']))
    cepImovel = str(dadosI['cepImovel'])
    valorImovel = str(dadosI['valorImovel']).replace(",",".")
    Matricula = str(dadosC['Matrícula'])
    nomeCartorio = unidecode(str(dadosC['nomeCartorio']))



    url = "https://api.pipefy.com/graphql"

    payload = "{\"query\":\"mutation {\\r\\n  createCard(input:{\\r\\n    pipe_id: 303034998 \\r\\n fields_attributes: [\\r\\n       \\r\\n        {field_id:\\\"nome_do_cliente\\\", field_value: \\\""+nomeTitular+"\\\"}{field_id:\\\"id_aztronic\\\", field_value: "+str(idAztronic)+"}{field_id:\\\"id_pipefy_antigo\\\", field_value: "+str(idPipefy)+"}{field_id:\\\"produto\\\", field_value: \\\""+produto+"\\\"}{field_id:\\\"tipo_de_opera_o\\\", field_value: \\\""+operação+"\\\"}{field_id:\\\"cpf\\\", field_value: "+str(cpfTitular)+"}{field_id:\\\"data_de_nascimento\\\", field_value: \\\""+dataNascimentoTitular+"\\\"}{field_id:\\\"participa_o\\\", field_value: "+str(participacaoTitular)+"}{field_id:\\\"valor_bruto\\\", field_value: "+str(valorBruto)+"}{field_id:\\\"taxa_de_juros_aa\\\", field_value: "+str(taxaAoAno)+"}{field_id:\\\"sistema_de_amortiza_o\\\", field_value: \\\""+tabela+"\\\"}{field_id:\\\"ndice_de_corre_o\\\", field_value: \\\""+indice+"\\\"}{field_id:\\\"pular_m_s\\\", field_value: \\\""+pularMes+"\\\"}{field_id:\\\"prazo_da_opera_o\\\", field_value: "+str(prazoOps)+"}{field_id:\\\"n_mero_de_parcelas\\\", field_value: "+str(numeroParcelas)+"}{field_id:\\\"data_de_desembolso\\\", field_value: \\\""+dataDesembolso+"\\\"}{field_id:\\\"data_da_ltima_parcela\\\", field_value: \\\""+dataUltimaParcela+"\\\"}{field_id:\\\"primeira_parcela_amortiza_o_juros\\\", field_value: "+str(valorPriParcela)+"}{field_id:\\\"primeira_parcela_total\\\", field_value: "+str(valorTotalPriParcela)+"}{field_id:\\\"data_de_assinatura\\\", field_value: \\\""+dataContrato+"\\\"}{field_id:\\\"endere_o_do_im_vel_em_garantia\\\", field_value: \\\""+enderecoImovel+"\\\"}{field_id:\\\"n_mero_do_im_vel_em_garantia\\\", field_value: "+str(numeroImovel)+"}{field_id:\\\"complemento_do_im_vel_em_garantia\\\", field_value: \\\""+complementoImovel+"\\\"}{field_id:\\\"bairro_do_im_vel_em_garantia\\\", field_value: \\\""+bairroImovel+"\\\"}{field_id:\\\"cidade_do_im_vel_em_garantia\\\", field_value: \\\""+cidadeImovel+"\\\"}{field_id:\\\"estado_do_im_vel_em_garantia\\\", field_value: \\\""+estadoImovel+"\\\"}{field_id:\\\"cep_do_im_vel_em_garantia\\\", field_value: \\\""+cepImovel+"\\\"}{field_id:\\\"valor_de_avalia_o_do_im_vel_em_garantia\\\", field_value: "+str(valorImovel)+"}{field_id:\\\"matr_cula_do_im_vel_em_garantia\\\", field_value: "+str(Matricula)+"}{field_id:\\\"cart_rio_do_im_vel_em_garantia\\\", field_value: \\\""+nomeCartorio+"\\\"}    \\r\\n        ] \\r\\n  }){\\r\\n    card {\\r\\n      id\\r\\n      title\\r\\n    }\\r\\n  }\\r\\n}\",\"variables\":{}}"
    print(f'Payload: \n{payload}\n\n\n')
    headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VyIjp7ImlkIjozMDEyNjA0NzYsImVtYWlsIjoiZGV2QHBvbnR0ZS5jb20uYnIiLCJhcHBsaWNhdGlvbiI6MzAwMjI0MjU1fX0.mETDV7VXfKgr7ubBcEqtf1IyJ2OHbOjgUFKF3Bk7J2We_UUXNh0oq0N6ZEmVsLYaqPyQR2qx7yn7KfpztPoqcg',
    'Content-Type': 'application/json',
    'Cookie': '__cfruid=25df916f2006ec3736c28c23b0acc5774e071d3c-1677785914'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


#Realizar Testes

#Dict para teste
# dadosPipefyT = {'prazoOps': '240', 'numeroParcelas': '239', 'dataDesembolso': '06/03/2023', 'dataUltimaParcela': '20/03/2043', 'valorPriParcela': '4694,02', 'valorTotalPriParcela': '4844,41'}
# dadosContratoT = {'tabela': 'PRICE', 'indice': 'IPCA', 'dataContrato': '02/03/2023', 'taxaAoAno': '14.4353', 'Matrícula': '49661', 'Quantidade': '1', 'operação': 'PF', 'CCI': '0004474693/TJS', 'valorBruto': '380667,43', 'nomeCartorio': '1º OFÍCIO DE REGISTRO DE IMÓVEIS', 'idCartorio': 4155801}
# dadosImovelT = {'enderecoImovel': 'Rua Barão de Loreto', 'numeroImovel': '154', 'complementoImovel': 'N/A', 'bairroImovel': 'Vila Fujita', 'cepImovel': '86015-550', 'cidadeImovel': 'Londrina', 'estadoImovel': 'PR', 'unidadeImovel': '154', 'blocoImovel': 'ÚNICO', 'valorImovel': '1192000,00'}

# #Variáveis para teste
# nomeTeste = "CAMPIOL EMPREENDIMENTOS LTDA ."
# dataTeste = "26/05/2009"
# cpfTeste = "11.759.641/0001-40"
# idPipefyTeste = 589968041
# pularMesTeste = "Nenhum"
# idAztronicTeste = 130430
# participacaoTeste = 0
# produtoTeste = "HE"

# createCardPipefy(dadosPipefyT, dadosContratoT, dadosImovelT, nomeTeste, dataTeste, cpfTeste, idPipefyTeste,
#                  pularMesTeste, idAztronicTeste, participacaoTeste, produtoTeste)
