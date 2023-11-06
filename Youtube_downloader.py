import tkinter as tk
from tkinter import ttk
from pytube import YouTube

def download_video():
    video_url = url_entry.get()
    output_path = output_path_entry.get()
    selected_resolution = resolution_var.get()
    
    try:
        yt = YouTube(video_url)
        stream = get_stream_by_resolution(yt, selected_resolution)
        
        if stream:
            stream.download(output_path=output_path)
            status_label.config(text="Video downloaded successfully!")
        else:
            status_label.config(text="Selected resolution not available for this video.")
    except Exception as e:
        status_label.config(text="An error occurred: " + str(e))

def get_stream_by_resolution(yt, resolution):
    stream = None
    streams = yt.streams.filter(res=resolution)
    
    if streams:
        stream = streams.first()
    
    return stream

root = tk.Tk()
root.title("YouTube Video Downloader")

# Create a frame for URL input

url_frame = ttk.LabelFrame(root, text="Video URL")
url_frame.pack()
url_entry = ttk.Entry(url_frame, width=100)
url_entry.pack()

# Create a frame for output path input

output_path_frame = ttk.LabelFrame(root, text="Output Path")
output_path_frame.pack()
output_path_entry = ttk.Entry(output_path_frame, width=100)
output_path_entry.pack()

# Create a frame for resolution selection

resolution_frame = ttk.LabelFrame(root, text="Video Resolution")
resolution_frame.pack()
resolution_var = tk.StringVar(root)
available_resolutions = ["2160p", "1440p", "1080p", "720p", "480p", "360p", "240p", "144p"]
resolution_dropdown = ttk.Combobox(resolution_frame, textvariable=resolution_var, values=available_resolutions)
resolution_dropdown.pack()

download_button = ttk.Button(root, text="Download Video", command=download_video)
download_button.pack()

status_label = ttk.Label(root, text="")
status_label.pack()

root.mainloop()
