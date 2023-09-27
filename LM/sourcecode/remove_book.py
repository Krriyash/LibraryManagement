import tkinter as tk
import csv

def remove_book():
    def remove():
        title = title_entry.get().strip()
        isbn = isbn_entry.get().strip()
        
        # Initialize a flag to check if the book was found and removed
        book_removed = False
        
        # Read the entire CSV file into memory
        rows = []
        
        with open("library.csv", mode="r") as file:
            reader = csv.DictReader(file)
            header = reader.fieldnames
            
            for row in reader:
                if title.lower() != row['Title'].strip().lower() or isbn.lower() != row['ISBN'].strip().lower():
                    rows.append(row)
                else:
                    book_removed = True  # Set the flag to True if book found
        
        if book_removed:
            # Write the updated data back to the CSV file
            with open("library.csv", mode="w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=header)
                writer.writeheader()
                writer.writerows(rows)
            
            result_label.config(text="Book removed successfully.")
        else:
            result_label.config(text="Book not found.")

    remove_window = tk.Toplevel()
    remove_window.title("Remove Book")
    remove_window.geometry("1024x768")  # Set window dimensions to 1024x768
    remove_window.resizable(False, False)  # Make the window size fixed

    title_label = tk.Label(remove_window, text="Enter Book Title:")
    title_label.pack()
    title_entry = tk.Entry(remove_window)
    title_entry.pack()

    isbn_label = tk.Label(remove_window, text="Enter ISBN:")
    isbn_label.pack()
    isbn_entry = tk.Entry(remove_window)
    isbn_entry.pack()

    remove_button = tk.Button(remove_window, text="Remove", command=remove)
    remove_button.pack()

    result_label = tk.Label(remove_window, text="")
    result_label.pack()

    # Bind Enter key to remove function
    remove_window.bind('<Return>', lambda event=None: remove())

if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    root.title("Library Management System")
    root.geometry("1024x768")  # Set window dimensions to 1024x768

    # Example: Adding a button to open the remove book window
    remove_button = tk.Button(root, text="Remove Book", command=remove_book, font=("Helvetica", 16))
    remove_button.pack(padx=20, pady=20)

    # Start the main event loop
    root.mainloop()
