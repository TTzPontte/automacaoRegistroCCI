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

# def preencherAPI(anexoCalculoFluxo, contratoPath, laudoPath):

#ChromeDriver
driver = webdriver.Chrome(executable_path=r'G:\Drives compartilhados\Pontte\Operações\Automações\Scripts\Pontte\Driver\chromedriver.exe')

#Acessar API Aztronic
driver.get('http://aztronic.s3-website-us-east-1.amazonaws.com/')
sleep(3)

# Upload do Calculo de fluxo 
anexarCalculoFluxo = driver.find_element_by_xpath('//*[@id="main"]/div/section[1]/div/div/form/fieldset[1]/div[1]/label/input')
anexarCalculoFluxo.send_keys(anexoCalculoFluxo)
sleep(2)

# Extraido informações com o leitor de contratos
contrato = lerContrato(contratoPath)
Participantes = lc.dadosParticipantes(contratoPath,contrato)
Laudo = lerLaudo(laudoPath)

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