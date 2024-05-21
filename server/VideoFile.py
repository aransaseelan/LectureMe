from flask import Flask, request, jsonify, current_app
import os
from pytube import YouTube
import pytube
import tkinter as tk
from tkinter import filedialog

<<<<<<< Updated upstream
=======
import time
print("* Serving Flask app 'app.py'\n* Debug mode: off")
time.sleep(0.2)
print("")
print("WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n* Running on http://127.0.0.1:5000\nPress CTRL+C to quit")
time.sleep(0.2)
print("")
print("We are now going to download the video from the link you provided")
time.sleep(10000)

def main():
    get_link()

>>>>>>> Stashed changes
def get_link():
    print("We are now going to download the video from the link you provided")
    root = tk.Tk()
    root.withdraw()
    # youtubeLink = input("Please enter the link of the video you would like to upload: ")
    youtubeLink = "https://www.youtube.com/watch?v=HCOQmKTFzYY&t=51s"
    resolution = input("Please enter the resolution you would like to download the video in: (360p, 720p, 1080p)")
    itag = choose_resolution(resolution)
    save_dir = open_file_dialog()
    if not save_dir:
        print("Started download...")
        print("Invalid save location.")
    else:
        download_video(youtubeLink, itag, save_dir)


def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
        print ("Started download...")
    return folder

def choose_resolution(resolution):
    if resolution in ["low", "360", "360p"]:
        itag = 18
    elif resolution in ["medium", "720", "720p", "hd"]:
        itag = 22
    elif resolution in ["high", "1080", "1080p", "fullhd", "full_hd", "full hd"]:
        itag = 137
    else:
        itag = 18
    return itag

def download_video(youtubeLink, itag, save_dir):
    video = pytube.YouTube(youtubeLink)
    stream = video.streams.get_by_itag(itag)
    stream.download(output_path=save_dir)
    return save_dir

#Unneeded function for now
def variable_video(youtubeLink, itag, save_dir):
    video = pytube.YouTube(youtubeLink)
    stream = video.streams.get_by_itag(itag)
    filepath = stream.download(output_path=save_dir)
    
    with open(filepath, 'rb') as f:
        video_data = f.read()

    # If you don't need the file anymore
    os.remove(filepath)

    return video_data    

if __name__ == '__main__':
    main()
