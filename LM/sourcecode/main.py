import tkinter as tk
import csv
import os
from add_book import add_book
from remove_book import remove_book
from list_books import list_books
from search_book import search_book
from my_books import show_user_books

# Function to open the My Books window with the user's name
def open_my_books():
    user_name = name_entry.get()  # Get the user's name from the Entry widget

    # Ensure the "Users" folder exists
    users_folder = "Users"
    if not os.path.exists(users_folder):
        os.mkdir(users_folder)

    # Check if the user's CSV file already exists
    user_csv_file = os.path.join(users_folder, f"{user_name}.csv")
    if not os.path.exists(user_csv_file):
        # Create a new user CSV file
        with open(user_csv_file, mode="w", newline='') as new_user_file:
            writer = csv.writer(new_user_file)
            writer.writerow(["Book Title", "Date Borrowed", "ISBN"])
    else:
        # If the user's CSV file exists, load their books from it
        show_user_books(user_name)

# Create the main window
root = tk.Tk()
root.title("Library Management System")
root.geometry("1024x768")  # Set the main window dimensions to 1024x768
root.resizable(False, False)

# Set a custom background image
background_image = tk.PhotoImage(file="g:\LM\sourcecode\covers/background.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Center the heading at the top
heading_frame = tk.Frame(root)
heading_frame.pack(side="top", pady=20)
heading_label = tk.Label(heading_frame, text="Welcome to the Library Management System", font=("Times New Roman", 20))
heading_label.pack()

# Create a frame for buttons and center-align them
button_frame = tk.Frame(root)
button_frame.pack(expand=True, pady=20)

add_book_button = tk.Button(button_frame, text="Add Book", command=add_book, font=("Times New Roman", 14))
remove_book_button = tk.Button(button_frame, text="Remove Book", command=remove_book, font=("Times New Roman", 14))
list_books_button = tk.Button(button_frame, text="List Books", command=list_books, font=("Times New Roman", 14))
search_book_button = tk.Button(button_frame, text="Search Book", command=search_book, font=("Times New Roman", 14))

# Pack the buttons with center and top alignment
add_book_button.pack(fill="x", padx=20, pady=10)
remove_book_button.pack(fill="x", padx=20, pady=10)
list_books_button.pack(fill="x", padx=20, pady=10)
search_book_button.pack(fill="x", padx=20, pady=10)

# Create an Entry widget to collect the user's name
name_entry_frame = tk.Frame(root)
name_entry_frame.pack(expand=True)
name_label = tk.Label(name_entry_frame, text="Enter Your Name:", font=("Times New Roman", 14))
name_label.pack(side="left", padx=20)
name_entry = tk.Entry(name_entry_frame, font=("Times New Roman", 14))
name_entry.pack(side="left", padx=10)
submit_button = tk.Button(name_entry_frame, text="Submit", command=open_my_books, font=("Times New Roman", 14))
submit_button.pack(side="left", padx=10)

# Run the main loop
root.mainloop()
