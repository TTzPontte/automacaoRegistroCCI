### Bibliotecas ###

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options



### Função para preencher os campos da API ###

def preencherAPI(calculoFluxoPath, textoContrato, textoLaudo, textoParticipantes):



    ### Funções Auxiliares ###

    # Função para limpar campos
    def limparCampo(campo):
        campo.send_keys(Keys.CONTROL,"a")
        campo.send_keys(Keys.DELETE)



    ### Declarar Variaveis ###

    # Laudo 
    Laudo = textoLaudo
    ruaL = Laudo['enderecoImovel']
    numeroL = Laudo['numeroImovel']
    complementoL = Laudo['complementoImovel']
    cidadeL = Laudo['cidadeImovel']
    bairroL = Laudo['bairroImovel']
    ufL = Laudo['estadoImovel']
    cepL = Laudo['cepImovel']
    unidadeL = Laudo['unidadeImovel']
    blocoL = Laudo['blocoImovel']

    # Contrato
    Contrato = textoContrato
    matriculaC = Contrato['Matrícula']
    dataContatoC = Contrato['dataContrato']
    codigoIntegracaoC = ''.join([d for d in Contrato['CCI'] if d.isdigit()])
    contadorC = int(Contrato['Quantidade'])
    indiceC = Contrato['indice']
    tabelaC = Contrato['tabela']
    taxaC = round(float(Contrato['taxaAoAno']),4)
    

    ### Abrir Front-End da API ###

    # ChromeDriver
    driver = webdriver.Chrome(executable_path=r'G:\Drives compartilhados\Pontte\Operações\Automações\Scripts\Pontte\Driver\chromedriver.exe')
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    
    # Abrir Link do Front-End
    driver.get('http://aztronic.s3-website-us-east-1.amazonaws.com/')
    sleep(5)



    ### Preencher Campos de Cadastro ###

    # Upload do calculo de fluxo
    calculoFluxoWeb = driver.find_element(by='xpath',value='/html/body/div/main/div/section[1]/div/div/form/fieldset[1]/div[1]/label/input')
    calculoFluxoWeb.send_keys(calculoFluxoPath)
    sleep(2)

    # Preenchendo Dados do Imovel em garantia
    dataContrato = driver.find_element('xpath','//*[@id="data_contrato"]')
    codigoIntegracao = driver.find_element('xpath','//*[@id="codigo_integracao"]')
    codigoIntegracao2 = driver.find_element('xpath','/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[1]/input')
    ruaGaranti = driver.find_element('xpath','//*[@id="rua"]')
    numeroGarantia = driver.find_element('xpath','//*[@id="numero"]')
    complementoGarantia = driver.find_element('xpath','//*[@id="complemento"]')
    cidadeGarantia = driver.find_element('xpath','//*[@id="cidade"]')
    bairroGarantia = driver.find_element('xpath','//*[@id="bairro"]')
    ufGarantia = driver.find_element('xpath','//*[@id="UF"]')
    cepGarantia = driver.find_element('xpath','//*[@id="cep"]')
    unidadeGarantia = driver.find_element('xpath','//*[@id="unidade"]')
    blocoGarantia = driver.find_element('xpath','//*[@id="Bloco"]')
    matriculaGarantia = driver.find_element('xpath','//*[@id="matricula"]')

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

    dataContrato.send_keys(dataContatoC)        
    codigoIntegracao.send_keys(codigoIntegracaoC)
    codigoIntegracao2.send_keys(codigoIntegracaoC)
    ruaGaranti.send_keys(ruaL)                                  
    numeroGarantia.send_keys(numeroL)                                  
    complementoGarantia.send_keys(complementoL)                        
    cidadeGarantia.send_keys(cidadeL)                                  
    bairroGarantia.send_keys(bairroL)                                  
    ufGarantia.send_keys(ufL)                                          
    cepGarantia.send_keys(cepL)                                         
    unidadeGarantia.send_keys(unidadeL)                                       
    blocoGarantia.send_keys(blocoL)                                          
    matriculaGarantia.send_keys(matriculaC)

    # Selecionar o cartório 
    cartorio = driver.find_element('xpath','//*[@id="numero_cartorio"]').click()
    sleep(0.5)      
    selectCartorio = driver.find_element('xpath','//*[@id="numero_cartorio"]/div[2]/ul/li[1]').click() # esta clicando sempre no primeito por enquanto.

    # Dicionario com os dados dos participantes
    Participantes = textoParticipantes

    # Adicionar campos de participantes
    numCamposParticipantes = contadorC
    for addCampo in range(0, numCamposParticipantes - 1):
        driver.find_element('xpath','//*[@id="main"]/div/section[1]/div/div/form/button').click()

    # Preenchendo participantes em loop (de acordo com a quantidade de integrantes no contrato)
    for quantidade in range(0, contadorC):
        nomeParticipantes = driver.find_element('xpath',f'/html/body/div/main/div/section[1]/div/div/form/fieldset[{quantidade+3}]/div/label[3]/input')
        emailParticipantes = driver.find_element('xpath',f'/html/body/div/main/div/section[1]/div/div/form/fieldset[{quantidade+3}]/div/label[4]/input')
        participação = driver.find_element('xpath',f'/html/body/div/main/div/section[1]/div/div/form/fieldset[{quantidade+3}]/div/label[5]/input')
        cnpjCpf = driver.find_element('xpath',f'/html/body/div/main/div/section[1]/div/div/form/fieldset[{quantidade+3}]/div/label[6]/input')
        pjOuPf = driver.find_element('xpath',f'/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[{quantidade+3}]/div/label[7]/select')
        sexo = driver.find_element('xpath',f'/html/body/div/main/div/section[1]/div/div/form/fieldset[{quantidade+3}]/div/label[8]/input')
        relacao = driver.find_element('xpath',f'/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[{quantidade+3}]/div/label[2]/select')
        dataNacimento = driver.find_element('xpath',f'/html/body/div/main/div/section[1]/div/div/form/fieldset[{quantidade+3}]/div/label[9]/input')
        telefone = driver.find_element('xpath',f'/html/body/div/main/div/section[1]/div/div/form/fieldset[{quantidade+3}]/div/label[10]/input')
        ruaParticipantes = driver.find_element('xpath',f'/html/body/div/main/div/section[1]/div/div/form/fieldset[{quantidade+3}]/div/label[11]/input')
        numeroParticipantes = driver.find_element('xpath',f'/html/body/div/main/div/section[1]/div/div/form/fieldset[{quantidade+3}]/div/label[12]/input')
        complementoParticipantes = driver.find_element('xpath',f'/html/body/div/main/div/section[1]/div/div/form/fieldset[{quantidade+3}]/div/label[13]/input')
        cidadeParticipantes = driver.find_element('xpath',f'/html/body/div/main/div/section[1]/div/div/form/fieldset[{quantidade+3}]/div/label[14]/input')
        bairroParticipantes = driver.find_element('xpath',f'/html/body/div/main/div/section[1]/div/div/form/fieldset[{quantidade+3}]/div/label[15]/input')
        ufParticipantes = driver.find_element('xpath',f'/html/body/div/main/div/section[1]/div/div/form/fieldset[{quantidade+3}]/div/label[16]/input')
        cepParticipantes = driver.find_element('xpath',f'/html/body/div/main/div/section[1]/div/div/form/fieldset[{quantidade+3}]/div/label[17]/input')

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
        
        # Preencher campos
        nomeParticipantes.send_keys(Participantes[f'nomeCompletoP{quantidade+1}'])
        emailParticipantes.send_keys(Participantes[f'emailP{quantidade+1}'])
        participação.send_keys(Participantes[f'participacaoNaOperacaoP{quantidade+1}'].replace('%',''))
        cnpjCpf.send_keys(Participantes[f'cpfP{quantidade+1}'])
        pjOuPf.click()
        if Participantes[f'operação{quantidade+1}'] == 'PF': driver.find_element(by='xpath', value=f'/html/body/div/main/div/section[1]/div/div/form/fieldset[{quantidade+3}]/div/label[7]/select/option[1]').click()
        else:driver.find_element(by='xpath', value=f'/html/body/div/main/div/section[1]/div/div/form/fieldset[{quantidade+3}]/div/label[7]/select/option[2]').click()
        sexo.send_keys(Participantes[f'sexoP{quantidade+1}'])
        relacao.click()
        if Participantes[f'relacaoDoP{quantidade+1}'] == 'Titular': driver.find_element(by='xpath',value=f'/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[{quantidade+3}]/div/label[2]/select/option[2]').click()
        elif Participantes[f'relacaoDoP{quantidade+1}'] == 'Cônjuge': driver.find_element(by='xpath',value=f'/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[{quantidade+3}]/div/label[2]/select/option[3]').click()
        elif Participantes[f'relacaoDoP{quantidade+1}'] == 'Procurador': driver.find_element(by='xpath',value=f'/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[{quantidade+3}]/div/label[2]/select/option[4]').click()
        elif Participantes[f'relacaoDoP{quantidade+1}'] == 'Pai': driver.find_element(by='xpath',value=f'/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[{quantidade+3}]/div/label[2]/select/option[5]').click()
        elif Participantes[f'relacaoDoP{quantidade+1}'] == 'Mãe': driver.find_element(by='xpath',value=f'/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[{quantidade+3}]/div/label[2]/select/option[6]').click()
        elif Participantes[f'relacaoDoP{quantidade+1}'] == 'Irmão': driver.find_element(by='xpath',value=f'/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[{quantidade+3}]/div/label[2]/select/option[7]').click()
        dataNacimento.send_keys(Participantes[f'dataNascimentoP{quantidade+1}'])
        telefone.send_keys(Participantes[f'telefoneP{quantidade+1}'])
        ruaParticipantes.send_keys(Participantes[f'endereçoP{quantidade+1}'])
        numeroParticipantes.send_keys(Participantes[f'numeroResidenciaP{quantidade+1}'])
        complementoParticipantes.send_keys(Participantes[f'complementoP{quantidade+1}'])
        cidadeParticipantes.send_keys(Participantes[f'cidadeP{quantidade+1}'])
        bairroParticipantes.send_keys(Participantes[f'bairroP{quantidade+1}'])
        ufParticipantes.send_keys(Participantes[f'estadoP{quantidade+1}'])
        cepParticipantes.send_keys(Participantes[f'cepP{quantidade+1}'])

    # Preencher tabela de venda
        dataBase = driver.find_element('xpath','//*[@id="data_base"]')
    indice = driver.find_element('xpath','//*[@id="indice_pre"]')
    taxaJuros = driver.find_element('xpath','//*[@id="taxa_juros"]')
    tipoAmortização = driver.find_element('xpath','//*[@id="taxa_juros"]')

    limparCampo(dataBase)
    limparCampo(taxaJuros)

    if indiceC == 'IPCA':
        indice.click()
        sleep(1)
        indice = driver.find_element(by='xpath',value='//*[@id="indice_pre"]/option[3]').click()

    if tabelaC == 'PRICE' or tabelaC == 'Price' or tabelaC == 'price':
        tipoAmortização.click()
        tipoAmortização =driver.find_element(by='xpath',value='//*[@id="tipo_amortizacao"]/option[3]').click()

    elif tabelaC == 'SAC':
        tipoAmortização.click()
        tipoAmortização =driver.find_element(by='xpath',value='//*[@id="tipo_amortizacao"]/option[2]').click()
    taxaJuros.send_keys(taxaC)
    dataBase.send_keys(dataContatoC)

    print("Valide os dados antes de confirmar o cadastramento!")
    print('Você tem 10 minutos para validação')
    sleep(600)