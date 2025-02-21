import streamlit as st
from emotion_detection import detect_emotion
from spotify_integration import create_spotify_client, create_playlist
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize session state for Spotify authentication
if 'spotify_auth_url' not in st.session_state:
    st.session_state.spotify_auth_url = None
if 'spotify_token_info' not in st.session_state:
    st.session_state.spotify_token_info = None

# Streamlit title
st.title("चित्तरंजनम् - Mood Based Playlist Generator 🎵")

# Initialize Spotify client if not already done
if 'sp_oauth' not in st.session_state:
    sp_oauth, auth_url = create_spotify_client()
    st.session_state.sp_oauth = sp_oauth
    st.session_state.spotify_auth_url = auth_url

# Check for Spotify authentication
if not st.session_state.spotify_token_info:
    # Get the code from query parameters using the new syntax
    code = st.query_params.get("code", None)
    
    if code:
        # Exchange code for token
        token_info = st.session_state.sp_oauth.get_access_token(code)
        st.session_state.spotify_token_info = token_info
        st.rerun()
    else:
        st.warning("Please authenticate with Spotify first!")
        st.markdown(f"[Connect Spotify]({st.session_state.spotify_auth_url})")
        st.stop()

# File uploader
uploaded_file = st.file_uploader("Upload a selfie!")

if uploaded_file:
    # Save the uploaded file temporarily
    with open("temp.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Detect emotion from the selfie
    emotion = detect_emotion("temp.jpg")
    st.success(f"Your mood: {emotion}!")
    
    # Create a playlist based on the detected emotion
    if st.button("Generate Playlist"):
        with st.spinner("Creating your mood playlist..."):
            try:
                # Pass the token_info from session state to create_playlist
                playlist_url = create_playlist(
                    emotion, 
                    st.session_state.spotify_token_info
                )
                st.write("Here's your mood playlist!")
                st.markdown(f"[Open Playlist]({playlist_url})")
            except Exception as e:
                st.error(f"Error creating playlist: {str(e)}")