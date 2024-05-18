from youtube_transcript_api import YouTubeTranscriptApi
import re

def main():
    videoTranscript('https://www.youtube.com/watch?v=HCOQmKTFzYY&t=51s')

def videoTranscript(youtube_link):
    # Get the transcript of the video
    video_id = extract_video_id(youtube_link)
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    print(transcript)
    # print(video_id)

def extract_video_id(url):
    # Regular expression pattern to match YouTube video IDs
    pattern = re.compile(r'^.*(youtu\.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=)([^#\&\?]*).*')
    
    # Match the pattern with the given URL
    match = pattern.match(url)
    
    # Check if a match is found and the length of the video ID is 11
    if match and len(match.group(2)) == 11:
        return match.group(2)
    else:
        # Handle error (e.g., raise an exception, return None, etc.)
        return None

if __name__ == '__main__':
    main()