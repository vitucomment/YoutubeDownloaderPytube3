from pytube import YouTube as yt

endereco = str(input('Digite o endereço do video: '))

video = yt(endereco)

# Titulo do video
print(f'Titulo: {video.title}')
# Visualizações
print(f'Nº de visualizações: {video.views}')
# Duração
print(f'Duração: {video.length}')
# Descrição do video
print(f'Descrição: {video.description}')

# Melhor qualidade
video_q = video.streams.get_highest_resolution()

video_q.download('Downloads')
