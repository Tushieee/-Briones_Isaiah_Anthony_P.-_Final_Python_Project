import os
import tkinter as tk
import sqlite3
from tkinter import filedialog, messagebox
from PIL import Image

# Function to convert JPG to PNG
def convert_jpg_to_png(jpg_path):
    try:
        # Extract base name and script directory
        base_name = os.path.splitext(os.path.basename(jpg_path))[0]
        script_directory = os.path.dirname(os.path.abspath(__file__))

        # Define the output folder ("files" folder next to the converter folder)
        files_folder = os.path.join(script_directory, "..", "files")
        if not os.path.exists(files_folder):
            os.makedirs(files_folder)

        # Define initial PNG file path
        png_file_name = f"{base_name} (jpg converted into png).png"
        png_file_path = os.path.join(files_folder, png_file_name)

        # Check if the file exists, and if so, increment the name
        counter = 1
        while os.path.exists(png_file_path):
            png_file_name = f"{base_name} ({counter}) (jpg converted into png).png"
            png_file_path = os.path.join(files_folder, png_file_name)
            counter += 1

        # Open the JPG image and save it as PNG
        image = Image.open(jpg_path)
        image.save(png_file_path, "PNG")

        return png_file_path
    except Exception as e:
        print(f"Error during conversion: {e}")
        return None

# Select JPG file using file dialog
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("JPG Images", "*.jpg *.jpeg")], title="Select a JPG file")
    if file_path:
        entry_file_path.delete(0, tk.END)
        entry_file_path.insert(0, file_path)

def update_conversion_counter(converter_name):
    conn = sqlite3.connect('acp.db')
    cursor = conn.cursor()

    # Check if a row exists for id = 1 in the conversion_counter table
    cursor.execute('SELECT id FROM conversion_counter WHERE id = 1')
    row = cursor.fetchone()

    if row:
        # Increment the TotalConversions, update the last used converter, and the timestamp
        cursor.execute('''
        UPDATE conversion_counter
        SET total_conversions = total_conversions + 1,
            last_used_converter = ?, 
            timestamp = CURRENT_TIMESTAMP
        WHERE id = 1
        ''', (converter_name,))

    # Commit changes and close the connection
    conn.commit()
    conn.close()


# Convert the JPG file when button is clicked
def convert():
    jpg_path = entry_file_path.get()
    if not jpg_path.lower().endswith((".jpg", ".jpeg")):
        messagebox.showerror("Error", "Please select a valid .jpg file")
        return
    
    # Perform conversion and show success message with file path
    png_path = convert_jpg_to_png(jpg_path)
    if png_path:
        messagebox.showinfo("Success", f"File converted successfully to PNG:\n{png_path}")
        update_conversion_counter('JPG TO PNG')
    else:
        messagebox.showerror("Error", "Failed to convert the file.")

# GUI setup
root = tk.Tk()
root.title("JPG to PNG Converter")
root.geometry('300x165')  
root.configure(bg="#2e2e2e")  # Darker background for modern theme
root.resizable(False, False)

# Entry field for file path
entry_file_path = tk.Entry(root, width=30, font=("Arial", 12), fg="white", bg="#3a3f5c", bd=2, relief="solid")
entry_file_path.pack(pady=20)

# Browse button
browse_button = tk.Button(root, text="Browse", command=select_file, font=("Arial", 10), bg="#00bcd4", cursor='hand2', fg="white", relief="flat", activebackground="#0097a7")
browse_button.pack(pady=5)

# Convert button
convert_button = tk.Button(root, text="Convert to PNG", command=convert, font=("Arial", 10), bg="#00bcd4", cursor='hand2', fg="white", relief="flat", activebackground="#0097a7")
convert_button.pack(pady=10)

root.mainloop()