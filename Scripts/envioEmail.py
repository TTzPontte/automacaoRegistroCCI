from datetime import date
import os 
import smtplib
from email.message import EmailMessage
import time

def enviarEmail(idContrato, produto, valorBruto):
    # Criar e-mail 
    msg = EmailMessage()
    msg['Subject'] = f'Entrada de Novo Cliente no Aztronic - {date.today().strftime("%d/%m")}'          # Titulo do e-mail
    msg['From'] = 'opscontrole@pontte.com.br'
    msg['To'] = 'henrique.scripelliti@pontte.com.br'
    msg['CC'] = ['luis.caram@pontte.com.br', 'solange.souza@pontte.com.br', 'ops@pontte.com.br']
    msg.set_content(f'''Prezados, foi realizado uma nova implantação no Aztronic, segue os dados da operação abaixo:

   ID: {idContrato}
   Produto: {produto}
   Valor Bruto: {valorBruto}


    Att, 
    Ops team. ''')                                          # mensagem corpo do e-mail

    # Enviar um e-mail
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login("matheus.duarte@pontte.com.br","ifovusblhzjwazpa")
        smtp.send_message(msg)


        '''Apos arrumar as mensagens adicionando o nome do cliente inputado, ajudar o destinatario do email'''


### Teste

#test = enviarEmail("123456","HE",100)