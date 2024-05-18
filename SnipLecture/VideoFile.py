'''Uploading of the video file to the server'''

from flask import Flask, request, jsonify

'''The youtube link is put in the form of a string'''
'''May need to download the video so that we can clip the parts?'''
def getYoutubeLink():
    youtube_link = request.form['input']
    print(youtube_link)
    return youtube_link

'''Calls the API which gets a youtube link and extracts the transcript from the video'''

   