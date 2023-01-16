from baixar_music import baixar_musica, pesquisar_video

def PegarMusica(string=str):
    if len(string) > 0:
        if '!musica' in string:
            if not string == '!musica':
                string = string.split('!musica')
                return ''.join(string).strip()
            else:
                print('Digite algo após o comando..')
                return False
        else:
            return False

print(PegarMusica('!musica bury me alive'))
baixar_musica(pesquisar_video(PegarMusica('!musica bury me alive')))
