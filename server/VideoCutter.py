from moviepy.editor import *

def videoCutter(keyPoints, video):
    '''Cuts up the video using the key points'''
    clips = [];
    for i in keyPoints:
        # Cut the video at the given time
        clip = VideoFileClip(video).subclip(i[0], (i[0]+i[1]))
        clips.append(clip)
        
    return clips

def main():
    videoCutter([(0, 10), (20, 30), (40, 50)], 'video.mp4')

if __name__ == '__main__':
    main()