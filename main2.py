import tkinter
import customtkinter
from pytube import YouTube

#System settings
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')

#initializing our window
app = customtkinter.CTk()
app.geometry('720x480')
app.title("YT Downloader - AYG3")

#Title
title = customtkinter.CTkLabel(app, text='')
title.pack()

#Link
url_link = tkinter.StringVar()
link = customtkinter.CTkEntry(app, textvariable=url_link, width=300)
link.pack(padx=10, pady=10)

#Download button
button = customtkinter.CTkButton(app, text='Download')
button.pack()

app.mainloop()