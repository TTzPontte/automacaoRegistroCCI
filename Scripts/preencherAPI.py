# Bibliotecas
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from time import sleep
import re 
from selenium.webdriver.common.keys import Keys
import lerContrato as lc
from lerContrato import lerContrato
from lerPDFLaudo import lerPDF
from lerLaudo import lerLaudo

def preencherAPI(calculoFluxoPath, textoContrato, textoLaudo, textoParticipantes):
    
    print(calculoFluxoPath)
    print(textoContrato)
    print(textoLaudo)
    print(textoParticipantes)

    ### Funções

    # Função para limpar campos
    def limparCampo(campo):
        campo.send_keys(Keys.CONTROL,"a")
        campo.send_keys(Keys.DELETE)

    ### Abrir front-end

    #ChromeDriver
    driver = webdriver.Chrome(executable_path=r'G:\Drives compartilhados\Pontte\Operações\Automações\Scripts\Pontte\Driver\chromedriver.exe')

    #Acessar API Aztronic
    driver.get('http://aztronic.s3-website-us-east-1.amazonaws.com/')
    sleep(5)

    ### Preencher

    # Upload do Calculo de fluxo 
    calculoFluxoWeb = driver.find_element_by_xpath('//*[@id="main"]/div/section[1]/div/div/form/fieldset[1]/div[1]/label/input')
    calculoFluxoWeb.send_keys(calculoFluxoPath)
    sleep(2)

    
    # Extraido informações com o leitor de contratos
    contrato = textoContrato
    Participantes = textoParticipantes
    Laudo = textoLaudo

    # Pegando Xpath para preencher API
    dataContrato = driver.find_element_by_xpath('//*[@id="data_contrato"]')
    codigoIntegracao = driver.find_element_by_xpath('//*[@id="codigo_integracao"]')
    ruaGaranti = driver.find_element_by_xpath('//*[@id="rua"]')
    numeroGarantia = driver.find_element_by_xpath('//*[@id="numero"]')
    complementoGarantia = driver.find_element_by_xpath('//*[@id="complemento"]')
    cidadeGarantia = driver.find_element_by_xpath('//*[@id="cidade"]')
    bairroGarantia = driver.find_element_by_xpath('//*[@id="bairro"]')
    ufGarantia = driver.find_element_by_xpath('//*[@id="UF"]')
    cepGarantia = driver.find_element_by_xpath('//*[@id="cep"]')
    unidadeGarantia = driver.find_element_by_xpath('//*[@id="unidade"]')
    blocoGarantia = driver.find_element_by_xpath('//*[@id="Bloco"]')
    matriculaGarantia = driver.find_element_by_xpath('//*[@id="matricula"]')


    limparCampo(dataContrato)
    limparCampo(numeroGarantia)
    limparCampo(complementoGarantia)
    limparCampo(cidadeGarantia)
    limparCampo(bairroGarantia)
    limparCampo(ufGarantia)
    limparCampo(cepGarantia)
    limparCampo(unidadeGarantia)
    limparCampo(blocoGarantia)
    limparCampo(matriculaGarantia)

    # Preenchendo API
    dataContrato.send_keys(contrato['dataContrato'])        
    codigoIntegracao.send_keys(contrato['CCI'])
    driver.find_element_by_xpath('/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[1]/input').send_keys(contrato['CCI'])

    ruaGaranti.send_keys(Laudo['enderecoImovel'])                                  
    numeroGarantia.send_keys(Laudo['numeroImovel'])                                  
    complementoGarantia.send_keys(Laudo['complementoImovel'])                        
    cidadeGarantia.send_keys(Laudo['cidadeImovel'])                                  
    bairroGarantia.send_keys(Laudo['bairroImovel'])                                  
    ufGarantia.send_keys(Laudo['estadoImovel'])                                          
    cepGarantia.send_keys(Laudo['cepImovel'])                                         
    unidadeGarantia.send_keys(Laudo['unidadeImovel'])                                       
    blocoGarantia.send_keys(Laudo['blocoImovel'])                                          
    matriculaGarantia.send_keys(contrato['Matrícula'])

    # Selecionar o cartório 
    cartorio = driver.find_element_by_xpath('//*[@id="numero_cartorio"]').click()              # Por enquanto tem que arrumar na Az até Tech arrumar
    sleep(1)
    selectCartorio = driver.find_element_by_xpath('//*[@id="numero_cartorio"]/div[2]/ul/li[1]').click()

    # Adicionar campos de participantes
    numCamposParticipantes = int(contrato['Quantidade'])
    print(numCamposParticipantes)
    print(type(numCamposParticipantes))
    for addCampo in range(0, numCamposParticipantes - 1):
        driver.find_element_by_xpath('//*[@id="main"]/div/section[1]/div/div/form/button').click()
        sleep(1)

    contador = int(contrato['Quantidade'])

    for quantidade in range(0, contador):
        # Preenchendo participantes
        nomeParticipantes = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[{quantidade+3}]/div/label[3]/input')
        emailParticipantes = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[{quantidade+3}]/div/label[4]/input')
        participação = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[{quantidade+3}]/div/label[5]/input')
        cnpjCpf = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[{quantidade+3}]/div/label[6]/input')
        sexo = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[{quantidade+3}]/div/label[8]/input')
        dataNacimento = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[{quantidade+3}]/div/label[9]/input')
        telefone = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[{quantidade+3}]/div/label[10]/input')
        ruaParticipantes = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[{quantidade+3}]/div/label[11]/input')
        numeroParticipantes = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[{quantidade+3}]/div/label[12]/input')
        complementoParticipantes = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[{quantidade+3}]/div/label[13]/input')
        cidadeParticipantes = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[{quantidade+3}]/div/label[14]/input')
        bairroParticipantes = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[{quantidade+3}]/div/label[15]/input')
        ufParticipantes = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[{quantidade+3}]/div/label[16]/input')
        cepParticipantes = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[{quantidade+3}]/div/label[17]/input')

        # Limpar campos
        limparCampo(nomeParticipantes)
        limparCampo(emailParticipantes)
        limparCampo(participação)
        limparCampo(cnpjCpf)
        limparCampo(sexo)
        limparCampo(dataNacimento)
        limparCampo(telefone)
        limparCampo(ruaParticipantes)
        limparCampo(numeroParticipantes)
        limparCampo(complementoParticipantes)
        limparCampo(cidadeParticipantes)
        limparCampo(bairroParticipantes)
        limparCampo(ufParticipantes)
        limparCampo(cepParticipantes)
        sleep(1)
        
        # Preencher campos
        nomeParticipantes.send_keys(Participantes[f'nomeCompletoP{quantidade+1}'])
        emailParticipantes.send_keys(Participantes[f'emailP{quantidade+1}'])
        participação.send_keys(Participantes[f'participacaoNaOperacaoP{quantidade+1}'])
        cnpjCpf.send_keys(Participantes[f'cpfP{quantidade+1}'])
        sexo.send_keys(Participantes[f'sexoP{quantidade+1}'])
        dataNacimento.send_keys(Participantes[f'dataNascimentoP{quantidade+1}'])
        telefone.send_keys(Participantes[f'telefoneP{quantidade+1}'])
        ruaParticipantes.send_keys(Participantes[f'endereçoP{quantidade+1}'])
        numeroParticipantes.send_keys(Participantes[f'numeroResidenciaP{quantidade+1}'])
        complementoParticipantes.send_keys(Participantes[f'complementoP{quantidade+1}'])
        cidadeParticipantes.send_keys(Participantes[f'cidadeP{quantidade+1}'])
        bairroParticipantes.send_keys(Participantes[f'bairroP{quantidade+1}'])
        ufParticipantes.send_keys(Participantes[f'estadoP{quantidade+1}'])
        cepParticipantes.send_keys(Participantes[f'cepP{quantidade+1}'])
        sleep(1)

    # Tabela de Venda
    dataBase = driver.find_element_by_xpath('//*[@id="data_base"]')
    indice = driver.find_element_by_xpath('//*[@id="indice_pre"]')
    taxaJuros = driver.find_element_by_xpath('//*[@id="taxa_juros"]')
    tipoAmortização = driver.find_element_by_xpath('//*[@id="taxa_juros"]')

    limparCampo(dataBase)
    limparCampo(taxaJuros)

    if contrato['indice'] == 'IPCA':
        indice.click()
        indice =driver.find_element_by_css_selector('#indice_pre > option:nth-child(2)').click()

    if contrato['tabela'] == 'PRICE' or contrato['tabela'] == 'Price' or contrato['tabela'] == 'price':
        tipoAmortização.click()
        tipoAmortização =driver.find_element_by_css_selector('#tipo_amortizacao > option:nth-child(2)').click()

    elif contrato['tabela'] == 'SAC':
        tipoAmortização.click()
        tipoAmortização =driver.find_element_by_css_selector('#tipo_amortizacao > option:nth-child(1)').click()
    taxaJuros.send_keys(str(contrato['taxaAoAno']*100).replace('.',','))
    dataBase.send_keys(contrato['dataContrato'])

    # Upa operação para Aztronic

    #driver.find_element_by_xpath('/html/body/div/main/div/section[1]/div/div/form/div[4]/button').click() # Botão Cadastrar contrato