from tkinter import*

from PIL import Image, ImageTk

import pygame
from pygame import mixer

import os

co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#3fb5a3"  # verde
co3 = "#2e2d2c"  # black
co4 = "#403d3d"   # letra
co5 = "#4a88e8"  # Azul / Bblue

janela = Tk()
janela.title("")
janela.geometry('352x255')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

frame_esquerda = Frame(janela,width=150, height=150, bg=co3)
frame_esquerda.grid(row=0, column=0, pady=1, padx=1, sticky=NSEW)

frame_direita = Frame(janela,width=250, height=150, bg=co3)
frame_direita.grid(row=0, column=1, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela,width=404, height=100, bg=co3)
frame_baixo.grid(row=1, column=0, columnspan=3 ,pady=1, padx=0, sticky=NSEW)

# configurando o frame esquerda

img_1 = Image.open('icon1.png')
img_1 = img_1.resize((130,130))
img_1 = ImageTk.PhotoImage(img_1)

l_logo = Label(frame_esquerda, height=130, image=img_1, compound=LEFT, padx=0, anchor='nw', font=('ivy 16 bold'), bg=co3, fg=co3)
l_logo.place(x=14, y=15)

def play_musica():
    rodando = listbox.get(ACTIVE)
    l_rodando['text'] = rodando
    mixer.music.load(rodando)
    mixer.music.play()

def pausar_musica():
    mixer.music.pause()

def continuar_musica():
    mixer.music.unpause()

def parar_musica():
    mixer.music.stop()   

def proxima_musica():
    tocando = l_rodando['text']
    index = musicas.index(tocando)

    novoindex = index + 1
    tocando = musicas[novoindex]

    mixer.music.load(tocando)
    mixer.music.play()

    listbox.delete(0,END)

    mostrar()

    listbox.select_set(novoindex)
    listbox.config(selectmode=SINGLE)
    l_rodando['text'] = tocando

def anterior_musica():
    tocando = l_rodando['text']
    index = musicas.index(tocando)

    novoindex = index - 1
    tocando = musicas[novoindex]

    mixer.music.load(tocando)
    mixer.music.play()

    listbox.delete(0,END)

    mostrar()

    listbox.select_set(novoindex)
    listbox.config(selectmode=SINGLE)
    l_rodando['text'] = tocando

def aum_vol():
    atual = mixer.music.get_volume()
    mixer.music.set_volume(atual + 0.05)

def dim_vol():
    atual = mixer.music.get_volume()
    mixer.music.set_volume(atual - 0.05)



lista = ['joao', 'futi', 'muanda','joao', 'futi', 'muanda','joao', 'futi', 'muanda','joao', 'futi', 'muanda']

listbox = Listbox(frame_direita, width=22, height=10, selectmode=SINGLE, font=('arial 9 bold'), bg=co3, fg=co1)
listbox.grid(row=0, column=0)

s = Scrollbar(frame_direita)
s.grid(row=0, column=1, sticky=NSEW)

listbox.config(yscrollcommand=s.set)
s.config(command=listbox.yview)



l_rodando = Label(frame_baixo, text='Escolha uma música na lista', width=44, justify=LEFT, anchor='nw', font=('ivy 10'), bg=co1, fg=co4)
l_rodando.place(x=0, y=1)

img_2 = Image.open('2.png')
img_2 = img_2.resize((30,30))
img_2 = ImageTk.PhotoImage(img_2)

b_anterior = Button(frame_baixo, command=anterior_musica, width=40, height=40, image=img_2, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=co3, fg=co1)
b_anterior.place(x=15, y=35)

img_3 = Image.open('3.png')
img_3 = img_3.resize((30,30))
img_3 = ImageTk.PhotoImage(img_3)

b_play = Button(frame_baixo, command=play_musica , width=40, height=40, image=img_3, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=co3, fg=co1)
b_play.place(x=61, y=35)

img_4 = Image.open('4.png')
img_4 = img_4.resize((30,30))
img_4 = ImageTk.PhotoImage(img_4)

b_proxima = Button(frame_baixo, command=proxima_musica, width=40, height=40, image=img_4, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=co3, fg=co1)
b_proxima.place(x=107, y=35)

img_5 = Image.open('5.png')
img_5 = img_5.resize((30,30))
img_5 = ImageTk.PhotoImage(img_5)

b_pausar = Button(frame_baixo, command=pausar_musica, width=40, height=40, image=img_5, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=co3, fg=co1)
b_pausar.place(x=153, y=35)

img_6 = Image.open('6.png')
img_6 = img_6.resize((30,30))
img_6 = ImageTk.PhotoImage(img_6)

b_continuar = Button(frame_baixo, command=continuar_musica, width=40, height=40, image=img_6, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=co3, fg=co1)
b_continuar.place(x=199, y=35)

img_7 = Image.open('7.png')
img_7 = img_7.resize((30,30))
img_7 = ImageTk.PhotoImage(img_7)

b_stop = Button(frame_baixo, command=parar_musica,  width=40, height=40, image=img_7, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=co3, fg=co1)
b_stop.place(x=245, y=35)

img_8 = Image.open('8.png')
img_8 = img_8.resize((25,25))
img_8 = ImageTk.PhotoImage(img_8)

b_volm = Button(frame_baixo, command=aum_vol,  width=40, height=20, image=img_8, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=co3, fg=co1)
b_volm.place(x=300, y=30)

img_9 = Image.open('9.png')
img_9 = img_9.resize((25,25))
img_9 = ImageTk.PhotoImage(img_9)

b_voln = Button(frame_baixo, command=dim_vol,  width=40, height=20, image=img_9, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=co3, fg=co1)
b_voln.place(x=300, y=60)

os.chdir(r'C:\Users\noteb\Desktop\music_player\Musica')
musicas = os.listdir()

def mostrar():
    for i in musicas:
        listbox.insert(END,i)

mostrar()

mixer.init()

janela.mainloop()