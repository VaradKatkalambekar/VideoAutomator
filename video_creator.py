from gtts import gTTS
import os

mytext = 'Welcome you Noobie, You are definitely gonna be a great man one day! And also Prasad is a good boy'

language = 'en'

myobj = gTTS(text = mytext, lang = language, slow = False)

myobj.save("welcome.mp3")

os.system("mpg321 welcome.mp3")
