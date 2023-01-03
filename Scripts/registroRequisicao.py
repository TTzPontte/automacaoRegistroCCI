import datetime 
import os

def registrarRequisicao(json, nomeDoCliente, codigoCliente):
    
    jsonFile = json
    nomeCliente = nomeDoCliente.lower()
    codigoAz = codigoCliente
    
    path = rf'G:\Drives compartilhados\Pontte\Operações\Implantação\{nomeCliente+" - "+codigoAz}'
    path = path.replace('/','')

    #Verifica se existe a pasta
    isExist = os.path.exists(path)
    if not isExist:
        #Caso não exista a pasta, cria a pasta
        os.makedirs(path)
    
    
    namePC = os.environ.get("USERNAME")
    dataHoje = datetime.datetime.today().strftime("%d.%m.%y - %Hh%M")
    
    with open(os.path.join(path, f'Requisicao - {dataHoje}.txt'), "w") as f:
        f.write(f'Realizado por: {namePC} em {dataHoje}\n'+'\n'+str(jsonFile)+'\n')
    
