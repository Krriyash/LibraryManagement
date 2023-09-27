import tkinter as tk
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
        # Clear the results by destroying widgets
        for result_frame in result_frames:
            result_frame.destroy()

    def display_results(results, header):
        # Create rows with a maximum of 4 results per row
        for i in range(0, len(results), 4):
            row_results = results[i:i+4]  # Get up to 4 results for this row

            # Create a frame for this row of results
            row_frame = tk.Frame(result_container)
            row_frame.pack(fill="both")

            # Display each result in the row
            for result in row_results:
                # Create a frame for displaying a book's details with thick outline
                result_frame = tk.Frame(row_frame, padx=10, pady=10, bd=4, relief="solid")
                result_frame.pack(side="left", padx=10, pady=10, fill="both", expand=True)

                # Add labels for Title, Genre, Rating, Author
                for idx, value in enumerate(result):
                    tk.Label(result_frame, text=f"{header[idx]}: {value}", font=("Times New Roman", 14)).pack(anchor="w")

                # Append the result frame to the list of frames
                result_frames.append(result_frame)

    search_window = tk.Toplevel()
    search_window.title("Search Book")
    search_window.geometry("1024x768")  # Set window dimensions to 1024x768
    search_window.resizable(False, False)  # Make the window size fixed

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

    # Create a container for the search results
    result_container = tk.Frame(search_window)
    result_container.pack(pady=(20, 0))

    # Create a list to store result frames
    result_frames = []

if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    root.title("Library Management System")
    root.geometry("1024x768")  # Set window dimensions to 1024x768
    root.resizable(False, False)  # Make the window size fixed

    # Example: Adding a button to open the search window
    search_button = tk.Button(root, text="Search Books", command=search_book, font=("Times New Roman", 16))
    search_button.pack(padx=20, pady=20)

    # Start the main event loop
    root.mainloop()
