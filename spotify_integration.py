import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
import random

load_dotenv()

def create_spotify_client():
    """Create and return Spotify OAuth manager and authentication URL."""
    scope = "playlist-modify-public user-library-read"
    
    sp_oauth = SpotifyOAuth(
        client_id=os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI"),
        scope=scope,
        cache_path=None
    )
    
    auth_url = sp_oauth.get_authorize_url()
    return sp_oauth, auth_url

def get_mood_seeds(mood):
    """Return genre and keyword seeds based on detected mood."""
    mood_mappings = {
        "happy": {
            "genres":  ["pop", "dance", "feel-good", "funk", "indie pop"],
            "keywords":  ["upbeat", "joy", "cheerful", "energizing", "positive", "carefree", "celebratory", "optimistic"],
        },
        "sad": {
            "genres":  ["sad", "acoustic", "melancholic", "blues", "slow ballads"],
            "keywords":  ["heartbreak", "grief", "loneliness", "melancholy", "reflection", "nostalgia", "emotional", "soulful"],
        },
        "angry": {
            "genres": ["metal", "rock", "punk", "hardcore", "industrial", "rap", "grunge"],
            "keywords":  ["rage", "powerful", "intense", "rebellious", "aggressive"],
        },
        "surprise": {
            "genres": ["pop", "electronic", "dance", "experimental", "future bass", "trap"],
            "keywords":  ["exciting", "unexpected", "energetic", "shocking", "vibrant", "playful", "adventurous", "thrilling"],
        },
        "fear": {
            "genres": ["dark-ambient", "atmospheric", "industrial", "synthwave", "gothic", "psychedelic", "horror soundtrack"],
            "keywords": ["atmospheric", "mysterious", "intense", "uneasy", "unsettling", "tense", "suspense", "horror", "dark"],
        },
        "neutral": {
            "genres": ["indie", "alternative", "chill", "lo-fi", "soft rock", "acoustic"],
            "keywords":  ["chill", "relaxing", "balanced", "calm", "grounded", "focused", "instrumental", "piano"],
        }
    }
    return mood_mappings.get(mood.lower(), mood_mappings["neutral"])

def create_playlist(mood, token_info):
    """Create a playlist based on the detected mood using the provided token."""
    if not token_info or 'access_token' not in token_info:
        raise ValueError("Invalid or missing Spotify authentication token")

    try:
        # Create Spotify client with the token
        sp = spotipy.Spotify(auth=token_info['access_token'])
        
        # Get mood-specific seeds
        mood_seeds = get_mood_seeds(mood)
        
        # Try multiple search strategies
        tracks = set()
        
        # Strategy 1: Search using genres
        for genre in mood_seeds["genres"]:
            try:
                recommendations = sp.recommendations(
                    seed_genres=[genre],
                    limit=5,
                    target_valence=0.8 if mood.lower() == "happy" else 0.2 if mood.lower() == "sad" else 0.5
                )
                for track in recommendations["tracks"]:
                    tracks.add(track["uri"])
            except Exception as e:
                print(f"Error getting recommendations for genre {genre}: {e}")
                continue

        # Strategy 2: Search using keywords
        for keyword in mood_seeds["keywords"]:
            try:
                results = sp.search(
                    q=f"{keyword}",
                    type="track",
                    limit=5,
                    market="US"
                )
                for track in results["tracks"]["items"]:
                    tracks.add(track["uri"])
            except Exception as e:
                print(f"Error searching for keyword {keyword}: {e}")
                continue

        # Convert tracks set to list and shuffle
        track_list = list(tracks)
        random.shuffle(track_list)
        
        # Create new playlist
        user_id = sp.current_user()["id"]
        playlist = sp.user_playlist_create(
            user_id,
            f"Your {mood.capitalize()} Mood Mix",
            description=f"Custom playlist generated based on your {mood} mood"
        )
        
        # Add tracks to playlist
        if track_list:
            sp.playlist_add_items(playlist["id"], track_list[:30])  # Limit to 30 tracks
            return playlist["external_urls"]["spotify"]
        
        # Fallback to curated playlists if no tracks found
        fallback_playlists = {
            "happy": "37i9dQZF1DXdPec7aLTmlC",
            "sad": "37i9dQZF1DX7qK8ma5wgG1",
            "angry": "37i9dQZF1EIhuf6Y9zbnVa",
            "surprise": "37i9dQZF1EIhq2vQuxpBQS",
            "fear": "37i9dQZF1EIhtBm8L7FW0x",
            "neutral": "37i9dQZF1DX3rxVfibe1L0"
        }
        return f"https://open.spotify.com/playlist/{fallback_playlists.get(mood.lower(), '37i9dQZF1DX3rxVfibe1L0')}"
        
    except Exception as e:
        print(f"Error creating playlist: {e}")
        raise Exception(f"Failed to create playlist: {str(e)}")