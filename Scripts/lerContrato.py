# importa as bibliotecas necessárias
from multiprocessing.sharedctypes import Value
import PyPDF2
import re
import pandas as pd
import string

def lerContrato(path):
    if "FI_" in path:
        #Faz a leitura usando a biblioteca
        read_pdf = PyPDF2.PdfFileReader(path)

        # pega o numero de páginas
        number_of_pages = read_pdf.getNumPages()

        #Extriar Texto Página 1 a 5
        text=''
        for i in range(0,6):
            #Ler Página PDF
            pageObj = read_pdf.getPage(i)
            #Extrair Texto
            text=text+pageObj.extractText()

        #Tratar Texto (Remover Quebra de Linhas)
        text = re.sub('\r', '', text) 
        text = re.sub('\n', '', text)
        text = re.sub(' {2,}', ' ', text).strip(' ')
        text = re.sub(' :', ':', text)
        listaDePara = {'valorTotal':'1. Valor do Financiamento: R$','tabela': 'Sistema de Amortização:','Taxa ao Mes':'2.1.1. Juros de','registro':'4.3. Despesas','valorLiquido': '7. Valor Líquido a Liberar do Financiamento: R$',
                'prazoMes': 'PRAZO DE AMORTIZAÇÃO:','valorPrimeiraParcelaComEncargos':'VALOR TOTAL DO PRIMEIRO ENCARGO, NESTA DATA: R$',
                'valorImóvel':'Imóvel para fins de leilão: R$','prazoContrato': 'N.º DE PRESTAÇÕES:','ultimaParcela':'DATA DE VENCIMENTO DA ÚLTIMA PRESTAÇÃO:','dataContrato': 'Data de Liberação dos Recursos: ',
                'valorPrimeiraParcela':'), NESTA DATA: R$','primeiraParcela':'DATA DE VENCIMENTO DA PRIMEIRA PRESTAÇÃO: ','indice':'ÍNDICE: MENSAL do'
                }

        listaKey = []
        listaValues = []

        for key, value in listaDePara.items():
            if key == 'registro':

                #Definir Variáveis Auxiliares
                topico4 = '4. Despesas'
                topico5 = '5. Valor Destinado'

                #Pegar posição das variáveis auxiliares no texto
                inicioTopico = text.find(topico4, 0)
                finalTopico = text.find(topico5, 0)

                #Criar Paragráfo Auxiliar (Somente com os sub itens do tópico 4. Despesas)
                paragrafo4 = text[inicioTopico+len(topico4)+1:finalTopico-1]
                paragrafo4 = re.sub('\s+',' ', paragrafo4)

                listaChave = ['4.3.','4.4.', '4.5.']
                inicioItens = []

                for item in listaChave:
                    inicioP = paragrafo4.find(item,0)
                    inicioItens.append(inicioP)
                    
                item1 = paragrafo4[inicioItens[0]:inicioItens[1]-1]
                try:
                    item2 = paragrafo4[inicioItens[1]:inicioItens[2]-1]
                except:
                    item2 = paragrafo4[inicioItens[2]:len(paragrafo4)]
                try:
                    item3 = paragrafo4[inicioItens[2]:len(paragrafo4)]
                except:
                    item3 = "N/A"

                listaFinal = [item1, item2, item3,]
                listaValor = []

                for itemAux in listaFinal:
                    if '[X]' in itemAux:
                        inicioAux = itemAux.find('R$ ', 0)
                        fimAux = itemAux.find(",", inicioAux) + 3
                        resultadoAux = itemAux[inicioAux+3:fimAux]
                        if '.' in resultadoAux:
                            resultadoAux = resultadoAux.replace(".", "")
                            resultadoAux = resultadoAux.replace(",", ".")
                    else:
                        resultadoAux = '0.00'

                    listaValor.append(resultadoAux)

                #Criar Dicionario das duas Listas
                dict_chaveValor = dict(zip(listaChave,listaValor))
                 
                
                # Somar valores de registro
                sumRegistro = 0
                for key, value in dict_chaveValor.items():

                    sumRegistro = sumRegistro + float(value)
                valorExtraido = sumRegistro
                key = 'registro'

            else:
                inicioFrase = text.find(value,0)
                finalFrase = inicioFrase + len(value) + 1
                proximoEspaco = text.find(" ", finalFrase)
                valorExtraido = text[finalFrase:proximoEspaco]

                #Ajustar Valores Númericos
                if '.' in valorExtraido:
                    valorExtraido = valorExtraido.replace(".", "")
                    valorExtraido = valorExtraido.replace(",", ".")
                
                #Ajustar Valores Percentuais
                if '%' in valorExtraido:
                    valorExtraido = valorExtraido.replace(",", ".")
                    valorExtraido = valorExtraido.replace("%", "")
                    valorExtraido = round(float(valorExtraido)/100,4)
                elif 'IPCA' or 'IGPM' in valorExtraido:
                    valorExtraido = valorExtraido.replace(",", "")

            listaKey.append(key)
            listaValues.append(valorExtraido)

        # Extraindo numero da matricula
        inicioFrase = text.find('Matriculado sob nº ',0)
        finalFrase = inicioFrase + len('Matriculado sob nº') + 1
        ultimaMatricula = text.find("no", finalFrase)
        valorExtraido = text[finalFrase:ultimaMatricula]
        valorExtraido = valorExtraido.replace(",", "")
        valorExtraido = valorExtraido.replace(" ", "")
        if 3> len(valorExtraido) or len(valorExtraido) > 9:
            valorExtraido = 0
            inicioFrase = text.find('Matriculados sob nºs',0)
            finalFrase = inicioFrase + len('Matriculados sob nºs') + 1
            ultimaMatricula = text.find("no", finalFrase)
            valorExtraido = text[finalFrase:ultimaMatricula]
            valorExtraido = valorExtraido.replace(",", "")
            valorExtraido = valorExtraido.replace("e ", "")

        listaKey.append('Matrícula')
        listaValues.append(valorExtraido)
        

        # Extraindo cartório
        inicioFrase = text.find(f'{valorExtraido[-4:].strip()}, no',0)
        finalFrase = inicioFrase + len(f'{valorExtraido[-4:].strip()}, no') + 1
        ultimaMatricula = text.find("Forma de aquisição", finalFrase)
        valorExtraido = text[finalFrase:ultimaMatricula-1]

        listaKey.append('Cartório')
        listaValues.append(valorExtraido)
        
        # Extraindo CCI
        inicioFrase = text.find('NÚMERO: ',0)
        finalFrase = inicioFrase + len('NÚMERO: ') + 1
        ultimaMatricula = text.find(" ", finalFrase)
        valorExtraido = text[finalFrase:ultimaMatricula]
        listaKey.append('CCI')
        listaValues.append(valorExtraido)

        # Extraindo titular
        campo3 = 'CAMPO 3 -'        # intervalo de extração 
        campo4 = 'CARACTERÍSTICAS DO FINANCIAMENTO'
        operacao = 'PF'
        # Pegar posição das variáveis auxiliares no texto
        inicioTopico = text.find(campo3, 0)
        finalTopico = text.find(campo4, 0)

        # Criar Paragráfo Auxiliar (Somente com os sub itens do tópico 4. Despesas)
        campoTitular= text[inicioTopico+len(campo3)+1:finalTopico-1]
        campoTitular = re.sub('\s+',' ', campoTitular)
        if 'RAZÃO SOCIAL' in campoTitular:
            operacao = 'PJ'
            inicioFrase = campoTitular.find('RAZÃO SOCIAL: ',0)
            finalFrase = inicioFrase + len('RAZÃO SOCIAL: ')
            fimTitular = campoTitular.find("ENDEREÇO", finalFrase)
            valorExtraido = campoTitular[finalFrase:fimTitular]
            listaKey.append('Titular')
            listaValues.append(valorExtraido)
        elif 'FIDUCIANTE NOME:':
            operacao = 'PF'
            inicioFrase = campoTitular.find('ANUENTE(S) NOME: ',0)
            finalFrase = inicioFrase + len('ANUENTE(S) NOME: ')
            fimTitular = campoTitular.find("CPF", finalFrase)
            valorExtraido = campoTitular[finalFrase:fimTitular]
            listaKey.append('Titular')
            listaValues.append(valorExtraido)

        # Extraindo participantes da operação 
        campo5 = 'fins de indenização do Seguro'                         #inicio e fim da extração
        campo6 = 'VI – CLÁUSULA(S)'

        #Pegar posição das variáveis auxiliares no texto
        inicioTopico = text.find(campo5, 0)
        finalTopico = text.find(campo6, 0)

        #Criar Paragráfo Auxiliar
        paragrafoAux = text[inicioTopico+len(campo5)+1:finalTopico-1]
        paragrafoAux = re.sub('\s+',' ', paragrafoAux)
        totalParticipantes = paragrafoAux.count('Nome: ')

        participantesKey = []
        participantesValues = []

        # Extraindo participantes
        fimValor = 0

        for num in range(0, totalParticipantes):
            paragrafoAux = paragrafoAux[fimValor:]
            inicioFrase = paragrafoAux.find('Nome: ',0)
            finalFrase = inicioFrase + len('Nome: ') 
            ultimoNome = paragrafoAux.find("Participação: ", finalFrase)
            nomeExtraido = paragrafoAux[finalFrase:ultimoNome]
            participantesKey.append(f'Participante{num+1}')
            participantesKey.append(f'Participação{num+1}')
            participantesValues.append(nomeExtraido.strip())
            inicioFrase = paragrafoAux.find('Participação:',0)
            finalFrase = inicioFrase + len('Participação:') 
            fimValor = paragrafoAux.find("%", finalFrase)
            participacaoExtraido = paragrafoAux[finalFrase:fimValor+1]
            participantesValues.append(participacaoExtraido.strip())
            dict_participantes = dict(zip(participantesKey,participantesValues))

        #Criar Dicionario das duas Listas
        dict_keyValue = dict(zip(listaKey,listaValues))
        dict_keyValue.update(dict_participantes)
        # Extraindo data do contrato

        text=''
        #Ler Página PDF
        pageObj = read_pdf.getPage(number_of_pages-2)
        text=text+pageObj.extractText()
        pageObj = read_pdf.getPage(number_of_pages-1)
        text=text+pageObj.extractText()
        #Tratar Texto (Remover Quebra de Linhas e espaços duplos)
        text = re.sub('\r', '', text) 
        text = re.sub('\n', '', text)
        text = re.sub(' {2,}', ' ', text).strip(' ')
        inicioFrase = text.find('SÃO PAULO, ',0)
        finalFrase = inicioFrase + len('SÃO PAULO, ')
        ultimaMatricula = text.find(".", finalFrase)
        valorExtraido = text[finalFrase:ultimaMatricula]
        valorExtraido = valorExtraido.replace(' DE ','/').strip()
        if 'JANEIRO' in valorExtraido:
            dict_keyValue['dataContrato'] = valorExtraido.replace('JANEIRO','01')
        elif 'FEVEREIRO' in valorExtraido:
            dict_keyValue['dataContrato'] = valorExtraido.replace('FEVEREIRO','02')
        elif 'MARÇO' in valorExtraido:
            dict_keyValue['dataContrato'] = valorExtraido.replace('MARÇO','03')
        elif 'ABRIL' in valorExtraido:
            dict_keyValue['dataContrato'] = valorExtraido.replace('ABRIL','04')
        elif 'MAIO' in valorExtraido:
            dict_keyValue['dataContrato'] = valorExtraido.replace('MAIO','05')
        elif 'JUNHO' in valorExtraido:
            dict_keyValue['dataContrato'] = valorExtraido.replace('JUNHO','06')
        elif 'JULHO' in valorExtraido:
            dict_keyValue['dataContrato'] = valorExtraido.replace('JULHO','07')
        elif 'AGOSTO' in valorExtraido:
            dict_keyValue['dataContrato'] = valorExtraido.replace('AGOSTO','08')
        elif 'SETEMBRO' in valorExtraido:
            dict_keyValue['dataContrato'] = valorExtraido.replace('SETEMBRO','09')
        elif 'OUTUBRO' in valorExtraido:
            dict_keyValue['dataContrato'] = valorExtraido.replace('OUTUBRO','10')
        elif 'NOVEMBRO' in valorExtraido:
            dict_keyValue['dataContrato'] = valorExtraido.replace('NOVEMBRO','11')
        elif 'DEZEMBRO' in valorExtraido:
            dict_keyValue['dataContrato'] = valorExtraido.replace('DEZEMBRO','12')
            
    elif "HE_" in path:
        #Faz a leitura usando a biblioteca
        read_pdf = PyPDF2.PdfFileReader(path)

        # pega o numero de páginas
        number_of_pages = read_pdf.getNumPages()

        #Extriar Texto Página 1 a 5
        text=''
        for i in range(0,9):
            #Ler Página PDF
            pageObj = read_pdf.getPage(i)
            #Extrair Texto
            text=text+pageObj.extractText()

        #Tratar Texto (Remover Quebra de Linhas)
        text = re.sub('\r', '', text) 
        text = re.sub('\n', '', text)
        text = re.sub(' {2,}', ' ', text).strip(' ')
        text = re.sub(' :', ':', text)
        
        listaDePara = {'valorTotal':'VALOR DO EMPRÉSTIMO: R$','tabela': 'SISTEMA DE AMORTIZAÇÃO:','registro': 'DESPESAS DE REGISTRO: R$','Taxa ao Mes':'H.1. NOMINAL:','valorLiquido': '-J-K-L-M-N): R$',
                'prazoMes': 'PRAZO DE AMORTIZAÇÃO:','valorPrimeiraParcelaComEncargos':'VALOR TOTAL DO PRIMEIRO ENCARGO, NESTA DATA: R$',
                'valorImóvel':'Valor de avaliação do Imóvel para fins de leilão: R$','prazoContrato': 'N.º DE PRESTAÇÕES:','ultimaParcela':'DATA DO TÉRMINO DO PRAZO CONTRATUAL:','dataContrato': 'DATA DE DESEMBOLSO:',
                'valorPrimeiraParcela':'VALOR DA PARCELA MENSAL (AMORTIZAÇÃO E JUROS), NESTA DATA: R$','primeiraParcela':'VENCIMENTO DA PRIMEIRA PRESTAÇÃO:','indice':'ÍNDICE: MENSAL do'
                }

        #len(listaHE) # <--- Qtd de Itens na Lista
        listaKey = []
        listaValues = []

        for key, value in listaDePara.items():
            inicioFrase = text.find(value,0)
            finalFrase = inicioFrase + len(value) + 1
            proximoEspaco = text.find(" ", finalFrase)
            valorExtraido = text[finalFrase:proximoEspaco]

            #Ajustar Valores Númericos
            if '.' in valorExtraido:
                valorExtraido = valorExtraido.replace(".", "")
                valorExtraido = valorExtraido.replace(",", ".")
            
            #Ajustar Valores Percentuais
            if '%' in valorExtraido:
                valorExtraido = valorExtraido.replace(",", ".")
                valorExtraido = valorExtraido.replace("%", "")
                valorExtraido = round(float(valorExtraido)/100,4)
            elif 'IPCA' or 'IGPM' in valorExtraido:
                valorExtraido = valorExtraido.replace(",", "")
            
            listaKey.append(key)
            listaValues.append(valorExtraido)

        # Extraindo numero da matricula
        inicioFrase = text.find('matrícula nº',0)
        finalFrase = inicioFrase + len('matrícula nº') + 1
        ultimaMatricula = text.find("do", finalFrase)
        valorExtraido = text[finalFrase:ultimaMatricula]
        valorExtraido = valorExtraido.replace(",", "")
        if 3> len(valorExtraido) or len(valorExtraido) > 9:
            valorExtraido = 0
            inicioFrase = text.find('nas matrículas nºs',0)
            finalFrase = inicioFrase + len('nas matrículas nºs') + 1
            ultimaMatricula = text.find("do", finalFrase)
            valorExtraido = text[finalFrase:ultimaMatricula]
            valorExtraido = valorExtraido.replace(",", "")
            valorExtraido = valorExtraido.replace("e ", "")

        listaKey.append('Matrícula')
        listaValues.append(valorExtraido.strip())

        # Extraindo cartório
        inicioFrase = text.find(' do Livro N°',0)
        finalFrase = inicioFrase + len(' do Livro N°') + 1
        ultimaMatricula = text.find(".", finalFrase)
        valorExtraido = text[finalFrase:ultimaMatricula]

        listaKey.append('Cartório')
        listaValues.append(valorExtraido)

        # Extraindo CCI
        inicioFrase = text.find('NÚMERO:',0)
        finalFrase = inicioFrase + len('NÚMERO:') + 1
        ultimaMatricula = text.find(" ", finalFrase)
        valorExtraido = text[finalFrase:ultimaMatricula]
        valorExtraido
        listaKey.append('CCI')
        listaValues.append(valorExtraido)

        # Extraindo participantes da operação 

        campo7 = 'CAMPO 7'                         #Definir Variáveis Auxiliares
        campo8 = 'CAMPO 8 – CLÁUSULA(S)'

        #Pegar posição das variáveis auxiliares no texto
        inicioTopico = text.find(campo7, 0)
        finalTopico = text.find(campo8, 0)

        #Criar Paragráfo Auxiliar
        paragrafoAux = text[inicioTopico+len(campo7)+1:finalTopico-1]
        paragrafoAux = re.sub('\s+',' ', paragrafoAux)
        

        participantesKey = []
        participantesValues = []
        totalParticipantes = paragrafoAux.count('NOME: ')
        # Extraindo participantes
        fimValor = 0

        for num in range(0, totalParticipantes):
            paragrafoAux = paragrafoAux[fimValor:]
            inicioFrase = paragrafoAux.find('NOME: ',0)
            finalFrase = inicioFrase + len('NOME: ') 
            ultimoNome = paragrafoAux.find("PARTICIPAÇÃO: ", finalFrase)
            nomeExtraido = paragrafoAux[finalFrase:ultimoNome]
            participantesKey.append(f'Participante{num+1}')
            participantesKey.append(f'Participação{num+1}')
            participantesValues.append(nomeExtraido.strip())
            inicioFrase = paragrafoAux.find('PARTICIPAÇÃO:',0)
            finalFrase = inicioFrase + len('PARTICIPAÇÃO:') 
            fimValor = paragrafoAux.find("%", finalFrase)
            participacaoExtraido = paragrafoAux[finalFrase:fimValor+1]
            participantesValues.append(participacaoExtraido.strip())
        dict_participantes = dict(zip(participantesKey,participantesValues))

        # Extraindo titular
        campo2 = 'CAMPO 2 -'        # intervalo de extração 
        campo3 = 'CAMPO 3 -'
        operacao = 'PF'
        # Pegar posição das variáveis auxiliares no texto
        inicioTopico = text.find(campo2, 0)
        finalTopico = text.find(campo3, 0)

        # Criar Paragráfo Auxiliar (Somente com os sub itens do tópico 4. Despesas)
        campoTitular= text[inicioTopico+len(campo2)+1:finalTopico-1]
        campoTitular = re.sub('\s+',' ', campoTitular)
        if 'RAZÃO SOCIAL' in campoTitular:
            operacao = 'PJ'
            inicioFrase = campoTitular.find('RAZÃO SOCIAL: ',0)
            finalFrase = inicioFrase + len('RAZÃO SOCIAL: ')
            fimTitular = campoTitular.find("ENDEREÇO", finalFrase)
            valorExtraido = campoTitular[finalFrase:fimTitular]
            listaKey.append('Titular')
            listaValues.append(valorExtraido)
        elif 'FIDUCIANTE NOME:':
            operacao = 'PF'
            inicioFrase = campoTitular.find('FIDUCIANTE NOME: ',0)
            finalFrase = inicioFrase + len('FIDUCIANTE NOME: ')
            fimTitular = campoTitular.find("CPF", finalFrase)
            valorExtraido = campoTitular[finalFrase:fimTitular]
            listaKey.append('Titular')
            listaValues.append(valorExtraido)

        #Criar Dicionario das duas Listas
        dict_keyValue = dict(zip(listaKey,listaValues))
        dict_keyValue.update(dict_participantes)

        # Extraindo data do contrato

        text=''
        #Ler Página PDF
        pageObj = read_pdf.getPage(number_of_pages-2)
        text=text+pageObj.extractText()
        #Tratar Texto (Remover Quebra de Linhas e espaços duplos)
        text = re.sub('\r', '', text) 
        text = re.sub('\n', '', text)
        text = re.sub(' {2,}', ' ', text).strip(' ')

        inicioFrase = text.find('SÃO PAULO, ',0)
        finalFrase = inicioFrase + len('SÃO PAULO, ')
        ultimaMatricula = text.find(".", finalFrase)
        valorExtraido = text[finalFrase:ultimaMatricula]
        valorExtraido = valorExtraido.replace(' DE ','/').strip()
        if 'JANEIRO' in valorExtraido:
            dict_keyValue['dataContrato'] = valorExtraido.replace('JANEIRO','01')
        elif 'FEVEREIRO' in valorExtraido:
            dict_keyValue['dataContrato'] = valorExtraido.replace('FEVEREIRO','02')
        elif 'MARÇO' in valorExtraido:
            dict_keyValue['dataContrato'] = valorExtraido.replace('MARÇO','03')
        elif 'ABRIL' in valorExtraido:
            dict_keyValue['dataContrato'] = valorExtraido.replace('ABRIL','04')
        elif 'MAIO' in valorExtraido:
            dict_keyValue['dataContrato'] = valorExtraido.replace('MAIO','05')
        elif 'JUNHO' in valorExtraido:
            dict_keyValue['dataContrato'] = valorExtraido.replace('JUNHO','06')
        elif 'JULHO' in valorExtraido:
            dict_keyValue['dataContrato'] = valorExtraido.replace('JULHO','07')
        elif 'AGOSTO' in valorExtraido:
            dict_keyValue['dataContrato'] = valorExtraido.replace('AGOSTO','08')
        elif 'SETEMBRO' in valorExtraido:
            dict_keyValue['dataContrato'] = valorExtraido.replace('SETEMBRO','09')
        elif 'OUTUBRO' in valorExtraido:
            dict_keyValue['dataContrato'] = valorExtraido.replace('OUTUBRO','10')
        elif 'NOVEMBRO' in valorExtraido:
            dict_keyValue['dataContrato'] = valorExtraido.replace('NOVEMBRO','11')
        elif 'DEZEMBRO' in valorExtraido:
            dict_keyValue['dataContrato'] = valorExtraido.replace('DEZEMBRO','12')
    return dict_keyValue    


def dadosParticipantes(path, contrato):
    #Faz a leitura usando a biblioteca
    pdf_file = open(path, 'rb')
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    #Extriar Texto Página 1 a 5
    text=''
    listaKey = []
    listaValues = []
    if "HE_" in path:
        for i in range(0,9):
            #Ler Página PDF
            pageObj = read_pdf.getPage(i)
            #Extrair Texto
            text=text+pageObj.extractText()

        #Tratar Texto (Remover Quebra de Linhas e espaços duplos)
        text = re.sub('\r', '', text) 
        text = re.sub('\n', '', text)
        text = re.sub(' {2,}', ' ', text).strip(' ')

        # Extraindo participantes da operação 
        campo7 = 'CAMPO 7'                         #inicio e fim da extração
        campo8 = 'CAMPO 8 – CLÁUSULA(S)'

        #Pegar posição das variáveis auxiliares no texto
        inicioTopico = text.find(campo7, 0)
        finalTopico = text.find(campo8, 0)

        #Criar Paragráfo Auxiliar
        paragrafoAux = text[inicioTopico+len(campo7)+1:finalTopico-1]
        paragrafoAux = re.sub('\s+',' ', paragrafoAux)
        totalParticipantes = paragrafoAux.count('NOME: ')
        listaKey.append('Quantidade')
        listaValues.append(totalParticipantes)

        # Extrair dados dos participantes
        listaDePara = {'cpf':'CPF:','data de nascimento':'DATA DE NASCIMENTO:','endereço':'ENDEREÇO RESIDENCIAL E DOMICILIAR:','complemento':'COMPLEMENTO:','bairro':'BAIRRO:','cidade':'CIDADE:','uf':'UF:','cep':'CEP:',
                'telefone':'TELEFONE(S)','email':'EMAIL:'}
        for qtdParticipantes in range(0, totalParticipantes):
            # Extraindo participantes da operação 
            começo = contrato[f'Participante{qtdParticipantes+1}']                        #inicio e fim da extração
            fim = 'CAMPO 3 -'
            #Pegar posição das variáveis auxiliares no texto
            inicioTopico = text.find(começo, 0)
            finalTopico = text.find(fim, 0)

            #Criar Paragráfo Auxiliar
            paragrafoAux = text[inicioTopico+len(começo)+1:finalTopico-1]
            paragrafoAux = re.sub('\s+',' ', paragrafoAux)
            for key, value in listaDePara.items():
                if key == 'endereço':
                    inicioFrase = paragrafoAux.find(value,0)
                    finalFrase = inicioFrase + len(value) + 1
                    proximoEspaco = paragrafoAux.find("COMPLEMENTO:", finalFrase)
                    valorExtraido = paragrafoAux[finalFrase:proximoEspaco]
                elif key == 'complemento':
                    inicioFrase = paragrafoAux.find(value,0)
                    finalFrase = inicioFrase + len(value) + 1
                    proximoEspaco = paragrafoAux.find("BAIRRO:", finalFrase)
                    valorExtraido = paragrafoAux[finalFrase:proximoEspaco]
                elif key == 'bairro':
                    inicioFrase = paragrafoAux.find(value,0)
                    finalFrase = inicioFrase + len(value) + 1
                    proximoEspaco = paragrafoAux.find("CIDADE:", finalFrase)
                    valorExtraido = paragrafoAux[finalFrase:proximoEspaco]
                elif key == 'cidade':
                    inicioFrase = paragrafoAux.find(value,0)
                    finalFrase = inicioFrase + len(value) + 1
                    proximoEspaco = paragrafoAux.find("UF:", finalFrase)
                    valorExtraido = paragrafoAux[finalFrase:proximoEspaco]
                elif key == 'telefone':
                    inicioFrase = paragrafoAux.find(value,0)
                    finalFrase = inicioFrase + len(value) + 1
                    proximoEspaco = paragrafoAux.find("EMAIL:", finalFrase)
                    valorExtraido = paragrafoAux[finalFrase:proximoEspaco].strip()
                else:
                    inicioFrase = paragrafoAux.find(value,0)
                    finalFrase = inicioFrase + len(value) + 1
                    proximoEspaco = paragrafoAux.find(" ", finalFrase)
                    valorExtraido = paragrafoAux[finalFrase:proximoEspaco]

                listaKey.append(f'{key}{qtdParticipantes+1}')
                listaValues.append(valorExtraido.strip())

    
    elif "FI_" in path:
        for i in range(0,6):
            #Ler Página PDF
            pageObj = read_pdf.getPage(i)
            #Extrair Texto
            text=text+pageObj.extractText()

        #Tratar Texto (Remover Quebra de Linhas)
        text = re.sub('\r', '', text) 
        text = re.sub('\n', '', text)
        text = re.sub(' {2,}', ' ', text).strip(' ')

        # Extraindo participantes da operação 
        campo5 = 'fins de indenização do Seguro'                         #inicio e fim da extração
        campo6 = 'VI – CLÁUSULA(S)'

        #Pegar posição das variáveis auxiliares no texto
        inicioTopico = text.find(campo5, 0)
        finalTopico = text.find(campo6, 0)

        #Criar Paragráfo Auxiliar
        paragrafoAux = text[inicioTopico+len(campo5)+1:finalTopico-1]
        paragrafoAux = re.sub('\s+',' ', paragrafoAux)
        totalParticipantes = paragrafoAux.count('Nome: ')
        listaKey.append('Quantidade')
        listaValues.append(totalParticipantes)
        # Extrair dados dos participantes
        listaDePara = {'cpf':'CPF:','data de nascimento':'DATA DE NASCIMENTO:','endereço':'ENDEREÇO RESIDENCIAL E DOMICILIAR:','complemento':'COMPLEMENTO:','bairro':'BAIRRO:','cidade':'CIDADE:','uf':'UF:','cep':'CEP:',
                'telefone':'TELEFONE(S)','email':'EMAIL:'}
        for qtdParticipantes in range(0, totalParticipantes):
            # Extraindo participantes da operação 
            começo = contrato[f'Participante{qtdParticipantes+1}']                        #inicio e fim da extração
            fim = 'CARACTERÍSTICAS DO FINANCIAMENTO'
            #Pegar posição das variáveis auxiliares no texto
            inicioTopico = text.find(começo, 0)
            finalTopico = text.find(fim, 0)

            #Criar Paragráfo Auxiliar
            paragrafoAux = text[inicioTopico+len(começo)+1:finalTopico-1]
            paragrafoAux = re.sub('\s+',' ', paragrafoAux)
            paragrafoAux
            for key, value in listaDePara.items():
                if key == 'endereço':
                    inicioFrase = paragrafoAux.find(value,0)
                    finalFrase = inicioFrase + len(value) + 1
                    proximoEspaco = paragrafoAux.find("COMPLEMENTO:", finalFrase)
                    valorExtraido = paragrafoAux[finalFrase:proximoEspaco]
                elif key == 'complemento':
                    inicioFrase = paragrafoAux.find(value,0)
                    finalFrase = inicioFrase + len(value) + 1
                    proximoEspaco = paragrafoAux.find("BAIRRO:", finalFrase)
                    valorExtraido = paragrafoAux[finalFrase:proximoEspaco]
                elif key == 'bairro':
                    inicioFrase = paragrafoAux.find(value,0)
                    finalFrase = inicioFrase + len(value) + 1
                    proximoEspaco = paragrafoAux.find("CIDADE:", finalFrase)
                    valorExtraido = paragrafoAux[finalFrase:proximoEspaco]
                elif key == 'cidade':
                    inicioFrase = paragrafoAux.find(value,0)
                    finalFrase = inicioFrase + len(value) + 1
                    proximoEspaco = paragrafoAux.find("UF:", finalFrase)
                    valorExtraido = paragrafoAux[finalFrase:proximoEspaco]
                elif key == 'telefone':
                    inicioFrase = paragrafoAux.find(value,0)
                    finalFrase = inicioFrase + len(value) + 1
                    proximoEspaco = paragrafoAux.find("EMAIL:", finalFrase)
                    valorExtraido = paragrafoAux[finalFrase:proximoEspaco].strip()
                else:
                    inicioFrase = paragrafoAux.find(value,0)
                    finalFrase = inicioFrase + len(value) + 1
                    proximoEspaco = paragrafoAux.find(" ", finalFrase)
                    valorExtraido = paragrafoAux[finalFrase:proximoEspaco]

                listaKey.append(f'{key}{qtdParticipantes+1}')
                listaValues.append(valorExtraido.strip())
    #Criar Dicionario das duas Listas
    dict_keyValue = dict(zip(listaKey,listaValues))
    return dict_keyValue


### Area de teste ###

# patha = r'C:\Users\MatheusPereira\OneDrive - Pontte\Área de Trabalho\automacaoRegistroCCI\Contratos\FI_Contrato_Cristiano_Assinatura Digital-Manifesto.pdf'

# test = lerContrato(patha)

# # for key, valu in test.items():
# #     print(f'{key} : {valu}')

# testnum = dadosParticipantes(patha,test)
# print(testnum)

