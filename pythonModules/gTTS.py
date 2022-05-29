#Text to speech
from gtts import gTTS

sample='Frankly, my dear, I dont give a damn'
lang='ja' #can be ja, hi

audio=gTTS(sample,lang=lang)

audio.save('audioSample.mp3')
print('done....')