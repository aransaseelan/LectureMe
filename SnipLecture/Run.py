from VideoFile import getYoutubeLink
from TranscriptAPI import videoTranscript
from MainPointsAPI import MainPoints
from VideoCutter import videoCutter
'''Runner of the Python program.'''

def main():
    '''Goes to VideoFile which gets the youtube link from the user'''
    youtubeLink = getYoutubeLink()
    '''Goes to TranscriptAPI which extracts the transcript from the video with time stamps'''
    transcript = videoTranscript(youtubeLink)
    '''Goes to OpenAI API which will determine the key points of the video transcript'''
    mainPoints = MainPoints(transcript)
    '''Cuts up the video using the key points'''
    VideoCutter = VideoCutter(mainPoints)
    
    
if __name__ == '__main__':
    main()