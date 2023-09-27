import tkinter as tk
import csv

def add_book():
    def save_book():
        title = title_entry.get()
        author = author_entry.get()
        genre = genre_entry.get()
        rating = rating_entry.get()
        isbn = isbn_entry.get()
        
        # Append the book details to the CSV file
        with open("library.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([title, author, genre, rating, isbn])
        
        add_window.destroy()

    add_window = tk.Toplevel()
    add_window.title("Add Book")
    add_window.geometry("1024x768")  # Set window dimensions to 1024x768

    title_label = tk.Label(add_window, text="Title:")
    title_label.pack()
    title_entry = tk.Entry(add_window)
    title_entry.pack()

    author_label = tk.Label(add_window, text="Author:")
    author_label.pack()
    author_entry = tk.Entry(add_window)
    author_entry.pack()

    genre_label = tk.Label(add_window, text="Genre:")
    genre_label.pack()
    genre_entry = tk.Entry(add_window)
    genre_entry.pack()

    rating_label = tk.Label(add_window, text="Rating:")
    rating_label.pack()
    rating_entry = tk.Entry(add_window)
    rating_entry.pack()

    isbn_label = tk.Label(add_window, text="ISBN:")
    isbn_label.pack()
    isbn_entry = tk.Entry(add_window)
    isbn_entry.pack()

    save_button = tk.Button(add_window, text="Save", command=save_book)
    save_button.pack()

    # Bind Enter key to save_book function
    add_window.bind('<Return>', lambda event=None: save_book())
