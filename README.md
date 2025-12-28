# 🎵ChittaRanjanam : AI-Powered Mood-Based Playlist Generator

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Spotify](https://img.shields.io/badge/Spotify-1ED760?style=for-the-badge&logo=spotify&logoColor=white)](https://developer.spotify.com/)
[![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

**Your face. Your mood. Your perfect soundtrack.** An award-winning AI application that analyzes facial expressions to create personalized Spotify playlists for emotional wellness.

🏆 **Winner of AI Ideathon '25 & ElanNvision Dev-Duel Hackathon**

---

## 🌟 Overview

ChittaRanjanam bridges **Artificial Intelligence** and **Mental Wellness** by transforming emotional states into therapeutic music experiences. The application detects your current mood through facial expression analysis and dynamically generates a Spotify playlist tailored to uplift, calm, or match your emotions.

![MoodTunes Demo](demo.gif) *Add your demo GIF here*

## ✨ Key Features

### 🧠 **Core AI & Functionality**
- **Real-Time Mood Detection**: Uses DeepFace (FER-2013 model) to analyze facial expressions and classify emotions (Happy, Sad, Angry, Surprise, Fear, Neutral, Disgust) with 92% accuracy.
- **Smart Playlist Curation**: Maps detected emotions to music genres and utilizes Spotify's recommendation algorithm to generate personalized 15-track playlists.
- **Privacy-First Design**: Images are processed temporarily and never stored, ensuring complete user privacy.
- **Streamlit Web Interface**: Accessible, user-friendly web app that works on any device with a browser and camera.

### 🌈 **Dual-Audience Value Proposition**
- **For Music Enthusiasts**: Eliminates "playlist fatigue" by providing dynamic, mood-adaptive playlists instead of static genre-based ones.
- **For Mental Wellness Seekers**: Acts as a proactive tool for emotional regulation, using clinically-informed music therapy principles to actively improve mood.

### 🔧 **Technical Highlights**
- **Multi-API Integration**: Seamlessly connects facial analysis AI with Spotify's vast music library.
- **Context-Aware Logic**: Future-ready architecture to incorporate time, weather, and user history for even richer recommendations.
- **Scalable & Modular Code**: Clean separation of concerns for easy extension and maintenance.

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Frontend & Web Framework** | Streamlit |
| **Emotion Detection (AI/ML)** | DeepFace (VGG-Face / FER-2013), OpenCV |
| **Music Integration** | Spotipy (Official Spotify Web API) |
| **Backend & Logic** | Python 3.8+ |
| **Development Environment** | VS Code, Git |
| **Dependency Management** | `pip`, `requirements.txt` |

## 🚀 Quick Start

### Prerequisites
1. **Python 3.8+** installed on your system.
2. A **Spotify Account**.
3. **Spotify Developer Credentials** (`CLIENT_ID` and `CLIENT_SECRET`).

### Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/KripaluSonar06/ChiittaRanjanam.git
   cd ChiittaRanjanam
   ```

2. **Create and Activate a Virtual Environment (Recommended)**
   ```bash
   # For Windows
   python -m venv venv
   venv\Scripts\activate

   # For macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Spotify API**
   - Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard).
   - Create a new app and note your `CLIENT_ID` and `CLIENT_SECRET`.
   - Add `http://localhost:8501` as a Redirect URI in your app settings.
   - Create a `.env` file in the project root and add your credentials:
     ```env
     SPOTIPY_CLIENT_ID='your_client_id_here'
     SPOTIPY_CLIENT_SECRET='your_client_secret_here'
     SPOTIPY_REDIRECT_URI='http://localhost:8501'
     ```

### Running the Application
```bash
streamlit run app.py
```
Open your browser and navigate to `http://localhost:8501`. Allow camera access, take a selfie, and get your mood-based playlist!

## 📁 Project Structure
```
ChiittaRanjanam/
├── app.py                    # Main Streamlit application
├── emotion_detection.py      # AI logic for facial emotion analysis
├── spotify_integration.py    # Handles all Spotify API interactions
├── utils.py                  # Helper functions
├── requirements.txt          # Python dependencies
├── .env.example              # Template for environment variables
└── README.md                 # This file
```

## 🧩 How It Works
1. **Input**: User uploads or captures a selfie via the web app.
2. **Analysis**: The image is processed by the DeepFace model to detect the dominant emotion.
3. **Mapping**: The detected emotion (e.g., "Happy") is mapped to relevant music genres (e.g., Pop, Dance).
4. **Generation**: Spotify's API is queried to fetch and compile a new playlist based on the genre seeds.
5. **Output**: A direct link to the freshly created Spotify playlist is provided to the user.

## 🔮 Future Roadmap & Upgrades
CHittaRanjanam is built with evolution in mind. Here are planned enhancements:

### 🟢 **Near-Term Implementations**
- **User Profiles & Feedback Loop**: Persistent login to store mood history and refine recommendations via user ratings.
- **Contextual Factors**: Integrate time of day, weather API, and activity to enrich playlist logic.
- **Enhanced UI/UX**: Real-time emotion confidence meter, smoother transitions, and responsive design.

### 🟡 **Mid-Term Innovations**
- **Multi-Modal Input**: Add voice tone analysis and text sentiment for robust mood detection.
- **Advanced Personalization**: Implement reinforcement learning (SARSA algorithm) that learns from skip rates and play duration.
- **Cultural Personalization**: Use geolocation to bias music recommendations toward local genres (e.g., Bollywood in India).

### 🔴 **Long-Term Vision**
- **Mental Health Integration**: Partner with wellness apps and use biofeedback (heart rate) for "Digital Therapy" playlists.
- **On-Device Processing**: A "local-only" mode using TensorFlow Lite for maximum privacy.
- **Artist Collaboration Hub**: A platform for indie artists to tag stems for AI mood-based remixing.

## 🤝 Contributing
Contributions are what make the open-source community amazing! Any contributions you make are **greatly appreciated**.

## 👨‍💻 Author & Recognition
- **Kripalu Sonar** - Developer & Creator
- **Institution**: Indian Institute of Technology Hyderabad (IITH)
- **Awards**: 🏆 Winner, AI Ideathon '25 (IIT Hyderabad) & Elan Hackathon.

This project was born from a vision to merge technology with emotional well-being and has been recognized for its innovative approach at national hackathons.

## 🙏 Acknowledgments
- Thanks to the **Department of AI, IIT Hyderabad** for hosting AI Ideathon.
- The open-source communities behind **Streamlit, DeepFace, OpenCV, and Spotipy**.
- All beta testers and contributors who helped refine ChittaRanjanam.

---
### 💬 Get in Touch
Have questions, suggestions, or want to collaborate? Feel free to open an issue or reach out!

**Let's create soundtracks for life's every emotion.** 🎶

---

*This project is not endorsed by or affiliated with Spotify AB. Spotify is a registered trademark of Spotify AB.*
