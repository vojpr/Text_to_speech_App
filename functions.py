from tkinter import filedialog
import pyttsx3
from PyPDF2 import PdfReader
import os
import threading
from downloads_folder_finder import get_download_folder


def select_file(text):
    """Opens filedialog and uploads selected PDF file"""
    global pdf_file, name_without_filetype
    # Load file
    filetypes = (("PDF files", '.pdf'), ("all files", "*.*"))
    pdf_file = filedialog.askopenfilename(title="Select a file", initialdir="/", filetypes=filetypes)
    # Gets name of the selected file
    name_with_filetype = os.path.basename(pdf_file)
    name_without_filetype = os.path.splitext(name_with_filetype)[0]
    # Shows name of the selected file on screen
    text.configure(text=f"File selected:\n{name_with_filetype}", text_color="white")


def run_pyttsx3():
    """Converts string to mp3 file and saves it to downloads folder"""
    engine = pyttsx3.init()
    engine.setProperty('rate', 155)
    engine.save_to_file(pdf_string, f"{get_download_folder()}/{name_without_filetype}.mp3")
    engine.runAndWait()


def download_converted_file(text):
    """Converts uploaded PDF file to mp3 format and saves it to downloads folder"""
    global pdf_string
    # Get string from PDF
    pdf_string = ""
    try:
        reader = PdfReader(pdf_file)
        number_of_pages = len(reader.pages)
        for number in range(number_of_pages):
            page = reader.pages[number]
            pdf_string += page.extract_text()
        # Convert string to mp3 (using threading so that Tk window doesn't exit the mainloop)
        threading.Thread(
            target=run_pyttsx3, daemon=True
        ).start()
        text.configure(text=f"{name_without_filetype}.mp3\ndownloaded", text_color="green")
    except (NameError, FileNotFoundError):
        text.configure(text=f"File selected:\nnone", text_color="red")
