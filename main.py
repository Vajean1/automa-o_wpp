from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from os import getcwd
from time import sleep
from baixar_music import baixar_musica, pesquisar_video
from chatbot import chatbot
import base64

__Variaveis = {
    'Cordialidades': ['bom dia', 'boa tarde', 'boa noite', 'tarde', 'noite', 'dia', 'eai', 'dale', 'oi', 'koe', 'salve', 'thiago'],
    'Comandos': ['!comandos', '!ola', '!comofuifeito', '!travazap'],
    'ComandosParametros' : ['!bot', '!imagem', '!musica']
}

nav = webdriver.Chrome()

nav.get('https://web.whatsapp.com/')
sleep(10)

input('Enter depois de ler o QR Code')
sleep(5)

div_chats = nav.find_element(By.XPATH, '//*[@id="pane-side"]/div[2]/div/div')   
chats = div_chats.find_elements(By.CLASS_NAME ,'_1Oe6M')

def mandar_msg(msg=str):
    bloco_msg = nav.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
    bloco_msg.send_keys(msg)
    try:
        bloco_msg.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()
    except Exception as err:
        print(err)

def mandar_img(img):
    blocofooter = nav.find_element(By.XPATH, '//*[@id="main"]/footer')
    blocofooter.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]').click()
    sleep(1)
    listaelementos = nav.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div')
    listaelementos.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[1]/button/input').send_keys(getcwd()+f'/{img}')
    sleep(1)
    painelimg = nav.find_element(By.CLASS_NAME, '_2uGbr')
    try:
        painelimg.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div').click()
    except Exception as err:
        print(err)
        pass

def mandar_audio(audio=str):
    blocofooter = nav.find_element(By.XPATH, '//*[@id="main"]/footer')
    blocofooter.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]').click()
    sleep(2)
    listaelementos = nav.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div')
    listaelementos.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[4]/button/input').send_keys(getcwd()+f'/{audio}')
    sleep(2)
    painelimg = nav.find_element(By.CLASS_NAME, '_2uGbr')
    try:
        painelimg.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div').click()
    except Exception as err:
        print(err)
        pass

def VerificarItensDoSplit(String: str, Lista: list, Split: str):
    if len(String) > 0 and " " in String:
        Separação = String.split(f"{Split}")
        for Valores in Separação:
            if Valores in Lista:
                return True
    if not " " in String:
        if String in Lista:
            return True
    return False

def VarrerComandos(string=str, comandos=list):
    if len(string) > 0:
        string = list(string)
        if string[0] == "!":
            string = ''.join(string)
            if string in comandos:
                return True
            else:
                mandar_msg('Não temos esse comando no momento..')
                return False

def ConversaComBot(string=str):
    if len(string) > 0:
        if '!bot' in string:
            if not string == '!bot':
                string = string.split('!bot')
                return ''.join(string).strip()
            else:
                mandar_msg('Digite algo após o comando..')
                return False
        else:
            return False

def PegarImagem(string=str):
    if len(string) > 0:
        if '!imagem' in string:
            if not string == '!imagem':
                string = string.split('!imagem')
                return ''.join(string).strip()
            else:
                mandar_msg('Digite algo após o comando..')
                return False
        else:
            return False
        
def PegarMusica(string=str):
    if len(string) > 0:
        if '!musica' in string:
            if not string == '!musica':
                string = string.split('!musica')
                return ''.join(string).strip()
            else:
                mandar_msg('Digite algo após o comando..')
                return False
        else:
            return False

#_2KKXC
#vQ0w7
while True:
    for c in range(len(chats)):
        if VerificarItensDoSplit(str(chats[c].find_element(By.CLASS_NAME, 'vQ0w7').text).lower(), __Variaveis['Cordialidades'], ' '):
            chats[c].click()
            mandar_msg('Olá, Eu sou o bot dele. Posso responder algumas perguntas básicas por ele... Digite a opção desejada: 0 - Preciso falar com o ele de verdade!! 1 - Quero conversar com você Bot.')
            sleep(5)
        elif str(chats[c].find_element(By.CLASS_NAME, 'vQ0w7').text).lower() == '1':
            chats[c].click()
            mandar_msg('Para falar comigo exitem alguns comandos básicos: !musica <nome_da_imagem> -> Retorna uma música !imagem <nome_da_imagem>, !travazap -> Envia travazap, !ola -> Apresentação, !comofuifeito -> Explica sobre o bot, !comandos -> Retorna alguns comandos')
            sleep(5)
        elif str(chats[c].find_element(By.CLASS_NAME, 'vQ0w7').text).lower() == '0':
            chats[c].click()
            mandar_msg('Estou chamando ele, aguarde alguns segundos, por favor..')
            sleep(5)
        elif PegarImagem(str(chats[c].find_element(By.CLASS_NAME, 'vQ0w7').text).lower()) == 'teste':
            chats[c].click()
            mandar_img('qr.png')
            sleep(10)
        elif PegarMusica(str(chats[c].find_element(By.CLASS_NAME, 'vQ0w7').text).lower()):
            chats[c].click()
            mandar_msg('Estamos iniciando o downlaod da sua música, aguarde 1 ou 2 minutos, por favor!')
            music = str(chats[c].find_element(By.CLASS_NAME, 'vQ0w7').text).lower().split('!musica')
            print(music)
            #baixar_musica(pesquisar_video(music))
            #sleep(30)
            #mandar_audio('music.mp3')
            #sleep(10)
        elif ConversaComBot(str(chats[c].find_element(By.CLASS_NAME, 'vQ0w7').text).lower()):
            chats[c].click()
            mandar_msg(chatbot(str(chats[c].find_element(By.CLASS_NAME, 'vQ0w7').text).lower().split('!bot')))
            sleep(5)
        elif VarrerComandos(str(chats[c].find_element(By.CLASS_NAME, 'vQ0w7').text).lower(), __Variaveis['Comandos']):
            if str(chats[c].find_element(By.CLASS_NAME, 'vQ0w7').text).lower() == "!comandos":
                chats[c].click()
                mandar_msg('Os comandos básicos são: !musica, !imagem, !ola, !comofuifeito')
                sleep(10)
            elif str(chats[c].find_element(By.CLASS_NAME, 'vQ0w7').text).lower() == "!ola":
                chats[c].click()
                mandar_msg('Olá, Pode me chamar de BOT, gosto de computadores. É isso aí!')
                sleep(10)
            elif str(chats[c].find_element(By.CLASS_NAME, 'vQ0w7').text).lower() == "!travazap":
                chats[c].click()
                mandar_msg(f'zoas'*50)
                sleep(10)
            elif str(chats[c].find_element(By.CLASS_NAME, 'vQ0w7').text).lower() == "!comofuifeito":
                chats[c].click()
                mandar_msg('Para mais informações sobre a minha construção acesse o github: github.com/Vajean1')
                sleep(10)        
