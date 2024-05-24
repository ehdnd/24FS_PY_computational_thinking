from gtts import gTTS
from playsound import playsound

s = gTTS("Hello, nice to meet you.")

s.save('hello.mp3')
playsound('hello.mp3')