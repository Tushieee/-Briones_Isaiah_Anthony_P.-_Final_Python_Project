from tkinter import *
from tkinter import messagebox
import sqlite3
import subprocess  # for switching pages
import datetime

# This is for switching the page to sign up
def open_signup():
    root.destroy()  # Close the current window
    subprocess.run(["python", "signup.py"])


def signin():
    username = user_si.get()
    password = pass_si.get()

    try:
        connect = sqlite3.connect('acp.db')
        cursor = connect.cursor()

        cursor.execute("SELECT * FROM accounts WHERE Username = ? AND Password = ?", (username, password))
        user = cursor.fetchone()

        if user: 
            messagebox.showinfo("Success", "Logged in successfully!")

            cursor.execute("""
                INSERT INTO logs (Username, Action, Timestamp) VALUES (?, ?, ?)
            """, (username, "Log", datetime.datetime.now()))
            connect.commit()

            root.destroy()  
            subprocess.run(["python", "main.py"])  
        else:
            messagebox.showerror("Invalid", "Invalid username or password!")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        if 'connect' in locals():
            connect.close()


# The body of the page
root = Tk()
root.title('Sign In')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

# Logo Image
logo = PhotoImage(file='signin.png')  
Label(root, image=logo, bg='white').place(x=50, y=50)

# Sign In Box
BigBox = Frame(root, width=350, height=350, bg="#fff")
BigBox.place(x=480, y=70)
heading = Label(BigBox, text='Sign In', fg="#57a1f8", bg='white', font=('Microsoft Yahei UI', 23, 'bold'))
heading.place(x=100, y=5)

# Username Entry
user_si = Entry(BigBox, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI', 11))
user_si.place(x=30, y=80)
user_si.insert(0, 'Username')

def clear_user(e): 
    if user_si.get() == 'Username':  
        user_si.delete(0, 'end')

def reset_user(e): 
    if user_si.get() == '':  
        user_si.insert(0, 'Username')

user_si.bind('<FocusIn>', clear_user)
user_si.bind('<FocusOut>', reset_user)
Frame(BigBox, width=295, height=2, bg='black').place(x=25, y=107)

# Password Entry
pass_si = Entry(BigBox, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI', 11), show='*')
pass_si.place(x=30, y=150)
pass_si.insert(0, 'Password')

def clear_pass(e): 
    if pass_si.get() == 'Password':
        pass_si.delete(0, 'end')

def reset_pass(e): 
    if pass_si.get() == '': 
        pass_si.insert(0, 'Password')

pass_si.bind('<FocusIn>', clear_pass)
pass_si.bind('<FocusOut>', reset_pass)
Frame(BigBox, width=295, height=2, bg='black').place(x=25, y=177)

def toggle_password():
    if pass_si.cget('show') == '*':  
        pass_si.config(show='') 
        toggle_button.config(text="Hide") 
    else:
        pass_si.config(show='*')  
        toggle_button.config(text="Show")  

# Show password button
toggle_button = Button(BigBox, text="Show", cursor='hand2', bg='#57a1f8', fg='white', command=toggle_password, border=0)
toggle_button.place(x=284, y=150)  

# Sign In Button
Button(BigBox, width=39, pady=7, text='Sign In', cursor='hand2', bg='#57a1f8', fg='white', command=signin, border=0).place(x=35, y=204)

# Switch to Sign Up
Label(BigBox, text="Don't have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9)).place(x=75, y=270)
Button(BigBox, width=6, text='Sign Up', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=open_signup).place(x=215, y=270)

root.mainloop()
