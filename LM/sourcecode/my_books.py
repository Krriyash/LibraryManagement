import tkinter as tk
import csv
import os

def show_user_books(user_name):
    def borrow_book():
        def submit_borrow():
            isbn = isbn_entry.get()
            with open("library.csv", mode="r") as library_file:
                reader = csv.reader(library_file)
                found = False
                for row in reader:
                    if row[4] == isbn:  # Check the 5th element (index 4) for ISBN
                        found = True
                        user_csv_file = os.path.join("Users", f"{user_name}.csv")
                        with open(user_csv_file, mode="a", newline='') as user_file:
                            writer = csv.writer(user_file)
                            writer.writerow([row[0], row[2], isbn])
                        break
                if found:
                    success_label.config(text="Book successfully borrowed!")
                else:
                    error_label.config(text="Book not found in the library.")

        borrow_window = tk.Toplevel(user_books_window)
        borrow_window.title("Borrow a Book")
        borrow_window.geometry("400x200")
        borrow_window.resizable(False, False)

        isbn_label = tk.Label(borrow_window, text="Enter ISBN:", font=("Times New Roman", 14))
        isbn_label.pack(pady=20)

        isbn_entry = tk.Entry(borrow_window, font=("Times New Roman", 14))
        isbn_entry.pack(pady=10)

        submit_button = tk.Button(borrow_window, text="Submit", command=submit_borrow, font=("Times New Roman", 14))
        submit_button.pack(pady=20)

    def return_book():
        def submit_return():
            isbn = isbn_entry.get()
            user_csv_file = os.path.join("Users", f"{user_name}.csv")
            temp_csv_file = os.path.join("Users", f"{user_name}_temp.csv")

            with open(user_csv_file, mode="r") as user_file, open(temp_csv_file, mode="w", newline='') as temp_file:
                reader = csv.reader(user_file)
                writer = csv.writer(temp_file)
                found = False
                for row in reader:
                    if row[2] == isbn:
                        found = True
                    else:
                        writer.writerow(row)

            os.remove(user_csv_file)
            os.rename(temp_csv_file, user_csv_file)

            if found:
                success_label.config(text="Book successfully returned!")
            else:
                error_label.config(text="Book not found in your list.")

        return_window = tk.Toplevel(user_books_window)
        return_window.title("Return a Book")
        return_window.geometry("400x200")
        return_window.resizable(False, False)

        isbn_label = tk.Label(return_window, text="Enter ISBN:", font=("Times New Roman", 14))
        isbn_label.pack(pady=20)

        isbn_entry = tk.Entry(return_window, font=("Times New Roman", 14))
        isbn_entry.pack(pady=10)

        submit_button = tk.Button(return_window, text="Submit", command=submit_return, font=("Times New Roman", 14))
        submit_button.pack(pady=20)

    user_books_window = tk.Toplevel()
    user_books_window.title(f"{user_name}'s Books")
    user_books_window.geometry("1024x768")
    user_books_window.resizable(False, False)

    user_label = tk.Label(user_books_window, text=f"Books borrowed by {user_name}:", font=("Times New Roman", 16))
    user_label.pack(pady=20)

    user_books_listbox = tk.Listbox(user_books_window, font=("Times New Roman", 14))
    user_books_listbox.pack(fill="both", expand=True, padx=20, pady=10)

    with open(f"Users/{user_name}.csv", mode="r") as user_file:
        reader = csv.reader(user_file)
        for row in reader:
            user_books_listbox.insert("end", row[0])

    borrow_button = tk.Button(user_books_window, text="Borrow", command=borrow_book, font=("Times New Roman", 14))
    borrow_button.pack(side="left", padx=20, pady=10)

    return_button = tk.Button(user_books_window, text="Return", command=return_book, font=("Times New Roman", 14))
    return_button.pack(side="right", padx=20, pady=10)

    success_label = tk.Label(user_books_window, text="", font=("Times New Roman", 14))
    success_label.pack()
    error_label = tk.Label(user_books_window, text="", font=("Times New Roman", 14))
    error_label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Library Management System")
    root.geometry("1024x768")
    root.resizable(False, False)

    root.mainloop()
