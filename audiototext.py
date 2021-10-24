import speech_recognition as sr
from os import path
from pydub import AudioSegment
import os
import wave

# convert mp3 file to wav                                                       
""" sound = AudioSegment.from_mp3("transcript.mp3")
sound.export("transcript.wav", format="wav") """


# transcribe audio file                                                         
def audiototext(filename):
# use the audio file as the audio source                                        
        r = sr.Recognizer()
        os.chdir(r'C:wordcloud.py')
        with sr.AudioFile(filename) as source:
                audio = r.record(source)  # read the entire audio file                  
                text = r.recognize_google(audio)
        return text
        