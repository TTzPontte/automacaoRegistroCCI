### Bibliotecas ###

import requests
import json
from lerCalculoFluxo import lerCF
### Função para preencher os campos da API ###

def preencherAPI(pathCF, textoContrato, textoLaudo, textoParticipantes, produto):

    # Url da API
    url = "https://dev.aztronic.com.br/AZ/APICollect/api/contrato/set"



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
    valorL = Laudo['valorImovel']

    # Contrato
    Contrato = textoContrato
    matriculaC = Contrato['Matrícula']
    dataContatoC = Contrato['dataContrato']
    codigoIntegracaoC = ''.join([d for d in Contrato['CCI'] if d.isdigit()])
    contadorC = int(Contrato['Quantidade'])
    indiceC = Contrato['indice']
    tabelaC = 1 if Contrato['tabela'] == "SAC" else 2
    taxaC = round(float(Contrato['taxaAoAno']),4)
    if produto == "HE":
        produtoC = "15"
    elif produto == "FI":
        produtoC = "16"

    #Fluxo
    fluxoJson = lerCF(pathCF, codigoIntegracaoC)

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
            "cartorio": "",
            "valor_avaliacao": valorL,
            "unidade": unidadeL,
            "Bloco": blocoL,
            "matricula": matriculaC,
            "numero_cartorio": 0000,
            "data_habitese": "01/01/2000"
            }



    
# Montar Dicionario dos participantes
    listaDeParaP = {"codigo_integracao": 0,"relacao": 0,"nome": 0,"email": 0,"participacao": 0,"cnpj_cpf": 0,"pf_pj": 0,"sexo": 0,"telefone": 0,"data_nascimento": 0,"rua": 0,"numero": 0,"complemento": 0,
"cidade": 0,"bairro": 0,"UF": 0,"cep": 0
            }
    quant = participantes["Quantidade"]
    dadosParticipantes={}
    participantesJson = []
    for cont in range(0,quant):
        for key in listaDeParaP.keys():
            if key == "relacao":
                dadosParticipantes[key] = participantes[f"relacaoDoP{cont+1}"]
            elif key == "nome":
                dadosParticipantes[key]= participantes[f"nomeDoP{cont+1}"]
            elif key == "email":
                dadosParticipantes[key]= participantes[f"emailP{cont+1}"]
            elif key == "participacao":
                dadosParticipantes[key]= participantes[f"participacaoNaOperacaoP{cont+1}"]
            elif key == "cnpj_cpf":
                dadosParticipantes[key]= participantes[f"cpfP{cont+1}"]
            elif key == "pf_pj":
                dadosParticipantes[key]= participantes[f"tipoOperacaoP{cont+1}"]
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
            "id_projeto": "",
            "id_tipocontrato": produtoC,
            "id_tipovenda": "1",
            "valor_contrato": 272099.1707828351,
            "data_contrato": dataContatoC,
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
            "data_base": "10/31/2022",
            "data_averbacao": "11/01/2022",
            "indice_pre": "7",
            "defasagem": "2",
            "taxa_juros": taxaC,
            "tipo_amortizacao": tabelaC
            },
            "fluxo": fluxoJson,
        }
        }
    
    print(jsonFinal)
    return jsonFinal
    
    
    
    
    
''' ## Json POST ##
    payload = json.dumps({
        "contrato": {
            "codigo_integracao": codigoIntegracaoC,
            "pep": "",
            "id_projeto": "379",
            "id_tipocontrato": produtoC,
            "id_tipovenda": "1",
            "valor_contrato": 272099.1707828351,
            "data_contrato": dataContatoC,
            "valor_venda": "580000.00",
            "taxa_multa": "2",
            "taxa_mora": "1",
            "venda_no_estado": "S",
            "score_automatico": "80",
            "score_manual": "85",
            "seguro_mip": 0.021,
            "seguro_dfi": 0.0037,
            "taxa_administracao": 25,
            "unidade": {
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
            "cartorio": "1º OFÍCIO DE REGISTRO DE IMÓVEIS",
            "valor_avaliacao": "580000.00",
            "unidade": unidadeL,
            "Bloco": blocoL,
            "matricula": matriculaC,
            "numero_cartorio": 4146224,
            "data_habitese": "01/01/2000"
            },
            "participante": [
            {
                "codigo_integracao": "0123456",
                "relacao": "1",
                "nome": "Nome 1",
                "email": "email@email.com",
                "participacao": "100",
                "cnpj_cpf": "42061100856",
                "pf_pj": "F",
                "sexo": "M",
                "telefone": "(11) 981.395.095",
                "data_nascimento": "04/23/2018",
                "rua": "Rua Dom Giocondo Grotti",
                "numero": "637",
                "complemento": "NA",
                "cidade": "São Paulo",
                "bairro": "Centro",
                "UF": "SP",
                "cep": "08311-120"
            }
            ],
            "tabelavenda": {
            "codigo_integracao": "0123456",
            "data_base": "10/31/2022",
            "data_averbacao": "11/01/2022",
            "indice_pre": "7",
            "defasagem": "2",
            "taxa_juros": "14.0286",
            "tipo_amortizacao": "1"
            },
            "fluxo": [
            {
                "codigo_integracao": "0123456",
                "data_vencto": "02/10/2023",
                "id_tipo_parcela": "2",
                "numero_parcela": "1/242",
                "valor_principal": 1173.29,
                "valor_futuro": 4244.95,
                "Aplica_Correcao": "S",
                "Aplica_Juros": "S",
                "periodicidade": "1"
            }
            ]
        }
        })'''