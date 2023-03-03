import pyttsx3
import PyPDF2

from PyPDF2 import PdfReader
book = open("Seminar Topics.pdf", "rb")
reader = PyPDF2.PdfReader(book)
page_num = int(input(f"Enter the page number (1 to {len(reader.pages)}): "))
#pages = len(reader.pages)

print(pages)


speaker = pyttsx3.init()
for i in range(pages):
    page = reader.pages[i]
    text = page.extract_text()
    speaker.say(text)
    speaker.runAndWait()
