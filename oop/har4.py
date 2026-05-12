"""Book store."""
import tkinter as tk
from tkinter import messagebox


class Book:
    """Represent book model."""

    def __init__(self, title: str, author: str, price: float, rating: float):
        """
        Class constructor. Each book has title, author and price.

        :param title: book's title
        :param author: book's author
        :param price: book's price
        """
        self.title = title
        self.author = author
        self.price = price
        self.rating = rating

    def __str__(self):
        """Represent name and author of book."""
        return f"{self.title} by {self.author}"




class Store:
    """Represent book store model."""

    def __init__(self, name: str, rating: float):
        """
        Class constructor.

        Each book store has name.
        There also should be an overview of all books present in store

        :param name: book store name
        :param rating: book store minimum rating
        """
        self.name = name
        self.rating = rating
        self._books = []

    def can_add_book(self, book: Book) -> bool:
        """
        Check if book can be added.

        It is possible to add book to book store if:
        1. The book with the same author and title is not yet present in this book store
        2. book's own rating is >= than store's rating
        :return: bool
        """
        if book.rating <= self.rating:
            return False
        for b in self._books:
            if b.title == book.title and b.author == book.author:
                return False
        return True

    def add_book(self, book: Book):
        """
        Add new book to book store if possible.

        :param book: Book
        Function does not return anything
        """
        if self.can_add_book(book):
            self._books.append(book)

    def can_remove_book(self, book: Book) -> bool:
        """
        Check if book can be removed from store.

        Book can be successfully removed if it is actually present in store

        :return: bool
        """
        return book in self._books

    def remove_book(self, book: Book):
        """
        Remove book from store if possible.

        Function does not return anything
        """
        if self.can_remove_book(book):
            self._books.remove(book)

    def get_all_books(self) -> list:
        """
        Return a list of all books in current store.

        :return: list of Book objects
        """
        return self._books

    def get_books_by_price(self) -> list:
        """
        Return a list of books ordered by price (from cheapest).

        :return: list of Book objects
        """
        return sorted(self._books, key=lambda book: book.price)

    def get_most_popular_book(self) -> list:
        """
        Return a list of book (books) with the highest rating.

        :return: list of Book objects
        """
        if not self._books:
            return []
        max_rating = max(book.rating for book in self._books)
        return [book for book in self._books if book.rating == max_rating]


class StoreApp:
    """Tkinter GUI for the Book Store."""

    def __init__(self, root, store):
        self.root = root
        self.store = store
        self.root.title(f"{self.store.name} Manager")
        self.root.geometry("600x400")

        # Track the list of books currently shown in the Listbox
        # (so we know which object to remove when an item is selected)
        self.current_display_list = []

        self.create_widgets()
        self.refresh_listbox()

    def create_widgets(self):
        # --- Left Frame: Add Book Form ---
        form_frame = tk.LabelFrame(self.root, text="Add a New Book", padx=10, pady=10)
        form_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        tk.Label(form_frame, text="Title:").grid(row=0, column=0, sticky="e", pady=5)
        self.entry_title = tk.Entry(form_frame)
        self.entry_title.grid(row=0, column=1, pady=5)

        tk.Label(form_frame, text="Author:").grid(row=1, column=0, sticky="e", pady=5)
        self.entry_author = tk.Entry(form_frame)
        self.entry_author.grid(row=1, column=1, pady=5)

        tk.Label(form_frame, text="Price:").grid(row=2, column=0, sticky="e", pady=5)
        self.entry_price = tk.Entry(form_frame)
        self.entry_price.grid(row=2, column=1, pady=5)

        tk.Label(form_frame, text="Rating:").grid(row=3, column=0, sticky="e", pady=5)
        self.entry_rating = tk.Entry(form_frame)
        self.entry_rating.grid(row=3, column=1, pady=5)

        add_btn = tk.Button(form_frame, text="Add Book", command=self.add_book_ui, bg="lightblue")
        add_btn.grid(row=4, column=0, columnspan=2, pady=15, sticky="we")

        # --- Right Frame: Inventory View & Controls ---
        inventory_frame = tk.LabelFrame(self.root, text="Inventory", padx=10, pady=10)
        inventory_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Listbox and Scrollbar
        scroll = tk.Scrollbar(inventory_frame)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox = tk.Listbox(inventory_frame, yscrollcommand=scroll.set, width=50)
        self.listbox.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        scroll.config(command=self.listbox.yview)

        # Control Buttons
        btn_frame = tk.Frame(inventory_frame)
        btn_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

        tk.Button(btn_frame, text="Remove Selected", command=self.remove_book_ui).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Show All", command=self.refresh_listbox).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Sort by Price", command=self.sort_by_price_ui).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Most Popular", command=self.show_popular_ui).grid(row=0, column=3, padx=5)

    def add_book_ui(self):
        """Read entries, create a Book, and add to Store."""
        title = self.entry_title.get().strip()
        author = self.entry_author.get().strip()

        if not title or not author:
            messagebox.showerror("Input Error", "Title and Author cannot be empty.")
            return

        try:
            price = float(self.entry_price.get())
            rating = float(self.entry_rating.get())
        except ValueError:
            messagebox.showerror("Input Error", "Price and Rating must be numbers.")
            return

        new_book = Book(title, author, price, rating)

        if self.store.can_add_book(new_book):
            self.store.add_book(new_book)
            self.refresh_listbox()
            self.clear_entries()
            messagebox.showinfo("Success", f"'{title}' added successfully!")
        else:
            messagebox.showwarning("Rejected",
                                   f"Cannot add '{title}'. It may be a duplicate or its rating ({rating}) "
                                   f"is too low for this store (Minimum: >{self.store.rating}).")

    def remove_book_ui(self):
        """Remove the book currently selected in the listbox."""
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showwarning("Selection Error", "Please select a book from the list to remove.")
            return

        index = selection[0]
        book_to_remove = self.current_display_list[index]

        self.store.remove_book(book_to_remove)
        self.refresh_listbox()

    def refresh_listbox(self, books=None):
        """Update the listbox with a list of books."""
        if books is None:
            books = self.store.get_all_books()

        self.listbox.delete(0, tk.END)
        self.current_display_list = books  # Save the reference for removals

        for book in books:
            display_text = f"{book.title} by {book.author} | ${book.price:.2f} | Rating: {book.rating}"
            self.listbox.insert(tk.END, display_text)

    def sort_by_price_ui(self):
        """Fetch sorted books and update listbox."""
        sorted_books = self.store.get_books_by_price()
        self.refresh_listbox(sorted_books)

    def show_popular_ui(self):
        """Fetch most popular books and update listbox."""
        popular_books = self.store.get_most_popular_book()
        self.refresh_listbox(popular_books)

    def clear_entries(self):
        """Clear form inputs after a successful add."""
        self.entry_title.delete(0, tk.END)
        self.entry_author.delete(0, tk.END)
        self.entry_price.delete(0, tk.END)
        self.entry_rating.delete(0, tk.END)


if __name__ == '__main__':
    # Initialize your store with some default data
    my_store = Store("Magic Store", 2.0)
    my_store.add_book(Book("Potter", "Ludwig", 10.0, 5.0))
    my_store.add_book(Book("Potter 2", "Ludwig", 15.0, 4.5))
    my_store.add_book(Book("Potter 3", "Ludwig", 20.0, 5.0))

    # Setup Tkinter and run the app
    root = tk.Tk()
    app = StoreApp(root, my_store)
    root.mainloop()


