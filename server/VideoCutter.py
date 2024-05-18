from moviepy.editor import *

def videoCutter(keyPoints, video):
    '''Cuts up the video using the key points'''
    clips = [];
    for i in keyPoints:
        # Cut the video at the given time
        clip = VideoFileClip(video).subclip(i[0], (i[0]+i[1]))
        clips.append(clip)
        
    return clips
