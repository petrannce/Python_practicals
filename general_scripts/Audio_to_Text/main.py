import speech_recognition as sr
from pydub import AudioSegment

# pip install SpeechRecognition

recognizer = sr.Recognizer()

audio_file = "general_scripts/Audio_to_Text/audio.wav"

AudioSegment.from_mp3(audio_file).export(audio_file, format="wav")

with sr.AudioFile(audio_file) as source:
    audio_data = recognizer.record(source)

try:
    text = recognizer.recognize_google(audio_data, language="en-US")
    print("Extracted Text: ", text)

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand the audio")

except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")


    