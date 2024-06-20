import subprocess
from pytube import YouTube
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def download_youtube_video(url, output_path):
    yt = YouTube(url)
    ys = yt.streams.get_highest_resolution()
    ys.download(output_path)
    return os.path.join(output_path, ys.default_filename)

def extract_segment(ffmpeg_path, input_file, output_file, start_time, duration):
    command = [
        ffmpeg_path,
        '-i', input_file,
        '-ss', start_time,
        '-t', duration,
        '-vf', 'fps=10,scale=320:-1',
        '-c:v', 'gif',
        '-preset', 'slow',
        output_file
    ]
    subprocess.run(command)

def process_video():
    youtube_url = url_entry.get()
    start_time = start_time_entry.get()
    duration = duration_entry.get()
    output_file = 'output-v2.gif'
    download_path = '.'
    ffmpeg_path = 'C:\\ffmpeg-7.0.1-essentials_build\\ffmpeg-7.0.1-essentials_build\\bin\\ffmpeg.exe'
    
    try:
        # Download the video from YouTube
        input_file = download_youtube_video(youtube_url, download_path)
        
        # Extract segment and convert to GIF
        extract_segment(ffmpeg_path, input_file, output_file, start_time, duration)
        
        messagebox.showinfo("Success", "GIF created successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI setup
root = tk.Tk()
root.title("YouTube to GIF Converter")

tk.Label(root, text="YouTube URL").grid(row=0)
tk.Label(root, text="Start Time (HH:MM:SS)").grid(row=1)
tk.Label(root, text="Duration (seconds)").grid(row=2)

url_entry = tk.Entry(root)
start_time_entry = tk.Entry(root)
duration_entry = tk.Entry(root)

url_entry.grid(row=0, column=1)
start_time_entry.grid(row=1, column=1)
duration_entry.grid(row=2, column=1)

tk.Button(root, text="Convert to GIF", command=process_video).grid(row=3, column=1, pady=4)

root.mainloop()
