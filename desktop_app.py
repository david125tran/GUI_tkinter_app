#----------------------------------------Terminal Installs----------------------------------------#
# pip install pyinstaller
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

# Add audiobook image
canvas.create_image(100, 150, image=logo_img)
canvas.grid(column=1, row=0)

#--------------------------------------Select File Button-------------------------------------#
filename = "" # The variable filename is declared and will be changed once the user selects a file

def select_file():
    '''This function allows the user to open the file explorer to select a pdf file'''

    global filename
    filetypes = (
        ('pdf files', '*.pdf'),
    )

    filename = fd.askopenfilename(   # The file path then gets saved as the variable "filename" at the global level
        title='Open a file',
        initialdir='/',
        filetypes=filetypes
    )
    info_label.config(text=filename)

def submit_button_clicked():
    '''When the submit button is clicked, the selected pdf file then gets converted into mp3 audio file'''

    # --------------------------------------Open The PDF-------------------------------------#
    pdf = open(filename, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf)

    # -----------------------------Get The Total Number of Pages-----------------------------#
    total_pages = pdf_reader.numPages

    # -----------------------------------Extract The Text------------------------------------#
    text = ""
    for page_number in range(0, total_pages):
        # Extract the text from each page
        new_page = pdf_reader.getPage(page_number)
        new_page_text = new_page.extractText()
        text = text + "\n\n" + new_page_text   # Add the text to the previous pages if there are any

    # -----------------------------------Convert the text to mp3 audio------------------------------------#
    audio = gTTS(text=text, lang='en', slow=False)
    # Each page becomes a new file
    audio_file_name = f"{audio_name.get()}.mp3"
    audio.save(audio_file_name)

    # -----------------------------------Play the Speech------------------------------------#
    os.system("audio.mp3")
    print(text)

# -----------------------------------Buttons------------------------------------#
file_explorer_button = Button(text="Open", highlightthickness=0, width=14, command=select_file)
file_explorer_button.grid(column=1, row=2)

submit_button = Button(text="Submit", highlightthickness=0, width=14, command=submit_button_clicked)
submit_button.grid(column=1, row=3)

# -----------------------------------Labels------------------------------------#
info_label = Label(text="Enter the file name", fg=BLACK, bg=WHITE, font=(FONT_NAME, 12))
info_label.grid(column=1, row=1)

mp3_label = Label(text=".mp3", fg=BLACK, bg=WHITE, font=(FONT_NAME, 12))
mp3_label.grid(column=2, row=5)

audio_name_label = Label(text="Enter a name for the new audio:", fg=BLACK, bg=WHITE, font=(FONT_NAME, 12))
audio_name_label.grid(column=1, row=4)

# -----------------------------------Entries------------------------------------#
audio_name = Entry(fg=BLACK, bg=WHITE, font=(FONT_NAME, 12))
audio_name.grid(column=1, row=5)

window.mainloop()   # Keep the window open
