from pytube import YouTube

def guarda_link(link):
    video = YouTube(link)
    return video

def mostra_titulo(video):
    titulo = video.title
    print(f'Titulo: {titulo}')

def mostra_visualizacoes(video):
    visualizacoes = video.views
    print(f'Visualizacoes: {visualizacoes}')

def mostra_duracao(video):
    duracao = video.length
    print(f'Duracao: {duracao}')

def mostra_descricao(video):
    descricao = video.description
    print(f'Descricao: {descricao}')

link = guarda_link(input('Digite o endereço: '))
mostra_titulo(link)
mostra_visualizacoes(link)
mostra_duracao(link)
mostra_descricao(link)