from deepface import DeepFace

def detect_emotion(image_path):
    try:
        # Analyze the emotion from the image
        analysis = DeepFace.analyze(image_path, actions=['emotion'])

        # Check if the analysis returned a valid result
        if analysis and isinstance(analysis, list) and len(analysis) > 0:
            # Return the detected emotion
            return analysis[0]['dominant_emotion']
        else:
            # Return a default message if no emotion is detected
            return "Neutral"

    except Exception as e:
        # Handle exceptions (like no face detected, etc.)
        print(f"Error in emotion detection: {e}")
        return "Error"
