def calculate_grade(score, attendance):
    """
    Calculate grade based on score and attendance.
    
    Args:
        score (int): Test score (0-100)
        attendance (int): Attendance percentage (0-100)
    
    Returns:
        str: Grade result
    """
    if score >= 50 and attendance >= 70:
        return "Pass"
    elif score >= 50:
        return "Conditional Pass"
    else:
        return "Fail"


def validate_password(password):
    """
    Validate password strength.
    
    Args:
        password (str): Password to validate
    
    Returns:
        tuple: (bool, str) - (is_valid, message)
    """
    if len(password) < 8:
        return (False, "Too short")
    if not any(char.isdigit() for char in password):
        return (False, "Must contain digit")
    if not any(char.isupper() for char in password):
        return (False, "Must contain uppercase")
    return (True, "Valid password")