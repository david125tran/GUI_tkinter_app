#----------------------------------------Terminal Installs----------------------------------------#
# pip install gTTS
# pip install pypdf2
# pip install mutagen
# pip install python-time

#----------------------------------------Imports----------------------------------------#
from tkinter import filedialog as fd
from gtts import *
import os
import PyPDF2
import time
from mutagen.mp3 import MP3
from tkinter import *


#----------------------------------------Constants----------------------------------------#
FONT_NAME = "Arial"
BLACK = "#000000"
WHITE = "#ffffff"

#--------------------------------------GUI Setup-------------------------------------#
window = Tk()
window.title("PDF to Audio Converter")
window.config(padx=50, pady=50, bg=WHITE)

canvas = Canvas(width=200, height=300, bg=WHITE, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")

# Add an image later
canvas.create_image(100, 150, image=logo_img)
canvas.grid(column=1, row=0)

#--------------------------------------Select File Button-------------------------------------#
def select_file():
    filetypes = (
        ('pdf files', '*.pdf'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes
    )
    # The file path then gets saved as the variable "filename"

    # --------------------------------------Open The PDF-------------------------------------#
    pdf = open(filename, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf)

    # -----------------------------Get The Total Number of Pages-----------------------------#
    total_pages = pdf_reader.numPages

    # -----------------------------------Extract The Text------------------------------------#
    for page_number in range(0, total_pages):
    # Extract the text from each page
        new_page = pdf_reader.getPage(page_number)
        new_page_text = new_page.extractText()
        # Convert the text to speech (.mp3 file)
        new_page_speech = gTTS(text=new_page_text, lang='en', slow=False)
        # Each page becomes a new file
        new_page_speech.save(f"new_page_speech_{page_number}.mp3")

    # -----------------------------------Play the Speech------------------------------------#
    for page_number in range(0, total_pages):
        os.system(f"new_page_speech_{page_number}.mp3")
        audio = MP3(f"new_page_speech_{page_number}.mp3")  # Extract the length of the mp3 of the page
        time.sleep(int(audio.info.length) + 2)  # Wait for the mp3 of the page to finish playing before looping to
        # the next page

# open button
file_explorer_button = Button(text="Open", highlightthickness=0, width=14, command=select_file)
file_explorer_button.grid(column=1, row=2)

#
file_name_label = Label(text="Select PDF File to Convert to Audio:", fg=BLACK, bg=WHITE, font=(FONT_NAME, 12))
file_name_label.grid(column=1, row=1)

window.mainloop()






