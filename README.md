# -Briones_Isaiah_Anthony_P.-_Final_Python_Project

# Project Overview
The primary objective of Helpify is to simplify file conversion, allowing users to handle various file formats with ease. By offering a centralized platform, Helpify enables users to convert multiple files simultaneously while preserving content quality. The project aims to make file conversion accessible, providing a secure, reliable, and user-friendly tool that saves time and effort. With features like batch processing, multi-format support, and history tracking, Helpify helps users manage their file needs efficiently, enhancing productivity. It aims to reduce frustration, making life easier for students, professionals, and anyone in need of an effective file management tool.


# Python Libraries and Concepts
Tkinter
Description: GUI library for creating desktop applications. Allows creation of windows, buttons, labels, and event handling.
Usage: Used to create the graphical interface for the application, including buttons and windows.

Subprocess:
Description: Provides functions for spawning new processes, connecting to their input/output/error pipes, and obtaining their return codes.
Usage: Used to connect other `.py` files to be accessed via buttons.

Sqlite3.connector
Description: Library for connecting and interacting with SQLite3 databases.
Usage: Used to store and fetch user sessions.

Pillow (PIL)
Description: Library for image processing and handling GIF animations.
Usage: Used to display and animate GIF images in the GUI.

Pdf2docx
Description: Built-in module for handling date and time operations.
Usage: Used to record timestamps for session tracking.

Pdfplumber
Description: Python tool that extracts text, tables, and metadata from PDF files into a structured format (e.g., plain text).
Usage: Used to convert PDF files into text files.

Docx
Description: Python imports the Document class from the `python-docx` library to create, modify, and save DOCX files programmatically.
Usage: Used to convert DOCX files to text files.

OS
Description: Provides a way to interact with the operating system, including file and directory manipulation, path handling, and environment variable access.
Usage: Used to access the "file" folder where converted files are stored.

Datetime:
Description: Supplies classes for manipulating dates and times, including getting the current date/time, formatting, and performing date arithmetic.
Usage: Used to put history logs in the database.

Sqlite3.connector "counter"
Description: Library for connecting and interacting with SQLite3 databases.
Usage: Used to put a point in the `converter_counter` in the database.

Scrollable Widgets:
Description: Dynamic task lists with scrollbars.
Usage: Used to create a scrollable canvas for tasks.


# Sustainable Development Goals
The HELPIFY system addresses key areas of digital productivity, making it aligned with several Sustainable Development Goals (SDGs). It contributes to SDG 9: Industry, Innovation, and Infrastructure by providing an efficient, innovative tool for seamless file conversions, supporting digital transformation across industries. HELPIFY also supports SDG 4: Quality Education by offering students, educators, and professionals an easy-to-use tool for converting documents and resources, enhancing accessibility and usability of learning materials. By enabling users to convert files offline, HELPIFY promotes SDG 12: Responsible Consumption and Production, reducing reliance on online services and contributing to sustainable practices in digital work. Additionally, HELPIFY helps to bridge digital gaps, aligning with SDG 10: Reduced Inequalities, by offering an accessible solution for individuals across various demographics. These alignments emphasize HELPIFY’s role in improving digital workflows and promoting sustainability in the digital age.


# Instructions

1. **Sign In**: 
   - Start by visiting the sign-in page. 
   - If you have an account, enter your username and password to sign in. 
   - Once signed in successfully, you will be directed to the main page.

2. **Sign Up**: 
   - If you don't have an account, press the "Sign Up" button at the bottom of the sign-in page. 
   - Enter your desired username, then set a password. 
   - Confirm your password by retyping it.
   - After completing the sign-up process, you will be redirected to the sign-in page where you can log in using the newly created account.

3. **Update Account**: 
   - If you want to update your account details, go to the sign-up page and click the "Update" button at the bottom.
   - You will be prompted to choose the desired account by its username.
   - Enter the new password and confirm it by retyping it. 
   - After updating, you will be redirected to the sign-in page to log in with your updated account.

4. **Main Page**: 
   - After signing in, you will be directed to the main page, where you can see all 9 available converters.
   - Click on any converter to open its corresponding GUI.

5. **Converter GUI**: 
   - Each converter's GUI will have two buttons:
     - **Browse**: For selecting the file you want to convert.
     - **Convert**: To start the conversion process.

6. **View Converted Files**: 
   - Once you're done with the conversion, you can find your converted files by clicking the "Files" button located on the left side of the main page.

7. **Admin Button**: 
   - If you have admin access, you can click the "Admin" button on the main page.
   - This will take you to the database viewing area, which is strictly prohibited to non-authorized users.
   - In the accounts area, you will find the following options:
     - **View**: Allows you to view account details.
     - **Delete Account**: Allows you to delete accounts.
   - There is also a **Log History** section, which contains:
     - **View**: Allows you to view the history of actions taken in the system.
   - The **User Statistics** section contains:
     - **View**: Allows you to view user statistics.


