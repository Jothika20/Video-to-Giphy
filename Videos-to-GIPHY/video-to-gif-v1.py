import subprocess
from pytube import YouTube
import os

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

def main():
    youtube_url = 'https://youtu.be/9jWK9ZIN86Y?si=rKSPI7dCF-7otCVV'  # Replace with your YouTube video URL
    download_path = '.'  # Path where the video will be downloaded
    output_file = 'output.gif'
    start_time = '00:00:10'  # Start time of the segment (e.g., 10 seconds)
    duration = '5'  # Duration of the segment (e.g., 5 seconds)
    ffmpeg_path = 'C:\\ffmpeg-7.0.1-essentials_build\\ffmpeg-7.0.1-essentials_build\\bin\\ffmpeg.exe'  # Full path to ffmpeg.exe

    # Download the video from YouTube
    input_file = download_youtube_video(youtube_url, download_path)

    # Extract segment and convert to GIF
    extract_segment(ffmpeg_path, input_file, output_file, start_time, duration)

if __name__ == "__main__":
    main()
