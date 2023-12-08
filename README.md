Este código Python verifica se uma página da web contém a palavra-chave especificada e, se não a encontrar,
envia um e-mail de notificação sobre um possível erro na página.

O código usa a biblioteca requests para fazer solicitações HTTP à página e a biblioteca smtplib para enviar e-mails por meio de um servidor SMTP. Um loop infinito verifica
a página a cada 5 minutos e notifica por e-mail se um erro for detectado.
