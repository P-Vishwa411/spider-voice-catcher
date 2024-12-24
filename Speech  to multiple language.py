import azure.cognitiveservices.speech as speechsdk

# Azure Speech service credentials
speech_key = "CqZk7RHeS5csXUIjIZpm6VCjJgp5XkrOR6vguRRy4j3KVkACTsIbJQQJ99ALACYeBjFXJ3w3AAAYACOGM2y9"
service_region = "eastus"

# Function for Real-Time Speech-to-Text Translation in Top 5 Indian Languages
def real_time_speech_translation():
    print("Starting real-time speech translation.\n")
    
    # Display supported Indian languages
    indian_languages = {
        "1": {"name": "Hindi", "code": "hi-IN"},
        "2": {"name": "Tamil", "code": "ta-IN"},
        "3": {"name": "Telugu", "code": "te-IN"},
        "4": {"name": "Gujarati", "code": "gu-IN"},
        "5": {"name": "Marathi", "code": "mr-IN"},
        "6": {"name": "Bengali", "code": "bn-IN"},
        "7": {"name": "Kannada", "code": "kn-IN"},
        "8": {"name": "Malayalam", "code": "ml-IN"},
        "9": {"name": "Odia", "code": "or-IN"},
        "10": {"name": "Punjabi", "code": "pa-IN"},
        "11": {"name": "English", "code": "en-IN"}
    }

    print("Supported Indian Languages:")
    for key, lang in indian_languages.items():
        print(f"{key}. {lang['name']}")

    # Prompt user for input speech language
    input_choice = input("\nSelect the input speech language (1-5): ").strip()
    target_choice = input("Select the target translation language (1-5): ").strip()

    if input_choice not in indian_languages or target_choice not in indian_languages:
        print("Invalid choice. Please select valid options (1-5).")
        return

    input_language = indian_languages[input_choice]["code"]
    target_language = indian_languages[target_choice]["code"].split("-")[0]  # Extract language code for target

    print(f"\nListening for speech in '{indian_languages[input_choice]['name']}' and translating to '{indian_languages[target_choice]['name']}'.\n")

    # Configure speech and translation services
    translation_config = speechsdk.translation.SpeechTranslationConfig(subscription=speech_key, region=service_region)
    translation_config.speech_recognition_language = input_language  # Input language
    translation_config.add_target_language(target_language)         # Target language

    audio_config = speechsdk.AudioConfig(use_default_microphone=True)
    recognizer = speechsdk.translation.TranslationRecognizer(translation_config=translation_config, audio_config=audio_config)

    print("Speak now! (Press Ctrl+C to stop)\n")

    try:
        while True:
            # Recognize speech and translate in real time
            result = recognizer.recognize_once()
            if result.reason == speechsdk.ResultReason.TranslatedSpeech:
                print(f"Recognized ({indian_languages[input_choice]['name']}): {result.text}")
                print(f"Translated ({indian_languages[target_choice]['name']}): {result.translations[target_language]}")
            elif result.reason == speechsdk.ResultReason.NoMatch:
                print("No speech could be recognized. Try again.")
            elif result.reason == speechsdk.ResultReason.Canceled:
                cancellation_details = result.cancellation_details
                print(f"Error: {cancellation_details.reason}")
                break
    except KeyboardInterrupt:
        print("\nTranslation stopped by user.")

# Main Menu for User Interaction
def main():
    print("\nChoose an option:")
    print("1. Real-Time Speech Translation (Top 5 Indian Languages)")
    print("2. Exit")

    while True:
        choice = input("Enter your choice (1/2): ").strip()
        if choice == "1":
            real_time_speech_translation()
        elif choice == "2":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
