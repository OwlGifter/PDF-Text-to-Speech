# importing the modules 
import PyPDF2 
from gtts import gTTS
from playsound import playsound
import keyboard
import time
import os
import tempfile


#method to turn text to mp3 file and play it, then delete it after playthrough
def speak_text(text, lang='en'):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tts = gTTS(text=text, lang=lang)
        tts.save(tmp.name)
        tmp_path = tmp.name
    
    playsound(tmp_path)
    os.remove(tmp_path)

paused = False

# path of the PDF file, strips spaces and unnecessary ""
inputPath = input('Path to pdf file(respond "default" to select book.pdf next to python file): ').strip().strip('"')
if inputPath == "default" :
    path = open('./book.pdf', 'rb')
else:
    path = open(inputPath, 'rb')

# creating a PdfFileReader object 
pdfReader = PyPDF2.PdfReader(path) 

#number of pages in the book:
maxPages = pdfReader._get_num_pages()

#the start of the tts
firstPage = 32
#makes first page start from 1,2,3 not 0,1,2
firstPage -=1

#add all pages to the text
for i in range(firstPage, maxPages):
    print(f"loop {i}")
    # this will add a page to the queue. 
    from_page = pdfReader.pages[i]
    
    # extracting the text from the PDF 
    text = from_page.extract_text() 

    #debugging
    print(f"\n--- Page {i+1} ---")
    print(repr(text))

    time.sleep(1)

    # reading the text 
    if text and text.strip():
        #clean text from unknown characters
        text = text.strip('\n-')
        speak_text(text) 
    #if no text, then let user know
    else:
        text = f'Page {i+1} has no readable text.'
        speak_text(text)
    time.sleep(1)

    while True:
        if keyboard.is_pressed('p'):
            if not paused:
                print("Paused. Press 'p' again to resume")
                paused = True
                time.sleep(5)
                while paused:
                    time.sleep(0.1)
                    if keyboard.is_pressed('p'):
                        print("Resuming...")
                        paused = False
                        break
        break

