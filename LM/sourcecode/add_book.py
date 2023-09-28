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
    
    # Calculate window dimensions
    window_width = 400
    window_height = 240
    
    # Get the screen width and height
    screen_width = add_window.winfo_screenwidth()
    screen_height = add_window.winfo_screenheight()
    
    # Calculate x and y coordinates for the centered window
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    
    add_window.geometry(f"{window_width}x{window_height}+{x}+{y}")  # Center the window

    # Create labels and entries using the pack layout with centered alignment
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

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Library Management System")
    root.geometry("1024x768")
    root.resizable(False, False)

    root.mainloop()
