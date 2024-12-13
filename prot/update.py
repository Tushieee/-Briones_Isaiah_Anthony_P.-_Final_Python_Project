from tkinter import *
from tkinter import messagebox
import sqlite3
import subprocess

def open_signin():
    window.destroy()  # Close the current window
    subprocess.run(["python", "signin.py"]) 

def update_password():
    username = user_su.get()
    new_password = pass_su.get()
    confirm_password = confrm.get()

    if new_password == confirm_password:
        try:
            # Connect to the SQLite database
            connect = sqlite3.connect('acp.db')
            cursor = connect.cursor()

            # Check if the username exists
            cursor.execute("SELECT * FROM accounts WHERE Username = ?", (username,))
            existing_user = cursor.fetchone()

            if existing_user:
                # Update the password
                cursor.execute("UPDATE accounts SET Password = ? WHERE Username = ?", (new_password, username))
                connect.commit()
                messagebox.showinfo('Success', 'Password updated successfully!')
                
                # Redirect to the sign-in page
                window.destroy()
                subprocess.run(["python", "signin.py"])
            else:
                messagebox.showerror('Error', 'Username not found!')

        except Exception as e:
            messagebox.showerror('Error', f"An error occurred: {e}")
        finally:
            # Close the database connection
            if 'connect' in locals():
                connect.close()

    else:
        messagebox.showerror('Error', 'Passwords do not match!')

window = Tk()
window.title("Update Password")
window.geometry('925x500+300+200')
window.configure(bg='#fff')
window.resizable(False, False)

# Update Password Box
frame = Frame(window, width=350, height=390, bg='#fff')
frame.place(relx=0.5, rely=0.5, anchor=CENTER)  # Center the frame in the window

heading = Label(frame, text='Update Password', fg="#57a1f8", bg='white', font=('Microsoft Yahei UI', 23, 'bold'))
heading.place(relx=0.5, rely=0.05, anchor=N)  # Center the heading

# Username Entry
user_su = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI', 11))
user_su.place(relx=0.5, rely=0.2, anchor=N)
user_su.insert(0, 'Username')

# Clear placeholder text when focused
def clear_user(e): 
    if user_su.get() == 'Username':  # Only clear if it's the default text
        user_su.delete(0, 'end')

# Reset placeholder text if the entry is empty
def reset_user(e): 
    if user_su.get() == '':  # Only reset if the user hasn't entered anything
        user_su.insert(0, 'Username')

user_su.bind('<FocusIn>', clear_user)
user_su.bind('<FocusOut>', reset_user)
Frame(frame, width=295, height=2, bg='black').place(relx=0.5, rely=0.27, anchor=N)

# New Password Entry
pass_su = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI', 11))
pass_su.place(relx=0.5, rely=0.4, anchor=N)
pass_su.insert(0, 'New Password')

# Clear placeholder text when focused
def clear_pass(e): 
    if pass_su.get() == 'New Password':  # Only clear if it's the default text
        pass_su.delete(0, 'end')

# Reset placeholder text if the entry is empty
def reset_pass(e): 
    if pass_su.get() == '':  # Only reset if the user hasn't entered anything
        pass_su.insert(0, 'New Password')

pass_su.bind('<FocusIn>', clear_pass)
pass_su.bind('<FocusOut>', reset_pass)
Frame(frame, width=295, height=2, bg='black').place(relx=0.5, rely=0.47, anchor=N)

# Confirm Password Entry
confrm = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI', 11))
confrm.place(relx=0.5, rely=0.6, anchor=N)
confrm.insert(0, 'Confirm Password')

# Clear placeholder text when focused
def clear_confrm(e): 
    if confrm.get() == 'Confirm Password':  # Only clear if it's the default text
        confrm.delete(0, 'end')

# Reset placeholder text if the entry is empty
def reset_confrm(e): 
    if confrm.get() == '':  # Only reset if the user hasn't entered anything
        confrm.insert(0, 'Confirm Password')

confrm.bind('<FocusIn>', clear_confrm)
confrm.bind('<FocusOut>', reset_confrm)
Frame(frame, width=295, height=2, bg='black').place(relx=0.5, rely=0.67, anchor=N)

# Update Password Button
update_button = Button(frame, width=39, pady=7, text='Update Password', bg='#57a1f8', fg='white', command=update_password, border=0)
update_button.place(relx=0.5, rely=0.75, anchor=N)

# Switch to Sign In
signin_label = Label(frame, text='I have an account', fg='black', bg='white', font=('Microsoft YaHei UI', 9))
signin_label.place(relx=0.5, rely=0.85, anchor=N) 
signin_button = Button(frame, width=6, text='Sign In', border=0, bg='white', fg='#57a1f8', command=open_signin)
signin_button.place(relx=0.5, rely=0.9, anchor=N)

window.mainloop()
