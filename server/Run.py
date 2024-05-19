from VideoFile import get_link
from TranscriptAPI import videoTranscript
from MainPointsAPI import MainPoints
from VideoCutter import videoCutter
'''Runner of the Python program.'''
def main():
    get_clipped_videos("https://www.youtube.com/watch?v=JGwWNGJdvx8")
    
def get_clipped_videos(youtube_link):
    # '''Goes to VideoFile which gets the youtube link from the user'''
    youtubeFile = get_link(youtube_link)

    '''Goes to TranscriptAPI which extracts the transcript from the video with time stamps'''
    transcript = videoTranscript(youtube_link)

    '''Goes to OpenAI API which will determine the key points of the video transcript'''
    mainPoints = MainPoints(transcript)

    '''Cuts up the video using the key points'''
    trimmed_video = videoCutter(youtubeFile, mainPoints)
    
if __name__ == '__main__':
    main()