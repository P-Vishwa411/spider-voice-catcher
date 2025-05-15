# spider-voice-catcher
Azure Speech Services for Indian Languages
This repository contains Python scripts that leverage Azure Cognitive Services to perform real-time Speech-to-Text Translation and Text-to-Speech (TTS) synthesis, with support for multiple Indian languages. The scripts are designed to enable seamless speech translation and synthesis for Indian languages, making them useful for applications like accessibility tools, language learning, and multilingual communication.
Features

Real-Time Speech-to-Text Translation: Translate spoken input in one Indian language to text in another Indian language in real time.
Text-to-Speech Synthesis: Convert text into spoken audio with voice options (male/female) for various Indian languages.
Supported Indian Languages:
Hindi (hi-IN)
Tamil (ta-IN)
Telugu (te-IN)
Gujarati (gu-IN)
Marathi (mr-IN)
Bengali (bn-IN)
Kannada (kn-IN)
Malayalam (ml-IN)
Odia (or-IN)
Punjabi (pa-IN)
English (India) (en-IN)



Prerequisites
To run these scripts, you need the following:

Python 3.6+: Ensure Python is installed on your system.
Azure Cognitive Services Subscription:
Sign up for an Azure account and create a Speech Service resource.
Obtain your speech_key and service_region from the Azure portal.
For translation, you'll also need a Translator resource key and endpoint.


Microphone: Required for real-time speech input (Speech-to-Text Translation).
Dependencies: Install the required Python packages using the following command:pip install azure-cognitiveservices-speech requests



Setup

Clone the Repository:
git clone https://github.com/your-username/azure-speech-indian-languages.git
cd azure-speech-indian-languages


Configure Azure Credentials:

Open the script files (speech_to_text_translation.py and text_to_speech.py).
Replace the placeholder values for speech_key and service_region with your Azure Speech Service credentials.
For the translation script (translator.py), replace key, endpoint, and location with your Azure Translator resource credentials.

Example:
speech_key = "your-speech-key-here"
service_region = "your-region-here"  # e.g., "eastus"


Install Dependencies:Ensure you have the required packages installed (as mentioned in the Prerequisites section).


Usage
1. Real-Time Speech-to-Text Translation (speech_to_text_translation.py)
This script listens to speech in one Indian language and translates it into another in real time.

Run the Script:python speech_to_text_translation.py


Steps:
Choose the input and target languages from the menu (e.g., Hindi to Tamil).
Speak into your microphone.
The script will display the recognized speech and its translation.
Press Ctrl+C to stop the translation.



2. Text-to-Speech Synthesis (text_to_speech.py)
This script converts text into spoken audio with voice options for Indian languages.

Run the Script:python text_to_speech.py


Steps:
Select a language (e.g., Telugu).
Choose a voice gender (male/female).
Enter the text you want to convert to speech.
The script will generate and play the audio using the selected voice.



3. Text Translation (translator.py)
This script translates text from English to multiple Indian languages using the Azure Translator API.

Run the Script:python translator.py


Output:The script translates the hardcoded text ("Hello, how are you?") into Telugu, Hindi, Gujarati, Kannada, and Tamil, and prints the result in JSON format.

File Structure

speech_to_text_translation.py: Script for real-time speech-to-text translation.
text_to_speech.py: Script for text-to-speech synthesis with voice selection.
translator.py: Script for text translation using Azure Translator API.
README.md: This file, containing project documentation.

Example Output
Speech-to-Text Translation
Supported Indian Languages:
1. Hindi
2. Tamil
3. Telugu
4. Gujarati
5. Marathi
...

Select the input speech language (1-5): 1
Select the target translation language (1-5): 2

Listening for speech in 'Hindi' and translating to 'Tamil'.

Speak now! (Press Ctrl+C to stop)

Recognized (Hindi): नमस्ते, आप कैसे हैं?
Translated (Tamil): வணக்கம், நீங்கள் எப்படி இருக்கிறீர்கள்?

Text-to-Speech
Supported Languages:
1. English (India)
2. Hindi
3. Tamil
...

Select a language (1-7): 3
Select voice gender (male/female): female
Enter the text you want to convert to speech: வணக்கம், நான் பல்லவி.

Generating speech using 'ta-IN-PallaviNeural'...
Speech synthesis succeeded!

Text Translation
[
    {
        "translations": [
            { "text": "హలో, నీవు ఎలా ఉన్నావు?", "to": "te" },
            { "text": "नमस्ते, आप कैसे हैं?", "to": "hi" },
            { "text": "હેલો, તમે કેવા છો?", "to": "gu" },
            { "text": "ಹಲೋ, ನೀವು ಹೇಗಿದ್ದೀರಿ?", "to": "kn" },
            { "text": "வணக்கம், நீங்கள் எப்படி இருக்கிறீர்கள்?", "to": "ta" }
        ]
    }
]

Notes

Ensure your microphone is working for the Speech-to-Text Translation script.
The scripts require an active internet connection to communicate with Azure services.
Replace the placeholder credentials (your key, your region, your end point) with your actual Azure credentials.
Some Azure voices may require a specific subscription tier (e.g., Neural voices may not be available in the free tier).

Contributing
Contributions are welcome! If you’d like to add support for more languages, improve the UI, or fix bugs:

Fork the repository.
Create a new branch (git checkout -b feature-name).
Make your changes and commit (git commit -m "Add feature").
Push to your branch (git push origin feature-name).
Create a Pull Request.

License
This project is licensed under the MIT License. See the LICENSE file for details.
Contact
For questions or suggestions, feel free to open an issue on this repository.
