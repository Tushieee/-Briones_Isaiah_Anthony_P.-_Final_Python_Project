import subprocess
import os
import sqlite3
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to rename the PDF file after conversion
def rename_pdf(pdf_path):
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    new_pdf_name = f"{base_name} (converted into pdf).pdf"
    new_pdf_path = os.path.join(os.path.dirname(pdf_path), new_pdf_name)

    counter = 1
    while os.path.exists(new_pdf_path):
        new_pdf_name = f"{base_name} ({counter}) (converted into pdf).pdf"
        new_pdf_path = os.path.join(os.path.dirname(pdf_path), new_pdf_name)
        counter += 1

    os.rename(pdf_path, new_pdf_path)
    return new_pdf_path

# Function to convert DOCX to PDF
def convert_docx_to_pdf(docx_path):
    libreoffice_path = "C:\\Program Files\\LibreOffice\\program\\soffice.exe"
    files_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "files")

    if not os.path.exists(files_folder):
        os.makedirs(files_folder)

    pdf_file_path = os.path.join(files_folder, f"{os.path.splitext(os.path.basename(docx_path))[0]}.pdf")

    try:
        subprocess.run([libreoffice_path, '--headless', '--convert-to', 'pdf', '--outdir', files_folder, docx_path], check=True)
        return rename_pdf(pdf_file_path)
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        return None

# Function to select a DOCX file
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Word Documents", "*.docx")], title="Select a DOCX file")
    if file_path:
        entry_file_path.delete(0, tk.END)
        entry_file_path.insert(0, file_path)


def update_conversion_counter(converter_name):
    conn = sqlite3.connect('acp.db')
    cursor = conn.cursor()

    cursor.execute('SELECT id FROM conversion_counter WHERE id = 1')
    row = cursor.fetchone()

    if row:
        cursor.execute('''
        UPDATE conversion_counter
        SET total_conversions = total_conversions + 1,
            last_used_converter = ?, 
            timestamp = CURRENT_TIMESTAMP
        WHERE id = 1
        ''', (converter_name,))

    conn.commit()
    conn.close()

update_conversion_counter('DOCX TO PDF')  





# Function to perform conversion and update the counter
def convert():
    docx_path = entry_file_path.get()

    if not docx_path.endswith(".docx"):
        messagebox.showerror("Error", "Please select a valid .docx file")
        return

    pdf_path = convert_docx_to_pdf(docx_path)
    if pdf_path:
        messagebox.showinfo("Success", f"File converted to PDF: {pdf_path}\nConversion count updated.")
        update_conversion_counter('DOCX TO PDF') 
    else:
        messagebox.showerror("Error", "Failed to convert the file.")

# GUI setup
root = tk.Tk()
root.title("DOCX to PDF Converter")
root.geometry('300x165')  
root.configure(bg="#2e2e2e")  
root.resizable(False, False)

# Entry field for file path
entry_file_path = tk.Entry(root, width=30, font=("Arial", 12), fg="white", bg="#3a3f5c", bd=2, relief="solid")
entry_file_path.pack(pady=10)

# Browse button
browse_button = tk.Button(root, text="Browse", command=select_file, font=("Arial", 10), bg="#00bcd4", cursor='hand2', fg="white", relief="flat", activebackground="#0097a7")
browse_button.pack(pady=5)

# Convert button
convert_button = tk.Button(root, text="Convert to PDF", command=convert, font=("Arial", 10), bg="#00bcd4", cursor='hand2', fg="white", relief="flat", activebackground="#0097a7")
convert_button.pack(pady=10)

root.mainloop()
