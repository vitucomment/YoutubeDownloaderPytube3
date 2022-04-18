import tkinter
from tkinter import *
from pytube import YouTube



interface = Tk()
interface.title('Youtube Video Downloader')
interface.geometry("600x400+300+300")
interface.configure(background='grey')

def interacoes():
    video = YouTube(ed.get())
    lb_titulo["text"] = f'Titulo: {video.title}'
    lb_views["text"] = f'Visualizações: {video.views}'
    lb_duracao["text"] = f'Duração: {video.length} segundos'
    lb_descricao["text"] = f'Descrição: {video.description}'
    return video

def download():
    video = YouTube(ed.get())
    ytvideo = video.streams.get_highest_resolution()
    ytvideo.download()
    lb_down["text"] = "Download concluido"

ed = Entry(interface)
ed.place(x=92, y=5, width=300)

lb_inter = Label(interface, text="Coloque a url: ")
lb_inter.place(x=5,y=5)
lb_titulo = Label(interface, text = "Informações" )
lb_titulo.place(x=5, y= 55)
lb_views = Label(interface, text ="Visualizações: ")
lb_views.place(x=5, y= 75)
lb_duracao = Label(interface, text="Duração: ")
lb_duracao.place(x=5, y= 95)
lb_descricao = Label(interface, text="Descrição: ", wraplength=590)
lb_descricao.place(x=5, y=115)

bt_ed = Button(interface, width=2, text="Ok", command=interacoes)
bt_ed.place(x=396, y=2)

bt_dl = Button(interface, width=15, text="Fazer download", command=download)
bt_dl.place(x=426, y=2)

lb_down = Label(interface, text="Clique para baixar")
lb_down.place(x=433, y = 30)

rolagem = tkinter.Scrollbar(interface)

interface.mainloop()