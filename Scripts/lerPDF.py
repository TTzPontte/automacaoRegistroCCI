# importa as bibliotecas necessárias
import re
import os
import PyPDF2
import pikepdf

# Abre o arquivo pdf 
#path = r'C:\Users\Matheus\Documents\Git\Pontte\automacaoRegistroAztronic\automacaoRegistroCCI\Laudos\Laudo - Agostinho.pdf'

def lerPDF(path, numberOfPages):
    #Transformar PDF
    pdf = pikepdf.open(path, allow_overwriting_input=True)
    pdf.save(path)

    #Abrir PDF 
    pdf_file = open(path, 'rb')

    #Faz a leitura usando a biblioteca
    read_pdf = PyPDF2.PdfFileReader(pdf_file)

    # pega o numero de páginas
    number_of_pages = read_pdf.getNumPages()

    #Extriar Texto de n Paginas
    text=''
    for i in range(0,numberOfPages):
        #Ler Página PDF
        pageObj = read_pdf.getPage(i)
        #Extrair Texto
        text=text+pageObj.extractText()

    #Tratar Texto (Remover Quebra de Linhas)
    text = re.sub('\r', '', text) 
    text = re.sub('\n', '', text)

    #Retornar Texto
    return text
