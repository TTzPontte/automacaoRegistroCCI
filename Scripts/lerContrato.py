# importa as bibliotecas necessárias
import PyPDF2
import re
import pandas as pd
import string

# Apagar ao finalizar
#patha = r'C:\Users\MatheusPereira\OneDrive - Pontte\Área de Trabalho\automacaoRegistroCCI\Contratos\HE_Contrato_Agostinho_Assinatura Digital_VFinal.pdf'
#patha = r'C:\Users\Matheus\Documents\Git\Pontte\automacaoRegistroAztronic\automacaoRegistroCCI\Contratos\HE_Contrato_Agostinho_Assinatura Digital_VFinal.pdf'
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
        listaDePara = {'valorTotal':'1. Valor do Financiamento: R$','tabela': 'Sistema de Amortização:','Taxa ao Mes':'2.1.1. Juros de','registro':'4.3. Despesas','valorLiquido': '7. Valor Líquido a Liberar do  Financiamento : R$',
                'prazoMes': 'PRAZO DE AMORTIZAÇÃO :','valorPrimeiraParcelaComEncargos':'VALOR TOTAL DO PRIMEIRO ENCARGO, NESTA DATA:  R$',
                'valorImóvel':'Imóvel para fins de leilão:  R$','prazoContrato': 'N.º DE PRESTAÇÕES: ','ultimaParcela':'DATA DE VENCIMENTO DA ÚLTIMA PRESTAÇÃO: ','dataContrato': 'Data de Liberação dos Recursos: ',
                'valorPrimeiraParcela':'VALOR  DA  PARCELA  MENSAL  (AMORTIZAÇÃO  E  JUROS),  NESTA  DATA: R$','primeiraParcela':'DATA DE VENCIMENTO DA PRIMEIRA PRESTAÇÃO: ','indice':'ÍNDICE: MENSAL do'
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

        listaKey.append('Matrícula')
        listaValues.append(valorExtraido)
        

        # Extraindo cartório
        inicioFrase = text.find(f'Matriculado sob nº {valorExtraido}, no',0)
        finalFrase = inicioFrase + len(f'Matriculado sob nº {valorExtraido}, no') + 1
        ultimaMatricula = text.find("Forma de aquisição", finalFrase)
        valorExtraido = text[finalFrase:ultimaMatricula-2]

        listaKey.append('Cartório')
        listaValues.append(valorExtraido)
        

        #Criar Dicionario das duas Listas
        dict_keyValue = dict(zip(listaKey,listaValues))
        
    
    elif "HE_" in path:
        #Faz a leitura usando a biblioteca
        read_pdf = PyPDF2.PdfFileReader(path)

        # pega o numero de páginas
        number_of_pages = read_pdf.getNumPages()

        #Extriar Texto Página 1 a 5
        text=''
        for i in range(0,4):
            #Ler Página PDF
            pageObj = read_pdf.getPage(i)
            #Extrair Texto
            text=text+pageObj.extractText()

        #Tratar Texto (Remover Quebra de Linhas)
        text = re.sub('\r', '', text) 
        text = re.sub('\n', '', text)
        
        listaDePara = {'valorTotal':'VALOR DO EMPRÉSTIMO: R$','tabela': 'SISTEMA DE AMORTIZAÇÃO:','registro': 'DESPESAS DE REGISTRO: R$','Taxa ao Mes':'H.1. NOMINAL:','valorLiquido': '-J-K-L-M-N): R$',
                'prazoMes': 'PRAZO DE AMORTIZAÇÃO:','valorPrimeiraParcelaComEncargos':'VALOR TOTAL DO PRIMEIRO ENCARGO, NESTA DATA:  R$',
                'valorImóvel':'Valor de avaliação do Imóvel para fins de leilão:  R$','prazoContrato': 'N.º DE PRESTAÇÕES:','ultimaParcela':'DATA DO TÉRMINO DO PRAZO CONTRATUAL: ','dataContrato': 'DATA DE DESEMBOLSO:',
                'valorPrimeiraParcela':'VALOR DA PARCELA MENSAL (AMORTIZAÇÃO E JUROS), NESTA DATA:  R$','primeiraParcela':'VENCIMENTO DA PRIMEIRA PRESTAÇÃO :','indice':'ÍNDICE: MENSAL do'
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
        if len(valorExtraido) > 9:
            valorExtraido = 0
            inicioFrase = text.find('nas matrículas nºs',0)
            finalFrase = inicioFrase + len('nas matrículas nºs') + 1
            ultimaMatricula = text.find("do", finalFrase)
            valorExtraido = text[finalFrase:ultimaMatricula]
            valorExtraido = valorExtraido.replace(",", "")
            valorExtraido = valorExtraido.replace("e ", "")

        listaKey.append('Matrícula')
        listaValues.append(valorExtraido)

        # Extraindo cartório
        inicioFrase = text.find(' do Livro N°',0)
        finalFrase = inicioFrase + len(' do Livro N°') + 1
        ultimaMatricula = text.find(".", finalFrase)
        valorExtraido = text[finalFrase:ultimaMatricula]

        listaKey.append('Cartório')
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
        print(paragrafoAux)

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
            participantesValues.append(nomeExtraido)
            inicioFrase = paragrafoAux.find('PARTICIPAÇÃO:',0)
            finalFrase = inicioFrase + len('PARTICIPAÇÃO:') 
            fimValor = paragrafoAux.find("%", finalFrase)
            participacaoExtraido = paragrafoAux[finalFrase:fimValor+1]
            participantesValues.append(participacaoExtraido)
            dict_participantes = dict(zip(participantesKey,participantesValues))
        #Criar Dicionario das duas Listas
        dict_keyValue = dict(zip(listaKey,listaValues))
        dict_keyValue.update(dict_participantes)
    return dict_keyValue    

#test = lerContrato(patha)
#print(test)
