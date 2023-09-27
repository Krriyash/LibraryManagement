import tkinter as tk
import csv
import os

# Create a global list to store image references
image_references = []

def list_books():
    def show_book_details(event):
        # Get the selected book title
        selected_index = book_listbox.curselection()
        if selected_index:
            selected_title = book_listbox.get(selected_index)
            selected_isbn = book_data[selected_title]['ISBN']
            
            # Debugging: Print selected title and ISBN
            print(f"Selected Title: {selected_title}")
            print(f"Selected ISBN: {selected_isbn}")
            
            # Display book details and cover image
            title_label.config(text=f"Title: {selected_title}", font=("Poppins", 16))
            author_label.config(text=f"Author: {book_data[selected_title]['Author']}", font=("Poppins", 16))
            genre_label.config(text=f"Genre: {book_data[selected_title]['Genre']}", font=("Poppins", 16))
            rating_label.config(text=f"Rating: {book_data[selected_title]['Rating']}", font=("Poppins", 16))
            isbn_label.config(text=f"ISBN: {selected_isbn}", font=("Poppins", 16))
            
            # Construct the file path for the cover image
            script_dir = os.path.dirname(os.path.abspath(__file__))
            cover_image_path = os.path.join(script_dir, "covers", f"{selected_isbn}.png")
            
            # Check if the image file exists
            if os.path.exists(cover_image_path):
                # Load and resize the cover image
                cover_image = tk.PhotoImage(file=cover_image_path)
                resized_cover_image = cover_image.subsample(4, 4)  # Adjust the subsample values as needed
                cover_label.config(image=resized_cover_image)
                cover_label.image = resized_cover_image  # Store a reference to the image
                image_references.append(resized_cover_image)  # Add the image to the global list
            else:
                # Display a message when no cover image is available
                cover_label.config(image=None, text="No cover image available", font=("Poppins", 16))

    list_window = tk.Toplevel()
    list_window.title("List Books")
    list_window.geometry("1024x768")  # Set window dimensions to 1024x768

    # Read book data from the CSV file and store it in a dictionary
    book_data = {}
    with open("library.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            book_data[row['Title']] = {
                'Author': row['Author'],
                'Genre': row['Genre'],
                'Rating': row['Rating'],
                'ISBN': row['ISBN']
            }

    # Create a Listbox to display book titles on the left side
    book_listbox = tk.Listbox(list_window, font=("Helvetica", 13), fg="white", selectmode="single")
    book_listbox.pack(side="left", fill="y", pady=(10, 10))  # Increased vertical gap between rows

    # Add alternating background colors and gap between rows
    for index, title in enumerate(book_data.keys()):
        color = "#4a4a4a" if index % 2 == 0 else "#383838"
        book_listbox.insert("end", title)
        book_listbox.itemconfig(index, {'bg': color})

    # Create a Frame on the right side for book details and cover image
    details_frame = tk.Frame(list_window)
    details_frame.pack(side="right", fill="both", expand=True)

    # Create labels for book details
    title_label = tk.Label(details_frame, text="", font=("Poppins", 16))
    author_label = tk.Label(details_frame, text="", font=("Poppins", 16))
    genre_label = tk.Label(details_frame, text="", font=("Poppins", 16))
    rating_label = tk.Label(details_frame, text="", font=("Poppins", 16))
    isbn_label = tk.Label(details_frame, text="", font=("Poppins", 16))
    
    # Pack labels with a slight gap between them
    title_label.pack(anchor="w", padx=10, pady=10)
    author_label.pack(anchor="w", padx=10, pady=10)
    genre_label.pack(anchor="w", padx=10, pady=10)
    rating_label.pack(anchor="w", padx=10, pady=10)
    isbn_label.pack(anchor="w", padx=10, pady=10)

    # Create a Label for the cover image
    cover_label = tk.Label(details_frame, text="No cover image available", font=("Poppins", 16))
    cover_label.pack(anchor="center", padx=10, pady=10)

    # Bind the Listbox selection event to display book details
    book_listbox.bind('<<ListboxSelect>>', show_book_details)

    # Bind Enter key to close the list window
    list_window.bind('<Return>', lambda event=None: list_window.destroy())

if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    root.title("Library Management System")
    root.geometry("1024x768")  # Set window dimensions to 1024x768
    root.config(bg="white")  # Set background color to white

    # Start the main event loop
    root.mainloop()
