import os 
import smtplib
from email.message import EmailMessage

def enviarEmail(EMAIL_ADDRESS,EMAIL_PASSWORD):
    # Criar e-mail 
    msg = EmailMessage()
    msg['Subject'] = 'TESTE Nova operação em carteira'          # Titulo do e-mail
    msg['From'] = 'opscontrole@pontte.com.br'
    msg['To'] = 'matheus.pereira@pontte.com.br; matheus.duarte@pontte.com.br'            
    msg.set_content('''Prezados, 

    O cliente FULANO foi add a carteira

    Att, 
    Ops team. ''')                                          # mensagem corpo do e-mail

    # Enviar um e-mail
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
        smtp.send_message(msg)


        '''Apos arrumar as mensagens adicionando o nome do cliente inputado, ajudar o destinatario do email'''


### Teste

# EMAIL_ADDRESS = "opscontrole@pontte.com.br"
# EMAIL_PASSWORD = "PontteOps22"
# test = enviarEmail(EMAIL_ADDRESS,EMAIL_PASSWORD)