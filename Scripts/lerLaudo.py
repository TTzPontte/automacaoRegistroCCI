from lerPDFLaudo import lerPDF
import re 

def lerLaudo(laudoPDF):
    #Extrair Texto
    pathDocument = laudoPDF
    extTexto = lerPDF(pathDocument,4)
    extTexto = re.sub(' {2,}', ' ', extTexto).strip(' ')
    #print(extTexto)
    #DICT DE-PARA dos arquivos que serão extraídos
    listaDePara = {"Valor de Mercado: ": "","Matrícula: ": "", "Cartório": "", "Endereço: ": "", "Número: ":"", "Complemento: ": "","Bairro: ":"","Cidade: ":"","UF: ":"", "CEP ": ""}

    for key, value in listaDePara.items(): 
        if key == "Valor de Mercado: " or key == "Endereço: ":
            #Extrair Valores
            inicioFrase = extTexto.find(key,0)
            finalFrase = inicioFrase + len(key)
            breakLine = extTexto.find(" | ", finalFrase)
            saida = extTexto[finalFrase:breakLine+2]

            #Tratamento Endereço
            if key == "Endereço: ":
                posicaoNumero = saida.find("nº",0) + len("nº")
                nextSpace = saida.find(" ", posicaoNumero)
                if posicaoNumero == nextSpace:
                    posicaoNumero = posicaoNumero+1
                    nextSpace = saida.find(" ", posicaoNumero)
                numeroEndereco = saida[posicaoNumero:nextSpace+1]
                auxComplemento = len(saida)-(posicaoNumero+len(numeroEndereco))
                if auxComplemento >= 5:
                    complemento = saida[nextSpace+2:len(saida)]
                else:
                    complemento = 'N/A'

                saida = saida[0:posicaoNumero-len("nº ")]
                
                #Adicionar na Lista
                listaDePara["Número: "] = numeroEndereco.strip()
                listaDePara["Complemento: "] = complemento.strip()
            
            #Atribuir Valor ao DICT
            listaDePara[key] = saida.strip().replace('| ', '')
            
        elif key == "Matrícula: ":
            #Extrair Número da Matrícula
            inicioFrase = extTexto.find(key,0)
            finalFrase = inicioFrase + len(key)
            proximoEspaco = extTexto.find(" ", finalFrase)
            numeroMat = extTexto[finalFrase:proximoEspaco]
            if "|" in numeroMat:
                #Extrair Número da Matrícula Novamente
                key = "Matrícula: | "
                inicioFrase = extTexto.find(key,0)
                finalFrase = inicioFrase + len(key)
                proximoEspaco = extTexto.find(" ", finalFrase)
                numeroMat = extTexto[finalFrase:proximoEspaco]
                

            
            #Auxiliar Pós Número Matrícula
            posMat = extTexto.find(numeroMat,0)+len(numeroMat)+1
            finalCart = extTexto.find(" | ",posMat)

            #Extraír dados do cartório
            cartorio = extTexto[posMat+3:finalCart]

            #Atribuir Valor ao DICT
            listaDePara['Matrícula: '] = numeroMat
            listaDePara['Cartório'] = cartorio
        
        elif key=="Bairro: " or key=="Cidade: " or key=="UF: | ":
            inicioFrase = extTexto.find(key,0)
            if key=="Bairro: ":
                finalFrase=extTexto.find("Cidade",inicioFrase)
            elif key=="Cidade: ":
                finalFrase=extTexto.find("UF",inicioFrase)
            else:
                finalFrase=extTexto.find(" | ",inicioFrase)

            result = extTexto[inicioFrase+len(key):finalFrase].replace('\xa0', '').replace(' | ', '').replace('| ', '')
            listaDePara[key] = result

        elif key=="CEP ":
            inicioFrase = extTexto.find(key,0)
            finalFrase = extTexto.find("-", inicioFrase)
            cep = extTexto[inicioFrase+len(key):finalFrase+4]
            listaDePara[key] = cep

    print(pathDocument)
    print(listaDePara, "\n")
    
    
    return listaDePara

lerLaudo(r'G:\Drives compartilhados\Pontte Crédito\0_HOME EQUITY\0_Analises\ILSON BARON ROTH - ID 548733160\KIT QI\5. Laudo.pdf')