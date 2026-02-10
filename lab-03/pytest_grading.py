"""
Lab 03: Pytest Grading Tests
"""
import pytest
from grading import calculate_grade, validate_password


# ==========================================
# Calculate Grade Tests 
# ==========================================

def test_pass_grade():
    """Test Case 2: D1 True, D2 True - Both conditions met"""
    assert calculate_grade(50, 70) == "Pass"


def test_conditional_pass():
    """Test Case 1: D1 True, D2 False - Score sufficient, attendance low"""
    assert calculate_grade(50, 60) == "Conditional Pass"


def test_fail_grade():
    """Test Case 3: D1 False - Score insufficient"""
    assert calculate_grade(40, 60) == "Fail"


# ==========================================
# Calculate Grade - Parameterized Tests
# ==========================================

@pytest.mark.parametrize("score,attendance,expected", [
    # Branch coverage test cases
    (50, 70, "Pass"),                    # D1: True, D2: True
    (50, 60, "Conditional Pass"),        # D1: True, D2: False
    (40, 60, "Fail"),                    # D1: False
    
    # Additional boundary and equivalence tests
    (60, 80, "Pass"),                    # Well above thresholds
    (55, 50, "Conditional Pass"),        # Score ok, attendance very low
    (30, 50, "Fail"),                    # Both below thresholds
    (50, 70, "Pass"),                    # Exact boundary values
])
def test_calculate_grade_all_cases(score, attendance, expected):
    """Comprehensive test achieving 100% branch coverage"""
    assert calculate_grade(score, attendance) == expected


# ==========================================
# Password Validation Tests
# ==========================================

def test_valid_password():
    """Valid password with uppercase, digit, and length >= 8"""
    is_valid, message = validate_password("Secure123")
    assert is_valid == True
    assert message == "Valid password"


def test_password_too_short():
    """Password less than 8 characters"""
    is_valid, message = validate_password("Short1")
    assert is_valid == False
    assert message == "Too short"


def test_password_no_digit():
    """Password missing digit"""
    is_valid, message = validate_password("NoDigits")
    assert is_valid == False
    assert message == "Must contain digit"


def test_password_no_uppercase():
    """Password missing uppercase letter"""
    is_valid, message = validate_password("noupper1")
    assert is_valid == False
    assert message == "Must contain uppercase"


def test_password_multiple_failures():
    """Password too short AND no digit"""
    is_valid, message = validate_password("short")
    assert is_valid == False
    assert message == "Too short"


# ==========================================
# Password Validation - Parameterized Tests
# ==========================================

@pytest.mark.parametrize("password,expected_valid,expected_message", [
    # Valid passwords
    ("Secure123", True, "Valid password"),
    ("MyPass99", True, "Valid password"),
    ("ABCD1234", True, "Valid password"),
    
    # Too short
    ("Short1", False, "Too short"),
    ("Ab1", False, "Too short"),
    
    # No digit
    ("NoDigits", False, "Must contain digit"),
    ("PASSWORDONLY", False, "Must contain digit"),
    
    # No uppercase
    ("noupper1", False, "Must contain uppercase"),
    ("lowercase123", False, "Must contain uppercase"),
    
    # Multiple failures (too short takes precedence)
    ("short", False, "Too short"),
    ("abc", False, "Too short"),
])
def test_validate_password_all_paths(password, expected_valid, expected_message):
    """Test all validation paths with parameterization"""
    is_valid, message = validate_password(password)
    assert is_valid == expected_valid
    assert message == expected_message


# ==========================================
# Pytest Fixtures Example
# ==========================================

@pytest.fixture
def valid_grade_inputs():
    """Fixture providing valid grade calculation inputs"""
    return {"score": 75, "attendance": 85}


@pytest.fixture
def valid_password():
    """Fixture providing a valid password"""
    return "StrongPass123"


def test_with_grade_fixture(valid_grade_inputs):
    """Example using a fixture for grade calculation"""
    result = calculate_grade(**valid_grade_inputs)
    assert result == "Pass"


def test_with_password_fixture(valid_password):
    """Example using a fixture for password validation"""
    is_valid, message = validate_password(valid_password)
    assert is_valid == True
    assert message == "Valid password"
