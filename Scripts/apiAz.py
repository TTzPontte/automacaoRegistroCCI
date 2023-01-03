### Bibliotecas ###

import requests
import json
from lerCalculoFluxo import lerCF
import datetime
### Função para preencher os campos da API ###

def preencherAPI(pathCF, textoContrato, textoLaudo, textoParticipantes, produto):

    # Url da API
    url = "https://srv1.aztronic.com.br/AZ/APICollect/api/contrato/set" #prod
    #url = "https://dev.aztronic.com.br/AZ/APICollect/api/contrato/set" #DEV

    # Data do dia
    dataHoje = datetime.date.today()
    data_em_texto = '{}/{}/{}'.format(dataHoje.month, dataHoje.day,dataHoje.year)


    # Dicionario com os dados
    participantes = textoParticipantes
    Laudo = textoLaudo
# Montar Dicionario garantia
    # Laudo 
 
    ruaL = Laudo['enderecoImovel']
    numeroL = Laudo['numeroImovel']
    complementoL = Laudo['complementoImovel']
    cidadeL = Laudo['cidadeImovel']
    bairroL = Laudo['bairroImovel']
    ufL = Laudo['estadoImovel']
    cepL = Laudo['cepImovel']
    unidadeL = Laudo['unidadeImovel']
    blocoL = Laudo['blocoImovel']
    #valorL = Laudo['valorImovel'] #Base Teste Aztronic
    valorL = float(Laudo['valorImovel'].replace(".","").replace(",","."))

    # Contrato
    Contrato = textoContrato
    matriculaC = Contrato['Matrícula']
    dataContratoCon = Contrato['dataContrato']
    date = datetime.datetime.strptime(dataContratoCon, '%d/%m/%Y')
    dataContratoC = '{}/{}/{}'.format(date.month, date.day,date.year)
    codigoIntegracaoC = ''.join([d for d in Contrato['CCI'] if d.isdigit()])
    #valorC = Contrato["valorBruto"] #Base Teste Aztronic
    valorC = float(Contrato["valorBruto"].replace(".","").replace(",","."))
    contadorC = int(Contrato['Quantidade'])
    indiceC = Contrato['indice']
    tabelaC = 1 if Contrato['tabela'] == "SAC" else 2
    taxaC = round(float(Contrato['taxaAoAno']),4)
    CartorioC = Contrato['nomeCartorio']
    idCartorioC = Contrato['idCartorio']
    if produto == "HE":
        produtoC = "15"
    elif produto == "FI":
        produtoC = "16"

    #Fluxo
    fluxoJson = lerCF(pathCF, codigoIntegracaoC)
    fluxo = json.loads(fluxoJson)
    unidadeJson = { 
            "codigo_integracao": codigoIntegracaoC,
            "rua": ruaL,
            "numero": numeroL,
            "complemento": complementoL,
            "cidade": cidadeL,
            "bairro": bairroL,
            "UF": ufL,
            "cep": cepL,
            "cnpj_SPE": "32.402.502/0001-35",
            "SPE": "QI SOCIEDADE DE CREDITO DIRETO S.A.",
            "cartorio": CartorioC, # nome do cartório
            "valor_avaliacao": valorL,
            "unidade": unidadeL,
            "Bloco": blocoL,
            "matricula": matriculaC,
            "numero_cartorio": idCartorioC, # id do cartório
            "data_habitese": "01/01/2000"
            }



    
# Montar Dicionario dos participantes
    listaDeParaP = {"relacao": 0,"nome": 0,"email": 0,"participacao": 0,"cnpj_cpf": 0,"pf_pj": 0,"sexo": 0,"telefone": 0,"data_nascimento": 0,"rua": 0,"numero": 0,"complemento": 0,
"cidade": 0,"bairro": 0,"UF": 0,"cep": 0
            }
    quant = int(Contrato["Quantidade"])
    dadosParticipantes={}
    participantesJson = []
    for cont in range(0,quant):
        dadosParticipantes["codigo_integracao"] = codigoIntegracaoC
        for key in listaDeParaP.keys():         
            if key == "relacao":
                if participantes[f"relacaoDoP{cont+1}"] == "Cônjuge":
                    dadosParticipantes[key] = "2"
                elif participantes[f"relacaoDoP{cont+1}"] == "Sócio(a)":
                    dadosParticipantes[key] = "11"
                elif participantes[f"relacaoDoP{cont+1}"] == "Titular":
                    dadosParticipantes[key] = "1"
                elif participantes[f"relacaoDoP{cont+1}"] == "Representante Legal":
                    dadosParticipantes[key] = "13"
                elif participantes[f"relacaoDoP{cont+1}"] == "Adquirinte":
                    dadosParticipantes[key] = "14"   
                elif participantes[f"relacaoDoP{cont+1}"] == "Procurador":
                    dadosParticipantes[key] = "15"      
                elif participantes[f"relacaoDoP{cont+1}"] == "Fiador(a)":
                    dadosParticipantes[key] = "16"   
                elif participantes[f"relacaoDoP{cont+1}"] == "Pai":
                    dadosParticipantes[key] = "17"
                elif participantes[f"relacaoDoP{cont+1}"] == "Mãe":
                    dadosParticipantes[key] = "18"
                elif participantes[f"relacaoDoP{cont+1}"] == "Irmão":
                    dadosParticipantes[key] = "19"                                              
            elif key == "nome":
                dadosParticipantes[key]= participantes[f"nomeCompletoP{cont+1}"]
            elif key == "email":
                dadosParticipantes[key]= participantes[f"emailP{cont+1}"]
            elif key == "participacao":
                dadosParticipantes[key]= participantes[f"participacaoNaOperacaoP{cont+1}"]
            elif key == "cnpj_cpf":
                dadosParticipantes[key]= participantes[f"cpfP{cont+1}"]
            elif key == "pf_pj":
                if participantes[f"tipoOperacaoP{cont+1}"] == "PF":
                    dadosParticipantes[key] = "F"  
                elif participantes[f"tipoOperacaoP{cont+1}"] == "PJ":
                    dadosParticipantes[key] = "J"
            elif key == "sexo":
                dadosParticipantes[key]= participantes[f"sexoP{cont+1}"]
            elif key == "telefone":
                dadosParticipantes[key]= participantes[f"telefoneP{cont+1}"]
            elif key == "data_nascimento":
                dadosParticipantes[key]= participantes[f"dataNascimentoP{cont+1}"]
            elif key == "rua":
                dadosParticipantes[key]= participantes[f"endereçoP{cont+1}"]
            elif key == "numero":
                dadosParticipantes[key]= participantes[f"numeroResidenciaP{cont+1}"]
            elif key == "complemento":
                dadosParticipantes[key]= participantes[f"complementoP{cont+1}"]
            elif key == "cidade":
                dadosParticipantes[key]= participantes[f"cidadeP{cont+1}"]
            elif key == "bairro":
                dadosParticipantes[key]= participantes[f"bairroP{cont+1}"]
            elif key == "UF":
                dadosParticipantes[key]= participantes[f"estadoP{cont+1}"]
            elif key == "cep":
                dadosParticipantes[key]= participantes[f"cepP{cont+1}"]

        participantesJson.append(dadosParticipantes.copy())



    
    
    # Montar o Json (contrato, participantes, tabela de vendas, fluxo)
    
    jsonFinal = {"contrato": {
            "codigo_integracao": codigoIntegracaoC,
            "pep": "",
            "id_projeto": "379",
            "id_tipocontrato": produtoC,
            "id_tipovenda": "1",
            "valor_contrato": valorC,
            "data_contrato": dataContratoC,
            "valor_venda": valorL,
            "taxa_multa": "2",
            "taxa_mora": "1",
            "venda_no_estado": "S",
            "score_automatico": "80",
            "score_manual": "85",
            "seguro_mip": 0.021,
            "seguro_dfi": 0.0037,
            "taxa_administracao": 25,

            "unidade": unidadeJson,

            "participante": participantesJson,

            "tabelavenda": {
            "codigo_integracao": codigoIntegracaoC,
            "data_base":     dataContratoC,
            "data_averbacao": data_em_texto,
            "indice_pre": "2" if indiceC == "IGPM" else "7",
            "defasagem": "2",
            "taxa_juros": taxaC,
            "tipo_amortizacao": tabelaC
            },
            "fluxo": fluxo,
        }
        }
    ## Json POST ##
    #print(jsonFinal)
    payload = json.dumps(jsonFinal)
    headers = {
    #'Authorization': 'Basic QVotQVBJS0VZOkM4NTE5QTJCLTJGNjYtNDI4Mi1CRTQzLUQwMkNBNTE2NzE3MQ==', #Dev
    'Authorization': 'Basic QVotQVBJS0VZOjZCRjRDNDg5LTFCREEtNDc3QS05MTA4LTNGRUY0NUZCRTU4OQ==', #Prod
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

    return response.text, jsonFinal
