import os

from gtts import gTTS

fh = open("text.txt", "r")  # path of text
myText = fh.read().replace("\n", " ")
language = 'ru'  # set language
output = gTTS(text=myText, lang=language, slow=False)
output.save("output.mp3")
fh.close()
os.system("start output.mp3")

"""TEXT TO SPEACH"""
# myText = "Love you too!"
# language = 'en'
# output = gTTS(text=myText, lang=language, slow=False)
# output.save("output.mp3")
# os.system("start output.mp3")
