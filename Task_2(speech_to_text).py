import speech_recognition as sr
from pydub import AudioSegment
input_mp3_path = '/content/Record (online-voice-recorder.com) (1).mp3'
output_wav_path = '/content/output_audio.wav'
try:
    audio = AudioSegment.from_mp3(input_mp3_path)
    audio.export(output_wav_path, format="wav")
    print(f"Successfully converted {input_mp3_path} to {output_wav_path}")
except FileNotFoundError:
    print(f"Error: Input file not found at {input_mp3_path}")
except Exception as e:
    print(f"An error occurred during conversion: {e}")
recognizer = sr.Recognizer()
with sr.AudioFile("/content/output_audio.wav") as source:
    audio = recognizer.record(source)
try:
    text = recognizer.recognize_google(audio)
    print("Transcription:", text)
except sr.UnknownValueError:
    print("Speech Recognition could not understand audio")
except sr.RequestError as e:
    print(f"Could not request results from Speech Recognition service; {e}")