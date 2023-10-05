import tkinter as tk
import sqlite3
from tkinter import ttk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Credit Data Table")
root.geometry("800x600")

# Create a menu
menu = tk.Menu(root)
root.config(menu=menu)

# Create a submenu for Personal Info
personal_menu = tk.Menu(menu)
menu.add_cascade(label="Personal Info", menu=personal_menu)

# Create a submenu for Credit Accounts
credit_menu = tk.Menu(menu)
menu.add_cascade(label="Credit Accounts", menu=credit_menu)

# Variables to track table visibility
personal_table_visible = False
credit_table_visible = False

def display_personal_info_table():
    global personal_table_visible
    global credit_table_visible

    # Hide the credit accounts table if visible
    if credit_table_visible:
        credit_tree.pack_forget()
        credit_table_visible = False

    # Show the personal info table if not visible
    if not personal_table_visible:
        personal_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        personal_table_visible = True


def display_credit_accounts_table():
    global personal_table_visible
    global credit_table_visible

    # Hide the personal info table if visible
    if personal_table_visible:
        personal_tree.pack_forget()
        personal_table_visible = False

    # Show the credit accounts table if not visible
    if not credit_table_visible:
        credit_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        credit_table_visible = True


def search_personal_info():
    def search():
        person_id = search_entry.get()
        conn = sqlite3.connect('credit_data.db')
        c = conn.cursor()
        c.execute("SELECT first_name, last_name, credit_score FROM personal_info WHERE id=?", (person_id,))
        result = c.fetchone()

        if result:
            messagebox.showinfo(
                "Search Result",
                f"Person Found:\n\nFirst Name: {result[0]}\nLast Name: {result[1]}\nCredit Score: {result[2]}"
            )
        else:
            messagebox.showinfo("Search Result", "Person Not Found")

        conn.close()

    # Create a search window
    search_window = tk.Toplevel(root)
    search_window.title("Search Personal Info")
    search_window.geometry("400x150")

    search_label = tk.Label(search_window, text="Enter ID:")
    search_label.pack()

    search_entry = tk.Entry(search_window)
    search_entry.pack()

    search_button = tk.Button(search_window, text="Search", command=search)
    search_button.pack()


def search_credit_accounts():
    def search():
        person_id = search_entry.get()
        conn = sqlite3.connect('credit_data.db')
        c = conn.cursor()
        c.execute("SELECT * FROM credit_accounts WHERE id=?", (person_id,))
        result = c.fetchone()

        if result:
            messagebox.showinfo("Search Result", f"Person Found:\n\n{result}")
        else:
            messagebox.showinfo("Search Result", "Person Not Found")

        conn.close()

    # Create a search window
    search_window = tk.Toplevel(root)
    search_window.title("Search Credit Accounts")
    search_window.geometry("400x150")

    search_label = tk.Label(search_window, text="Enter ID:")
    search_label.pack()

    search_entry = tk.Entry(search_window)
    search_entry.pack()

    search_button = tk.Button(search_window, text="Search", command=search)
    search_button.pack()

# Create a label for the personal info table
personal_label = tk.Label(root, text="Personal Info Table", font=("Helvetica", 14, "bold"))
personal_label.pack()

# Create a frame for the personal info table
personal_frame = tk.Frame(root)
personal_frame.pack(pady=20)

# Create a treeview widget for the personal info table
personal_tree = ttk.Treeview(personal_frame)

# Define columns for the personal info table
personal_tree["columns"] = (
    "First Name",
    "Last Name",
    "Address",
    "Post Code",
    "Date of Birth",
    "Phone Number",
    "Email",
    "Credit Score"
)

# Format the columns for the personal info table
personal_tree.column("#0", width=0, stretch=tk.NO)
personal_tree.column("First Name", anchor=tk.W, width=120)
personal_tree.column("Last Name", anchor=tk.W, width=120)
personal_tree.column("Address", anchor=tk.W, width=180)
personal_tree.column("Post Code", anchor=tk.W, width=120)
personal_tree.column("Date of Birth", anchor=tk.W, width=120)
personal_tree.column("Phone Number", anchor=tk.W, width=120)
personal_tree.column("Email", anchor=tk.W, width=180)
personal_tree.column("Credit Score", anchor=tk.W, width=100)

# Add headings for the personal info table
personal_tree.heading("#0", text="")
personal_tree.heading("First Name", text="First Name")
personal_tree.heading("Last Name", text="Last Name")
personal_tree.heading("Address", text="Address")
personal_tree.heading("Post Code", text="Post Code")
personal_tree.heading("Date of Birth", text="Date of Birth")
personal_tree.heading("Phone Number", text="Phone Number")
personal_tree.heading("Email", text="Email")
personal_tree.heading("Credit Score", text="Credit Score")

# Retrieve data from the personal info table
conn = sqlite3.connect('credit_data.db')
c = conn.cursor()
c.execute("SELECT * FROM personal_info")
personal_rows = c.fetchall()

for row in personal_rows:
    personal_tree.insert("", tk.END, text="", values=row[1:])
    personal_tree.insert("", tk.END, text="", values=row[1:])

# Add a scrollbar for the personal info table
personal_scrollbar = ttk.Scrollbar(personal_frame, orient="vertical", command=personal_tree.yview)
personal_tree.configure(yscroll=personal_scrollbar.set)
personal_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a label for the credit accounts table
credit_label = tk.Label(root, text="Credit Accounts Table", font=("Helvetica", 14, "bold"))
credit_label.pack()

# Create a frame for the credit accounts table
credit_frame = tk.Frame(root)
credit_frame.pack(pady=20)

# Create a treeview widget for the credit accounts table
credit_tree = ttk.Treeview(credit_frame)

# Define columns for the credit accounts table
credit_tree["columns"] = (
    "Account Type",
    "Date Opened",
    "Credit Limit",
    "Loan Amount",
    "Current Balance",
    "Payment History",
    "Credit Utilization",
    "Public Records",
    "Inquiries",
    "Collections",
    "Credit Age",
    "Credit Accounts",
    "Credit Mix"
)

# Format the columns for the credit accounts table
credit_tree.column("#0", width=0, stretch=tk.NO)
credit_tree.column("Account Type", anchor=tk.W, width=100)
credit_tree.column("Date Opened", anchor=tk.W, width=100)
credit_tree.column("Credit Limit", anchor=tk.W, width=100)
credit_tree.column("Loan Amount", anchor=tk.W, width=100)
credit_tree.column("Current Balance", anchor=tk.W, width=120)
credit_tree.column("Payment History", anchor=tk.W, width=120)
credit_tree.column("Credit Utilization", anchor=tk.W, width=120)
credit_tree.column("Public Records", anchor=tk.W, width=100)
credit_tree.column("Inquiries", anchor=tk.W, width=100)
credit_tree.column("Collections", anchor=tk.W, width=100)
credit_tree.column("Credit Age", anchor=tk.W, width=100)
credit_tree.column("Credit Accounts", anchor=tk.W, width=120)
credit_tree.column("Credit Mix", anchor=tk.W, width=100)

# Add headings for the credit accounts table
credit_tree.heading("#0", text="")
credit_tree.heading("Account Type", text="Account Type")
credit_tree.heading("Date Opened", text="Date Opened")
credit_tree.heading("Credit Limit", text="Credit Limit")
credit_tree.heading("Loan Amount", text="Loan Amount")
credit_tree.heading("Current Balance", text="Current Balance")
credit_tree.heading("Payment History", text="Payment History")
credit_tree.heading("Credit Utilization", text="Credit Utilization")
credit_tree.heading("Public Records", text="Public Records")
credit_tree.heading("Inquiries", text="Inquiries")
credit_tree.heading("Collections", text="Collections")
credit_tree.heading("Credit Age", text="Credit Age")
credit_tree.heading("Credit Accounts", text="Credit Accounts")
credit_tree.heading("Credit Mix", text="Credit Mix")

# Retrieve data from the credit accounts table
c.execute("SELECT * FROM credit_accounts")
credit_rows = c.fetchall()

# Insert data into the credit accounts table
for row in credit_rows:
    credit_tree.insert("", tk.END, text="", values=row[1:])

# Add a scrollbar for the credit accounts table
credit_scrollbar = ttk.Scrollbar(credit_frame, orient="vertical", command=credit_tree.yview)
credit_tree.configure(yscroll=credit_scrollbar.set)
credit_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Pack the credit accounts table
credit_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Add menu options for personal info
personal_menu.add_command(label="Display", command=display_personal_info_table)
personal_menu.add_command(label="Search", command=search_personal_info)

# Add menu options for credit accounts
credit_menu.add_command(label="Display", command=display_credit_accounts_table)
credit_menu.add_command(label="Search", command=search_credit_accounts)

# Run the GUI
root.mainloop()
