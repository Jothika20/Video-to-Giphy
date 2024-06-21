### README.md

---

# YouTube to GIF Converter

This application allows you to download a YouTube video, extract a segment from it, and convert that segment into a GIF with customizable frame rate and resolution using `ffmpeg`.

## Requirements

Before running this script, ensure you have the following installed:

- Python 3.x
- `pytube` library
- `tkinter` library
- `ffmpeg`

## Installation

1. **Install Python Libraries**

   Open your terminal (or Command Prompt) and run:

   ```sh
   pip install pytube
   ```

2. **Download and Install `ffmpeg`**

   - Download the `ffmpeg` essentials build from [here](https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip).
   - Extract the downloaded zip file to a directory, e.g., `C:\ffmpeg-7.0.1-essentials_build`.
   - Ensure the path to `ffmpeg.exe` (e.g., `C:\ffmpeg-7.0.1-essentials_build\ffmpeg-7.0.1-essentials_build\bin\ffmpeg.exe`) is correctly specified in the script.

## Usage

1. **Clone or Download the Repository**

   Download the script file or clone this repository to your local machine.

2. **Run the Script**

   Open a terminal (or Command Prompt) in the directory where the script is located and execute:

   ```sh
   python your_script_name.py
   ```

   Replace `your_script_name.py` with the actual name of your script file.

3. **Fill in the Details in the GUI**

   - **YouTube URL:** Enter the URL of the YouTube video you want to convert to a GIF.
   - **Start Time (HH:MM:SS):** Enter the start time of the segment you want to convert.
   - **Duration (seconds):** Enter the duration of the segment.
   - **Frame Rate:** Enter the desired frame rate for the GIF. Default is 10.
   - **Resolution (W:H):** Enter the desired resolution for the GIF. Default is `320:-1` (which maintains aspect ratio).

4. **Convert to GIF**

   Click the "Convert to GIF" button. The script will download the video, extract the specified segment, and convert it to a GIF.

## Troubleshooting

- Ensure all dependencies are installed correctly.
- Verify the `ffmpeg` path is correct in the script.
- If you encounter any issues, ensure you have an active internet connection for downloading YouTube videos.

## Example

1. Enter `https://www.youtube.com/watch?v=dQw4w9WgXcQ` in the YouTube URL field.
2. Enter `00:00:10` for Start Time.
3. Enter `10` for Duration.
4. Enter `15` for Frame Rate (optional).
5. Enter `320:240` for Resolution (optional).

Click "Convert to GIF" and wait for the process to complete. The GIF will be saved as `output-v2.gif` in the script's directory.
