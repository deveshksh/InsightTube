import streamlit as st
from video_info import GetVideo

st.title("InsightTube")

youtube_url = st.text_input("Enter YouTube Video Link")

if youtube_url:
    video_id = youtube_url.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)
    
import streamlit as st

# Add the CSS styling code
st.markdown(
    """
    <style>
    .kHtcsd {
      display: flex;
      justify-content: space-around;
      align-items: center;
      background-color: #007bff;
      color: white;
      padding: 10px 20px;
      border: none;
      cursor: pointer;
    }

    .clOxle {
      flex: 1;
    }
    </style>
    """,
    unsafe_allow_html=True
)


if st.button("Get summary"):
    transcript = GetVideo.transcript(youtube_url)
    st.write(transcript)  # Displaying the transcript for now
