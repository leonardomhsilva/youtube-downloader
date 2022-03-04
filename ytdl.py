from sqlite3 import Row
import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import filedialog, messagebox



def createWidgets():

    link_label = Label(root, text="Link do Vídeo:  ", font="arial 10 bold", bg="#FFE4E1")
    link_label.grid(row=1, column=0, pady=5, padx=5)

    root.link_text = Entry(root, width=60, textvariable=video_link)
    root.link_text.grid(row=1,column=1, pady=5, padx=5)

    destination_label = Label(root, text="Destino:  ",font="arial 10 bold", bg="#FFE4E1")
    destination_label.grid(row=2, column=0, pady=5, padx=5)

    root.destination_text = Entry(root, width=45, textvariable=download_path)
    root.destination_text.grid(row=2, column=1, pady=3, padx=3)

    browse_but = Button(root, text="Procurar",font="impact 10", command=browse , width=12, bg="#B22222")
    browse_but.grid(row=2, column=2, pady=1, padx=1)

    download_but = Button(root, text="Baixar",font="Arial 12 bold", command=download_video, width=25, bg="#800000")
    download_but.grid(row=3, column=1, pady=3, padx=3 )

def browse():

    download_dir = filedialog.askdirectory(initialdir="Sua pasta")

    download_path.set(download_dir)

def download_video():

    url = video_link.get()
    folder = download_path.get()

    get_video = YouTube(url)
    get_stream = get_video.streams.get_highest_resolution()
    get_stream.download(folder)

    messagebox.showinfo("Download bem Sucedido!!", "Você vai encontrar seu vídeo em\n"+folder)

root = tk.Tk()

root.geometry("600x120")
root.resizable(False, False)
root.title("Youtube Downloader")
root.config(background="#FFE4E1")
root.wm_iconbitmap("coffe.ico")



video_link = StringVar()
download_path = StringVar()

createWidgets()

root.mainloop()