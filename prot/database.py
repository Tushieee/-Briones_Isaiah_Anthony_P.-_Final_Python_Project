import sqlite3
import datetime
from tkinter import *
from tkinter import messagebox

# Setup the main window
root = Tk()
root.title('Database')
root.geometry("900x500")  # 16:9 aspect ratio
root.config(bg='#2e2e2e')

def log_action(username=None, action=""):
    conn = sqlite3.connect('acp.db')
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO logs (Username, Action, Timestamp) VALUES (?, ?, ?)
    """, (username, action, datetime.datetime.now()))
    conn.commit()
    conn.close()

def view_db():
    conn = sqlite3.connect('acp.db')
    cursor = conn.cursor()
    cursor.execute("""
    SELECT accounts.Username, accounts.Password
    FROM accounts
    """)
    rows = cursor.fetchall()

    listbox_accounts.delete(0, END)
    for row in rows:
        listbox_accounts.insert(END, f"Username: {row[0]} | Password: {row[1]}")
    conn.close()

def view_user_stats():
    conn = sqlite3.connect('acp.db')
    cursor = conn.cursor()

    cursor.execute("""
    SELECT last_used_converter, timestamp
    FROM conversion_counter
    WHERE id = 1
    """)
    result = cursor.fetchone()

    cursor.execute("""
    SELECT Username, COUNT(*) AS login_count
    FROM logs
    GROUP BY Username
    ORDER BY login_count DESC
    LIMIT 1;
    """)
    most_active_user = cursor.fetchone()

    listbox_stats.delete(0, END)
    if result:
        last_used_converter, timestamp = result
        listbox_stats.insert(END, f"Last Used Converter: {last_used_converter}")
        if most_active_user:
            username, login_count = most_active_user
            listbox_stats.insert(END, f"Most Active User: {username} (Actions: {login_count})")
        else:
            listbox_stats.insert(END, "Most Active User: None")
        listbox_stats.insert(END, f"Timestamp: {timestamp}")
    
    conn.close()


def view_logs():
    conn = sqlite3.connect('acp.db')
    cursor = conn.cursor()
    
    cursor.execute("""
    SELECT total_conversions
    FROM conversion_counter
    WHERE id = 1
    """)
    total_conversions_result = cursor.fetchone()
    total_conversions = total_conversions_result[0] if total_conversions_result else 0
    
    cursor.execute("""
    SELECT logs.Timestamp, logs.Username
    FROM logs
    """)
    rows = cursor.fetchall()
    listbox_logs.delete(0, END)

    for row in rows:
        user = row[1] if row[1] else "N/A"
        timestamp = row[0] if row[0] else "No timestamp recorded"
        listbox_logs.insert(END, f"{user} |ConvertHistory: {total_conversions} |Time: {timestamp}")
    
    conn.close()



def delete_account():
    selected_item = listbox_accounts.curselection()
    if not selected_item:
        messagebox.showerror("Error", "Please select an account to delete.")
        return

    selected_account = listbox_accounts.get(selected_item[0])
    username = selected_account.split(" | ")[0].split(": ")[1]
    conn = sqlite3.connect('acp.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM accounts WHERE Username = ?", (username,))
    conn.commit()
    conn.close()
    log_action(username, "Deleted account")
    view_db()

conn = sqlite3.connect('acp.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts (
    Username TEXT PRIMARY KEY NOT NULL,
    Password TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS logs (
    Log_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Username TEXT NOT NULL,
    Action TEXT NOT NULL,
    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    total_conversions INTEGER,
    FOREIGN KEY (Username) REFERENCES accounts(Username),
    FOREIGN KEY (total_conversions) REFERENCES conversion_counter(total_conversions)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS conversion_counter (
    id INTEGER PRIMARY KEY,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    last_used_converter TEXT,
    total_conversions INTEGER DEFAULT 0
)

""")

conn.commit()
conn.close()

# Styling
bg_color = '#333333'
fg_color = '#ffffff'
listbox_bg = '#555555'
button_bg = '#4CAF50'
button_fg = '#ffffff'
button_font = ('Arial', 12)

# Frames for side-by-side layout
main_frame = Frame(root, bg=bg_color)
main_frame.pack(fill=BOTH, expand=True, padx=30, pady=30)  # Increased padding for spaciousness

# Left section (Account management)
account_frame = Frame(main_frame, bg=bg_color, bd=4, relief="solid", highlightbackground="#888", highlightthickness=1)  # Rounded and smooth borders
account_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

Label(account_frame, text="Account Management", bg=bg_color, fg=fg_color, font=('Arial', 16, 'bold')).pack(pady=15)
listbox_accounts = Listbox(account_frame, width=60, height=15, bg=listbox_bg, fg=fg_color, font=('Arial', 14), bd=0, relief="flat")
listbox_accounts.pack(pady=10)

view_button = Button(account_frame, text="View Accounts", command=view_db, bg=button_bg, fg=button_fg, font=button_font, width=22, relief="flat", bd=3)
view_button.pack(pady=10)

delete_button = Button(account_frame, text="Delete Account", command=delete_account, bg='#f44336', fg=button_fg, font=button_font, width=22, relief="flat", bd=3)
delete_button.pack(pady=10)

# Center section (Log history)
log_frame = Frame(main_frame, bg=bg_color, bd=4, relief="solid", highlightbackground="#888", highlightthickness=1)  # Rounded and smooth borders
log_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

Label(log_frame, text="Log History", bg=bg_color, fg=fg_color, font=('Arial', 16, 'bold')).pack(pady=15)
listbox_logs = Listbox(log_frame, width=60, height=15, bg=listbox_bg, fg=fg_color, font=('Arial', 14), bd=0, relief="flat")
listbox_logs.pack(pady=10)

view_logs_button = Button(log_frame, text="View Logs", command=view_logs, bg=button_bg, fg=button_fg, font=button_font, width=22, relief="flat", bd=3)
view_logs_button.pack(pady=10)

# Right section (User statistics)
stats_frame = Frame(main_frame, bg=bg_color, bd=4, relief="solid", highlightbackground="#888", highlightthickness=1)  # Rounded and smooth borders
stats_frame.grid(row=0, column=2, sticky="nsew", padx=20, pady=20)

Label(stats_frame, text="User Statistics", bg=bg_color, fg=fg_color, font=('Arial', 16, 'bold')).pack(pady=15)
listbox_stats = Listbox(stats_frame, width=60, height=15, bg=listbox_bg, fg=fg_color, font=('Arial', 14), bd=0, relief="flat")
listbox_stats.pack(pady=10)

view_stats_button = Button(stats_frame, text="View User Stats", command=view_user_stats, bg=button_bg, fg=button_fg, font=button_font, width=22, relief="flat", bd=3)
view_stats_button.pack(pady=10)

# Adjust grid weights for resizing
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)
main_frame.grid_columnconfigure(2, weight=1)
main_frame.grid_rowconfigure(0, weight=1)

root.mainloop()

