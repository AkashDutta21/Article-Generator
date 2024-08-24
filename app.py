import streamlit as st
# from getTranscript import fetch_transcript
from generateOutput import generate_output

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

# streamlit App
st.header(":red[Youtube] Video to :blue[Article] Generator")

video_url = st.text_input("Enter the YouTube video URL:")

col1, col2 = st.columns([2, 2])

# Dropdown for selecting LLM model
with col1:
    model_name = st.selectbox(
        "Choose your LLM model:",
        ("llama-3.1-8b-instant", "llama-3.1-70b-versatile", "llama3-8b-8192", "llama3-70b-8192")
    )

with col2:
    word_count = st.text_input("Enter your Article Word Count:")


if st.button("Generate"):
    if video_url:
        
        transcript = fetch_transcript(video_url)
        
        if transcript:
            st.write("Transcript fetched successfully. Generating article...")
            article = generate_output(transcript, model_name, word_count)
            st.subheader("Generated Article:")
            st.write(article)
        else:
            st.error("Failed to fetch transcript. Please check the URL.")