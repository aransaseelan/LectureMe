from flask import Flask, request, jsonify, current_app
import os
from pytube import YouTube
import pytube
import tkinter as tk
from tkinter import filedialog

print("We are now going to download the video from the link you provided")

def get_link(youtube_link):
    root = tk.Tk()
    root.withdraw()
    # youtubeLink = input("Please enter the link of the video you would like to upload: ")
    resolution = input("Please enter the resolution you would like to download the video in: (360p, 720p, 1080p)")
    itag = choose_resolution(resolution)
    save_dir = open_file_dialog()
    if not save_dir:
        print("Started download...")
        print("Invalid save location.")
    else:
        # download_video(youtubeLink, itag, save_dir) 
        download_video(youtube_link, itag, save_dir)

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