from flask import Flask, request, jsonify, current_app
import os
from pytube import YouTube


def get_link():
    print("Please enter the link of the video you would like to upload: ")
    youtubeLink = input()
    download_video(youtubeLink)

def download_video(youtubeLink):
    
    yt = YouTube(youtubeLink)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if stream:
        return True, None
    else:
        return False, "Failed to download video"


if __name__ == '__main__':
    app.run(debug=True)

