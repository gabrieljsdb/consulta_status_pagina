Este código Python verifica se uma página da web contém a palavra-chave especificada e, se não a encontrar,
envia um e-mail de notificação sobre um possível erro na página.

O código usa a biblioteca requests para fazer solicitações HTTP à página e a biblioteca smtplib para enviar e-mails por meio de um servidor SMTP. Um loop infinito verifica
a página a cada 5 minutos e notifica por e-mail se um erro for detectado.

Você consegue criar um executavel desse arquivo utilizando pyinstaller

Passo 1: Instalar o PyInstaller
Se você ainda não tem o PyInstaller instalado, pode fazer isso via pip:

pip install pyinstaller

Passo 2: Criar o Executável
Depois de instalar o PyInstaller, abra um terminal ou prompt de comando e navegue até o diretório onde está o seu script Python. Em seguida, execute o seguinte comando:

pyinstaller --onefile seu_script.py

Substitua seu_script.py pelo nome do seu arquivo Python.

Isso criará um diretório dist no mesmo local onde seu script Python está localizado.
Dentro dele, você encontrará o executável. O parâmetro --onefile indica que você deseja
que o PyInstaller crie um único arquivo executável.
