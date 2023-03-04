# GUI made with Tkinter
I have built this desktop application.  
  
This Tkinter GUI converts PDF files to MP3 files and immediately opens the new audio file for the user.

pdf_file.pdf is an example PDF of a Spring poem. Open the pdf to have it played to you in audio.
  
You an run desktop_app.py file in a Python IDE such as PyCharm or alternatively, you can create a desktop app by following below:

Find your location of your download folder for this package

Open your command prompt and type the following:  
1) cd followed by the location of your download folder for this package  
   Example: cd C:\Users\Albert\desktop\GUI_tkinter_app
2) pip install mutagen 
3) pip install pyinstaller
4) pip install gTTS
5) pip install PyPDF2
6) pyinstaller --onefile desktop_app.py

Go to the folder of this package, "GUI_tkinter_app". Then go to the "dist folder".  The application is called "desktop_app"

