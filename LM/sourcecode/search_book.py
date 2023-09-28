import tkinter as tk
from tkinter import scrolledtext
import csv

def search_book():
    def search():
        query = title_entry.get().lower()  # Get the user's query
        clear_results()  # Clear previous results

        with open("library.csv", mode="r") as file:
            reader = csv.reader(file)
            header = next(reader)  # Skip the first row (header)

            results = []  # Store matching results
            for row in reader:
                # Check if the query matches any of the parameters: Title, Genre, Rating, Author
                if (query in row[0].lower() or  # Title
                    query in row[2].lower() or  # Genre
                    query in row[3].lower() or  # Rating
                    query in row[1].lower()):   # Author

                    results.append(row)  # Add the matching result

            display_results(results, header)

    def clear_results():
        result_text.delete(1.0, "end")  # Clear the text widget

    def display_results(results, header):
        for result in results:
            # Add labels for Title, Genre, Rating, Author
            result_text.insert("end", "\n")
            for idx, value in enumerate(result):
                result_text.insert("end", f"{header[idx]}: {value}\n", ("bold",))
            
            # Add a separator between results
            result_text.insert("end", "\n" + "-"*50 + "\n\n")

    search_window = tk.Toplevel()
    search_window.title("Search Book")
    search_window.geometry("1024x768")  # Set window dimensions to 1024x768

    # Center the title label and reduce its font size
    title_label = tk.Label(search_window, text="Search by Title, Genre, Rating, or Author:", font=("Times New Roman", 14))
    title_label.pack(pady=(20, 0))

    title_entry = tk.Entry(search_window, font=("Times New Roman", 16))
    title_entry.pack(pady=(0, 20))

    # Create a frame for search and clear buttons, side by side with a gap
    button_frame = tk.Frame(search_window)
    button_frame.pack()

    search_button = tk.Button(button_frame, text="Search", command=search, font=("Times New Roman", 16))
    search_button.pack(side="left", padx=10)

    clear_button = tk.Button(button_frame, text="Clear", command=clear_results, font=("Times New Roman", 16))
    clear_button.pack(side="left", padx=10)

    # Create a scrolled text widget for displaying search results with a vertical scrollbar
    result_text = scrolledtext.ScrolledText(search_window, wrap=tk.WORD, font=("Times New Roman", 14))
    result_text.pack(pady=(20, 0), fill="both", expand=True)

if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    root.title("Library Management System")
    root.geometry("1024x768")  # Set window dimensions to 1024x768

    # Example: Adding a button to open the search window
    search_button = tk.Button(root, text="Search Books", command=search_book, font=("Times New Roman", 16))
    search_button.pack(padx=20, pady=20)

    # Start the main event loop
    root.mainloop()
