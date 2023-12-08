import requests
import smtplib
import time

# URL da página que você deseja monitorar
url = "https://servicos.oab-sc.org.br/hbconselhos/login/loginboleto.aspx"

# Palavra-chave que você deseja verificar na página
keyword = "Erro"

# Configurações do servidor de e-mail
email_usuario = "chamadosdti@oab-sc.org.br"  # Seu endereço de e-mail
senha = "Oab*2023"  # Sua senha de e-mail
servidor_smtp = "smtp.gmail.com"  # Servidor SMTP (no exemplo, usando o Gmail)
porta_smtp = 587  # Porta SMTP para o Gmail

# Variável de controle para evitar envio repetitivo de email
email_enviado = False

# Função para verificar o conteúdo da página
def check_page_content(url, keyword):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lança uma exceção se houver um erro HTTP

        # Verifique se a palavra-chave está presente no conteúdo da página
        if keyword in response.text:
            return True
        else:
            return False
    except Exception as e:
        # Trate qualquer exceção que possa ocorrer, como erros de rede
        print("Erro ao verificar a página:", e)
        return False

# Função para enviar e-mails
def enviar_email(destinatario, assunto, mensagem):
    try:
        # Configurar a conexão com o servidor SMTP
        servidor = smtplib.SMTP(servidor_smtp, porta_smtp)
        servidor.starttls()  # Usar TLS para criptografar a conexão

        # Efetuar login no servidor de e-mail
        servidor.login(email_usuario, senha)

        # Criar o e-mail com codificação UTF-8
        corpo_email = f"Assunto: {assunto}\n\n{mensagem}".encode('utf-8')

        servidor.sendmail(email_usuario, destinatario, corpo_email)

        # Encerrar a conexão
        servidor.quit()
        print("E-mail enviado com sucesso.")
    except Exception as e:
        print("Erro ao enviar o e-mail:", str(e))

# O código para verificar a página e enviar e-mails
def check_and_notify():
    global email_enviado  # Utiliza a variável de controle global

    if check_page_content(url, keyword):
        print("A página está online e não apresenta erros.")
        email_enviado = False  # Redefine a variável de controle
    else:
        if not email_enviado:  # Verifica se o email já foi enviado
            # Enviar notificação por e-mail
            destinatario = "dtioab@oab-sc.org.br"  # Endereço de e-mail do destinatário
            assunto = "Erro na página BRC detectado"
            mensagem = "Você foi notificado sobre um erro na página."
            enviar_email(destinatario, assunto, mensagem)
            email_enviado = True  # Define a variável de controle para evitar envios repetitivos

# Loop infinito para verificar a página a cada 5 minutos
while True:
    check_and_notify()
    time.sleep(300)  # Espera 300 segundos (5 minutos) antes de verificar novamente
