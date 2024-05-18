from flask import request, jsonify, current_app
import os
from pytube import YouTube


def upload_video():
    print("Please enter the link of the video you would like to upload: ")
    youtubeLink = input()
    yt = YouTube(youtubeLink)
    
    
    
    if 'video' not in request.files:
        return jsonify({"error": "No video part in the request"}), 400

    file = request.files['video']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file:
        filename = file.filename
        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        return jsonify({"message": "File uploaded successfully", "file_path": file_path}), 201

@main.route('/youtube', methods=['POST']) # POST request to download a YouTube video
def download_youtube_video():
    if 'link' not in request.form:
        return jsonify({"error": "No link part in the request"}), 400

    youtube_link = request.form['link']
    file_path = download_video(youtube_link)
    if file_path:
        return jsonify({"message": "Video downloaded successfully", "file_path": file_path}), 201
    else:
        return jsonify({"error": "Failed to download video"}), 400

def download_video(youtube_link): # Download a YouTube video
    try:
        yt = YouTube(youtube_link)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        filename = stream.default_filename
        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        stream.download(output_path=current_app.config['UPLOAD_FOLDER'])
        return file_path
    except Exception as e:
        print(f"Failed to download video: {e}")
        return None

