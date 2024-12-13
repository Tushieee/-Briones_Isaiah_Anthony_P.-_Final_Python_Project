from tkinter import *
import subprocess
import os

root = Tk()
root.title("Helpify")
root.geometry('1060x600')
root.configure(bg="#2e2e2e") 
root.resizable(False, False)

# -------- Header --------
header = Frame(root, bg="#333333", height=80)
title = Label(header, text="Helpify", fg="#00bcd4", bg="#333333", font=("Helvetica", 24, "bold"))

# -------- Sidebar --------
sidebar = Frame(root, bg="#212121", width=246)
sidebar.pack(side="left", fill="y")


# -------- Func for side --------
def database():
    subprocess.run(["python", "database.py"])

def open_folder():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    files_folder = os.path.join(script_directory, "..", "prot", "files")
    os.startfile(files_folder)


# Sidebar Buttons
btn1 = Button(sidebar, text="Files", font=("Arial", 12), bg="#00bcd4", fg="white", relief="flat", width=20, command=open_folder, activebackground="#0097a7")
btn1.place(x=27, y=80)

btn3 = Button(sidebar, text="Admin", font=("Arial", 12), bg="#00bcd4", fg="white", relief="flat", width=20, command=database, activebackground="#0097a7")
btn3.place(x=27, y=130)

btn_exit = Button(sidebar, text="Exit", font=("Arial", 12), bg="#f44336", fg="white", relief="flat", width=20, command=root.quit, activebackground="#e53935")
btn_exit.place(x=27, y=180)

# -------- Scrollable Content Area --------
canvas = Canvas(root, bg="#2e2e2e")
canvas.pack(side="left", fill="both", expand=True, padx=20, pady=20)

# Scrollbar linked to the canvas
scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.config(yscrollcommand=scrollbar.set)

# Frame to hold the content inside the canvas
content_frame = Frame(canvas, bg="#2e2e2e")
canvas.create_window((0, 0), window=content_frame, anchor="nw")

# Content Title
content_title = Label(content_frame, text="Welcome to Helpify!", font=("Arial", 24, "bold"), fg="#00bcd4", bg="#2e2e2e")
content_title.grid(row=0, column=0, columnspan=3, pady=10, sticky="n")

# Content Description
content_description = Label(content_frame, text="Helpify is a versatile tool designed to handle various file conversions with ease. \nWith just a few clicks, you can convert your documents to different formats, \nmaking it easier to work with your files.",
                            font=("Arial", 14), fg="#cccccc", bg="#2e2e2e", justify="center")
content_description.grid(row=1, column=0, columnspan=3, pady=10)

# Function to open the other files
def open_pdftodocx():
    subprocess.run(["python", "converter/pdf_to_docx.py"])

def open_pdftotxt():
    subprocess.run(["python", "converter/pdf_to_txt.py"])

def open_docxtopdf():
    subprocess.run(["python", "converter/docx_to_pdf.py"])

def open_docxtotxt():
    subprocess.run(["python", "converter/docx_to_txt.py"])

def open_pngtopdf():
    subprocess.run(["python", "converter/png_to_pdf.py"])

def open_jpgtopdf():
    subprocess.run(["python", "converter/jpg_to_pdf.py"])

def open_pngtojpg():
    subprocess.run(["python", "converter/png_to_jpg.py"])

def open_jpgtopng():
    subprocess.run(["python", "converter/jpg_to_png.py"])

def open_giftopng():
    subprocess.run(["python", "converter/gif_to_png.py"])

# ------- Buttons -------
# PDF to DOCX button 
convert_button1 = Button(content_frame, text="PDF to DOCX", font=("Arial", 14), bg="#00bcd4", fg="white", relief="flat", height=2, width=20, command=open_pdftodocx)  
convert_button1.grid(row=2, column=0, padx=10, pady=10)

# PDF to TXT button 
convert_button2 = Button(content_frame, text="PDF to TXT", font=("Arial", 14), bg="#00bcd4", fg="white", relief="flat", height=2, width=20, command=open_pdftotxt)  
convert_button2.grid(row=2, column=1, padx=10, pady=10)

# DOCX to PDF button 
convert_button3 = Button(content_frame, text="DOCX to PDF", font=("Arial", 14), bg="#00bcd4", fg="white", relief="flat", height=2, width=20, command=open_docxtopdf)  
convert_button3.grid(row=2, column=2, padx=10, pady=10)

# DOCX to TXT button 
convert_button4 = Button(content_frame, text="DOCX to TXT", font=("Arial", 14), bg="#00bcd4", fg="white", relief="flat", height=2, width=20, command=open_docxtotxt)  
convert_button4.grid(row=3, column=0, padx=10, pady=10)

# PNG to PDF button
convert_button5 = Button(content_frame, text="PNG to PDF", font=("Arial", 14), bg="#00bcd4", fg="white", relief="flat", height=2, width=20, command=open_pngtopdf)  
convert_button5.grid(row=3, column=1, padx=10, pady=10)

# JPG to PDF button
convert_button6 = Button(content_frame, text="JPG to PDF", font=("Arial", 14), bg="#00bcd4", fg="white", relief="flat", height=2, width=20, command=open_jpgtopdf)  
convert_button6.grid(row=3, column=2, padx=10, pady=10)

# PNG to JPG button
convert_button7 = Button(content_frame, text="PNG to JPG", font=("Arial", 14), bg="#00bcd4", fg="white", relief="flat", height=2, width=20, command=open_pngtojpg)  
convert_button7.grid(row=4, column=0, padx=10, pady=10)

# JPG to PNG button
convert_button8 = Button(content_frame, text="JPG to PNG", font=("Arial", 14), bg="#00bcd4", fg="white", relief="flat", height=2, width=20, command=open_jpgtopng)  
convert_button8.grid(row=4, column=1, padx=10, pady=10)

# GIF to PNG button
convert_button9 = Button(content_frame, text="GIF to PNG", font=("Arial", 14), bg="#00bcd4", fg="white", relief="flat", height=2, width=20, command=open_giftopng)  
convert_button9.grid(row=4, column=2, padx=10, pady=10)

# Update scroll region after content is placed
content_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

# Run the application
root.mainloop()
