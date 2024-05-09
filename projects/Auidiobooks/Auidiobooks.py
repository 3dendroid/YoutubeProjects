import PyPDF2
import pyttsx3

with open('book.pdf', 'rb') as book:
    full_text = ''

    reader = PyPDF2.PdfFileReader(book)

    audio_reader = pyttsx3.init()
    audio_reader.setProperty('rate', 100)

    for page in range(reader.numPages):
        next_page = reader.getPage(page)
        content = next_page.extractText()
        full_text += content + '\n'

    audio_reader.say(full_text, 'my_audio.mp3')
    audio_reader.runAndWait()
