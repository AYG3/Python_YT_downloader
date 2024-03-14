import tkinter
import customtkinter
from pytube import YouTube


def beginDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        vid = ytObject.streams.get_audio_only()
        vidtitle = ytObject.title
        title.configure(text=vidtitle)
        vid.download()
        print(vid)
    except:
        print('Error')



#System settings
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')

#initializing our window
app = customtkinter.CTk()
app.geometry('720x480')
app.title("YT Downloader - AYG3")

#Title
title = customtkinter.CTkLabel(app, text='Youtube Video')
title.pack()

#Link
url_link = tkinter.StringVar()
link = customtkinter.CTkEntry(app, textvariable=url_link, width=300)
link.pack(padx=10, pady=10)

#Download button
button = customtkinter.CTkButton(app, text='Download', command=beginDownload)
button.pack()

app.mainloop()