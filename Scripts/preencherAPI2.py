### Bibliotecas ###

from selenium.webdriver.support.ui import Select
from selenium import webdriver
from time import sleep
import re
from selenium.webdriver.common.keys import Keys

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
    codigoIntegracaoC = Contrato['CCI']
    contadorC = int(Contrato['Quantidade'])
    indiceC = Contrato['indice']
    tabelaC = Contrato['tabela']
    taxaC = Contrato['taxaAoAno']

    # Participantes
    Participantes = textoParticipantes
    if contadorC == 1:
        nomeP1 = Participantes[f'nomeCompletoP1'] 
        emailP1 = Participantes[f'emailP1']
        participacaoP1 = Participantes[f'participacaoNaOperacaoP1']
        cpfP1 = Participantes[f'cpfP1']
        sexoP1 = Participantes[f'sexoP1']
        relacaoP1 = Participantes[f'relacaoDoP1']
        dataNascimentoP1 = Participantes[f'dataNascimentoP1']
        telefoneP1 = Participantes[f'telefoneP1']
        ruaP1 = Participantes[f'endereçoP1']
        numeroP1 = Participantes[f'numeroResidenciaP1']
        complementoP1 = Participantes[f'complementoP1']
        cidadeP1 = Participantes[f'cidadeP1']
        bairroP1 = Participantes[f'bairroP1']
        ufP1 = Participantes[f'estadoP1']
        cepP1 =Participantes[f'cepP1']
    elif contadorC == 2:
        nomeP1 = Participantes[f'nomeCompletoP1'] 
        emailP1 = Participantes[f'emailP1']
        participacaoP1 = Participantes[f'participacaoNaOperacaoP1']
        cpfP1 = Participantes[f'cpfP1']
        sexoP1 = Participantes[f'sexoP1']
        relacaoP1 = Participantes[f'relacaoDoP1']
        dataNascimentoP1 = Participantes[f'dataNascimentoP1']
        telefoneP1 = Participantes[f'telefoneP1']
        ruaP1 = Participantes[f'endereçoP1']
        numeroP1 = Participantes[f'numeroResidenciaP1']
        complementoP1 = Participantes[f'complementoP1']
        cidadeP1 = Participantes[f'cidadeP1']
        bairroP1 = Participantes[f'bairroP1']
        ufP1 = Participantes[f'estadoP1']
        cepP1 =Participantes[f'cepP1']
        nomeP2 = Participantes[f'nomeCompletoP2'] 
        emailP2 = Participantes[f'emailP2']
        participacaoP2 = Participantes[f'participacaoNaOperacaoP2']
        cpfP2 = Participantes[f'cpfP2']
        sexoP2 = Participantes[f'sexoP2']
        relacaoP2 = Participantes[f'relacaoDoP2']
        dataNascimentoP2 = Participantes[f'dataNascimentoP2']
        telefoneP2 = Participantes[f'telefoneP2']
        ruaP2 = Participantes[f'endereçoP2']
        numeroP2 = Participantes[f'numeroResidenciaP2']
        complementoP2 = Participantes[f'complementoP2']
        cidadeP2 = Participantes[f'cidadeP2']
        bairroP2 = Participantes[f'bairroP2']
        ufP2 = Participantes[f'estadoP2']
        cepP2 =Participantes[f'cepP2']
    elif contadorC == 3:
        nomeP1 = Participantes[f'nomeCompletoP1'] 
        emailP1 = Participantes[f'emailP1']
        participacaoP1 = Participantes[f'participacaoNaOperacaoP1']
        cpfP1 = Participantes[f'cpfP1']
        sexoP1 = Participantes[f'sexoP1']
        relacaoP1 = Participantes[f'relacaoDoP1']
        dataNascimentoP1 = Participantes[f'dataNascimentoP1']
        telefoneP1 = Participantes[f'telefoneP1']
        ruaP1 = Participantes[f'endereçoP1']
        numeroP1 = Participantes[f'numeroResidenciaP1']
        complementoP1 = Participantes[f'complementoP1']
        cidadeP1 = Participantes[f'cidadeP1']
        bairroP1 = Participantes[f'bairroP1']
        ufP1 = Participantes[f'estadoP1']
        cepP1 =Participantes[f'cepP1']
        nomeP2 = Participantes[f'nomeCompletoP2'] 
        emailP2 = Participantes[f'emailP2']
        participacaoP2 = Participantes[f'participacaoNaOperacaoP2']
        cpfP2 = Participantes[f'cpfP2']
        sexoP2 = Participantes[f'sexoP2']
        relacaoP2 = Participantes[f'relacaoDoP2']
        dataNascimentoP2 = Participantes[f'dataNascimentoP2']
        telefoneP2 = Participantes[f'telefoneP2']
        ruaP2 = Participantes[f'endereçoP2']
        numeroP2 = Participantes[f'numeroResidenciaP2']
        complementoP2 = Participantes[f'complementoP2']
        cidadeP2 = Participantes[f'cidadeP2']
        bairroP2 = Participantes[f'bairroP2']
        ufP2 = Participantes[f'estadoP2']
        cepP2 =Participantes[f'cepP2']
        nomeP3 = Participantes[f'nomeCompletoP3'] 
        emailP3 = Participantes[f'emailP3']
        participacaoP3 = Participantes[f'participacaoNaOperacaoP3']
        cpfP3 = Participantes[f'cpfP3']
        sexoP3 = Participantes[f'sexoP3']
        relacaoP3 = Participantes[f'relacaoDoP3']
        dataNascimentoP3 = Participantes[f'dataNascimentoP3']
        telefoneP3 = Participantes[f'telefoneP3']
        ruaP3 = Participantes[f'endereçoP3']
        numeroP3 = Participantes[f'numeroResidenciaP3']
        complementoP3 = Participantes[f'complementoP3']
        cidadeP3 = Participantes[f'cidadeP3']
        bairroP3 = Participantes[f'bairroP3']
        ufP3 = Participantes[f'estadoP3']
        cepP3 =Participantes[f'cepP3']
    elif contadorC == 4:
        nomeP1 = Participantes[f'nomeCompletoP1'] 
        emailP1 = Participantes[f'emailP1']
        participacaoP1 = Participantes[f'participacaoNaOperacaoP1']
        cpfP1 = Participantes[f'cpfP1']
        sexoP1 = Participantes[f'sexoP1']
        relacaoP1 = Participantes[f'relacaoDoP1']
        dataNascimentoP1 = Participantes[f'dataNascimentoP1']
        telefoneP1 = Participantes[f'telefoneP1']
        ruaP1 = Participantes[f'endereçoP1']
        numeroP1 = Participantes[f'numeroResidenciaP1']
        complementoP1 = Participantes[f'complementoP1']
        cidadeP1 = Participantes[f'cidadeP1']
        bairroP1 = Participantes[f'bairroP1']
        ufP1 = Participantes[f'estadoP1']
        cepP1 =Participantes[f'cepP1']
        nomeP2 = Participantes[f'nomeCompletoP2'] 
        emailP2 = Participantes[f'emailP2']
        participacaoP2 = Participantes[f'participacaoNaOperacaoP2']
        cpfP2 = Participantes[f'cpfP2']
        sexoP2 = Participantes[f'sexoP2']
        relacaoP2 = Participantes[f'relacaoDoP2']
        dataNascimentoP2 = Participantes[f'dataNascimentoP2']
        telefoneP2 = Participantes[f'telefoneP2']
        ruaP2 = Participantes[f'endereçoP2']
        numeroP2 = Participantes[f'numeroResidenciaP2']
        complementoP2 = Participantes[f'complementoP2']
        cidadeP2 = Participantes[f'cidadeP2']
        bairroP2 = Participantes[f'bairroP2']
        ufP2 = Participantes[f'estadoP2']
        cepP2 =Participantes[f'cepP2']
        nomeP3 = Participantes[f'nomeCompletoP3'] 
        emailP3 = Participantes[f'emailP3']
        participacaoP3 = Participantes[f'participacaoNaOperacaoP3']
        cpfP3 = Participantes[f'cpfP3']
        sexoP3 = Participantes[f'sexoP3']
        relacaoP3 = Participantes[f'relacaoDoP3']
        dataNascimentoP3 = Participantes[f'dataNascimentoP3']
        telefoneP3 = Participantes[f'telefoneP3']
        ruaP3 = Participantes[f'endereçoP3']
        numeroP3 = Participantes[f'numeroResidenciaP3']
        complementoP3 = Participantes[f'complementoP3']
        cidadeP3 = Participantes[f'cidadeP3']
        bairroP3 = Participantes[f'bairroP3']
        ufP3 = Participantes[f'estadoP3']
        cepP3 =Participantes[f'cepP3']
        nomeP4 = Participantes[f'nomeCompletoP4'] 
        emailP4 = Participantes[f'emailP4']
        participacaoP4 = Participantes[f'participacaoNaOperacaoP4']
        cpfP4 = Participantes[f'cpfP4']
        sexoP4 = Participantes[f'sexoP4']
        relacaoP4 = Participantes[f'relacaoDoP4']
        dataNascimentoP4 = Participantes[f'dataNascimentoP4']
        telefoneP4 = Participantes[f'telefoneP4']
        ruaP4 = Participantes[f'endereçoP4']
        numeroP4 = Participantes[f'numeroResidenciaP4']
        complementoP4 = Participantes[f'complementoP4']
        cidadeP4 = Participantes[f'cidadeP4']
        bairroP4 = Participantes[f'bairroP4']
        ufP4 = Participantes[f'estadoP4']
        cepP4 =Participantes[f'cepP4']  
    elif contadorC == 5:
        nomeP1 = Participantes[f'nomeCompletoP1'] 
        emailP1 = Participantes[f'emailP1']
        participacaoP1 = Participantes[f'participacaoNaOperacaoP1']
        cpfP1 = Participantes[f'cpfP1']
        sexoP1 = Participantes[f'sexoP1']
        relacaoP1 = Participantes[f'relacaoDoP1']
        dataNascimentoP1 = Participantes[f'dataNascimentoP1']
        telefoneP1 = Participantes[f'telefoneP1']
        ruaP1 = Participantes[f'endereçoP1']
        numeroP1 = Participantes[f'numeroResidenciaP1']
        complementoP1 = Participantes[f'complementoP1']
        cidadeP1 = Participantes[f'cidadeP1']
        bairroP1 = Participantes[f'bairroP1']
        ufP1 = Participantes[f'estadoP1']
        cepP1 =Participantes[f'cepP1']
        nomeP2 = Participantes[f'nomeCompletoP2'] 
        emailP2 = Participantes[f'emailP2']
        participacaoP2 = Participantes[f'participacaoNaOperacaoP2']
        cpfP2 = Participantes[f'cpfP2']
        sexoP2 = Participantes[f'sexoP2']
        relacaoP2 = Participantes[f'relacaoDoP2']
        dataNascimentoP2 = Participantes[f'dataNascimentoP2']
        telefoneP2 = Participantes[f'telefoneP2']
        ruaP2 = Participantes[f'endereçoP2']
        numeroP2 = Participantes[f'numeroResidenciaP2']
        complementoP2 = Participantes[f'complementoP2']
        cidadeP2 = Participantes[f'cidadeP2']
        bairroP2 = Participantes[f'bairroP2']
        ufP2 = Participantes[f'estadoP2']
        cepP2 =Participantes[f'cepP2']
        nomeP3 = Participantes[f'nomeCompletoP3'] 
        emailP3 = Participantes[f'emailP3']
        participacaoP3 = Participantes[f'participacaoNaOperacaoP3']
        cpfP3 = Participantes[f'cpfP3']
        sexoP3 = Participantes[f'sexoP3']
        relacaoP3 = Participantes[f'relacaoDoP3']
        dataNascimentoP3 = Participantes[f'dataNascimentoP3']
        telefoneP3 = Participantes[f'telefoneP3']
        ruaP3 = Participantes[f'endereçoP3']
        numeroP3 = Participantes[f'numeroResidenciaP3']
        complementoP3 = Participantes[f'complementoP3']
        cidadeP3 = Participantes[f'cidadeP3']
        bairroP3 = Participantes[f'bairroP3']
        ufP3 = Participantes[f'estadoP3']
        cepP3 =Participantes[f'cepP3']
        nomeP4 = Participantes[f'nomeCompletoP4'] 
        emailP4 = Participantes[f'emailP4']
        participacaoP4 = Participantes[f'participacaoNaOperacaoP4']
        cpfP4 = Participantes[f'cpfP4']
        sexoP4 = Participantes[f'sexoP4']
        relacaoP4 = Participantes[f'relacaoDoP4']
        dataNascimentoP4 = Participantes[f'dataNascimentoP4']
        telefoneP4 = Participantes[f'telefoneP4']
        ruaP4 = Participantes[f'endereçoP4']
        numeroP4 = Participantes[f'numeroResidenciaP4']
        complementoP4 = Participantes[f'complementoP4']
        cidadeP4 = Participantes[f'cidadeP4']
        bairroP4 = Participantes[f'bairroP4']
        ufP4 = Participantes[f'estadoP4']
        cepP4 =Participantes[f'cepP4']
        nomeP5 = Participantes[f'nomeCompletoP5'] 
        emailP5 = Participantes[f'emailP5']
        participacaoP5 = Participantes[f'participacaoNaOperacaoP5']
        cpfP5 = Participantes[f'cpfP5']
        sexoP5 = Participantes[f'sexoP5']
        relacaoP5 = Participantes[f'relacaoDoP5']
        dataNascimentoP5 = Participantes[f'dataNascimentoP5']
        telefoneP5 = Participantes[f'telefoneP5']
        ruaP5 = Participantes[f'endereçoP5']
        numeroP5 = Participantes[f'numeroResidenciaP5']
        complementoP5 = Participantes[f'complementoP5']
        cidadeP5 = Participantes[f'cidadeP5']
        bairroP5 = Participantes[f'bairroP5']
        ufP5 = Participantes[f'estadoP5']
        cepP5 =Participantes[f'cepP5']
    elif contadorC == 6:
        nomeP1 = Participantes[f'nomeCompletoP1'] 
        emailP1 = Participantes[f'emailP1']
        participacaoP1 = Participantes[f'participacaoNaOperacaoP1']
        cpfP1 = Participantes[f'cpfP1']
        sexoP1 = Participantes[f'sexoP1']
        relacaoP1 = Participantes[f'relacaoDoP1']
        dataNascimentoP1 = Participantes[f'dataNascimentoP1']
        telefoneP1 = Participantes[f'telefoneP1']
        ruaP1 = Participantes[f'endereçoP1']
        numeroP1 = Participantes[f'numeroResidenciaP1']
        complementoP1 = Participantes[f'complementoP1']
        cidadeP1 = Participantes[f'cidadeP1']
        bairroP1 = Participantes[f'bairroP1']
        ufP1 = Participantes[f'estadoP1']
        cepP1 =Participantes[f'cepP1']
        nomeP2 = Participantes[f'nomeCompletoP2'] 
        emailP2 = Participantes[f'emailP2']
        participacaoP2 = Participantes[f'participacaoNaOperacaoP2']
        cpfP2 = Participantes[f'cpfP2']
        sexoP2 = Participantes[f'sexoP2']
        relacaoP2 = Participantes[f'relacaoDoP2']
        dataNascimentoP2 = Participantes[f'dataNascimentoP2']
        telefoneP2 = Participantes[f'telefoneP2']
        ruaP2 = Participantes[f'endereçoP2']
        numeroP2 = Participantes[f'numeroResidenciaP2']
        complementoP2 = Participantes[f'complementoP2']
        cidadeP2 = Participantes[f'cidadeP2']
        bairroP2 = Participantes[f'bairroP2']
        ufP2 = Participantes[f'estadoP2']
        cepP2 =Participantes[f'cepP2']
        nomeP3 = Participantes[f'nomeCompletoP3'] 
        emailP3 = Participantes[f'emailP3']
        participacaoP3 = Participantes[f'participacaoNaOperacaoP3']
        cpfP3 = Participantes[f'cpfP3']
        sexoP3 = Participantes[f'sexoP3']
        relacaoP3 = Participantes[f'relacaoDoP3']
        dataNascimentoP3 = Participantes[f'dataNascimentoP3']
        telefoneP3 = Participantes[f'telefoneP3']
        ruaP3 = Participantes[f'endereçoP3']
        numeroP3 = Participantes[f'numeroResidenciaP3']
        complementoP3 = Participantes[f'complementoP3']
        cidadeP3 = Participantes[f'cidadeP3']
        bairroP3 = Participantes[f'bairroP3']
        ufP3 = Participantes[f'estadoP3']
        cepP3 =Participantes[f'cepP3']
        nomeP4 = Participantes[f'nomeCompletoP4'] 
        emailP4 = Participantes[f'emailP4']
        participacaoP4 = Participantes[f'participacaoNaOperacaoP4']
        cpfP4 = Participantes[f'cpfP4']
        sexoP4 = Participantes[f'sexoP4']
        relacaoP4 = Participantes[f'relacaoDoP4']
        dataNascimentoP4 = Participantes[f'dataNascimentoP4']
        telefoneP4 = Participantes[f'telefoneP4']
        ruaP4 = Participantes[f'endereçoP4']
        numeroP4 = Participantes[f'numeroResidenciaP4']
        complementoP4 = Participantes[f'complementoP4']
        cidadeP4 = Participantes[f'cidadeP4']
        bairroP4 = Participantes[f'bairroP4']
        ufP4 = Participantes[f'estadoP4']
        cepP4 =Participantes[f'cepP4']
        nomeP5 = Participantes[f'nomeCompletoP5'] 
        emailP5 = Participantes[f'emailP5']
        participacaoP5 = Participantes[f'participacaoNaOperacaoP5']
        cpfP5 = Participantes[f'cpfP5']
        sexoP5 = Participantes[f'sexoP5']
        relacaoP5 = Participantes[f'relacaoDoP5']
        dataNascimentoP5 = Participantes[f'dataNascimentoP5']
        telefoneP5 = Participantes[f'telefoneP5']
        ruaP5 = Participantes[f'endereçoP5']
        numeroP5 = Participantes[f'numeroResidenciaP5']
        complementoP5 = Participantes[f'complementoP5']
        cidadeP5 = Participantes[f'cidadeP5']
        bairroP5 = Participantes[f'bairroP5']
        ufP5 = Participantes[f'estadoP5']
        cepP5 =Participantes[f'cepP5']
        nomeP6 = Participantes[f'nomeCompletoP6'] 
        emailP6 = Participantes[f'emailP6']
        participacaoP6 = Participantes[f'participacaoNaOperacaoP6']
        cpfP6 = Participantes[f'cpfP6']
        sexoP6 = Participantes[f'sexoP6']
        relacaoP6 = Participantes[f'relacaoDoP6']
        dataNascimentoP6 = Participantes[f'dataNascimentoP6']
        telefoneP6 = Participantes[f'telefoneP6']
        ruaP6 = Participantes[f'endereçoP6']
        numeroP6 = Participantes[f'numeroResidenciaP6']
        complementoP6 = Participantes[f'complementoP6']
        cidadeP6 = Participantes[f'cidadeP6']
        bairroP6 = Participantes[f'bairroP6']
        ufP6 = Participantes[f'estadoP6']
        cepP6 =Participantes[f'cepP6']
    elif contadorC == 7:
        nomeP1 = Participantes[f'nomeCompletoP1'] 
        emailP1 = Participantes[f'emailP1']
        participacaoP1 = Participantes[f'participacaoNaOperacaoP1']
        cpfP1 = Participantes[f'cpfP1']
        sexoP1 = Participantes[f'sexoP1']
        relacaoP1 = Participantes[f'relacaoDoP1']
        dataNascimentoP1 = Participantes[f'dataNascimentoP1']
        telefoneP1 = Participantes[f'telefoneP1']
        ruaP1 = Participantes[f'endereçoP1']
        numeroP1 = Participantes[f'numeroResidenciaP1']
        complementoP1 = Participantes[f'complementoP1']
        cidadeP1 = Participantes[f'cidadeP1']
        bairroP1 = Participantes[f'bairroP1']
        ufP1 = Participantes[f'estadoP1']
        cepP1 = Participantes[f'cepP1']
        nomeP2 = Participantes[f'nomeCompletoP2'] 
        emailP2 = Participantes[f'emailP2']
        participacaoP2 = Participantes[f'participacaoNaOperacaoP2']
        cpfP2 = Participantes[f'cpfP2']
        sexoP2 = Participantes[f'sexoP2']
        relacaoP2 = Participantes[f'relacaoDoP2']
        dataNascimentoP2 = Participantes[f'dataNascimentoP2']
        telefoneP2 = Participantes[f'telefoneP2']
        ruaP2 = Participantes[f'endereçoP2']
        numeroP2 = Participantes[f'numeroResidenciaP2']
        complementoP2 = Participantes[f'complementoP2']
        cidadeP2 = Participantes[f'cidadeP2']
        bairroP2 = Participantes[f'bairroP2']
        ufP2 = Participantes[f'estadoP2']
        cepP2 = Participantes[f'cepP2']
        nomeP3 = Participantes[f'nomeCompletoP3'] 
        emailP3 = Participantes[f'emailP3']
        participacaoP3 = Participantes[f'participacaoNaOperacaoP3']
        cpfP3 = Participantes[f'cpfP3']
        sexoP3 = Participantes[f'sexoP3']
        relacaoP3 = Participantes[f'relacaoDoP3']
        dataNascimentoP3 = Participantes[f'dataNascimentoP3']
        telefoneP3 = Participantes[f'telefoneP3']
        ruaP3 = Participantes[f'endereçoP3']
        numeroP3 = Participantes[f'numeroResidenciaP3']
        complementoP3 = Participantes[f'complementoP3']
        cidadeP3 = Participantes[f'cidadeP3']
        bairroP3 = Participantes[f'bairroP3']
        ufP3 = Participantes[f'estadoP3']
        cepP3 = Participantes[f'cepP3']
        nomeP4 = Participantes[f'nomeCompletoP4'] 
        emailP4 = Participantes[f'emailP4']
        participacaoP4 = Participantes[f'participacaoNaOperacaoP4']
        cpfP4 = Participantes[f'cpfP4']
        sexoP4 = Participantes[f'sexoP4']
        relacaoP4 = Participantes[f'relacaoDoP4']
        dataNascimentoP4 = Participantes[f'dataNascimentoP4']
        telefoneP4 = Participantes[f'telefoneP4']
        ruaP4 = Participantes[f'endereçoP4']
        numeroP4 = Participantes[f'numeroResidenciaP4']
        complementoP4 = Participantes[f'complementoP4']
        cidadeP4 = Participantes[f'cidadeP4']
        bairroP4 = Participantes[f'bairroP4']
        ufP4 = Participantes[f'estadoP4']
        cepP4 = Participantes[f'cepP4']
        nomeP5 = Participantes[f'nomeCompletoP5'] 
        emailP5 = Participantes[f'emailP5']
        participacaoP5 = Participantes[f'participacaoNaOperacaoP5']
        cpfP5 = Participantes[f'cpfP5']
        sexoP5 = Participantes[f'sexoP5']
        relacaoP5 = Participantes[f'relacaoDoP5']
        dataNascimentoP5 = Participantes[f'dataNascimentoP5']
        telefoneP5 = Participantes[f'telefoneP5']
        ruaP5 = Participantes[f'endereçoP5']
        numeroP5 = Participantes[f'numeroResidenciaP5']
        complementoP5 = Participantes[f'complementoP5']
        cidadeP5 = Participantes[f'cidadeP5']
        bairroP5 = Participantes[f'bairroP5']
        ufP5 = Participantes[f'estadoP5']
        cepP5 = Participantes[f'cepP5']
        nomeP6 = Participantes[f'nomeCompletoP6'] 
        emailP6 = Participantes[f'emailP6']
        participacaoP6 = Participantes[f'participacaoNaOperacaoP6']
        cpfP6 = Participantes[f'cpfP6']
        sexoP6 = Participantes[f'sexoP6']
        relacaoP6 = Participantes[f'relacaoDoP6']
        dataNascimentoP6 = Participantes[f'dataNascimentoP6']
        telefoneP6 = Participantes[f'telefoneP6']
        ruaP6 = Participantes[f'endereçoP6']
        numeroP6 = Participantes[f'numeroResidenciaP6']
        complementoP6 = Participantes[f'complementoP6']
        cidadeP6 = Participantes[f'cidadeP6']
        bairroP6 = Participantes[f'bairroP6']
        ufP6 = Participantes[f'estadoP6']
        cepP6 = Participantes[f'cepP6']
        nomeP7 = Participantes[f'nomeCompletoP7'] 
        emailP7 = Participantes[f'emailP7']
        participacaoP7 = Participantes[f'participacaoNaOperacaoP7']
        cpfP7 = Participantes[f'cpfP7']
        sexoP7 = Participantes[f'sexoP7']
        relacaoP7 = Participantes[f'relacaoDoP7']
        dataNascimentoP7 = Participantes[f'dataNascimentoP7']
        telefoneP7 = Participantes[f'telefoneP7']
        ruaP7 = Participantes[f'endereçoP7']
        numeroP7 = Participantes[f'numeroResidenciaP7']
        complementoP7 = Participantes[f'complementoP7']
        cidadeP7 = Participantes[f'cidadeP7']
        bairroP7 = Participantes[f'bairroP7']
        ufP7 = Participantes[f'estadoP7']
        cepP7 = Participantes[f'cepP7']
    else:
        print("há mais de 7 participantes ou menos de 1. Entrar em contato com a WAQ Corporetion")



    ### Abrir Front-End da API ###

    # ChromeDriver
    driver = webdriver.Chrome(executable_path=r'G:\Drives compartilhados\Pontte\Operações\Automações\Scripts\Pontte\Driver\chromedriver.exe')

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

    # Preenchendo participantes
    if contadorC == 1:
        nomeParticipantes1 = driver.find_element('xpath',f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[3]/input')
        emailParticipantes1 = driver.find_element('xpath',f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[4]/input')
        participação1 = driver.find_element('xpath',f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[5]/input')
        cnpjCpf1 = driver.find_element('xpath',f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[6]/input')
        sexo1 = driver.find_element('xpath',f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[8]/input')
        relacao1 = driver.find_element('xpath',f'/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select')
        dataNacimento1 = driver.find_element('xpath',f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[9]/input')
        telefone1 = driver.find_element('xpath',f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[10]/input')
        ruaParticipantes1 = driver.find_element('xpath',f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[11]/input')
        numeroParticipantes1 = driver.find_element('xpath',f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[12]/input')
        complementoParticipantes1 = driver.find_element('xpath',f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[13]/input')
        cidadeParticipantes1 = driver.find_element('xpath',f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[14]/input')
        bairroParticipantes1 = driver.find_element('xpath',f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[15]/input')
        ufParticipantes1 = driver.find_element('xpath',f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[16]/input')
        cepParticipantes1 = driver.find_element('xpath',f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[17]/input')
        # Limpar campos
        limparCampo(nomeParticipantes1)
        limparCampo(emailParticipantes1)
        limparCampo(participação1)
        limparCampo(cnpjCpf1)
        limparCampo(sexo1)
        limparCampo(dataNacimento1)
        limparCampo(telefone1)
        limparCampo(ruaParticipantes1)
        limparCampo(numeroParticipantes1)
        limparCampo(complementoParticipantes1)
        limparCampo(cidadeParticipantes1)
        limparCampo(bairroParticipantes1)
        limparCampo(ufParticipantes1)
        limparCampo(cepParticipantes1)
        sleep(1)

        nomeParticipantes1.send_keys(nomeP1)
        emailParticipantes1.send_keys(emailP1)
        participação1.send_keys(participacaoP1)
        cnpjCpf1.send_keys(cpfP1)
        sexo1.send_keys(sexoP1)
        relacao1.click()
        if relacaoP1 == 'Titular': relacaoP = driver.find_element('xpath','/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select/option[2]')
        elif relacaoP1 == 'Cônjuge': relacaoP = driver.find_element('xpath','/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select/option[3]')
        elif relacaoP1 == 'Procurador': relacaoP = driver.find_element('xpath','/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select/option[4]')
        elif relacaoP1 == 'Pai': relacaoP = driver.find_element('xpath','/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select/option[5]')
        elif relacaoP1 == 'Mãe': relacaoP = driver.find_element('xpath','/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select/option[6]')
        elif relacaoP1 == 'Irmão': relacaoP = driver.find_element('xpath','/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select/option[7]')
        dataNacimento1.send_keys(dataNascimentoP1)
        telefone1.send_keys(telefoneP1)
        ruaParticipantes1.send_keys(ruaP1)
        numeroParticipantes1.send_keys(numeroP1)
        complementoParticipantes1.send_keys(complementoP1)
        cidadeParticipantes1.send_keys(cidadeP1)
        bairroParticipantes1.send_keys(bairroP1)
        ufParticipantes1.send_keys(ufP1)
        cepParticipantes1.send_keys(cepP1)
        sleep(1)

    elif contadorC == 2:
        nomeParticipantes1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[3]/input')
        emailParticipantes1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[4]/input')
        participação1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[5]/input')
        cnpjCpf1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[6]/input')
        sexo1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[8]/input')
        relacao1 = driver.find_element_by_xpath(f'/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select')
        dataNacimento1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[9]/input')
        telefone1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[10]/input')
        ruaParticipantes1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[11]/input')
        numeroParticipantes1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[12]/input')
        complementoParticipantes1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[13]/input')
        cidadeParticipantes1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[14]/input')
        bairroParticipantes1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[15]/input')
        ufParticipantes1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[16]/input')
        cepParticipantes1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[17]/input')

        nomeParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[3]/input')
        emailParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[4]/input')
        participação2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[5]/input')
        cnpjCpf2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[6]/input')
        sexo2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[8]/input')
        relacao2 = driver.find_element_by_xpath(f'/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select')
        dataNacimento2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[9]/input')
        telefone2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[10]/input')
        ruaParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[11]/input')
        numeroParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[12]/input')
        complementoParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[13]/input')
        cidadeParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[14]/input')
        bairroParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[15]/input')
        ufParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[16]/input')
        cepParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[17]/input')

         # Limpar campos
        limparCampo(nomeParticipantes1)
        limparCampo(emailParticipantes1)
        limparCampo(participação1)
        limparCampo(cnpjCpf1)
        limparCampo(sexo1)
        limparCampo(dataNacimento1)
        limparCampo(telefone1)
        limparCampo(ruaParticipantes1)
        limparCampo(numeroParticipantes1)
        limparCampo(complementoParticipantes1)
        limparCampo(cidadeParticipantes1)
        limparCampo(bairroParticipantes1)
        limparCampo(ufParticipantes1)
        limparCampo(cepParticipantes1)
        sleep(1)
         
        limparCampo(nomeParticipantes2)
        limparCampo(emailParticipantes2)
        limparCampo(participação2)
        limparCampo(cnpjCpf2)
        limparCampo(sexo2)
        limparCampo(dataNacimento2)
        limparCampo(telefone2)
        limparCampo(ruaParticipantes2)
        limparCampo(numeroParticipantes2)
        limparCampo(complementoParticipantes2)
        limparCampo(cidadeParticipantes2)
        limparCampo(bairroParticipantes2)
        limparCampo(ufParticipantes2)
        limparCampo(cepParticipantes2)
        sleep(1)

        nomeParticipantes1.send_keys(nomeP1)
        emailParticipantes1.send_keys(emailP1)
        participação1.send_keys(participacaoP1)
        cnpjCpf1.send_keys(cpfP1)
        sexo1.send_keys(sexoP1)
        relacao1.click()
        if relacaoP1 == 'Titular': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select/option[2]')
        elif relacaoP1 == 'Cônjuge': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select/option[3]')
        elif relacaoP1 == 'Procurador': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select/option[4]')
        elif relacaoP1 == 'Pai': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select/option[5]')
        elif relacaoP1 == 'Mãe': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select/option[6]')
        elif relacaoP1 == 'Irmão': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select/option[7]')
        dataNacimento1.send_keys(dataNascimentoP1)
        telefone1.send_keys(telefoneP1)
        ruaParticipantes1.send_keys(ruaP1)
        numeroParticipantes1.send_keys(numeroP1)
        complementoParticipantes1.send_keys(complementoP1)
        cidadeParticipantes1.send_keys(cidadeP1)
        bairroParticipantes1.send_keys(bairroP1)
        ufParticipantes1.send_keys(ufP1)
        cepParticipantes1.send_keys(cepP1)
        sleep(1)

        nomeParticipantes2.send_keys(nomeP2)
        emailParticipantes2.send_keys(emailP2)
        participação2.send_keys(participacaoP2)
        cnpjCpf2.send_keys(cpfP2)
        sexo2.send_keys(sexoP2)
        relacao2.click()
        if relacaoP2 == 'Titular': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[4]/div/label[2]/select/option[2]')
        elif relacaoP2 == 'Cônjuge': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[4]/div/label[2]/select/option[3]')
        elif relacaoP2 == 'Procurador': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[4]/div/label[2]/select/option[4]')
        elif relacaoP2 == 'Pai': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[4]/div/label[2]/select/option[5]')
        elif relacaoP2 == 'Mãe': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[4]/div/label[2]/select/option[6]')
        elif relacaoP2 == 'Irmão': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[4]/div/label[2]/select/option[7]')
        dataNacimento2.send_keys(dataNascimentoP2)
        telefone2.send_keys(telefoneP2)
        ruaParticipantes2.send_keys(ruaP2)
        numeroParticipantes2.send_keys(numeroP2)
        complementoParticipantes2.send_keys(complementoP2)
        cidadeParticipantes2.send_keys(cidadeP2)
        bairroParticipantes2.send_keys(bairroP2)
        ufParticipantes2.send_keys(ufP2)
        cepParticipantes2.send_keys(cepP2)
        sleep(1)
    
    elif contadorC == 3:
        nomeParticipantes1 = driver.find_element('xpath',f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[3]/input')
        emailParticipantes1 = driver.find_element('xpath',f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[4]/input')
        participação1 = driver.find_element('xpath',f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[5]/input')
        cnpjCpf1 = driver.find_element('xpath',f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[6]/input')
        sexo1 = driver.find_element('xpath',f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[8]/input')
        relacao1 = driver.find_element('xpath',f'/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select')
        dataNacimento1 = driver.find_element('xpath',f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[9]/input')
        telefone1 = driver.find_element('xpath',f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[10]/input')
        ruaParticipantes1 = driver.find_element('xpath',f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[11]/input')
        numeroParticipantes1 = driver.find_element('xpath',f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[12]/input')
        complementoParticipantes1 = driver.find_element('xpath',f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[13]/input')
        cidadeParticipantes1 = driver.find_element('xpath',f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[14]/input')
        bairroParticipantes1 = driver.find_element('xpath',f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[15]/input')
        ufParticipantes1 = driver.find_element('xpath',f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[16]/input')
        cepParticipantes1 = driver.find_element('xpath',f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[17]/input')

        nomeParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[3]/input')
        emailParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[4]/input')
        participação2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[5]/input')
        cnpjCpf2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[6]/input')
        sexo2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[8]/input')
        relacao2 = driver.find_element_by_xpath(f'/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select')
        dataNacimento2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[9]/input')
        telefone2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[10]/input')
        ruaParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[11]/input')
        numeroParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[12]/input')
        complementoParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[13]/input')
        cidadeParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[14]/input')
        bairroParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[15]/input')
        ufParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[16]/input')
        cepParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[17]/input')

        nomeParticipantes3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[3]/input')
        emailParticipantes3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[4]/input')
        participação3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[5]/input')
        cnpjCpf3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[6]/input')
        sexo3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[8]/input')
        relacao3 = driver.find_element_by_xpath(f'/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select')
        dataNacimento3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[9]/input')
        telefone3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[10]/input')
        ruaParticipantes3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[11]/input')
        numeroParticipantes3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[12]/input')
        complementoParticipantes3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[13]/input')
        cidadeParticipantes3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[14]/input')
        bairroParticipantes3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[15]/input')
        ufParticipantes3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[16]/input')
        cepParticipantes3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[17]/input')

         # Limpar campos
        limparCampo(nomeParticipantes1)
        limparCampo(emailParticipantes1)
        limparCampo(participação1)
        limparCampo(cnpjCpf1)
        limparCampo(sexo1)
        limparCampo(dataNacimento1)
        limparCampo(telefone1)
        limparCampo(ruaParticipantes1)
        limparCampo(numeroParticipantes1)
        limparCampo(complementoParticipantes1)
        limparCampo(cidadeParticipantes1)
        limparCampo(bairroParticipantes1)
        limparCampo(ufParticipantes1)
        limparCampo(cepParticipantes1)
        sleep(1)

        limparCampo(nomeParticipantes2)
        limparCampo(emailParticipantes2)
        limparCampo(participação2)
        limparCampo(cnpjCpf2)
        limparCampo(sexo2)
        limparCampo(dataNacimento2)
        limparCampo(telefone2)
        limparCampo(ruaParticipantes2)
        limparCampo(numeroParticipantes2)
        limparCampo(complementoParticipantes2)
        limparCampo(cidadeParticipantes2)
        limparCampo(bairroParticipantes2)
        limparCampo(ufParticipantes2)
        limparCampo(cepParticipantes2)
        sleep(1)

        limparCampo(nomeParticipantes3)
        limparCampo(emailParticipantes3)
        limparCampo(participação3)
        limparCampo(cnpjCpf3)
        limparCampo(sexo3)
        limparCampo(dataNacimento3)
        limparCampo(telefone3)
        limparCampo(ruaParticipantes3)
        limparCampo(numeroParticipantes3)
        limparCampo(complementoParticipantes3)
        limparCampo(cidadeParticipantes3)
        limparCampo(bairroParticipantes3)
        limparCampo(ufParticipantes3)
        limparCampo(cepParticipantes3)
        sleep(1)

        nomeParticipantes1.send_keys(nomeP1)
        emailParticipantes1.send_keys(emailP1)
        participação1.send_keys(participacaoP1)
        cnpjCpf1.send_keys(cpfP1)
        sexo1.send_keys(sexoP1)
        relacao1.click()
        if relacaoP1 == 'Titular': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select/option[2]')
        elif relacaoP1 == 'Cônjuge': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select/option[3]')
        elif relacaoP1 == 'Procurador': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select/option[4]')
        elif relacaoP1 == 'Pai': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select/option[5]')
        elif relacaoP1 == 'Mãe': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select/option[6]')
        elif relacaoP1 == 'Irmão': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select/option[7]')
        dataNacimento1.send_keys(dataNascimentoP1)
        telefone1.send_keys(telefoneP1)
        ruaParticipantes1.send_keys(ruaP1)
        numeroParticipantes1.send_keys(numeroP1)
        complementoParticipantes1.send_keys(complementoP1)
        cidadeParticipantes1.send_keys(cidadeP1)
        bairroParticipantes1.send_keys(bairroP1)
        ufParticipantes1.send_keys(ufP1)
        cepParticipantes1.send_keys(cepP1)
        sleep(1)

        nomeParticipantes2.send_keys(nomeP2)
        emailParticipantes2.send_keys(emailP2)
        participação2.send_keys(participacaoP2)
        cnpjCpf2.send_keys(cpfP2)
        sexo2.send_keys(sexoP2)
        relacao2.click()
        if relacaoP2 == 'Titular': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[4]/div/label[2]/select/option[2]')
        elif relacaoP2 == 'Cônjuge': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[4]/div/label[2]/select/option[3]')
        elif relacaoP2 == 'Procurador': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[4]/div/label[2]/select/option[4]')
        elif relacaoP2 == 'Pai': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[4]/div/label[2]/select/option[5]')
        elif relacaoP2 == 'Mãe': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[4]/div/label[2]/select/option[6]')
        elif relacaoP2 == 'Irmão': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[4]/div/label[2]/select/option[7]')
        dataNacimento2.send_keys(dataNascimentoP2)
        telefone2.send_keys(telefoneP2)
        ruaParticipantes2.send_keys(ruaP2)
        numeroParticipantes2.send_keys(numeroP2)
        complementoParticipantes2.send_keys(complementoP2)
        cidadeParticipantes2.send_keys(cidadeP2)
        bairroParticipantes2.send_keys(bairroP2)
        ufParticipantes2.send_keys(ufP2)
        cepParticipantes2.send_keys(cepP2)
        sleep(1)

        nomeParticipantes3.send_keys(nomeP3)
        emailParticipantes3.send_keys(emailP3)
        participação3.send_keys(participacaoP3)
        cnpjCpf3.send_keys(cpfP3)
        sexo3.send_keys(sexoP3)
        relacao3.click()
        if relacaoP3 == 'Titular': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[5]/div/label[2]/select/option[2]')
        elif relacaoP3 == 'Cônjuge': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[5]/div/label[2]/select/option[3]')
        elif relacaoP3 == 'Procurador': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[5]/div/label[2]/select/option[4]')
        elif relacaoP3 == 'Pai': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[5]/div/label[2]/select/option[5]')
        elif relacaoP3 == 'Mãe': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[5]/div/label[2]/select/option[6]')
        elif relacaoP3 == 'Irmão': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[5]/div/label[2]/select/option[7]')
        dataNacimento3.send_keys(dataNascimentoP3)
        telefone3.send_keys(telefoneP3)
        ruaParticipantes3.send_keys(ruaP3)
        numeroParticipantes3.send_keys(numeroP3)
        complementoParticipantes3.send_keys(complementoP3)
        cidadeParticipantes3.send_keys(cidadeP3)
        bairroParticipantes3.send_keys(bairroP3)
        ufParticipantes3.send_keys(ufP3)
        cepParticipantes3.send_keys(cepP3)
        sleep(1)
    
    elif contadorC == 4:
        nomeParticipantes1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[3]/input')
        emailParticipantes1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[4]/input')
        participação1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[5]/input')
        cnpjCpf1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[6]/input')
        sexo1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[8]/input')
        relacao1 = driver.find_element_by_xpath(f'/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select')
        dataNacimento1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[9]/input')
        telefone1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[10]/input')
        ruaParticipantes1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[11]/input')
        numeroParticipantes1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[12]/input')
        complementoParticipantes1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[13]/input')
        cidadeParticipantes1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[14]/input')
        bairroParticipantes1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[15]/input')
        ufParticipantes1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[16]/input')
        cepParticipantes1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[17]/input')

        nomeParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[3]/input')
        emailParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[4]/input')
        participação2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[5]/input')
        cnpjCpf2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[6]/input')
        sexo2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[8]/input')
        relacao2 = driver.find_element_by_xpath(f'/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select')
        dataNacimento2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[9]/input')
        telefone2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[10]/input')
        ruaParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[11]/input')
        numeroParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[12]/input')
        complementoParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[13]/input')
        cidadeParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[14]/input')
        bairroParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[15]/input')
        ufParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[16]/input')
        cepParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[17]/input')

        nomeParticipantes3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[3]/input')
        emailParticipantes3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[4]/input')
        participação3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[5]/input')
        cnpjCpf3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[6]/input')
        sexo3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[8]/input')
        relacao3 = driver.find_element_by_xpath(f'/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select')
        dataNacimento3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[9]/input')
        telefone3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[10]/input')
        ruaParticipantes3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[11]/input')
        numeroParticipantes3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[12]/input')
        complementoParticipantes3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[13]/input')
        cidadeParticipantes3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[14]/input')
        bairroParticipantes3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[15]/input')
        ufParticipantes3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[16]/input')
        cepParticipantes3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[17]/input')

        nomeParticipantes4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[3]/input')
        emailParticipantes4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[4]/input')
        participação4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[5]/input')
        cnpjCpf4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[6]/input')
        sexo4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[8]/input')
        relacao4 = driver.find_element_by_xpath(f'/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select')
        dataNacimento4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[9]/input')
        telefone4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[10]/input')
        ruaParticipantes4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[11]/input')
        numeroParticipantes4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[12]/input')
        complementoParticipantes4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[13]/input')
        cidadeParticipantes4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[14]/input')
        bairroParticipantes4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[15]/input')
        ufParticipantes4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[16]/input')
        cepParticipantes4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[17]/input')
         # Limpar campos
        limparCampo(nomeParticipantes1)
        limparCampo(emailParticipantes1)
        limparCampo(participação1)
        limparCampo(cnpjCpf1)
        limparCampo(sexo1)
        limparCampo(dataNacimento1)
        limparCampo(telefone1)
        limparCampo(ruaParticipantes1)
        limparCampo(numeroParticipantes1)
        limparCampo(complementoParticipantes1)
        limparCampo(cidadeParticipantes1)
        limparCampo(bairroParticipantes1)
        limparCampo(ufParticipantes1)
        limparCampo(cepParticipantes1)
        sleep(1)

        limparCampo(nomeParticipantes2)
        limparCampo(emailParticipantes2)
        limparCampo(participação2)
        limparCampo(cnpjCpf2)
        limparCampo(sexo2)
        limparCampo(dataNacimento2)
        limparCampo(telefone2)
        limparCampo(ruaParticipantes2)
        limparCampo(numeroParticipantes2)
        limparCampo(complementoParticipantes2)
        limparCampo(cidadeParticipantes2)
        limparCampo(bairroParticipantes2)
        limparCampo(ufParticipantes2)
        limparCampo(cepParticipantes2)
        sleep(1)

        limparCampo(nomeParticipantes3)
        limparCampo(emailParticipantes3)
        limparCampo(participação3)
        limparCampo(cnpjCpf3)
        limparCampo(sexo3)
        limparCampo(dataNacimento3)
        limparCampo(telefone3)
        limparCampo(ruaParticipantes3)
        limparCampo(numeroParticipantes3)
        limparCampo(complementoParticipantes3)
        limparCampo(cidadeParticipantes3)
        limparCampo(bairroParticipantes3)
        limparCampo(ufParticipantes3)
        limparCampo(cepParticipantes3)
        sleep(1)

        limparCampo(nomeParticipantes4)
        limparCampo(emailParticipantes4)
        limparCampo(participação4)
        limparCampo(cnpjCpf4)
        limparCampo(sexo4)
        limparCampo(dataNacimento4)
        limparCampo(telefone4)
        limparCampo(ruaParticipantes4)
        limparCampo(numeroParticipantes4)
        limparCampo(complementoParticipantes4)
        limparCampo(cidadeParticipantes4)
        limparCampo(bairroParticipantes4)
        limparCampo(ufParticipantes4)
        limparCampo(cepParticipantes4)
        sleep(1)

        nomeParticipantes1.send_keys(nomeP1)
        emailParticipantes1.send_keys(emailP1)
        participação1.send_keys(participacaoP1)
        cnpjCpf1.send_keys(cpfP1)
        sexo1.send_keys(sexoP1)
        relacao1.click()
        if relacaoP1 == 'Titular': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select/option[2]')
        elif relacaoP1 == 'Cônjuge': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select/option[3]')
        elif relacaoP1 == 'Procurador': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select/option[4]')
        elif relacaoP1 == 'Pai': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select/option[5]')
        elif relacaoP1 == 'Mãe': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select/option[6]')
        elif relacaoP1 == 'Irmão': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select/option[7]')
        dataNacimento1.send_keys(dataNascimentoP1)
        telefone1.send_keys(telefoneP1)
        ruaParticipantes1.send_keys(ruaP1)
        numeroParticipantes1.send_keys(numeroP1)
        complementoParticipantes1.send_keys(complementoP1)
        cidadeParticipantes1.send_keys(cidadeP1)
        bairroParticipantes1.send_keys(bairroP1)
        ufParticipantes1.send_keys(ufP1)
        cepParticipantes1.send_keys(cepP1)
        sleep(1)

        nomeParticipantes2.send_keys(nomeP2)
        emailParticipantes2.send_keys(emailP2)
        participação2.send_keys(participacaoP2)
        cnpjCpf2.send_keys(cpfP2)
        sexo2.send_keys(sexoP2)
        relacao2.click()
        if relacaoP2 == 'Titular': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[4]/div/label[2]/select/option[2]')
        elif relacaoP2 == 'Cônjuge': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[4]/div/label[2]/select/option[3]')
        elif relacaoP2 == 'Procurador': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[4]/div/label[2]/select/option[4]')
        elif relacaoP2 == 'Pai': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[4]/div/label[2]/select/option[5]')
        elif relacaoP2 == 'Mãe': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[4]/div/label[2]/select/option[6]')
        elif relacaoP2 == 'Irmão': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[4]/div/label[2]/select/option[7]')
        dataNacimento2.send_keys(dataNascimentoP2)
        telefone2.send_keys(telefoneP2)
        ruaParticipantes2.send_keys(ruaP2)
        numeroParticipantes2.send_keys(numeroP2)
        complementoParticipantes2.send_keys(complementoP2)
        cidadeParticipantes2.send_keys(cidadeP2)
        bairroParticipantes2.send_keys(bairroP2)
        ufParticipantes2.send_keys(ufP2)
        cepParticipantes2.send_keys(cepP2)
        sleep(1)

        nomeParticipantes3.send_keys(nomeP3)
        emailParticipantes3.send_keys(emailP3)
        participação3.send_keys(participacaoP3)
        cnpjCpf3.send_keys(cpfP3)
        sexo3.send_keys(sexoP3)
        relacao3.click()
        if relacaoP3 == 'Titular': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[5]/div/label[2]/select/option[2]')
        elif relacaoP3 == 'Cônjuge': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[5]/div/label[2]/select/option[3]')
        elif relacaoP3 == 'Procurador': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[5]/div/label[2]/select/option[4]')
        elif relacaoP3 == 'Pai': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[5]/div/label[2]/select/option[5]')
        elif relacaoP3 == 'Mãe': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[5]/div/label[2]/select/option[6]')
        elif relacaoP3 == 'Irmão': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[5]/div/label[2]/select/option[7]')
        dataNacimento3.send_keys(dataNascimentoP3)
        telefone3.send_keys(telefoneP3)
        ruaParticipantes3.send_keys(ruaP3)
        numeroParticipantes3.send_keys(numeroP3)
        complementoParticipantes3.send_keys(complementoP3)
        cidadeParticipantes3.send_keys(cidadeP3)
        bairroParticipantes3.send_keys(bairroP3)
        ufParticipantes3.send_keys(ufP3)
        cepParticipantes3.send_keys(cepP3)
        sleep(1)

        nomeParticipantes4.send_keys(nomeP4)
        emailParticipantes4.send_keys(emailP4)
        participação4.send_keys(participacaoP4)
        cnpjCpf4.send_keys(cpfP4)
        sexo4.send_keys(sexoP4)
        relacao4.click()
        if relacaoP4 == 'Titular': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[6]/div/label[2]/select/option[2]')
        elif relacaoP4 == 'Cônjuge': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[6]/div/label[2]/select/option[3]')
        elif relacaoP4 == 'Procurador': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[6]/div/label[2]/select/option[4]')
        elif relacaoP4 == 'Pai': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[6]/div/label[2]/select/option[5]')
        elif relacaoP4 == 'Mãe': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[6]/div/label[2]/select/option[6]')
        elif relacaoP4 == 'Irmão': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[6]/div/label[2]/select/option[7]')
        dataNacimento4.send_keys(dataNascimentoP4)
        telefone4.send_keys(telefoneP4)
        ruaParticipantes4.send_keys(ruaP4)
        numeroParticipantes4.send_keys(numeroP4)
        complementoParticipantes4.send_keys(complementoP4)
        cidadeParticipantes4.send_keys(cidadeP4)
        bairroParticipantes4.send_keys(bairroP4)
        ufParticipantes4.send_keys(ufP4)
        cepParticipantes4.send_keys(cepP4)
        sleep(1)  
    
    elif contadorC == 5:
        nomeParticipantes1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[3]/input')
        emailParticipantes1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[4]/input')
        participação1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[5]/input')
        cnpjCpf1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[6]/input')
        sexo1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[8]/input')
        relacao1 = driver.find_element_by_xpath(f'/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select')
        dataNacimento1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[9]/input')
        telefone1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[10]/input')
        ruaParticipantes1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[11]/input')
        numeroParticipantes1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[12]/input')
        complementoParticipantes1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[13]/input')
        cidadeParticipantes1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[14]/input')
        bairroParticipantes1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[15]/input')
        ufParticipantes1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[16]/input')
        cepParticipantes1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[17]/input')

        nomeParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[3]/input')
        emailParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[4]/input')
        participação2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[5]/input')
        cnpjCpf2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[6]/input')
        sexo2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[8]/input')
        relacao2 = driver.find_element_by_xpath(f'/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select')
        dataNacimento2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[9]/input')
        telefone2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[10]/input')
        ruaParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[11]/input')
        numeroParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[12]/input')
        complementoParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[13]/input')
        cidadeParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[14]/input')
        bairroParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[15]/input')
        ufParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[16]/input')
        cepParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[17]/input')

        nomeParticipantes3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[3]/input')
        emailParticipantes3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[4]/input')
        participação3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[5]/input')
        cnpjCpf3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[6]/input')
        sexo3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[8]/input')
        relacao3 = driver.find_element_by_xpath(f'/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select')
        dataNacimento3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[9]/input')
        telefone3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[10]/input')
        ruaParticipantes3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[11]/input')
        numeroParticipantes3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[12]/input')
        complementoParticipantes3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[13]/input')
        cidadeParticipantes3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[14]/input')
        bairroParticipantes3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[15]/input')
        ufParticipantes3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[16]/input')
        cepParticipantes3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[17]/input')

        nomeParticipantes4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[3]/input')
        emailParticipantes4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[4]/input')
        participação4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[5]/input')
        cnpjCpf4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[6]/input')
        sexo4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[8]/input')
        relacao4 = driver.find_element_by_xpath(f'/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select')
        dataNacimento4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[9]/input')
        telefone4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[10]/input')
        ruaParticipantes4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[11]/input')
        numeroParticipantes4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[12]/input')
        complementoParticipantes4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[13]/input')
        cidadeParticipantes4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[14]/input')
        bairroParticipantes4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[15]/input')
        ufParticipantes4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[16]/input')
        cepParticipantes4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[17]/input')

        nomeParticipantes5 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[7]/div/label[3]/input')
        emailParticipantes5 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[7]/div/label[4]/input')
        participação5 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[7]/div/label[5]/input')
        cnpjCpf5 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[7]/div/label[6]/input')
        sexo5 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[7]/div/label[8]/input')
        relacao5 = driver.find_element_by_xpath(f'/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select')
        dataNacimento5 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[7]/div/label[9]/input')
        telefone5 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[7]/div/label[10]/input')
        ruaParticipantes5 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[7]/div/label[11]/input')
        numeroParticipantes5 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[7]/div/label[12]/input')
        complementoParticipantes5 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[7]/div/label[13]/input')
        cidadeParticipantes5 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[7]/div/label[14]/input')
        bairroParticipantes5 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[7]/div/label[15]/input')
        ufParticipantes5 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[7]/div/label[16]/input')
        cepParticipantes5 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[7]/div/label[17]/input')

         # Limpar campos
        limparCampo(nomeParticipantes1)
        limparCampo(emailParticipantes1)
        limparCampo(participação1)
        limparCampo(cnpjCpf1)
        limparCampo(sexo1)
        limparCampo(dataNacimento1)
        limparCampo(telefone1)
        limparCampo(ruaParticipantes1)
        limparCampo(numeroParticipantes1)
        limparCampo(complementoParticipantes1)
        limparCampo(cidadeParticipantes1)
        limparCampo(bairroParticipantes1)
        limparCampo(ufParticipantes1)
        limparCampo(cepParticipantes1)
        sleep(1)

        limparCampo(nomeParticipantes2)
        limparCampo(emailParticipantes2)
        limparCampo(participação2)
        limparCampo(cnpjCpf2)
        limparCampo(sexo2)
        limparCampo(dataNacimento2)
        limparCampo(telefone2)
        limparCampo(ruaParticipantes2)
        limparCampo(numeroParticipantes2)
        limparCampo(complementoParticipantes2)
        limparCampo(cidadeParticipantes2)
        limparCampo(bairroParticipantes2)
        limparCampo(ufParticipantes2)
        limparCampo(cepParticipantes2)
        sleep(1)

        limparCampo(nomeParticipantes3)
        limparCampo(emailParticipantes3)
        limparCampo(participação3)
        limparCampo(cnpjCpf3)
        limparCampo(sexo3)
        limparCampo(dataNacimento3)
        limparCampo(telefone3)
        limparCampo(ruaParticipantes3)
        limparCampo(numeroParticipantes3)
        limparCampo(complementoParticipantes3)
        limparCampo(cidadeParticipantes3)
        limparCampo(bairroParticipantes3)
        limparCampo(ufParticipantes3)
        limparCampo(cepParticipantes3)
        sleep(1)

        limparCampo(nomeParticipantes4)
        limparCampo(emailParticipantes4)
        limparCampo(participação4)
        limparCampo(cnpjCpf4)
        limparCampo(sexo4)
        limparCampo(dataNacimento4)
        limparCampo(telefone4)
        limparCampo(ruaParticipantes4)
        limparCampo(numeroParticipantes4)
        limparCampo(complementoParticipantes4)
        limparCampo(cidadeParticipantes4)
        limparCampo(bairroParticipantes4)
        limparCampo(ufParticipantes4)
        limparCampo(cepParticipantes4)
        sleep(1)

        limparCampo(nomeParticipantes5)
        limparCampo(emailParticipantes5)
        limparCampo(participação5)
        limparCampo(cnpjCpf5)
        limparCampo(sexo5)
        limparCampo(dataNacimento5)
        limparCampo(telefone5)
        limparCampo(ruaParticipantes5)
        limparCampo(numeroParticipantes5)
        limparCampo(complementoParticipantes5)
        limparCampo(cidadeParticipantes5)
        limparCampo(bairroParticipantes5)
        limparCampo(ufParticipantes5)
        limparCampo(cepParticipantes5)
        sleep(1)

        nomeParticipantes1.send_keys(nomeP1)
        emailParticipantes1.send_keys(emailP1)
        participação1.send_keys(participacaoP1)
        cnpjCpf1.send_keys(cpfP1)
        sexo1.send_keys(sexoP1)
        relacao1.click()
        if relacaoP1 == 'Titular': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select/option[2]')
        elif relacaoP1 == 'Cônjuge': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select/option[3]')
        elif relacaoP1 == 'Procurador': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select/option[4]')
        elif relacaoP1 == 'Pai': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select/option[5]')
        elif relacaoP1 == 'Mãe': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select/option[6]')
        elif relacaoP1 == 'Irmão': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select/option[7]')
        dataNacimento1.send_keys(dataNascimentoP1)
        telefone1.send_keys(telefoneP1)
        ruaParticipantes1.send_keys(ruaP1)
        numeroParticipantes1.send_keys(numeroP1)
        complementoParticipantes1.send_keys(complementoP1)
        cidadeParticipantes1.send_keys(cidadeP1)
        bairroParticipantes1.send_keys(bairroP1)
        ufParticipantes1.send_keys(ufP1)
        cepParticipantes1.send_keys(cepP1)
        sleep(1)

        nomeParticipantes2.send_keys(nomeP2)
        emailParticipantes2.send_keys(emailP2)
        participação2.send_keys(participacaoP2)
        cnpjCpf2.send_keys(cpfP2)
        sexo2.send_keys(sexoP2)
        relacao2.click()
        if relacaoP2 == 'Titular': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[4]/div/label[2]/select/option[2]')
        elif relacaoP2 == 'Cônjuge': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[4]/div/label[2]/select/option[3]')
        elif relacaoP2 == 'Procurador': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[4]/div/label[2]/select/option[4]')
        elif relacaoP2 == 'Pai': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[4]/div/label[2]/select/option[5]')
        elif relacaoP2 == 'Mãe': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[4]/div/label[2]/select/option[6]')
        elif relacaoP2 == 'Irmão': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[4]/div/label[2]/select/option[7]')
        dataNacimento2.send_keys(dataNascimentoP2)
        telefone2.send_keys(telefoneP2)
        ruaParticipantes2.send_keys(ruaP2)
        numeroParticipantes2.send_keys(numeroP2)
        complementoParticipantes2.send_keys(complementoP2)
        cidadeParticipantes2.send_keys(cidadeP2)
        bairroParticipantes2.send_keys(bairroP2)
        ufParticipantes2.send_keys(ufP2)
        cepParticipantes2.send_keys(cepP2)
        sleep(1)

        nomeParticipantes3.send_keys(nomeP3)
        emailParticipantes3.send_keys(emailP3)
        participação3.send_keys(participacaoP3)
        cnpjCpf3.send_keys(cpfP3)
        sexo3.send_keys(sexoP3)
        relacao3.click()
        if relacaoP3 == 'Titular': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[5]/div/label[2]/select/option[2]')
        elif relacaoP3 == 'Cônjuge': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[5]/div/label[2]/select/option[3]')
        elif relacaoP3 == 'Procurador': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[5]/div/label[2]/select/option[4]')
        elif relacaoP3 == 'Pai': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[5]/div/label[2]/select/option[5]')
        elif relacaoP3 == 'Mãe': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[5]/div/label[2]/select/option[6]')
        elif relacaoP3 == 'Irmão': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[5]/div/label[2]/select/option[7]')
        dataNacimento3.send_keys(dataNascimentoP3)
        telefone3.send_keys(telefoneP3)
        ruaParticipantes3.send_keys(ruaP3)
        numeroParticipantes3.send_keys(numeroP3)
        complementoParticipantes3.send_keys(complementoP3)
        cidadeParticipantes3.send_keys(cidadeP3)
        bairroParticipantes3.send_keys(bairroP3)
        ufParticipantes3.send_keys(ufP3)
        cepParticipantes3.send_keys(cepP3)
        sleep(1)

        nomeParticipantes4.send_keys(nomeP4)
        emailParticipantes4.send_keys(emailP4)
        participação4.send_keys(participacaoP4)
        cnpjCpf4.send_keys(cpfP4)
        sexo4.send_keys(sexoP4)
        relacao4.click()
        if relacaoP4 == 'Titular': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[6]/div/label[2]/select/option[2]')
        elif relacaoP4 == 'Cônjuge': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[6]/div/label[2]/select/option[3]')
        elif relacaoP4 == 'Procurador': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[6]/div/label[2]/select/option[4]')
        elif relacaoP4 == 'Pai': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[6]/div/label[2]/select/option[5]')
        elif relacaoP4 == 'Mãe': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[6]/div/label[2]/select/option[6]')
        elif relacaoP4 == 'Irmão': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[6]/div/label[2]/select/option[7]')
        dataNacimento4.send_keys(dataNascimentoP4)
        telefone4.send_keys(telefoneP4)
        ruaParticipantes4.send_keys(ruaP4)
        numeroParticipantes4.send_keys(numeroP4)
        complementoParticipantes4.send_keys(complementoP4)
        cidadeParticipantes4.send_keys(cidadeP4)
        bairroParticipantes4.send_keys(bairroP4)
        ufParticipantes4.send_keys(ufP4)
        cepParticipantes4.send_keys(cepP4)
        sleep(1)

        nomeParticipantes5.send_keys(nomeP5)
        emailParticipantes5.send_keys(emailP5)
        participação5.send_keys(participacaoP5)
        cnpjCpf5.send_keys(cpfP5)
        sexo5.send_keys(sexoP5)
        relacao5.click()
        if relacaoP5 == 'Titular': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[7]/div/label[2]/select/option[2]')
        elif relacaoP5 == 'Cônjuge': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[7]/div/label[2]/select/option[3]')
        elif relacaoP5 == 'Procurador': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[7]/div/label[2]/select/option[4]')
        elif relacaoP5 == 'Pai': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[7]/div/label[2]/select/option[5]')
        elif relacaoP5 == 'Mãe': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[7]/div/label[2]/select/option[6]')
        elif relacaoP5 == 'Irmão': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[7]/div/label[2]/select/option[7]')
        dataNacimento5.send_keys(dataNascimentoP5)
        telefone5.send_keys(telefoneP5)
        ruaParticipantes5.send_keys(ruaP5)
        numeroParticipantes5.send_keys(numeroP5)
        complementoParticipantes5.send_keys(complementoP5)
        cidadeParticipantes5.send_keys(cidadeP5)
        bairroParticipantes5.send_keys(bairroP5)
        ufParticipantes5.send_keys(ufP5)
        cepParticipantes5.send_keys(cepP5)
        sleep(1)
    
    elif contadorC == 6:
        nomeParticipantes1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[3]/input')
        emailParticipantes1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[4]/input')
        participação1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[5]/input')
        cnpjCpf1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[6]/input')
        sexo1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[8]/input')
        relacao1 = driver.find_element_by_xpath(f'/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select')
        dataNacimento1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[9]/input')
        telefone1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[10]/input')
        ruaParticipantes1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[11]/input')
        numeroParticipantes1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[12]/input')
        complementoParticipantes1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[13]/input')
        cidadeParticipantes1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[14]/input')
        bairroParticipantes1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[15]/input')
        ufParticipantes1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[16]/input')
        cepParticipantes1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[17]/input')

        nomeParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[3]/input')
        emailParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[4]/input')
        participação2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[5]/input')
        cnpjCpf2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[6]/input')
        sexo2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[8]/input')
        relacao2 = driver.find_element_by_xpath(f'/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select')
        dataNacimento2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[9]/input')
        telefone2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[10]/input')
        ruaParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[11]/input')
        numeroParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[12]/input')
        complementoParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[13]/input')
        cidadeParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[14]/input')
        bairroParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[15]/input')
        ufParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[16]/input')
        cepParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[17]/input')

        nomeParticipantes3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[3]/input')
        emailParticipantes3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[4]/input')
        participação3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[5]/input')
        cnpjCpf3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[6]/input')
        sexo3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[8]/input')
        relacao3 = driver.find_element_by_xpath(f'/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select')
        dataNacimento3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[9]/input')
        telefone3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[10]/input')
        ruaParticipantes3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[11]/input')
        numeroParticipantes3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[12]/input')
        complementoParticipantes3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[13]/input')
        cidadeParticipantes3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[14]/input')
        bairroParticipantes3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[15]/input')
        ufParticipantes3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[16]/input')
        cepParticipantes3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[17]/input')

        nomeParticipantes4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[3]/input')
        emailParticipantes4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[4]/input')
        participação4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[5]/input')
        cnpjCpf4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[6]/input')
        sexo4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[8]/input')
        relacao4 = driver.find_element_by_xpath(f'/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select')
        dataNacimento4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[9]/input')
        telefone4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[10]/input')
        ruaParticipantes4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[11]/input')
        numeroParticipantes4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[12]/input')
        complementoParticipantes4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[13]/input')
        cidadeParticipantes4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[14]/input')
        bairroParticipantes4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[15]/input')
        ufParticipantes4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[16]/input')
        cepParticipantes4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[17]/input')

        nomeParticipantes5 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[7]/div/label[3]/input')
        emailParticipantes5 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[7]/div/label[4]/input')
        participação5 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[7]/div/label[5]/input')
        cnpjCpf5 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[7]/div/label[6]/input')
        sexo5 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[7]/div/label[8]/input')
        relacao5 = driver.find_element_by_xpath(f'/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select')
        dataNacimento5 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[7]/div/label[9]/input')
        telefone5 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[7]/div/label[10]/input')
        ruaParticipantes5 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[7]/div/label[11]/input')
        numeroParticipantes5 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[7]/div/label[12]/input')
        complementoParticipantes5 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[7]/div/label[13]/input')
        cidadeParticipantes5 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[7]/div/label[14]/input')
        bairroParticipantes5 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[7]/div/label[15]/input')
        ufParticipantes5 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[7]/div/label[16]/input')
        cepParticipantes5 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[7]/div/label[17]/input')

        nomeParticipantes6 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[8]/div/label[3]/input')
        emailParticipantes6 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[8]/div/label[4]/input')
        participação6 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[8]/div/label[5]/input')
        cnpjCpf6 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[8]/div/label[6]/input')
        sexo6 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[8]/div/label[8]/input')
        relacao6 = driver.find_element_by_xpath(f'/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select')
        dataNacimento6 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[8]/div/label[9]/input')
        telefone6 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[8]/div/label[10]/input')
        ruaParticipantes6 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[8]/div/label[11]/input')
        numeroParticipantes6 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[8]/div/label[12]/input')
        complementoParticipantes6 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[8]/div/label[13]/input')
        cidadeParticipantes6 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[8]/div/label[14]/input')
        bairroParticipantes6 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[8]/div/label[15]/input')
        ufParticipantes6 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[8]/div/label[16]/input')
        cepParticipantes6 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[8]/div/label[17]/input')
         # Limpar campos
        limparCampo(nomeParticipantes1)
        limparCampo(emailParticipantes1)
        limparCampo(participação1)
        limparCampo(cnpjCpf1)
        limparCampo(sexo1)
        limparCampo(dataNacimento1)
        limparCampo(telefone1)
        limparCampo(ruaParticipantes1)
        limparCampo(numeroParticipantes1)
        limparCampo(complementoParticipantes1)
        limparCampo(cidadeParticipantes1)
        limparCampo(bairroParticipantes1)
        limparCampo(ufParticipantes1)
        limparCampo(cepParticipantes1)
        sleep(1)

        limparCampo(nomeParticipantes2)
        limparCampo(emailParticipantes2)
        limparCampo(participação2)
        limparCampo(cnpjCpf2)
        limparCampo(sexo2)
        limparCampo(dataNacimento2)
        limparCampo(telefone2)
        limparCampo(ruaParticipantes2)
        limparCampo(numeroParticipantes2)
        limparCampo(complementoParticipantes2)
        limparCampo(cidadeParticipantes2)
        limparCampo(bairroParticipantes2)
        limparCampo(ufParticipantes2)
        limparCampo(cepParticipantes2)
        sleep(1)

        limparCampo(nomeParticipantes3)
        limparCampo(emailParticipantes3)
        limparCampo(participação3)
        limparCampo(cnpjCpf3)
        limparCampo(sexo3)
        limparCampo(dataNacimento3)
        limparCampo(telefone3)
        limparCampo(ruaParticipantes3)
        limparCampo(numeroParticipantes3)
        limparCampo(complementoParticipantes3)
        limparCampo(cidadeParticipantes3)
        limparCampo(bairroParticipantes3)
        limparCampo(ufParticipantes3)
        limparCampo(cepParticipantes3)
        sleep(1)

        limparCampo(nomeParticipantes4)
        limparCampo(emailParticipantes4)
        limparCampo(participação4)
        limparCampo(cnpjCpf4)
        limparCampo(sexo4)
        limparCampo(dataNacimento4)
        limparCampo(telefone4)
        limparCampo(ruaParticipantes4)
        limparCampo(numeroParticipantes4)
        limparCampo(complementoParticipantes4)
        limparCampo(cidadeParticipantes4)
        limparCampo(bairroParticipantes4)
        limparCampo(ufParticipantes4)
        limparCampo(cepParticipantes4)
        sleep(1)

        limparCampo(nomeParticipantes5)
        limparCampo(emailParticipantes5)
        limparCampo(participação5)
        limparCampo(cnpjCpf5)
        limparCampo(sexo5)
        limparCampo(dataNacimento5)
        limparCampo(telefone5)
        limparCampo(ruaParticipantes5)
        limparCampo(numeroParticipantes5)
        limparCampo(complementoParticipantes5)
        limparCampo(cidadeParticipantes5)
        limparCampo(bairroParticipantes5)
        limparCampo(ufParticipantes5)
        limparCampo(cepParticipantes5)
        sleep(1)

        limparCampo(nomeParticipantes6)
        limparCampo(emailParticipantes6)
        limparCampo(participação6)
        limparCampo(cnpjCpf6)
        limparCampo(sexo6)
        limparCampo(dataNacimento6)
        limparCampo(telefone6)
        limparCampo(ruaParticipantes6)
        limparCampo(numeroParticipantes6)
        limparCampo(complementoParticipantes6)
        limparCampo(cidadeParticipantes6)
        limparCampo(bairroParticipantes6)
        limparCampo(ufParticipantes6)
        limparCampo(cepParticipantes6)
        sleep(1)
    
    
        nomeParticipantes1.send_keys(nomeP1)
        emailParticipantes1.send_keys(emailP1)
        participação1.send_keys(participacaoP1)
        cnpjCpf1.send_keys(cpfP1)
        sexo1.send_keys(sexoP1)
        relacao1.click()
        if relacaoP1 == 'Titular': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select/option[2]')
        elif relacaoP1 == 'Cônjuge': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select/option[3]')
        elif relacaoP1 == 'Procurador': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select/option[4]')
        elif relacaoP1 == 'Pai': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select/option[5]')
        elif relacaoP1 == 'Mãe': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select/option[6]')
        elif relacaoP1 == 'Irmão': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select/option[7]')
        dataNacimento1.send_keys(dataNascimentoP1)
        telefone1.send_keys(telefoneP1)
        ruaParticipantes1.send_keys(ruaP1)
        numeroParticipantes1.send_keys(numeroP1)
        complementoParticipantes1.send_keys(complementoP1)
        cidadeParticipantes1.send_keys(cidadeP1)
        bairroParticipantes1.send_keys(bairroP1)
        ufParticipantes1.send_keys(ufP1)
        cepParticipantes1.send_keys(cepP1)
        sleep(1)

        nomeParticipantes2.send_keys(nomeP2)
        emailParticipantes2.send_keys(emailP2)
        participação2.send_keys(participacaoP2)
        cnpjCpf2.send_keys(cpfP2)
        sexo2.send_keys(sexoP2)
        relacao2.click()
        if relacaoP2 == 'Titular': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[4]/div/label[2]/select/option[2]')
        elif relacaoP2 == 'Cônjuge': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[4]/div/label[2]/select/option[3]')
        elif relacaoP2 == 'Procurador': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[4]/div/label[2]/select/option[4]')
        elif relacaoP2 == 'Pai': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[4]/div/label[2]/select/option[5]')
        elif relacaoP2 == 'Mãe': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[4]/div/label[2]/select/option[6]')
        elif relacaoP2 == 'Irmão': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[4]/div/label[2]/select/option[7]')
        dataNacimento2.send_keys(dataNascimentoP2)
        telefone2.send_keys(telefoneP2)
        ruaParticipantes2.send_keys(ruaP2)
        numeroParticipantes2.send_keys(numeroP2)
        complementoParticipantes2.send_keys(complementoP2)
        cidadeParticipantes2.send_keys(cidadeP2)
        bairroParticipantes2.send_keys(bairroP2)
        ufParticipantes2.send_keys(ufP2)
        cepParticipantes2.send_keys(cepP2)
        sleep(1)

        nomeParticipantes3.send_keys(nomeP3)
        emailParticipantes3.send_keys(emailP3)
        participação3.send_keys(participacaoP3)
        cnpjCpf3.send_keys(cpfP3)
        sexo3.send_keys(sexoP3)
        relacao3.click()
        if relacaoP3 == 'Titular': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[5]/div/label[2]/select/option[2]')
        elif relacaoP3 == 'Cônjuge': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[5]/div/label[2]/select/option[3]')
        elif relacaoP3 == 'Procurador': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[5]/div/label[2]/select/option[4]')
        elif relacaoP3 == 'Pai': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[5]/div/label[2]/select/option[5]')
        elif relacaoP3 == 'Mãe': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[5]/div/label[2]/select/option[6]')
        elif relacaoP3 == 'Irmão': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[5]/div/label[2]/select/option[7]')
        dataNacimento3.send_keys(dataNascimentoP3)
        telefone3.send_keys(telefoneP3)
        ruaParticipantes3.send_keys(ruaP3)
        numeroParticipantes3.send_keys(numeroP3)
        complementoParticipantes3.send_keys(complementoP3)
        cidadeParticipantes3.send_keys(cidadeP3)
        bairroParticipantes3.send_keys(bairroP3)
        ufParticipantes3.send_keys(ufP3)
        cepParticipantes3.send_keys(cepP3)
        sleep(1)

        nomeParticipantes4.send_keys(nomeP4)
        emailParticipantes4.send_keys(emailP4)
        participação4.send_keys(participacaoP4)
        cnpjCpf4.send_keys(cpfP4)
        sexo4.send_keys(sexoP4)
        relacao4.click()
        if relacaoP4 == 'Titular': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[6]/div/label[2]/select/option[2]')
        elif relacaoP4 == 'Cônjuge': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[6]/div/label[2]/select/option[3]')
        elif relacaoP4 == 'Procurador': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[6]/div/label[2]/select/option[4]')
        elif relacaoP4 == 'Pai': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[6]/div/label[2]/select/option[5]')
        elif relacaoP4 == 'Mãe': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[6]/div/label[2]/select/option[6]')
        elif relacaoP4 == 'Irmão': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[6]/div/label[2]/select/option[7]')
        dataNacimento4.send_keys(dataNascimentoP4)
        telefone4.send_keys(telefoneP4)
        ruaParticipantes4.send_keys(ruaP4)
        numeroParticipantes4.send_keys(numeroP4)
        complementoParticipantes4.send_keys(complementoP4)
        cidadeParticipantes4.send_keys(cidadeP4)
        bairroParticipantes4.send_keys(bairroP4)
        ufParticipantes4.send_keys(ufP4)
        cepParticipantes4.send_keys(cepP4)
        sleep(1)

        nomeParticipantes5.send_keys(nomeP5)
        emailParticipantes5.send_keys(emailP5)
        participação5.send_keys(participacaoP5)
        cnpjCpf5.send_keys(cpfP5)
        sexo5.send_keys(sexoP5)
        relacao5.click()
        if relacaoP5 == 'Titular': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[7]/div/label[2]/select/option[2]')
        elif relacaoP5 == 'Cônjuge': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[7]/div/label[2]/select/option[3]')
        elif relacaoP5 == 'Procurador': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[7]/div/label[2]/select/option[4]')
        elif relacaoP5 == 'Pai': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[7]/div/label[2]/select/option[5]')
        elif relacaoP5 == 'Mãe': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[7]/div/label[2]/select/option[6]')
        elif relacaoP5 == 'Irmão': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[7]/div/label[2]/select/option[7]')
        dataNacimento5.send_keys(dataNascimentoP5)
        telefone5.send_keys(telefoneP5)
        ruaParticipantes5.send_keys(ruaP5)
        numeroParticipantes5.send_keys(numeroP5)
        complementoParticipantes5.send_keys(complementoP5)
        cidadeParticipantes5.send_keys(cidadeP5)
        bairroParticipantes5.send_keys(bairroP5)
        ufParticipantes5.send_keys(ufP5)
        cepParticipantes5.send_keys(cepP5)
        sleep(1)

        nomeParticipantes6.send_keys(nomeP6)
        emailParticipantes6.send_keys(emailP6)
        participação6.send_keys(participacaoP6)
        cnpjCpf6.send_keys(cpfP6)
        sexo6.send_keys(sexoP6)
        relacao6.click()
        if relacaoP6 == 'Titular': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[8]/div/label[2]/select/option[2]')
        elif relacaoP6 == 'Cônjuge': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[8]/div/label[2]/select/option[3]')
        elif relacaoP6 == 'Procurador': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[8]/div/label[2]/select/option[4]')
        elif relacaoP6 == 'Pai': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[8]/div/label[2]/select/option[5]')
        elif relacaoP6 == 'Mãe': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[8]/div/label[2]/select/option[6]')
        elif relacaoP6 == 'Irmão': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[8]/div/label[2]/select/option[7]')
        dataNacimento6.send_keys(dataNascimentoP6)
        telefone6.send_keys(telefoneP6)
        ruaParticipantes6.send_keys(ruaP6)
        numeroParticipantes6.send_keys(numeroP6)
        complementoParticipantes6.send_keys(complementoP6)
        cidadeParticipantes6.send_keys(cidadeP6)
        bairroParticipantes6.send_keys(bairroP6)
        ufParticipantes6.send_keys(ufP6)
        cepParticipantes6.send_keys(cepP6)
        sleep(1)

    elif contadorC == 7:
        nomeParticipantes1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[3]/input')
        emailParticipantes1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[4]/input')
        participação1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[5]/input')
        cnpjCpf1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[6]/input')
        sexo1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[8]/input')
        relacao1 = driver.find_element_by_xpath(f'/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select')
        dataNacimento1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[9]/input')
        telefone1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[10]/input')
        ruaParticipantes1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[11]/input')
        numeroParticipantes1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[12]/input')
        complementoParticipantes1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[13]/input')
        cidadeParticipantes1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[14]/input')
        bairroParticipantes1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[15]/input')
        ufParticipantes1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[16]/input')
        cepParticipantes1 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[3]/div/label[17]/input')

        nomeParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[3]/input')
        emailParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[4]/input')
        participação2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[5]/input')
        cnpjCpf2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[6]/input')
        sexo2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[8]/input')
        relacao2 = driver.find_element_by_xpath(f'/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select')
        dataNacimento2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[9]/input')
        telefone2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[10]/input')
        ruaParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[11]/input')
        numeroParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[12]/input')
        complementoParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[13]/input')
        cidadeParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[14]/input')
        bairroParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[15]/input')
        ufParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[16]/input')
        cepParticipantes2 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[4]/div/label[17]/input')

        nomeParticipantes3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[3]/input')
        emailParticipantes3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[4]/input')
        participação3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[5]/input')
        cnpjCpf3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[6]/input')
        sexo3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[8]/input')
        relacao3 = driver.find_element_by_xpath(f'/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select')
        dataNacimento3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[9]/input')
        telefone3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[10]/input')
        ruaParticipantes3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[11]/input')
        numeroParticipantes3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[12]/input')
        complementoParticipantes3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[13]/input')
        cidadeParticipantes3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[14]/input')
        bairroParticipantes3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[15]/input')
        ufParticipantes3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[16]/input')
        cepParticipantes3 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[5]/div/label[17]/input')

        nomeParticipantes4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[3]/input')
        emailParticipantes4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[4]/input')
        participação4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[5]/input')
        cnpjCpf4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[6]/input')
        sexo4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[8]/input')
        relacao4 = driver.find_element_by_xpath(f'/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select')
        dataNacimento4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[9]/input')
        telefone4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[10]/input')
        ruaParticipantes4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[11]/input')
        numeroParticipantes4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[12]/input')
        complementoParticipantes4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[13]/input')
        cidadeParticipantes4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[14]/input')
        bairroParticipantes4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[15]/input')
        ufParticipantes4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[16]/input')
        cepParticipantes4 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[6]/div/label[17]/input')

        nomeParticipantes5 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[7]/div/label[3]/input')
        emailParticipantes5 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[7]/div/label[4]/input')
        participação5 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[7]/div/label[5]/input')
        cnpjCpf5 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[7]/div/label[6]/input')
        sexo5 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[7]/div/label[8]/input')
        relacao5 = driver.find_element_by_xpath(f'/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select')
        dataNacimento5 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[7]/div/label[9]/input')
        telefone5 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[7]/div/label[10]/input')
        ruaParticipantes5 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[7]/div/label[11]/input')
        numeroParticipantes5 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[7]/div/label[12]/input')
        complementoParticipantes5 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[7]/div/label[13]/input')
        cidadeParticipantes5 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[7]/div/label[14]/input')
        bairroParticipantes5 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[7]/div/label[15]/input')
        ufParticipantes5 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[7]/div/label[16]/input')
        cepParticipantes5 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[7]/div/label[17]/input')

        nomeParticipantes6 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[8]/div/label[3]/input')
        emailParticipantes6 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[8]/div/label[4]/input')
        participação6 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[8]/div/label[5]/input')
        cnpjCpf6 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[8]/div/label[6]/input')
        sexo6 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[8]/div/label[8]/input')
        relacao6 = driver.find_element_by_xpath(f'/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select')
        dataNacimento6 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[8]/div/label[9]/input')
        telefone6 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[8]/div/label[10]/input')
        ruaParticipantes6 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[8]/div/label[11]/input')
        numeroParticipantes6 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[8]/div/label[12]/input')
        complementoParticipantes6 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[8]/div/label[13]/input')
        cidadeParticipantes6 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[8]/div/label[14]/input')
        bairroParticipantes6 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[8]/div/label[15]/input')
        ufParticipantes6 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[8]/div/label[16]/input')
        cepParticipantes6 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[8]/div/label[17]/input')

        nomeParticipantes7 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[9]/div/label[3]/input')
        emailParticipantes7 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[9]/div/label[4]/input')
        participação7 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[9]/div/label[5]/input')
        cnpjCpf7 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[9]/div/label[6]/input')
        sexo7 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[9]/div/label[8]/input')
        relacao7 = driver.find_element_by_xpath(f'/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select')
        dataNacimento7 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[9]/div/label[9]/input')
        telefone7 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[9]/div/label[10]/input')
        ruaParticipantes7 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[9]/div/label[11]/input')
        numeroParticipantes7 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[9]/div/label[12]/input')
        complementoParticipantes7 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[9]/div/label[13]/input')
        cidadeParticipantes7 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[9]/div/label[14]/input')
        bairroParticipantes7 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[9]/div/label[15]/input')
        ufParticipantes7 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[9]/div/label[16]/input')
        cepParticipantes7 = driver.find_element_by_xpath(f'/html/body/div/main/div/section[1]/div/div/form/fieldset[9]/div/label[17]/input')
         # Limpar campos
        limparCampo(nomeParticipantes1)
        limparCampo(emailParticipantes1)
        limparCampo(participação1)
        limparCampo(cnpjCpf1)
        limparCampo(sexo1)
        limparCampo(dataNacimento1)
        limparCampo(telefone1)
        limparCampo(ruaParticipantes1)
        limparCampo(numeroParticipantes1)
        limparCampo(complementoParticipantes1)
        limparCampo(cidadeParticipantes1)
        limparCampo(bairroParticipantes1)
        limparCampo(ufParticipantes1)
        limparCampo(cepParticipantes1)
        sleep(1)

        limparCampo(nomeParticipantes2)
        limparCampo(emailParticipantes2)
        limparCampo(participação2)
        limparCampo(cnpjCpf2)
        limparCampo(sexo2)
        limparCampo(dataNacimento2)
        limparCampo(telefone2)
        limparCampo(ruaParticipantes2)
        limparCampo(numeroParticipantes2)
        limparCampo(complementoParticipantes2)
        limparCampo(cidadeParticipantes2)
        limparCampo(bairroParticipantes2)
        limparCampo(ufParticipantes2)
        limparCampo(cepParticipantes2)
        sleep(1)

        limparCampo(nomeParticipantes3)
        limparCampo(emailParticipantes3)
        limparCampo(participação3)
        limparCampo(cnpjCpf3)
        limparCampo(sexo3)
        limparCampo(dataNacimento3)
        limparCampo(telefone3)
        limparCampo(ruaParticipantes3)
        limparCampo(numeroParticipantes3)
        limparCampo(complementoParticipantes3)
        limparCampo(cidadeParticipantes3)
        limparCampo(bairroParticipantes3)
        limparCampo(ufParticipantes3)
        limparCampo(cepParticipantes3)
        sleep(1)

        limparCampo(nomeParticipantes4)
        limparCampo(emailParticipantes4)
        limparCampo(participação4)
        limparCampo(cnpjCpf4)
        limparCampo(sexo4)
        limparCampo(dataNacimento4)
        limparCampo(telefone4)
        limparCampo(ruaParticipantes4)
        limparCampo(numeroParticipantes4)
        limparCampo(complementoParticipantes4)
        limparCampo(cidadeParticipantes4)
        limparCampo(bairroParticipantes4)
        limparCampo(ufParticipantes4)
        limparCampo(cepParticipantes4)
        sleep(1)

        limparCampo(nomeParticipantes5)
        limparCampo(emailParticipantes5)
        limparCampo(participação5)
        limparCampo(cnpjCpf5)
        limparCampo(sexo5)
        limparCampo(dataNacimento5)
        limparCampo(telefone5)
        limparCampo(ruaParticipantes5)
        limparCampo(numeroParticipantes5)
        limparCampo(complementoParticipantes5)
        limparCampo(cidadeParticipantes5)
        limparCampo(bairroParticipantes5)
        limparCampo(ufParticipantes5)
        limparCampo(cepParticipantes5)
        sleep(1)

        limparCampo(nomeParticipantes6)
        limparCampo(emailParticipantes6)
        limparCampo(participação6)
        limparCampo(cnpjCpf6)
        limparCampo(sexo6)
        limparCampo(dataNacimento6)
        limparCampo(telefone6)
        limparCampo(ruaParticipantes6)
        limparCampo(numeroParticipantes6)
        limparCampo(complementoParticipantes6)
        limparCampo(cidadeParticipantes6)
        limparCampo(bairroParticipantes6)
        limparCampo(ufParticipantes6)
        limparCampo(cepParticipantes6)
        sleep(1)

        limparCampo(nomeParticipantes7)
        limparCampo(emailParticipantes7)
        limparCampo(participação7)
        limparCampo(cnpjCpf7)
        limparCampo(sexo7)
        limparCampo(dataNacimento7)
        limparCampo(telefone7)
        limparCampo(ruaParticipantes7)
        limparCampo(numeroParticipantes7)
        limparCampo(complementoParticipantes7)
        limparCampo(cidadeParticipantes7)
        limparCampo(bairroParticipantes7)
        limparCampo(ufParticipantes7)
        limparCampo(cepParticipantes7)
        sleep(1)

        nomeParticipantes1.send_keys(nomeP1)
        emailParticipantes1.send_keys(emailP1)
        participação1.send_keys(participacaoP1)
        cnpjCpf1.send_keys(cpfP1)
        sexo1.send_keys(sexoP1)
        relacao1.click()
        if relacaoP1 == 'Titular': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select/option[2]')
        elif relacaoP1 == 'Cônjuge': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select/option[3]')
        elif relacaoP1 == 'Procurador': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select/option[4]')
        elif relacaoP1 == 'Pai': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select/option[5]')
        elif relacaoP1 == 'Mãe': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select/option[6]')
        elif relacaoP1 == 'Irmão': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[3]/div/label[2]/select/option[7]')
        dataNacimento1.send_keys(dataNascimentoP1)
        telefone1.send_keys(telefoneP1)
        ruaParticipantes1.send_keys(ruaP1)
        numeroParticipantes1.send_keys(numeroP1)
        complementoParticipantes1.send_keys(complementoP1)
        cidadeParticipantes1.send_keys(cidadeP1)
        bairroParticipantes1.send_keys(bairroP1)
        ufParticipantes1.send_keys(ufP1)
        cepParticipantes1.send_keys(cepP1)
        sleep(1)

        nomeParticipantes2.send_keys(nomeP2)
        emailParticipantes2.send_keys(emailP2)
        participação2.send_keys(participacaoP2)
        cnpjCpf2.send_keys(cpfP2)
        sexo2.send_keys(sexoP2)
        relacao2.click()
        if relacaoP2 == 'Titular': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[4]/div/label[2]/select/option[2]')
        elif relacaoP2 == 'Cônjuge': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[4]/div/label[2]/select/option[3]')
        elif relacaoP2 == 'Procurador': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[4]/div/label[2]/select/option[4]')
        elif relacaoP2 == 'Pai': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[4]/div/label[2]/select/option[5]')
        elif relacaoP2 == 'Mãe': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[4]/div/label[2]/select/option[6]')
        elif relacaoP2 == 'Irmão': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[4]/div/label[2]/select/option[7]')
        dataNacimento2.send_keys(dataNascimentoP2)
        telefone2.send_keys(telefoneP2)
        ruaParticipantes2.send_keys(ruaP2)
        numeroParticipantes2.send_keys(numeroP2)
        complementoParticipantes2.send_keys(complementoP2)
        cidadeParticipantes2.send_keys(cidadeP2)
        bairroParticipantes2.send_keys(bairroP2)
        ufParticipantes2.send_keys(ufP2)
        cepParticipantes2.send_keys(cepP2)
        sleep(1)

        nomeParticipantes3.send_keys(nomeP3)
        emailParticipantes3.send_keys(emailP3)
        participação3.send_keys(participacaoP3)
        cnpjCpf3.send_keys(cpfP3)
        sexo3.send_keys(sexoP3)
        relacao3.click()
        if relacaoP3 == 'Titular': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[5]/div/label[2]/select/option[2]')
        elif relacaoP3 == 'Cônjuge': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[5]/div/label[2]/select/option[3]')
        elif relacaoP3 == 'Procurador': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[5]/div/label[2]/select/option[4]')
        elif relacaoP3 == 'Pai': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[5]/div/label[2]/select/option[5]')
        elif relacaoP3 == 'Mãe': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[5]/div/label[2]/select/option[6]')
        elif relacaoP3 == 'Irmão': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[5]/div/label[2]/select/option[7]')
        dataNacimento3.send_keys(dataNascimentoP3)
        telefone3.send_keys(telefoneP3)
        ruaParticipantes3.send_keys(ruaP3)
        numeroParticipantes3.send_keys(numeroP3)
        complementoParticipantes3.send_keys(complementoP3)
        cidadeParticipantes3.send_keys(cidadeP3)
        bairroParticipantes3.send_keys(bairroP3)
        ufParticipantes3.send_keys(ufP3)
        cepParticipantes3.send_keys(cepP3)
        sleep(1)

        nomeParticipantes4.send_keys(nomeP4)
        emailParticipantes4.send_keys(emailP4)
        participação4.send_keys(participacaoP4)
        cnpjCpf4.send_keys(cpfP4)
        sexo4.send_keys(sexoP4)
        relacao4.click()
        if relacaoP4 == 'Titular': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[6]/div/label[2]/select/option[2]')
        elif relacaoP4 == 'Cônjuge': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[6]/div/label[2]/select/option[3]')
        elif relacaoP4 == 'Procurador': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[6]/div/label[2]/select/option[4]')
        elif relacaoP4 == 'Pai': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[6]/div/label[2]/select/option[5]')
        elif relacaoP4 == 'Mãe': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[6]/div/label[2]/select/option[6]')
        elif relacaoP4 == 'Irmão': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[6]/div/label[2]/select/option[7]')
        dataNacimento4.send_keys(dataNascimentoP4)
        telefone4.send_keys(telefoneP4)
        ruaParticipantes4.send_keys(ruaP4)
        numeroParticipantes4.send_keys(numeroP4)
        complementoParticipantes4.send_keys(complementoP4)
        cidadeParticipantes4.send_keys(cidadeP4)
        bairroParticipantes4.send_keys(bairroP4)
        ufParticipantes4.send_keys(ufP4)
        cepParticipantes4.send_keys(cepP4)
        sleep(1)

        nomeParticipantes5.send_keys(nomeP5)
        emailParticipantes5.send_keys(emailP5)
        participação5.send_keys(participacaoP5)
        cnpjCpf5.send_keys(cpfP5)
        sexo5.send_keys(sexoP5)
        relacao5.click()
        if relacaoP5 == 'Titular': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[7]/div/label[2]/select/option[2]')
        elif relacaoP5 == 'Cônjuge': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[7]/div/label[2]/select/option[3]')
        elif relacaoP5 == 'Procurador': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[7]/div/label[2]/select/option[4]')
        elif relacaoP5 == 'Pai': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[7]/div/label[2]/select/option[5]')
        elif relacaoP5 == 'Mãe': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[7]/div/label[2]/select/option[6]')
        elif relacaoP5 == 'Irmão': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[7]/div/label[2]/select/option[7]')
        dataNacimento5.send_keys(dataNascimentoP5)
        telefone5.send_keys(telefoneP5)
        ruaParticipantes5.send_keys(ruaP5)
        numeroParticipantes5.send_keys(numeroP5)
        complementoParticipantes5.send_keys(complementoP5)
        cidadeParticipantes5.send_keys(cidadeP5)
        bairroParticipantes5.send_keys(bairroP5)
        ufParticipantes5.send_keys(ufP5)
        cepParticipantes5.send_keys(cepP5)
        sleep(1)

        nomeParticipantes6.send_keys(nomeP6)
        emailParticipantes6.send_keys(emailP6)
        participação6.send_keys(participacaoP6)
        cnpjCpf6.send_keys(cpfP6)
        sexo6.send_keys(sexoP6)
        relacao6.click()
        if relacaoP6 == 'Titular': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[8]/div/label[2]/select/option[2]')
        elif relacaoP6 == 'Cônjuge': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[8]/div/label[2]/select/option[3]')
        elif relacaoP6 == 'Procurador': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[8]/div/label[2]/select/option[4]')
        elif relacaoP6 == 'Pai': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[8]/div/label[2]/select/option[5]')
        elif relacaoP6 == 'Mãe': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[8]/div/label[2]/select/option[6]')
        elif relacaoP6 == 'Irmão': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[8]/div/label[2]/select/option[7]')
        dataNacimento6.send_keys(dataNascimentoP6)
        telefone6.send_keys(telefoneP6)
        ruaParticipantes6.send_keys(ruaP6)
        numeroParticipantes6.send_keys(numeroP6)
        complementoParticipantes6.send_keys(complementoP6)
        cidadeParticipantes6.send_keys(cidadeP6)
        bairroParticipantes6.send_keys(bairroP6)
        ufParticipantes6.send_keys(ufP6)
        cepParticipantes6.send_keys(cepP6)
        sleep(1)

        nomeParticipantes7.send_keys(nomeP7)
        emailParticipantes7.send_keys(emailP7)
        participação7.send_keys(participacaoP7)
        cnpjCpf7.send_keys(cpfP7)
        sexo7.send_keys(sexoP7)
        relacao7.click()
        if relacaoP7 == 'Titular': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[9]/div/label[2]/select/option[2]')
        elif relacaoP7 == 'Cônjuge': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[9]/div/label[2]/select/option[3]')
        elif relacaoP7 == 'Procurador': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[9]/div/label[2]/select/option[4]')
        elif relacaoP7 == 'Pai': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[9]/div/label[2]/select/option[5]')
        elif relacaoP7 == 'Mãe': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[9]/div/label[2]/select/option[6]')
        elif relacaoP7 == 'Irmão': relacaoP = driver.find_element_by_xpath('/html/body/div[1]/main/div/section[1]/div/div/form/fieldset[9]/div/label[2]/select/option[7]')
        dataNacimento7.send_keys(dataNascimentoP7)
        telefone7.send_keys(telefoneP7)
        ruaParticipantes7.send_keys(ruaP7)
        numeroParticipantes7.send_keys(numeroP7)
        complementoParticipantes7.send_keys(complementoP7)
        cidadeParticipantes7.send_keys(cidadeP7)
        bairroParticipantes7.send_keys(bairroP7)
        ufParticipantes7.send_keys(ufP7)
        cepParticipantes7.send_keys(cepP7)
        sleep(1)

    




