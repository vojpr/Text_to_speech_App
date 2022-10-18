import tkinter
from tkinter import filedialog
import customtkinter
import pyttsx3
from PyPDF2 import PdfReader
import os
import threading
from downloads_folder_finder import get_download_folder


def select_file():
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


def download_converted_file():
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


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

window = customtkinter.CTk()
window.title("PDF to Speech Converter")
window.geometry("400x300")
window.config(padx=50, pady=50)

text = customtkinter.CTkLabel(master=window, text="File selected:\nnone", width=280, height=100,
                              fg_color=("white", "#2e2e2e"), corner_radius=8, text_font=('Arial', 18))
text.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

upload_button = customtkinter.CTkButton(master=window, text="Upload PDF file", width=200, command=select_file)
upload_button.place(relx=0.5, rely=0.65, anchor=tkinter.CENTER)
convert_button = customtkinter.CTkButton(master=window, text="Convert to MP3 and download", width=200,
                                         command=download_converted_file)
convert_button.place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)

window.mainloop()
