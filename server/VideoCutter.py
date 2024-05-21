
import os
os.environ["IMAGEIO_FFMPEG_EXE"] = "/opt/homebrew/bin/ffmpeg"
from moviepy.editor import *


def videoCutter(video, keyPoints):
    '''Cuts up the video using the key points'''
    clips = []
    for i in keyPoints:
        # Cut the video at the given time
        clip = VideoFileClip(video).subclip(i[0], (i[0]+i[1]))
        clips.append(clip)
        
    return clips

<<<<<<< Updated upstream
# def main():
#     clips = videoCutter('../server/test-assets/recording1.mp4', [(0, 10), (10,10)]);
#     clips[0].write_videofile("clip1.mp4")
#     clips[1].write_videofile("clip2.mp4")

=======
def main():
    clips = videoCutter('frontend/lectureme/public/test-assets', [(3, 10), (20,13), (40, 17), (60, 6), (80, 9)]);
    # clips[0].write_videofile("clip1.mp4")
    # clips[1].write_videofile("clip2.mp4")
    for i in range(len(clips)):
        clips[i].write_videofile(f'clip{i}.mp4')
>>>>>>> Stashed changes

# if __name__ == '__main__':
#     main()
