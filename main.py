import tkinter
import customtkinter
from functions import select_file, download_converted_file

# Set up Tkinter GUI window
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
window = customtkinter.CTk()
window.title("PDF to Speech Converter")
window.geometry("400x300")
window.config(padx=50, pady=50)

# Label
text = customtkinter.CTkLabel(master=window, text="File selected:\nnone", width=280, height=100,
                              fg_color=("white", "#2e2e2e"), corner_radius=8, text_font=('Arial', 18))
text.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

# Buttons
upload_button = customtkinter.CTkButton(master=window, text="Upload PDF file", width=200,
                                        command=lambda: select_file(text))
upload_button.place(relx=0.5, rely=0.65, anchor=tkinter.CENTER)
convert_button = customtkinter.CTkButton(master=window, text="Convert to MP3 and download", width=200,
                                         command=lambda: download_converted_file(text))
convert_button.place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)

window.mainloop()
