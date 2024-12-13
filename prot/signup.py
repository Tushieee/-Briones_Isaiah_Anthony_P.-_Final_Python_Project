from tkinter import *
from tkinter import messagebox
import sqlite3
import subprocess

def open_signin():
    window.destroy()  # Close the current window
    subprocess.run(["python", "signin.py"]) 

def open_update():
    window.destroy()  # Close the current window
    subprocess.run(["python", "update.py"]) 

def signup():
    username = user_su.get()
    password = pass_su.get()
    confirm_password = confrm.get()

    if password == confirm_password:
        try:
            connect = sqlite3.connect('acp.db')
            cursor = connect.cursor()

            cursor.execute("SELECT * FROM accounts WHERE Username = ?", (username,))
            existing_user = cursor.fetchone()

            if existing_user:
                messagebox.showerror('Error', 'Username already exists! Please choose a different username.')
            else:
                cursor.execute("INSERT INTO accounts (Username, Password) VALUES (?, ?)", (username, password))
                connect.commit()
                messagebox.showinfo('Success', 'Account created successfully!')
                
                window.destroy()
                subprocess.run(["python", "signin.py"])

        except Exception as e:
            messagebox.showerror('Error', f"An error occurred: {e}")
        finally:
            if 'connect' in locals():
                connect.close()

    else:
        messagebox.showerror('Error', 'Passwords do not match!')

window = Tk()
window.title("Sign Up")
window.geometry('925x500+300+200')
window.configure(bg='#fff')
window.resizable(False, False)

# Logo Image
img = PhotoImage(file='signup.png')  # Replace with your actual image file
Label(window, image=img, border=0, bg='white').place(x=50, y=50)

# Sign Up Box
frame = Frame(window, width=350, height=390, bg='#fff')
frame.place(x=480, y=50)
heading = Label(frame, text='Sign Up', fg="#57a1f8", bg='white', font=('Microsoft Yahei UI', 23, 'bold'))
heading.place(x=90, y=5) 

# Username Entry
user_su = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI', 11))
user_su.place(x=30, y=80)
user_su.insert(0, 'Username')

def clear_user(e): 
    if user_su.get() == 'Username':  
        user_su.delete(0, 'end')

def reset_user(e): 
    if user_su.get() == '': 
        user_su.insert(0, 'Username')

user_su.bind('<FocusIn>', clear_user)
user_su.bind('<FocusOut>', reset_user)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

# Password Entry
pass_su = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI', 11))
pass_su.place(x=30, y=150)
pass_su.insert(0, 'Password')

def clear_pass(e): 
    if pass_su.get() == 'Password': 
        pass_su.delete(0, 'end')

def reset_pass(e): 
    if pass_su.get() == '': 
        pass_su.insert(0, 'Password')

pass_su.bind('<FocusIn>', clear_pass)
pass_su.bind('<FocusOut>', reset_pass)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

# Confirm Password Entry
confrm = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI', 11))
confrm.place(x=30, y=220)
confrm.insert(0, 'Confirm Password')

def clear_confrm(e): 
    if confrm.get() == 'Confirm Password':  
        confrm.delete(0, 'end')

def reset_confrm(e): 
    if confrm.get() == '':  
        confrm.insert(0, 'Confirm Password')

confrm.bind('<FocusIn>', clear_confrm)
confrm.bind('<FocusOut>', reset_confrm)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

# Sign Up Button
signup_button = Button(frame, width=39, pady=7, text='Sign Up', bg='#57a1f8', fg='white', command=signup, border=0)
signup_button.place(x=35, y=280)

# Switch to Sign In
signin_label = Label(frame, text='I have an account', fg='black', bg='white', font=('Microsoft YaHei UI', 9))
signin_label.place(x=90, y=340) 
signin_button = Button(frame, width=6, text='Sign In', border=0, bg='white', fg='#57a1f8', command=open_signin)
signin_button.place(x=197, y=340)

# Switch to Sign In
signin_label = Label(frame, text='Update account', fg='black', bg='white', font=('Microsoft YaHei UI', 9))
signin_label.place(x=90, y=370) 
signin_button = Button(frame, width=6, text='Update', border=0, bg='white', fg='#57a1f8', command=open_update)
signin_button.place(x=197, y=370)

window.mainloop()
