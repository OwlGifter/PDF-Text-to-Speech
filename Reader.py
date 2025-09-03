# importing the modules 
import PyPDF2 
import pyttsx3 

# path of the PDF file
path = input('Path to pdf file(respond "default" to select book.pdf next to python file): ')
if path == "default" :
    path = open('./book.pdf', 'rb')

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
    # this will add a page to the queue. 
    from_page = pdfReader.pages[i]
    
    # extracting the text from the PDF 
    text = from_page.extract_text() 

    # reading the text 
    speak = pyttsx3.init() 
    speak.say(text) 
    speak.runAndWait()