def suppy_transcript():
    from getTranscript import fetch_transcript

    video_url = input("Please enter your youtube video URL")
    # file_name = input("Enter File Name")
    transcript = fetch_transcript(video_url)

    if transcript:
        return transcript
    else:
        print("Failed to fetch transcript.")

