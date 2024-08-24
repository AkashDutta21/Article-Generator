import streamlit as st
from getTranscript import fetch_transcript
from generateOutput import generate_output

# streamlit App
st.header(":red[Youtube] Video to :blue[Article] Generator")

video_url = st.text_input("Enter the YouTube video URL:")


if st.button("Generate"):
    if video_url:
        
        transcript = fetch_transcript(video_url)
        
        if transcript:
            st.write("Transcript fetched successfully. Generating article...")
            article = generate_output(transcript)
            st.subheader("Generated Article:")
            st.write(article)
        else:
            st.error("Failed to fetch transcript. Please check the URL.")