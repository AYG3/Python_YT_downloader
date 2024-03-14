import tkinter
import customtkinter
from pytube import YouTube


def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()

        # vidtitle = ytObject.title
        # videotitle.configure(text=vidtitle)
        title.configure(text=ytObject.title)
        finishLabel.configure(text='')
        video.download()
        finishLabel.configure(text='Download Complete')
    except:
        finishLabel.configure('Download Failed', text_color='red')
    
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_dowloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_dowloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()

    #Update progress bar
    progressBar.set(float(percentage_of_completion) / 100)


#System settings
customtkinter.set_appearance_mode('Dark')
customtkinter.set_default_color_theme('blue')


# Our app frame
app = customtkinter.CTk() #Initializes
app.geometry('720x480') #Size / resolution of the 
app.title("Youtube downloader")

#Display video title
# videotitle = customtkinter.CTkLabel(app, text='')
# videotitle.pack()

#Adding UI elements
title = customtkinter.CTkLabel(app, text='Insert a youtube link')
title.pack(padx=10, pady=10 )

#link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

#Finished Dowloading
finishLabel = customtkinter.CTkLabel(app, text='')
finishLabel.pack()

#Download button
download = customtkinter.CTkButton(app, text='Download', command=startDownload)
download.pack(padx=10, pady=10)

#Progress Bar
pPercentage = customtkinter.CTkLabel(app, text='0%')
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

#Run app - kinda running it as a loop
app.mainloop()