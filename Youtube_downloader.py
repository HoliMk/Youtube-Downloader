import tkinter as tk
from tkinter import ttk
from pytube import YouTube

def download_video():
    video_url = url_entry.get()
    output_path = output_path_entry.get()

#Get the selected resolution

    selected_resolution = resolution_var.get()
    try:
#Create a YouTube object

        yt = YouTube(video_url)

#Get the stream based on the selected resolution
        
        stream = get_stream_by_resolution(yt, selected_resolution)
        if stream:
            stream.download(output_path=output_path)
            status_label.config(text="Video downloaded successfully!")
        else:
            status_label.config(text="Selected resolution not available for this video.")

    except Exception as e:
        status_label.config(text="An error occurred: " + str(e))

#Filter streams based on the selected resolution

def get_stream_by_resolution(yt, resolution):
    stream = None
    if resolution == "Highest Resolution":
        stream = yt.streams.get_highest_resolution()
    else:
        streams = yt.streams.filter(res=resolution)
        if streams:
            stream = streams.first()
    return stream

#Main window

root = tk.Tk()
root.title("YouTube Video Downloader")

#Configure input fields and labels

url_label = ttk.Label(root, text="Enter YouTube Video URL:")
url_label.pack()
url_entry = ttk.Entry(root, width=100)
url_entry.pack()

output_path_label = ttk.Label(root, text="Enter Output Path:")
output_path_label.pack()
output_path_entry = ttk.Entry(root, width=100)
output_path_entry.pack()

#Dropdown for resolution selection

resolution_label = ttk.Label(root, text="Select Video Resolution:")
resolution_label.pack()
resolution_var = tk.StringVar(root)
available_resolutions = ["2160p", "1440p", "1080p", "720p", "480p", "360p", "240p", "144p"]
resolution_dropdown = ttk.Combobox(root, textvariable=resolution_var, values=available_resolutions)
resolution_dropdown.pack()

download_button = ttk.Button(root, text="Download Video", command=download_video)
download_button.pack()

status_label = ttk.Label(root, text="")
status_label.pack()

root.mainloop()
