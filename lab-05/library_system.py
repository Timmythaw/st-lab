class BookDB:
    """Simulates a database for books."""
    def __init__(self):
        self._books = {}  # {isbn: {"title": "...", "author": "...", "available": True}}

    def add_book(self, isbn, title, author):
        """Adds a book to the database."""
        if isbn in self._books:
            return False  # Book already exists
        self._books[isbn] = {"title": title, "author": author, "available": True}
        return True

    def get_book(self, isbn):
        """Retrieves a book by ISBN."""
        return self._books.get(isbn)

    def update_book_status(self, isbn, available):
        """Updates the availability status of a book."""
        if isbn in self._books:
            self._books[isbn]["available"] = available
            return True
        return False

    def delete_book(self, isbn):
        """Deletes a book from the database."""
        if isbn in self._books:
            del self._books[isbn]
            return True
        return False


class UserDB:
    """Simulates a database for users."""
    def __init__(self):
        self._users = {}  # {user_id: {"name": "...", "borrowed_books": []}}

    def add_user(self, user_id, name):
        """Adds a user to the database."""
        if user_id in self._users:
            return False
        self._users[user_id] = {"name": name, "borrowed_books": []}
        return True

    def get_user(self, user_id):
        """Retrieves a user by ID."""
        return self._users.get(user_id)

    def borrow_book(self, user_id, isbn):
        """Records a book as borrowed by a user."""
        user = self._users.get(user_id)
        if user:
            user["borrowed_books"].append(isbn)
            return True
        return False

    def return_book(self, user_id, isbn):
        """Records a book as returned by a user."""
        user = self._users.get(user_id)
        if user and isbn in user["borrowed_books"]:
            user["borrowed_books"].remove(isbn)
            return True
        return False


class BookManager:
    """Manages book-related business logic."""
    def __init__(self, book_db_instance):
        self.book_db = book_db_instance

    def add_book(self, isbn, title, author):
        """Adds a new book to the system."""
        # TODO: Implement this method to use self.book_db.add_book
        # Return True on success, False otherwise (e.g., if book already exists)
        return self.book_db.add_book(isbn, title, author)

    def get_book_details(self, isbn):
        """Retrieves details of a book."""
        return self.book_db.get_book(isbn)

    def is_book_available(self, isbn):
        """Checks if a book is available."""
        book = self.book_db.get_book(isbn)
        return book and book["available"]

    def _mark_book_borrowed(self, isbn):
        """Internal method to mark a book as unavailable."""
        return self.book_db.update_book_status(isbn, False)

    def _mark_book_returned(self, isbn):
        """Internal method to mark a book as available."""
        return self.book_db.update_book_status(isbn, True)


class UserManager:
    """Manages user-related business logic."""
    def __init__(self, user_db_instance):
        self.user_db = user_db_instance

    def register_user(self, user_id, name):
        """Registers a new user."""
        return self.user_db.add_user(user_id, name)

    def get_user_info(self, user_id):
        """Retrieves user information."""
        return self.user_db.get_user(user_id)

    def _record_borrow(self, user_id, isbn):
        """Internal method to record a book borrowed by a user."""
        return self.user_db.borrow_book(user_id, isbn)

    def _record_return(self, user_id, isbn):
        """Internal method to record a book returned by a user."""
        return self.user_db.return_book(user_id, isbn)


class LoanService:
    """Handles the business logic for borrowing and returning books."""
    def __init__(self, book_manager_instance, user_manager_instance):
        self.book_manager = book_manager_instance
        self.user_manager = user_manager_instance

    def borrow_book(self, user_id, isbn):
        """Allows a user to borrow an available book."""
        # TODO: Implement this method.
        # Check if user exists, book exists and is available.
        # If so, mark book as unavailable and record borrow for user.
        # Return True on success, False otherwise.
        if not self.user_manager.get_user_info(user_id):
            return False
        if not self.book_manager.get_book_details(isbn):
            return False
        if not self.book_manager.is_book_available(isbn):
            return False

        if self.book_manager._mark_book_borrowed(isbn) and \
           self.user_manager._record_borrow(user_id, isbn):
            return True
        return False

    def return_book(self, user_id, isbn):
        """Allows a user to return a borrowed book."""
        # TODO: Implement this method.
        # Check if user exists and has borrowed the book.
        # If so, mark book as available and record return for user.
        # Return True on success, False otherwise.
        user = self.user_manager.get_user_info(user_id)
        if not user or isbn not in user["borrowed_books"]:
            return False

        if self.book_manager._mark_book_returned(isbn) and \
           self.user_manager._record_return(user_id, isbn):
            return True
        return False


class LibraryUI:
    """Simulates the user interface for the library system."""
    def __init__(self, book_manager_instance, user_manager_instance, loan_service_instance):
        self.book_manager = book_manager_instance
        self.user_manager = user_manager_instance
        self.loan_service = loan_service_instance

    def display_message(self, message):
        """Displays a message to the user (simulated)."""
        print(f"UI Message: {message}")

    def add_new_book(self, isbn, title, author):
        """Handles adding a new book via UI."""
        if self.book_manager.add_book(isbn, title, author):
            self.display_message(f"Book '{title}' ({isbn}) added successfully.")
            return True
        else:
            self.display_message(f"Failed to add book '{title}' ({isbn}). It might already exist.")
            return False

    def register_new_user(self, user_id, name):
        """Handles registering a new user via UI."""
        if self.user_manager.register_user(user_id, name):
            self.display_message(f"User '{name}' ({user_id}) registered successfully.")
            return True
        else:
            self.display_message(f"Failed to register user '{name}' ({user_id}). User ID might be taken.")
            return False

    def perform_borrow_book(self, user_id, isbn):
        """Handles a user borrowing a book via UI."""
        if self.loan_service.borrow_book(user_id, isbn):
            self.display_message(f"User {user_id} successfully borrowed book {isbn}.")
            return True
        else:
            self.display_message(f"Failed to borrow book {isbn} for user {user_id}. Check user/book existence or availability.")
            return False

    def perform_return_book(self, user_id, isbn):
        """Handles a user returning a book via UI."""
        if self.loan_service.return_book(user_id, isbn):
            self.display_message(f"User {user_id} successfully returned book {isbn}.")
            return True
        else:
            self.display_message(f"Failed to return book {isbn} for user {user_id}. Check user/book or if user actually borrowed it.")
            return False

    def view_book_details(self, isbn):
        """Displays book details via UI."""
        book = self.book_manager.get_book_details(isbn)
        if book:
            self.display_message(f"Book Details: Title: {book['title']}, Author: {book['author']}, Available: {book['available']}")
            return book
        else:
            self.display_message(f"Book with ISBN {isbn} not found.")
            return None

    def view_user_borrowed_books(self, user_id):
        """Displays books borrowed by a user via UI."""
        user = self.user_manager.get_user_info(user_id)
        if user:
            borrowed = ', '.join(user['borrowed_books']) if user['borrowed_books'] else 'None'
            self.display_message(f"User {user['name']} ({user_id}) borrowed books: {borrowed}")
            return user["borrowed_books"]
        else:
            self.display_message(f"User with ID {user_id} not found.")
            return None
