from lerPDFLaudo import lerPDF

def lerLaudo(laudoPDF):
    #Extrair Texto
    pathDocument = laudoPDF
    extTexto = lerPDF(pathDocument,2)
    
    #DICT DE-PARA dos arquivos que serão extraídos
    listaDePara = {"Valor de Mercado: ": "","Matrícula: ": "", "Cartório": ""}

    for key, value in listaDePara.items(): 
        if key == "Valor de Mercado: ":
            inicioFrase = extTexto.find(key,0)
            finalFrase = inicioFrase + len(key)
            breakLine = extTexto.find(" | ", finalFrase)
            valorMercado = extTexto[finalFrase+3:breakLine]
            listaDePara['Valor de Mercado: '] = valorMercado
            
        elif key == "Matrícula: ":
            #Extrair Número da Matrícula
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
    
    return listaDePara
