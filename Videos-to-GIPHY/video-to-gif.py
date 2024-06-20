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

def extract_segment(ffmpeg_path, input_file, output_file, start_time, duration, frame_rate=10, resolution='320:-1'):
    command = [
        ffmpeg_path,
        '-i', input_file,
        '-ss', start_time,
        '-t', duration,
        '-vf', f'fps={frame_rate},scale={resolution}',
        '-c:v', 'gif',
        '-preset', 'slow',
        output_file
    ]
    subprocess.run(command)

def process_video():
    youtube_url = url_entry.get()
    start_time = start_time_entry.get()
    duration = duration_entry.get()
    frame_rate = frame_rate_entry.get()  # New: Get frame rate input
    resolution = resolution_entry.get()  # New: Get resolution input
    output_file = 'output-v2.gif'
    download_path = '.'
    ffmpeg_path = 'C:\\ffmpeg-7.0.1-essentials_build\\ffmpeg-7.0.1-essentials_build\\bin\\ffmpeg.exe'
    
    try:
        # Download the video from YouTube
        input_file = download_youtube_video(youtube_url, download_path)
        
        # Extract segment and convert to GIF with custom frame rate and resolution
        extract_segment(ffmpeg_path, input_file, output_file, start_time, duration, frame_rate, resolution)
        
        messagebox.showinfo("Success", "GIF created successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI setup
root = tk.Tk()
root.title("YouTube to GIF Converter")

# Step 1: Improve User Interface
tk.Label(root, text="YouTube URL").grid(row=0)
tk.Label(root, text="Start Time (HH:MM:SS)").grid(row=1)
tk.Label(root, text="Duration (seconds)").grid(row=2)
tk.Label(root, text="Frame Rate").grid(row=3)  # New: Frame rate label
tk.Label(root, text="Resolution (W:H)").grid(row=4)  # New: Resolution label

url_entry = tk.Entry(root)
start_time_entry = tk.Entry(root)
duration_entry = tk.Entry(root)
frame_rate_entry = tk.Entry(root)  # New: Frame rate entry
resolution_entry = tk.Entry(root)  # New: Resolution entry

url_entry.grid(row=0, column=1)
start_time_entry.grid(row=1, column=1)
duration_entry.grid(row=2, column=1)
frame_rate_entry.grid(row=3, column=1)  # New: Frame rate entry
resolution_entry.grid(row=4, column=1)  # New: Resolution entry

# Step 2: Add Basic Customization Options

# Default values for frame rate and resolution
frame_rate_entry.insert(0, "10")
resolution_entry.insert(0, "320:-1")

tk.Button(root, text="Convert to GIF", command=process_video).grid(row=5, column=1, pady=4)

root.mainloop()
