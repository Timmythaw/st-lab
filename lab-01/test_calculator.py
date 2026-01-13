# Lab 1: Basic Assertion Script
# TODO: Import functions from calculator.py here
from calculator import add, subtract

# --- Tests for add function ---
print("\n--- Testing add function ---")
# Test Case 1: Positive numbers
# TODO: Write an assertion for add(2, 3) == 5
assert add(2, 3) == 5, "Test Case 1 Failed: add(2, 3) should be 5"

# Test Case 2: Negative numbers
# TODO: Write an assertion for add(-1, 5) == 4
assert add(-1, 5) == 4, "Test Case 2 Failed: add(-1, 5) should be 4"

# Test Case 3: Zero
# TODO: Write an assertion for add(0, 0) == 0
assert add(0, 0) == 0, "Test Case 3 Failed: add(0, 0) should be 0"

# Test Case 4: Larger numbers
# TODO: Write an assertion for add(100, 200) == 300
assert add(100, 200) == 300, "Test Case 4 Failed: add(100, 200) should be 300"

print("All add function tests passed!")

# --- Tests for subtract function ---
print("\n--- Testing subtract function ---")
# Test Case 1: Basic subtraction
# TODO: Write an assertion for subtract(5, 2) == 3
assert subtract(5, 2) == 3, "Test Case 1 Failed: subtract(5, 2) should be 3"

# Test Case 2: Result is negative
# TODO: Write an assertion for subtract(2, 5) == -3
assert subtract(2, 5) == -3, "Test Case 2 Failed: subtract(2, 5) should be -3"

# Test Case 3: Subtracting zero
# TODO: Write an assertion for subtract(10, 0) == 10
assert subtract(10, 0) == 10, "Test Case 3 Failed: subtract(10, 0) should be 10"

# Test Case 4: Subtracting from zero
# TODO: Write an assertion for subtract(0, 5) == -5
assert subtract(0, 5) == -5, "Test Case 4 Failed: subtract(0, 5) should be -5"
print("All subtract function tests passed!")
print("\nAll tests completed successfully!")