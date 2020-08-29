from rivescript import RiveScript
import speech_recognition as sr  # recognise speech
import playsound  # to play an audio file
from gtts import gTTS  # google text to speech
import random
import os

r = sr.Recognizer()


def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')  # text to speech(voice)
    r = random.randint(1, 20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file)  # save as mp3
    playsound.playsound(audio_file)  # play the audio file
    print(f"kiri: {audio_string}")  # print what app said
    os.remove(audio_file)  # remove audio file


main = RiveScript()
main.load_directory("brain")
main.sort_replies()

while True:
    msg = input('User: ')
    if msg == "thank you":
        quit()
    reply = main.reply("random",msg)
    speak(reply)
