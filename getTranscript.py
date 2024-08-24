def fetch_transcript(video_url):
    
    from youtube_transcript_api import YouTubeTranscriptApi
    from getVideoID import get_youtube_video_id
    
    try:
        video_id = get_youtube_video_id(video_url)
        if not video_id:
            print("Invalid YouTube URL.")
            return None

        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        
        # Join the transcript parts into a single string
        full_transcript = "\n".join([entry['text'] for entry in transcript])
        
        return full_transcript
    except Exception as e:
        print(f"Error: {e}")
        return None