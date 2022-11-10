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
        listaKey = []
        listaValues = []
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
        text = re.sub(' /', '/', text)
        text = re.sub('/ ', '/', text)
        listaDePara = {'valorTotal':'1. Valor do Financiamento: R$','tabela': 'Sistema de Amortização:'}
        for key, value in listaDePara.items():
            inicioFrase = text.find(value,0)
            finalFrase = inicioFrase + len(value) + 1
            proximoEspaco = text.find(" ", finalFrase)
            valorExtraido = text[finalFrase:proximoEspaco]

            #Ajustar Valores Númericos
            if '.' in valorExtraido:
                valorExtraido = valorExtraido.replace(".", "")
                valorExtraido = valorExtraido.replace(",", ".")
            
            elif 'IPCA' or 'IGPM' in valorExtraido:
                valorExtraido = valorExtraido.replace(",", "")

            listaKey.append(key)
            listaValues.append(valorExtraido.strip())
        valorExtraido = valorExtraido.upper()
        if 'Data de Liberação dos Recursos:' in text:
            dataLib = 'Data de Liberação dos Recursos:'
        elif 'Data de Desembolso:' in text:
            dataLib = 'Data de Desembolso:'
        
        listaDePara = {'Taxa ao Mes':'mês, equivalente a de','registro':'4.3. Despesas','valorLiquido': '7. Valor Líquido a Liberar do Financiamento: R$',
                'prazoMes': 'PRAZO DE AMORTIZAÇÃO:','valorPrimeiraParcelaComEncargos':'VALOR TOTAL DO PRIMEIRO ENCARGO, NESTA DATA: R$',
                'valorImóvel':'Imóvel para fins de leilão: R$','prazoContrato': 'N.º DE PRESTAÇÕES:','ultimaParcela':'DATA DE VENCIMENTO DA ÚLTIMA PRESTAÇÃO:','dataLiberação': dataLib,
                'valorPrimeiraParcela':'), NESTA DATA: R$','primeiraParcela':'DATA DE VENCIMENTO DA PRIMEIRA PRESTAÇÃO:','indice':'ÍNDICE: MENSAL do'
                }

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
                        if ',' in resultadoAux:
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
                    valorExtraido = round(float(valorExtraido)/100,6)
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
        totalParticipantes = campoTitular.count('NOME')
        totalParticipantes = totalParticipantes + campoTitular.count('RAZÃO SOCIAL: ')
        listaKey.append('Quantidade')
        listaValues.append(totalParticipantes)

        if 'RAZÃO SOCIAL' in campoTitular:
            operacao = 'PJ'
            inicioFrase = campoTitular.find('RAZÃO SOCIAL: ',0)
            finalFrase = inicioFrase + len('RAZÃO SOCIAL: ')
            fimTitular = campoTitular.find("ENDEREÇO", finalFrase)
            valorExtraido = campoTitular[finalFrase:fimTitular]
            listaKey.append('Titular')
            listaValues.append(valorExtraido.strip())

        elif 'FIDUCIANTE NOME:':
            operacao = 'PF'
            inicioFrase = campoTitular.find('ANUENTE(S) NOME: ',0)
            finalFrase = inicioFrase + len('ANUENTE(S) NOME: ')
            fimTitular = campoTitular.find("CPF", finalFrase)
            valorExtraido = campoTitular[finalFrase:fimTitular]
            listaKey.append('Titular')
            listaValues.append(valorExtraido.strip())

        # Extraindo participantes da operacao 
        campo5 = 'fins de indenização do Seguro'                         #inicio e fim da extração
        campo6 = 'VI – CLÁUSULA(S)'

        #Pegar posição das variáveis auxiliares no texto
        inicioTopico = text.find(campo5, 0)
        finalTopico = text.find(campo6, 0)

        #Criar Paragráfo Auxiliar
        paragrafoAux = text[inicioTopico+len(campo5)+1:finalTopico-1]
        paragrafoAux = re.sub('\s+',' ', paragrafoAux)
        totalParticipantes = paragrafoAux.count('Nome')

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

        # Tipo de operacao 
        listaKey.append('operacao')
        listaValues.append(operacao)

        #Criar Dicionario das duas Listas
        dict_keyValue = dict(zip(listaKey,listaValues))
        dict_keyValue.update(dict_participantes)
        # Extraindo data do contrato

        text=''
        valid = False
        cont = 0
        while valid == False:
            text=''
            cont = cont + 1
            pageObj = read_pdf.getPage(number_of_pages - cont)
            text=text+pageObj.extractText()
            #Tratar Texto (Remover Quebra de Linhas e espaços duplos)
            text = re.sub('\r', '', text) 
            text = re.sub('\n', '', text)
            text = re.sub(' {2,}', ' ', text).strip(' ')
            if 'SÃO PAULO,' in text:
                break
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
        read_pdf = PyPDF2.PdfFileReader(path, strict = False)

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
                'valorImóvel':'Valor de avaliação do Imóvel para fins de leilão: R$','prazoContrato': 'N.º DE PRESTAÇÕES:','ultimaParcela':'DATA DO TÉRMINO DO PRAZO CONTRATUAL:','dataLiberação': 'DATA DE DESEMBOLSO:',
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
                valorExtraido = round(float(valorExtraido)/100,6)
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
        listaKey.append('CCI')
        listaValues.append(valorExtraido)

        # Extraindo participantes da operacao 

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
        totalParticipantes = paragrafoAux.count('NOME')
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
        totalParticipantes = campoTitular.count('NOME')
        totalParticipantes = totalParticipantes + campoTitular.count('RAZÃO SOCIAL: ')

        if 'RAZÃO SOCIAL' in campoTitular:
            operacao = 'PJ'
            inicioFrase = campoTitular.find('RAZÃO SOCIAL: ',0)
            finalFrase = inicioFrase + len('RAZÃO SOCIAL: ')
            fimTitular = campoTitular.find("ENDEREÇO", finalFrase)
            valorExtraido = campoTitular[finalFrase:fimTitular]
            listaKey.append('Titular')
            listaValues.append(valorExtraido)

        else:
            operacao = 'PF'
            inicioFrase = campoTitular.find('NOME: ',0)
            finalFrase = inicioFrase + len('NOME: ')
            fimTitular = campoTitular.find("CPF", finalFrase)
            valorExtraido = campoTitular[finalFrase:fimTitular]
            listaKey.append('Titular')
            listaValues.append(valorExtraido)

        # Tipo de operacao e Qtd de participantes
        listaKey.append('operacao')
        listaValues.append(operacao)
        listaKey.append('Quantidade')
        listaValues.append(totalParticipantes)

        # Criar Dicionario das duas Listas
        dict_keyValue = dict(zip(listaKey,listaValues))
        dict_keyValue.update(dict_participantes)

        # Extraindo data do contrato
        text=''
        
        #Ler Página PDF    
        valid = False
        cont = 0
        while valid == False:
            text=''
            cont = cont + 1
            pageObj = read_pdf.getPage(number_of_pages - cont)
            text=text+pageObj.extractText()
            #Tratar Texto (Remover Quebra de Linhas e espaços duplos)
            text = re.sub('\r', '', text) 
            text = re.sub('\n', '', text)
            text = re.sub(' {2,}', ' ', text).strip(' ')
            if 'SÃO PAULO,' in text:
                break


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

        # Extraindo participantes da operacao 
        campo7 = 'CAMPO 7'                         #inicio e fim da extração
        campo8 = 'CAMPO 8 – CLÁUSULA(S)'

        #Pegar posição das variáveis auxiliares no texto
        inicioTopico = text.find(campo7, 0)
        finalTopico = text.find(campo8, 0)

        #Criar Paragráfo Auxiliar
        paragrafoAux = text[inicioTopico+len(campo7)+1:finalTopico-1]
        paragrafoAux = re.sub('\s+',' ', paragrafoAux)
        totalParticipantes = paragrafoAux.count('NOME: ')
        listaKey.append('Quantidade')        # Quantidade de participates com participação maior que 0%
        listaValues.append(totalParticipantes)

        listaDePara = {'nome':'NOME:','cpf':'CPF:','data de nascimento':'DATA DE NASCIMENTO:','endereço':'ENDEREÇO RESIDENCIAL E DOMICILIAR:','complemento':'COMPLEMENTO:','bairro':'BAIRRO:','cidade':'CIDADE:','uf':'UF:','cep':'CEP:',
                'telefone':'TELEFONE(S)','email':'EMAIL:'}

        def removerText(valor):
            começo = 'CONTRATO DE EMPRÉSTIMO'                        #inicio e fim da extração
            fim = 'Física Página'
            #Pegar posição das variáveis auxiliares no texto
            inicioTopico = valor.find(começo, 0)
            finalTopico = valor.find(fim, 0)

            #Criar Paragráfo Auxiliar
            remover = valor[inicioTopico:finalTopico+len(fim)+8]
            remover = re.sub('\s+',' ', remover)
            return remover

        partida = text.find('CAMPO 2 -', 0)

        if  contrato['operacao'] == 'PJ':
            contador = contrato['Quantidade'] -1

        else:
            contador = contrato['Quantidade']

        for qtdParticipantes in range(0, contador):
            
            # Extraindo participantes da operacao 
            começo = 'NOME:'                       #inicio e fim da extração
            fim = 'CAMPO 3 -'
            #Pegar posição das variáveis auxiliares no texto
            inicioTopico = text.find(começo, partida)
            finalTopico = text.find(fim, 0)

            #Criar Paragráfo Auxiliar
            paragrafoAux = text[inicioTopico:finalTopico-1]
            paragrafoAux = re.sub('\s+',' ', paragrafoAux)
            for key, value in listaDePara.items():
                if key == 'endereço':
                    inicioFrase = paragrafoAux.find(value,0)
                    finalFrase = inicioFrase + len(value) + 1
                    proximoEspaco = paragrafoAux.find("COMPLEMENTO:", finalFrase)
                    valorExtraido = paragrafoAux[finalFrase:proximoEspaco]
                    if 'CONTRATO DE EMPRÉSTIMO' in valorExtraido:
                        apagar = removerText(valorExtraido)
                        valorExtraido = valorExtraido.replace(apagar,'')
                
                elif key == 'nome':
                    inicioFrase = paragrafoAux.find(value,0)
                    finalFrase = inicioFrase + len(value) + 1
                    proximoEspaco = paragrafoAux.find("CPF:", finalFrase)
                    valorExtraido = paragrafoAux[finalFrase:proximoEspaco]
                    if 'CONTRATO DE EMPRÉSTIMO' in valorExtraido:
                        apagar = removerText(valorExtraido)
                        valorExtraido = valorExtraido.replace(apagar,'')

                elif key == 'complemento':
                    inicioFrase = paragrafoAux.find(value,0)
                    finalFrase = inicioFrase + len(value) + 1
                    proximoEspaco = paragrafoAux.find("BAIRRO:", finalFrase)
                    valorExtraido = paragrafoAux[finalFrase:proximoEspaco]
                    if 'CONTRATO DE EMPRÉSTIMO' in valorExtraido:
                        apagar = removerText(valorExtraido)
                        valorExtraido = valorExtraido.replace(apagar,'')

                elif key == 'bairro':
                    inicioFrase = paragrafoAux.find(value,0)
                    finalFrase = inicioFrase + len(value) + 1
                    proximoEspaco = paragrafoAux.find("CIDADE:", finalFrase)
                    valorExtraido = paragrafoAux[finalFrase:proximoEspaco]
                    if 'CONTRATO DE EMPRÉSTIMO' in valorExtraido:
                        apagar = removerText(valorExtraido)
                        valorExtraido = valorExtraido.replace(apagar,'')

                elif key == 'cidade':
                    inicioFrase = paragrafoAux.find(value,0)
                    finalFrase = inicioFrase + len(value) + 1
                    proximoEspaco = paragrafoAux.find("UF:", finalFrase)
                    valorExtraido = paragrafoAux[finalFrase:proximoEspaco]
                    if 'CONTRATO DE EMPRÉSTIMO' in valorExtraido:
                        apagar = removerText(valorExtraido)
                        valorExtraido = valorExtraido.replace(apagar,'')
                elif key == 'telefone':
                    inicioFrase = paragrafoAux.find(value,0)
                    finalFrase = inicioFrase + len(value) + 1
                    proximoEspaco = paragrafoAux.find("EMAIL:", finalFrase)
                    valorExtraido = paragrafoAux[finalFrase:proximoEspaco]
                    if 'CONTRATO DE EMPRÉSTIMO' in valorExtraido:
                        apagar = removerText(valorExtraido)
                        valorExtraido = valorExtraido.replace(apagar,'')
                else:
                    paragrafoAux = paragrafoAux + ' '
                    inicioFrase = paragrafoAux.find(value,0)
                    finalFrase = inicioFrase + len(value) + 1
                    proximoEspaco = paragrafoAux.find(" ", finalFrase)
                    valorExtraido = paragrafoAux[finalFrase:proximoEspaco]
                    if 'CONTRATO DE EMPRÉSTIMO' in valorExtraido:
                        apagar = removerText(valorExtraido)
                        valorExtraido = valorExtraido.replace(apagar,'')
                listaKey.append(f'{key}{qtdParticipantes+1}')
                listaValues.append(valorExtraido.strip())
            partida = (inicioTopico - partida) + partida + 5
            listaKey.append(f'participação{qtdParticipantes+1}')
            listaValues.append(0)
            listaKey.append(f'operacao{qtdParticipantes+1}')
            listaValues.append('PF')
    
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

        # Extraindo participantes da operacao 
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
        listaDePara = {'nome':'NOME:','cpf':'CPF:','data de nascimento':'DATA DE NASCIMENTO:','endereço':'ENDEREÇO RESIDENCIAL E DOMICILIAR:','complemento':'COMPLEMENTO:','bairro':'BAIRRO:','cidade':'CIDADE:','uf':'UF:','cep':'CEP:',
                'telefone':'TELEFONE(S)','email':'EMAIL:'}

        def removerText(valor):
            começo = 'Este documento foi assinado digitalmente'                        #inicio e fim da extração
            fim = 'CCI e Outras Avenças nº'
            #Pegar posição das variáveis auxiliares no texto
            inicioTopico = valor.find(começo, 0)
            finalTopico = valor.find(fim, 0)

            #Criar Paragráfo Auxiliar
            remover = valor[inicioTopico:finalTopico+len(fim)+14]
            remover = re.sub('\s+',' ', remover)
            return remover

        partida = text.find('CAMPO 3 -', 0)
        if  contrato['operacao'] == 'PJ':
            contador = contrato['Quantidade'] -1

        else:
            contador = contrato['Quantidade']
        
        for qtdParticipantes in range(0, contador):
            # Extraindo participantes da operacao 
            começo = 'NOME:'                       #inicio e fim da extração
            fim = 'CARACTERÍSTICAS DO FINANCIAMENTO'
            #Pegar posição das variáveis auxiliares no texto
            inicioTopico = text.find(começo, partida)
            finalTopico = text.find(fim, 0)

            #Criar Paragráfo Auxiliar
            paragrafoAux = text[inicioTopico:finalTopico-1]
            paragrafoAux = re.sub('\s+',' ', paragrafoAux)
            for key, value in listaDePara.items():
                if key == 'endereço':
                    inicioFrase = paragrafoAux.find(value,0)
                    finalFrase = inicioFrase + len(value) + 1
                    proximoEspaco = paragrafoAux.find("COMPLEMENTO:", finalFrase)
                    valorExtraido = paragrafoAux[finalFrase:proximoEspaco]
                    if 'Este documento foi assinado digitalmente' in valorExtraido:
                        apagar = removerText(valorExtraido)
                        valorExtraido = valorExtraido.replace(apagar,'')
                
                elif key == 'nome':
                    inicioFrase = paragrafoAux.find(value,0)
                    finalFrase = inicioFrase + len(value) + 1
                    proximoEspaco = paragrafoAux.find("CPF:", finalFrase)
                    valorExtraido = paragrafoAux[finalFrase:proximoEspaco]
                    if 'Este documento foi assinado digitalmente' in valorExtraido:
                        apagar = removerText(valorExtraido)
                        valorExtraido = valorExtraido.replace(apagar,'')

                elif key == 'complemento':
                    inicioFrase = paragrafoAux.find(value,0)
                    finalFrase = inicioFrase + len(value) + 1
                    proximoEspaco = paragrafoAux.find("BAIRRO:", finalFrase)
                    valorExtraido = paragrafoAux[finalFrase:proximoEspaco]
                    if 'Este documento foi assinado digitalmente' in valorExtraido:
                        apagar = removerText(valorExtraido)
                        valorExtraido = valorExtraido.replace(apagar,'')

                elif key == 'bairro':
                    inicioFrase = paragrafoAux.find(value,0)
                    finalFrase = inicioFrase + len(value) + 1
                    proximoEspaco = paragrafoAux.find("CIDADE:", finalFrase)
                    valorExtraido = paragrafoAux[finalFrase:proximoEspaco]
                    if 'Este documento foi assinado digitalmente' in valorExtraido:
                        apagar = removerText(valorExtraido)
                        valorExtraido = valorExtraido.replace(apagar,'')

                elif key == 'cidade':
                    inicioFrase = paragrafoAux.find(value,0)
                    finalFrase = inicioFrase + len(value) + 1
                    proximoEspaco = paragrafoAux.find("UF:", finalFrase)
                    valorExtraido = paragrafoAux[finalFrase:proximoEspaco]
                    if 'Este documento foi assinado digitalmente' in valorExtraido:
                        apagar = removerText(valorExtraido)
                        valorExtraido = valorExtraido.replace(apagar,'')
                elif key == 'telefone':
                    inicioFrase = paragrafoAux.find(value,0)
                    finalFrase = inicioFrase + len(value) + 1
                    proximoEspaco = paragrafoAux.find("EMAIL:", finalFrase)
                    valorExtraido = paragrafoAux[finalFrase:proximoEspaco]
                    if 'Este documento foi assinado digitalmente' in valorExtraido:
                        apagar = removerText(valorExtraido)
                        valorExtraido = valorExtraido.replace(apagar,'')
                else:
                    paragrafoAux = paragrafoAux + ' '
                    inicioFrase = paragrafoAux.find(value,0)
                    finalFrase = inicioFrase + len(value) + 1
                    proximoEspaco = paragrafoAux.find(" ", finalFrase)
                    valorExtraido = paragrafoAux[finalFrase:proximoEspaco]
                    if 'Este documento foi assinado digitalmente' in valorExtraido:
                        apagar = removerText(valorExtraido)
                        valorExtraido = valorExtraido.replace(apagar,'')
                listaKey.append(f'{key}{qtdParticipantes+1}')
                listaValues.append(valorExtraido.strip())
            partida = (inicioTopico - partida) + partida + 5
            listaKey.append(f'participação{qtdParticipantes+1}')
            listaValues.append(0)
            listaKey.append(f'operacao{qtdParticipantes+1}')
            listaValues.append('PF')


    
    # Estrair dados do Titular
    if contrato['operacao'] == 'PJ':
        contador = contrato['Quantidade'] -1

        if "HE_" in path:
            listaDePara = {'nome':'RAZÃO SOCIAL:','endereço':'ENDEREÇO COMERCIAL:','complemento':'COMPLEMENTO:','bairro':'BAIRRO:','cidade':'CIDADE:','uf':'UF:',
            'cep':'CEP:','cpf':'CNPJ:', 'data de nascimento':'DATA DA CONSTITUIÇÃO:'}
            # Extraindo participantes da operacao 
            começo = contrato['Titular'].strip()                    #inicio e fim da extração
            fim = 'CARACTERÍSTICAS DO FINANCIAMENTO'
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
                    if 'CONTRATO DE EMPRÉSTIMO' in valorExtraido:
                        apagar = removerText(valorExtraido)
                        valorExtraido = valorExtraido.replace(apagar,'')

                elif key == 'nome':
                        valorExtraido = começo

                elif key == 'complemento':
                    inicioFrase = paragrafoAux.find(value,0)
                    finalFrase = inicioFrase + len(value) + 1
                    proximoEspaco = paragrafoAux.find("BAIRRO:", finalFrase)
                    valorExtraido = paragrafoAux[finalFrase:proximoEspaco]
                    if 'CONTRATO DE EMPRÉSTIMO' in valorExtraido:
                        apagar = removerText(valorExtraido)
                        valorExtraido = valorExtraido.replace(apagar,'')

                elif key == 'bairro':
                    inicioFrase = paragrafoAux.find(value,0)
                    finalFrase = inicioFrase + len(value) + 1
                    proximoEspaco = paragrafoAux.find("CIDADE:", finalFrase)
                    valorExtraido = paragrafoAux[finalFrase:proximoEspaco]
                    if 'CONTRATO DE EMPRÉSTIMO' in valorExtraido:
                        apagar = removerText(valorExtraido)
                        valorExtraido = valorExtraido.replace(apagar,'')

                elif key == 'cidade':
                    inicioFrase = paragrafoAux.find(value,0)
                    finalFrase = inicioFrase + len(value) + 1
                    proximoEspaco = paragrafoAux.find("UF:", finalFrase)
                    valorExtraido = paragrafoAux[finalFrase:proximoEspaco]
                    if 'CONTRATO DE EMPRÉSTIMO' in valorExtraido:
                        apagar = removerText(valorExtraido)
                        valorExtraido = valorExtraido.replace(apagar,'')
                else:
                    paragrafoAux = paragrafoAux + ' '
                    inicioFrase = paragrafoAux.find(value,0)
                    finalFrase = inicioFrase + len(value) + 1
                    proximoEspaco = paragrafoAux.find(" ", finalFrase)
                    valorExtraido = paragrafoAux[finalFrase:proximoEspaco]
                    if 'CONTRATO DE EMPRÉSTIMO' in valorExtraido:
                        apagar = removerText(valorExtraido)
                        valorExtraido = valorExtraido.replace(apagar,'')
            
                listaKey.append(f"{key}{contador+1}")
                listaValues.append(valorExtraido.strip())
                listaKey.append(f'participação{contador+1}')
                listaValues.append(0)
                listaKey.append(f'telefone{contador+1}')
                listaValues.append('N/A')
                listaKey.append(f'email{contador+1}')
                listaValues.append('N/A')
                listaKey.append(f'operacao{contador+1}')
                listaValues.append('PJ')

        elif 'FI_' in path:
            listaDePara = {'endereço':'ENDEREÇO COMERCIAL:','complemento':'COMPLEMENTO:','bairro':'BAIRRO:','cidade':'CIDADE:','uf':'UF:',
            'cep':'CEP:','cpf':'CNPJ:', 'data de nascimento':'DATA DA CONSTITUIÇÃO:'}
            # Extraindo participantes da operacao 
            começo = contrato['Titular'].strip()                    #inicio e fim da extração
            fim = 'CARACTERÍSTICAS DO FINANCIAMENTO'
            #Pegar posição das variáveis auxiliares no texto
            inicioTopico = text.find(começo, 0)
            finalTopico = text.find(fim, 0)

            #Criar Paragráfo Auxiliar
            paragrafoAux = text[inicioTopico+len(começo)+1:finalTopico-1]
            for key, value in listaDePara.items():
                if key == 'endereço':
                    inicioFrase = paragrafoAux.find(value,0)
                    finalFrase = inicioFrase + len(value) + 1
                    proximoEspaco = paragrafoAux.find("COMPLEMENTO:", finalFrase)
                    valorExtraido = paragrafoAux[finalFrase:proximoEspaco]
                    if 'CONTRATO DE EMPRÉSTIMO' in valorExtraido:
                        apagar = removerText(valorExtraido)
                        valorExtraido = valorExtraido.replace(apagar,'')

                elif key == 'complemento':
                    inicioFrase = paragrafoAux.find(value,0)
                    finalFrase = inicioFrase + len(value) + 1
                    proximoEspaco = paragrafoAux.find("BAIRRO:", finalFrase)
                    valorExtraido = paragrafoAux[finalFrase:proximoEspaco]
                    if 'CONTRATO DE EMPRÉSTIMO' in valorExtraido:
                        apagar = removerText(valorExtraido)
                        valorExtraido = valorExtraido.replace(apagar,'')

                elif key == 'nome':
                        valorExtraido = começo

                elif key == 'bairro':
                    inicioFrase = paragrafoAux.find(value,0)
                    finalFrase = inicioFrase + len(value) + 1
                    proximoEspaco = paragrafoAux.find("CIDADE:", finalFrase)
                    valorExtraido = paragrafoAux[finalFrase:proximoEspaco]
                    if 'CONTRATO DE EMPRÉSTIMO' in valorExtraido:
                        apagar = removerText(valorExtraido)
                        valorExtraido = valorExtraido.replace(apagar,'')

                elif key == 'cidade':
                    inicioFrase = paragrafoAux.find(value,0)
                    finalFrase = inicioFrase + len(value) + 1
                    proximoEspaco = paragrafoAux.find("UF:", finalFrase)
                    valorExtraido = paragrafoAux[finalFrase:proximoEspaco]
                    if 'CONTRATO DE EMPRÉSTIMO' in valorExtraido:
                        apagar = removerText(valorExtraido)
                        valorExtraido = valorExtraido.replace(apagar,'')
                else:
                    paragrafoAux = paragrafoAux + ' '
                    inicioFrase = paragrafoAux.find(value,0)
                    finalFrase = inicioFrase + len(value) + 1
                    proximoEspaco = paragrafoAux.find(" ", finalFrase)
                    valorExtraido = paragrafoAux[finalFrase:proximoEspaco]
                    if 'CONTRATO DE EMPRÉSTIMO' in valorExtraido:
                        apagar = removerText(valorExtraido)
                        valorExtraido = valorExtraido.replace(apagar,'')
                
                listaKey.append(f"{key}{contador+1}")
                listaValues.append(valorExtraido.strip())   
                listaKey.append(f'telefone{contador+1}')
                listaValues.append('N/A')
                listaKey.append(f'email{contador+1}')
                listaValues.append('N/A')
                listaKey.append(f'operacao{contador+1}')
                listaValues.append('PJ')


        #   elif contrato['operacao'] == 'PF':
    #     if "HE_" in path:
    #         listaDePara = {'cpfTitular':'CPF:','data de nascimentoTitular':'DATA DE NASCIMENTO:','endereçoTitular':'ENDEREÇO RESIDENCIAL E DOMICILIAR:','complementoTitular':'COMPLEMENTO:','bairroTitular':'BAIRRO:','cidadeTitular':'CIDADE:','ufTitular':'UF:','cepTitular':'CEP:',
    #                 'telefoneTitular':'TELEFONE(S)','emailTitular':'EMAIL:'}
    #         # Extraindo participantes da operacao 
    #         começo = contrato['Titular'].strip()                    #inicio e fim da extração
    #         fim = 'CARACTERÍSTICAS DO FINANCIAMENTO'
    #         #Pegar posição das variáveis auxiliares no texto
    #         inicioTopico = text.find(começo, 0)
    #         finalTopico = text.find(fim, 0)

    #         #Criar Paragráfo Auxiliar
    #         paragrafoAux = text[inicioTopico+len(começo)+1:finalTopico-1]
    #         paragrafoAux = re.sub('\s+',' ', paragrafoAux)

    #         for key, value in listaDePara.items():
    #             if key == 'endereço':
    #                 inicioFrase = paragrafoAux.find(value,0)
    #                 finalFrase = inicioFrase + len(value) + 1
    #                 proximoEspaco = paragrafoAux.find("COMPLEMENTO:", finalFrase)
    #                 valorExtraido = paragrafoAux[finalFrase:proximoEspaco]
    #                 if 'CONTRATO DE EMPRÉSTIMO' in valorExtraido:
    #                     apagar = removerText(valorExtraido)
    #                     valorExtraido = valorExtraido.replace(apagar,'')

    #             elif key == 'complemento':
    #                 inicioFrase = paragrafoAux.find(value,0)
    #                 finalFrase = inicioFrase + len(value) + 1
    #                 proximoEspaco = paragrafoAux.find("BAIRRO:", finalFrase)
    #                 valorExtraido = paragrafoAux[finalFrase:proximoEspaco]
    #                 if 'CONTRATO DE EMPRÉSTIMO' in valorExtraido:
    #                     apagar = removerText(valorExtraido)
    #                     valorExtraido = valorExtraido.replace(apagar,'')

    #             elif key == 'bairro':
    #                 inicioFrase = paragrafoAux.find(value,0)
    #                 finalFrase = inicioFrase + len(value) + 1
    #                 proximoEspaco = paragrafoAux.find("CIDADE:", finalFrase)
    #                 valorExtraido = paragrafoAux[finalFrase:proximoEspaco]
    #                 if 'CONTRATO DE EMPRÉSTIMO' in valorExtraido:
    #                     apagar = removerText(valorExtraido)
    #                     valorExtraido = valorExtraido.replace(apagar,'')

    #             elif key == 'cidade':
    #                 inicioFrase = paragrafoAux.find(value,0)
    #                 finalFrase = inicioFrase + len(value) + 1
    #                 proximoEspaco = paragrafoAux.find("UF:", finalFrase)
    #                 valorExtraido = paragrafoAux[finalFrase:proximoEspaco]
    #                 if 'CONTRATO DE EMPRÉSTIMO' in valorExtraido:
    #                     apagar = removerText(valorExtraido)
    #                     valorExtraido = valorExtraido.replace(apagar,'')
    #             elif key == 'telefone':
    #                 inicioFrase = paragrafoAux.find(value,0)
    #                 finalFrase = inicioFrase + len(value) + 1
    #                 proximoEspaco = paragrafoAux.find("EMAIL:", finalFrase)
    #                 valorExtraido = paragrafoAux[finalFrase:proximoEspaco]
    #                 if 'CONTRATO DE EMPRÉSTIMO' in valorExtraido:
    #                     apagar = removerText(valorExtraido)
    #                     valorExtraido = valorExtraido.replace(apagar,'')
    #             else:
    #                 paragrafoAux = paragrafoAux + ' '
    #                 inicioFrase = paragrafoAux.find(value,0)
    #                 finalFrase = inicioFrase + len(value) + 1
    #                 proximoEspaco = paragrafoAux.find(" ", finalFrase)
    #                 valorExtraido = paragrafoAux[finalFrase:proximoEspaco]
    #                 if 'CONTRATO DE EMPRÉSTIMO' in valorExtraido:
    #                     apagar = removerText(valorExtraido)
    #                     valorExtraido = valorExtraido.replace(apagar,'')
    #             listaKey.append(key)
    #             listaValues.append(valorExtraido.strip())
        
        elif 'FI_' in path:
            listaDePara = {'cpfTitular':'CPF:','data de nascimentoTitular':'DATA DE NASCIMENTO:','endereçoTitular':'ENDEREÇO RESIDENCIAL E DOMICILIAR:','complementoTitular':'COMPLEMENTO:','bairroTitular':'BAIRRO:','cidadeTitular':'CIDADE:','ufTitular':'UF:','cepTitular':'CEP:',
                    'telefoneTitular':'TELEFONE(S)','emailTitular':'EMAIL:'}
            # Extraindo participantes da operacao 
            começo = contrato['Titular'].strip()                    #inicio e fim da extração
            fim = 'CARACTERÍSTICAS DO FINANCIAMENTO'
            #Pegar posição das variáveis auxiliares no texto
            inicioTopico = text.find(começo, 0)
            finalTopico = text.find(fim, 0)

            #Criar Paragráfo Auxiliar
            paragrafoAux = text[inicioTopico+len(começo)+1:finalTopico-1]
            paragrafoAux = re.sub('\s+',' ', paragrafoAux)

            for key, value in listaDePara.items():
                if key == 'endereçoTitular':
                    inicioFrase = paragrafoAux.find(value,0)
                    finalFrase = inicioFrase + len(value) + 1
                    proximoEspaco = paragrafoAux.find("COMPLEMENTO:", finalFrase)
                    valorExtraido = paragrafoAux[finalFrase:proximoEspaco]
                    if 'CONTRATO DE EMPRÉSTIMO' in valorExtraido:
                        apagar = removerText(valorExtraido)
                        valorExtraido = valorExtraido.replace(apagar,'')

                elif key == 'complementoTitular':
                    inicioFrase = paragrafoAux.find(value,0)
                    finalFrase = inicioFrase + len(value) + 1
                    proximoEspaco = paragrafoAux.find("BAIRRO:", finalFrase)
                    valorExtraido = paragrafoAux[finalFrase:proximoEspaco]
                    if 'CONTRATO DE EMPRÉSTIMO' in valorExtraido:
                        apagar = removerText(valorExtraido)
                        valorExtraido = valorExtraido.replace(apagar,'')

                elif key == 'bairroTitular':
                    inicioFrase = paragrafoAux.find(value,0)
                    finalFrase = inicioFrase + len(value) + 1
                    proximoEspaco = paragrafoAux.find("CIDADE:", finalFrase)
                    valorExtraido = paragrafoAux[finalFrase:proximoEspaco]
                    if 'CONTRATO DE EMPRÉSTIMO' in valorExtraido:
                        apagar = removerText(valorExtraido)
                        valorExtraido = valorExtraido.replace(apagar,'')

                elif key == 'cidadeTitular':
                    inicioFrase = paragrafoAux.find(value,0)
                    finalFrase = inicioFrase + len(value) + 1
                    proximoEspaco = paragrafoAux.find("UF:", finalFrase)
                    valorExtraido = paragrafoAux[finalFrase:proximoEspaco]
                    if 'CONTRATO DE EMPRÉSTIMO' in valorExtraido:
                        apagar = removerText(valorExtraido)
                        valorExtraido = valorExtraido.replace(apagar,'')
                elif key == 'telefoneTitular':
                    inicioFrase = paragrafoAux.find(value,0)
                    finalFrase = inicioFrase + len(value) + 1
                    proximoEspaco = paragrafoAux.find("EMAIL:", finalFrase)
                    valorExtraido = paragrafoAux[finalFrase:proximoEspaco]
                    if 'CONTRATO DE EMPRÉSTIMO' in valorExtraido:
                        apagar = removerText(valorExtraido)
                        valorExtraido = valorExtraido.replace(apagar,'')
                else:
                    paragrafoAux = paragrafoAux + ' '
                    inicioFrase = paragrafoAux.find(value,0)
                    finalFrase = inicioFrase + len(value) + 1
                    proximoEspaco = paragrafoAux.find(" ", finalFrase)
                    valorExtraido = paragrafoAux[finalFrase:proximoEspaco]
                    if 'CONTRATO DE EMPRÉSTIMO' in valorExtraido:
                        apagar = removerText(valorExtraido)
                        valorExtraido = valorExtraido.replace(apagar,'')
                listaKey.append(key)
                listaValues.append(valorExtraido.strip())

    #Criar Dicionario das duas Listas
    dict_keyValue = dict(zip(listaKey,listaValues))
    if contrato['Quantidade'] == 1:
        for comparar in range(0, dict_keyValue['Quantidade']):
            for comparar2 in range(0, contrato['Quantidade']):
                if contrato[f"Participante{comparar+1}"] == dict_keyValue[f"nome{comparar2+1}"]:
                    dict_keyValue[f"participação{comparar2+1}"] = contrato[f"Participação{comparar+1}"]

    else:
        for comparar in range(0, dict_keyValue['Quantidade']):
            for comparar2 in range(0, contrato['Quantidade']-1):
                if contrato[f"Participante{comparar+1}"] == dict_keyValue[f"nome{comparar2+1}"]:
                    dict_keyValue[f"participação{comparar2+1}"] = contrato[f"Participação{comparar+1}"]

    return dict_keyValue


