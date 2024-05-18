from VideoFile import upload_video
from TranscriptAPI import videoTranscript
from MainPointsAPI import MainPoints
from VideoCutter import videoCutter
'''Runner of the Python program.'''

# def main(youtubeLink):
def get_clipped_videos(youtube_link):
    # '''Goes to VideoFile which gets the youtube link from the user'''
    # youtubeLink = getYoutubeLink()

    '''Goes to TranscriptAPI which extracts the transcript from the video with time stamps'''
    transcript = videoTranscript(youtube_link)

    '''Goes to OpenAI API which will determine the key points of the video transcript'''
    mainPoints = MainPoints(transcript)
    
    '''Cuts up the video using the key points'''
    VideoCutter = VideoCutter(youtube_link, mainPoints)
    