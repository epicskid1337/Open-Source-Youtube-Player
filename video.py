import subprocess
import ctypes
import os
import globals

def play():
    try:
        if globals.vidOrSong:
            subprocess.run(["vlc", "video.mp4"], check=True)
            os.remove("video.mp4")
        else:
            subprocess.run(["vlc", "audio.mp3"], check=True)
            os.remove("audio.mp3")
        
    except Exception as e:
        ctypes.windll.user32.MessageBoxW(0, "hi message the developer or open an issue on githyub with this screenshot please ", "error during playback", 0x40)
def download(video):
    try:
        subprocess.run(["yt-dlp.exe", "-o", "video.mp4", video], check=True)
    except Exception as e:
        ctypes.windll.user32.MessageBoxW(0, "hi message the developer or open an issue on githyub with this screenshot please ", "error during download", 0x40)
