
import azure.cognitiveservices.speech as speechsdk
import os

# Azure Speech service credentials
speech_key = "8vCfO6vj2tnzHNjtrrmFX9NJmCNNpouBa8VNKenexNM5z4ntVlhPJQQJ99ALACGhslBXJ3w3AAAYACOGpCVw"  # Replace with your Azure Speech key
service_region = "centralindia"  # Replace with your Azure region (e.g., "eastus")

# Function to select a voice based on language and gender
def get_voice(language, gender):
    voices = {
        "en-IN": {"male": "en-IN-PrabhatNeural", "female": "en-IN-NeerjaNeural"},
        "hi-IN": {"male": "hi-IN-MadhurNeural", "female": "hi-IN-SwaraNeural"},
        "ta-IN": {"male": "ta-IN-ValluvarNeural", "female": "ta-IN-PallaviNeural"},
        "te-IN": {"male": "te-IN-MohanNeural", "female": "te-IN-ShrutiNeural"},
        "mr-IN": {"male": "mr-IN-ManoharNeural", "female": "mr-IN-AarohiNeural"},
        "bn-IN": {"male": "bn-IN-BashkarNeural", "female": "bn-IN-TanishaaNeural"},
        "gu-IN": {"male": "gu-IN-MadhurNeural", "female": "gu-IN-DhwaniNeural"},

    }
    return voices.get(language, {}).get(gender, None)

# Function for Text-to-Speech
def text_to_speech(text, language_code, gender):
    try:
        # Get the appropriate voice based on language and gender
        voice_name = get_voice(language_code, gender)
        if not voice_name:
            print("Error: Invalid language or gender selection.")
            return

        # Configure the Speech service
        speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
        speech_config.speech_synthesis_voice_name = voice_name

        # Initialize the Speech Synthesizer
        synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

        print(f"\nGenerating speech using '{voice_name}'...")
        # Synthesize speech from text
        result = synthesizer.speak_text_async(text).get()

        # Check if synthesis was successful
        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print("Speech synthesis succeeded!")
        else:
            # Print detailed cancellation error information
            print(f"Speech synthesis failed: {result.reason}")
            if result.cancellation_details:
                print(f"Error details: {result.cancellation_details}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Main function
def main():
    print("Welcome to the Azure Text-to-Speech Converter with Voice Options!\n")

    # Supported languages and genders
    languages = {
        "1": {"name": "English (India)", "code": "en-IN"},
        "2": {"name": "Hindi", "code": "hi-IN"},
        "3": {"name": "Tamil", "code": "ta-IN"},
        "4": {"name": "Telugu", "code": "te-IN"},
        "5": {"name": "Marathi", "code": "mr-IN"},
        "6": {"name": "Bengali", "code": "bn-IN"},
        "7": {"name": "Gujarati", "code": "gu-IN"},
    }

    # Display supported languages
    print("Supported Languages:")
    for key, lang in languages.items():
        print(f"{key}. {lang['name']}")

    # User selects a language
    language_choice = input("\nSelect a language (1-7): ").strip()
    if language_choice not in languages:
        print("Invalid choice. Exiting.")
        return
    language_code = languages[language_choice]["code"]

    # User selects gender
    gender_choice = input("Select voice gender (male/female): ").strip().lower()
    if gender_choice not in ["male", "female"]:
        print("Invalid gender choice. Exiting.")
        return

    # Get the text input
    text_input = input("\nEnter the text you want to convert to speech: ").strip()
    if not text_input:
        print("Error: No text entered. Please enter some text.")
        return

    # Perform Text-to-Speech
    text_to_speech(text_input, language_code, gender_choice)

if __name__ == "__main__":
    main()
