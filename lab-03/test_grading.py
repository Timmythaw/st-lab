import unittest
from grading import calculate_grade, validate_password

class TestGradeCalculation(unittest.TestCase):
    """Tests for the calculate_grade function."""
    
    def setUp(self):
        """Set up any resources needed for tests (not strictly necessary for this simple function)."""
        pass
    
    # TODO: Implement test methods here to achieve 100% branch coverage for calculate_grade
    # Use the test inputs you identified in Task 2.
    # Example:
    # def test_grade_pass(self):
    #     self.assertEqual(calculate_grade(75, 80), "Pass")
    def test_pass_grade(self):
        """Test Case 2: D1 True, D2 True"""
        self.assertEqual(calculate_grade(50, 70), "Pass")
    
    def test_conditional_pass(self):
        """Test Case 1: D1 True, D2 False"""
        self.assertEqual(calculate_grade(50, 60), "Conditional Pass")
    
    def test_fail_grade(self):
        """Test Case 3: D1 False"""
        self.assertEqual(calculate_grade(40, 60), "Fail")


class TestPasswordValidation(unittest.TestCase):
    """Tests for the validate_password function."""
    
    def setUp(self):
        """Set up any resources needed for tests."""
        pass
    
    # TODO: Implement test methods here to cover all validation paths for validate_password
    # Example:
    # def test_password_valid(self):
    #     is_valid, message = validate_password("StrongPass1!")
    #     self.assertTrue(is_valid)
    #     self.assertEqual(message, "Valid password")
    
    # def test_password_too_short(self):
    #     is_valid, message = validate_password("short")
    #     self.assertFalse(is_valid)
    #     self.assertEqual(message, "Too short")
    def test_valid_password(self):
        """Valid password with uppercase, digit, and length >= 8"""
        is_valid, message = validate_password("Secure123")
        self.assertTrue(is_valid)
        self.assertEqual(message, "Valid password")
    
    def test_password_too_short(self):
        """Password less than 8 characters"""
        is_valid, message = validate_password("Short1")
        self.assertFalse(is_valid)
        self.assertEqual(message, "Too short")
    
    def test_password_no_digit(self):
        """Password missing digit"""
        is_valid, message = validate_password("NoDigits")
        self.assertFalse(is_valid)        
        self.assertEqual(message, "Must contain digit")
    
    def test_password_no_uppercase(self):
        """Password missing uppercase letter"""
        is_valid, message = validate_password("noupper1")
        self.assertEqual(message, "Must contain uppercase")
    
    def test_password_multiple_failures(self):
        """Password too short AND no digit"""
        is_valid, message = validate_password("short")
        self.assertFalse(is_valid)
        self.assertEqual(message, "Too short")


if __name__ == '__main__':
    unittest.main()