import streamlit as st
from audio_to_txt import download_audio, transcribe_audio
from summary import summarize_text_file
from caption import generate_caption
import os

def process_video(video_url):
    # Download audio from video
    audio_output_folder = "Audio"
    text_output_folder = "Text"

    audio_path = download_audio(video_url, audio_output_folder)
    transcription_path = transcribe_audio(audio_path, text_output_folder)

    # Summarize the transcription text
    summary = summarize_text_file(transcription_path)

    # Generate captions from the transcription
    caption = generate_caption(transcription_path)

    return summary, caption

# Streamlit UI setup
st.set_page_config(
    page_title="Video Captioning & Summarization",
    page_icon="🎥",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Sidebar navigation
st.sidebar.title("Navigation")
st.sidebar.write("Choose an option:")
options = st.sidebar.radio("", ["Home", "Process Video", "About"])

if options == "Home":
    # Home page
    st.title("🎥 Automatic Caption Generation and Summarization for Educational Videos")
    st.write(
        """
        **Welcome!** This app helps you generate **captions** and **summaries** for educational videos.
        - Simply paste a Video URL.
        - Let the app process the video.
        - View the generated captions and summaries!
        
        **Get started** by navigating to the **Process Video** section.
        """
    )
    #st.image("https://via.placeholder.com/800x400.png?text=Educational+Videos", use_column_width=True)
    st.image(r"C:\Users\Sonali Thakur\Downloads\firstPage.png", use_container_width=True)


elif options == "Process Video":
    # Video URL input
    st.title("📹 Process Your Video")
    st.write("Enter the video URL below to start processing.")

    video_url = st.text_input("🔗 Video URL:")
    if video_url:
        if st.button("🚀 Process Video"):
            with st.spinner("Processing video... This may take a few minutes."):
                summary, caption = process_video(video_url)

            # Display results
            st.success("Video processed successfully!")
            st.subheader("📝 Summary:")
            st.write(summary)

            st.subheader("🎬 Caption:")
            st.write(caption)

elif options == "About":
    # About page
    st.title("ℹ️ About")
    st.write(
        """
        This application is developed to assist educators and learners in generating **captions** and 
        **summaries** for educational videos using advanced AI techniques. It simplifies the process 
        of extracting meaningful content from video lectures, tutorials, or webinars.
        
        **Features:**
        - **Automatic audio transcription**
        - **Text summarization**
        - **Caption generation**

        **Tools Used:**
        - Streamlit for the user interface
        - AI models for transcription and summarization
        
        **Credits:**
        - Developed by **Sonali Thakur**(https://github.com/sonali123123)
        """
    )
    st.image(r"C:\Users\Sonali Thakur\Downloads\notion_logo.webp", width=300)

# Footer
st.sidebar.markdown("---")
st.sidebar.write("💡 Developed with ❤️ using Streamlit.")
