from pytube import YouTube
import os
from moviepy.editor import *
import requests

global __Variaveis
__Variaveis = {
    'titulo': '',
    'video': '',
    'playlist': []
}

def baixar_musica(link=str):
    global __Variaveis
    __Variaveis['titulo'] = YouTube(link).title
    
    def verificar():
        if os.path.exists('video.mp4'):
            os.remove('video.mp4')
        if os.path.exists(f"{__Variaveis['titulo']}.mp3"):
            os.remove(f"{__Variaveis['titulo']}.mp3")
        if os.path.exists('music.mp3'):
            os.remove('music.mp3')
            
    verificar()
    
    print('[+] Iniciando Download')
    print(f"[+] {__Variaveis['titulo']}")
    try:
        yt = YouTube(link).streams.filter(file_extension='mp4').first().download()
        if not os.path.exists('video.mp4'):
            print('[+] Iniciando processo de conversão..')
            os.rename(yt, 'video.mp4')
            vd = VideoFileClip('video.mp4')
            vd.audio.write_audiofile('audio.mp3')
            vd.close()
            os.rename('audio.mp3', 'music.mp3')
            os.remove('video.mp4')
            print('[+] Convertido!')
    except Exception as err:
        print(f'O erro está: {err}')


def pesquisar_video(nome=str):
    nome = nome.replace(' ', '+')
    pag = requests.get(f"https://www.youtube.com/results?search_query={nome}").text
    __Variaveis['video'] = str(pag).split('{"videoId":"')[1].split('"')[0]
    link = f"https://www.youtube.com/watch?v={__Variaveis['video']}"
    return link
