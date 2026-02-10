import unittest
from unittest.mock import MagicMock, patch
from library_system import BookDB, UserDB, BookManager, UserManager, LoanService, LibraryUI


class TestIntegration(unittest.TestCase):
    """
    Base class for integration tests.
    """
    def setUp(self):
        """
        Set up fresh instances for each test.
        """
        self.book_db = BookDB()
        self.user_db = UserDB()
        self.book_manager = BookManager(self.book_db)
        self.user_manager = UserManager(self.user_db)
        self.loan_service = LoanService(self.book_manager, self.user_manager)
        self.library_ui = LibraryUI(self.book_manager, self.user_manager, self.loan_service)

    # --- Task 2: Implement your integration tests here ---
    # Example: A simple test to verify BookDB functionality (more like a unit test for BookDB)
    def test_book_db_add_and_get_book(self):
        """Verifies that BookDB can add and retrieve a book."""
        self.assertTrue(self.book_db.add_book("12345", "The Great Python", "A. Coder"))
        book = self.book_db.get_book("12345")
        self.assertIsNotNone(book)
        self.assertEqual(book["title"], "The Great Python")
        self.assertEqual(book["author"], "A. Coder")
        self.assertTrue(book["available"])

    # TODO: Add your integration test for BookManager and BookDB here (Task 2)
    # This test should verify that BookManager's add_book method correctly uses BookDB.
    # No mocking needed for this specific integration.
    def test_book_manager_adds_book_to_db(self):
        """
        TASK 2: Integration test for BookManager and BookDB.
        Tests Bottom-Up integration: BookManager (higher layer) uses BookDB (lower layer).
        """
        # Act: Add book through BookManager
        result = self.book_manager.add_book("67890", "Python Testing Guide", "Jane Developer")

        # Assert: BookManager operation succeeded
        self.assertTrue(result)

        # Assert: Book was actually stored in BookDB (integration verification)
        book = self.book_db.get_book("67890")
        # Assert: Book is not None
        self.assertIsNotNone(book)

        # Assert: Book title is correct
        self.assertEqual(book["title"], "Python Testing Guide")

        # Assert: Book author is correct
        self.assertEqual(book["author"], "Jane Developer")

        # Assert: Book is marked as available
        self.assertTrue(book["available"])

    def test_book_manager_prevents_duplicate_books(self):
        """
        TASK 2 BONUS: Integration test verifying BookManager + BookDB handle duplicates.
        """
        # Add book first time
        self.assertTrue(self.book_manager.add_book("11111", "Duplicate Test", "Author A"))

        # Try to add same ISBN again
        result = self.book_manager.add_book("11111", "Different Title", "Author B")

        # Assert: Second add should fail
        self.assertFalse(result)

        # Assert if Original book unchanged in database
        book = self.book_db.get_book("11111")

        # Assert: Title remains as first added
        self.assertEqual(book["title"], "Duplicate Test")

        # Assert: Author remains as first added
        self.assertEqual(book["author"], "Author A")

    # ==================== ADDITIONAL INTEGRATION TESTS ====================

    def test_user_manager_registers_user_to_db(self):
        """
        Integration test: UserManager + UserDB.
        Tests Bottom-Up integration for user registration.
        """
        # Act: Register user through UserManager
        result = self.user_manager.register_user("user001", "Alice Smith")

        # Assert: Registration succeeded
        self.assertTrue(result)

        # Assert: User stored in UserDB
        user = self.user_db.get_user("user001")
        self.assertIsNotNone(user)
        self.assertEqual(user["name"], "Alice Smith")
        self.assertEqual(user["borrowed_books"], [])

    def test_loan_service_borrow_workflow(self):
        """
        Integration test: LoanService + BookManager + UserManager + BookDB + UserDB.
        Tests complete borrow workflow across multiple layers.
        """
        # Arrange: Set up book and user
        self.book_db.add_book("22222", "Integration Testing", "Test Author")
        self.user_db.add_user("user002", "Bob Johnson")

        # Act: Borrow book through LoanService
        result = self.loan_service.borrow_book("user002", "22222")

        # Assert: Borrow succeeded
        self.assertTrue(result)

        # Assert: Book marked as unavailable
        book = self.book_db.get_book("22222")
        self.assertFalse(book["available"])

        # Assert: User has book in borrowed list
        user = self.user_db.get_user("user002")
        self.assertIn("22222", user["borrowed_books"])

    def test_loan_service_return_workflow(self):
        """
        Integration test: Complete borrow and return workflow.
        Tests all layers working together.
        """
        # Arrange: Set up book, user, and borrow
        self.book_db.add_book("33333", "Return Test Book", "Return Author")
        self.user_db.add_user("user003", "Carol White")
        self.loan_service.borrow_book("user003", "33333")

        # Act: Return the book
        result = self.loan_service.return_book("user003", "33333")

        # Assert: Return succeeded
        self.assertTrue(result)

        # Assert: Book marked as available again
        book = self.book_db.get_book("33333")
        self.assertTrue(book["available"])

        # Assert: User no longer has book in borrowed list
        user = self.user_db.get_user("user003")
        self.assertNotIn("33333", user["borrowed_books"])

    def test_loan_service_prevents_borrowing_unavailable_book(self):
        """
        Integration test: Business logic validation across layers.
        Tests that LoanService correctly prevents borrowing unavailable books.
        """
        # Arrange: Create book and two users
        self.book_db.add_book("44444", "Popular Book", "Famous Author")
        self.user_db.add_user("user004", "David Brown")
        self.user_db.add_user("user005", "Eve Green")

        # Act: First user borrows the book
        self.loan_service.borrow_book("user004", "44444")

        # Act: Second user tries to borrow same book
        result = self.loan_service.borrow_book("user005", "44444")

        # Assert: Second borrow should fail
        self.assertFalse(result)

        # Assert: Only first user has the book
        user4 = self.user_db.get_user("user004")
        user5 = self.user_db.get_user("user005")
        self.assertIn("44444", user4["borrowed_books"])
        self.assertNotIn("44444", user5["borrowed_books"])

    def test_library_ui_complete_workflow(self):
        """
        Integration test: All layers (UI + Services + Managers + Database).
        Tests Top-Down integration from UI layer down to database layer.
        """
        # Act: Add book through UI
        add_book_result = self.library_ui.add_new_book("55555", "UI Test Book", "UI Author")

        # Act: Register user through UI
        register_result = self.library_ui.register_new_user("user006", "Frank Miller")

        # Act: Borrow book through UI
        borrow_result = self.library_ui.perform_borrow_book("user006", "55555")

        # Assert: All operations succeeded
        self.assertTrue(add_book_result)
        self.assertTrue(register_result)
        self.assertTrue(borrow_result)

        # Assert: Data persisted correctly in database layer
        book = self.book_db.get_book("55555")
        user = self.user_db.get_user("user006")
        self.assertFalse(book["available"])
        self.assertIn("55555", user["borrowed_books"])

    # TODO: Consider how you would use stubs/drivers for other integration strategies later
    # For example, if testing LoanService in isolation from UI, you might 'drive' it directly.
    # If testing UI, you might 'stub' BookManager/UserManager/LoanService methods.


class TestTopDownWithStubs(unittest.TestCase):
    """
    Example of Top-Down integration testing using stubs.
    This demonstrates how to test UI layer in isolation using stubbed lower layers.
    """

    def test_ui_with_stubbed_managers(self):
        """
        Top-Down integration test: Test LibraryUI with stubbed managers.
        Stubs simulate the behavior of BookManager, UserManager, and LoanService.
        """
        # Arrange: Create stubs (simplified mock objects)
        stub_book_manager = MagicMock()
        stub_user_manager = MagicMock()
        stub_loan_service = MagicMock()

        # Configure stub responses
        stub_book_manager.add_book.return_value = True
        stub_loan_service.borrow_book.return_value = True

        # Create UI with stubbed dependencies
        ui = LibraryUI(stub_book_manager, stub_user_manager, stub_loan_service)

        # Act: Test UI methods
        result = ui.add_new_book("99999", "Stubbed Book", "Stub Author")

        # Assert: UI correctly called the stubbed manager
        self.assertTrue(result)
        stub_book_manager.add_book.assert_called_once_with("99999", "Stubbed Book", "Stub Author")


class TestBottomUpWithDrivers(unittest.TestCase):
    """
    Example of Bottom-Up integration testing with drivers.
    The test methods themselves act as drivers for lower-level components.
    """

    def test_book_db_as_driver(self):
        """
        Bottom-Up integration test: Test BookDB directly (test acts as driver).
        This verifies the lowest layer before integrating with higher layers.
        """
        # This test itself is the "driver" - it calls BookDB directly
        book_db = BookDB()

        # Driver action: Add book
        result = book_db.add_book("88888", "Driver Test", "Driver Author")
        self.assertTrue(result)

        # Driver action: Verify storage
        book = book_db.get_book("88888")
        self.assertEqual(book["title"], "Driver Test")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
