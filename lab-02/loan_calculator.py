'''
This module contains the loan eligibility calculator function.
'''

def is_eligible_for_loan(age: int, income: int, credit_score: int, employment_status: str, customer_type: str) -> bool:
    """
    Determines if a person is eligible for a loan based on several criteria.
    
    Args:
        age (int): The applicant's age.
        income (int): The applicant's annual income.
        credit_score (int): The applicant's credit score.
        employment_status (str): The applicant's employment status (e.g., "employed",
        "unemployed", "student").
        customer_type (str): The applicant's customer type (e.g., "new", "existing",
        "premium").
    
    Returns:
        bool: True if the applicant is eligible for a loan, False otherwise.
    """
    
    # Rule 1: Age must be between 18-65
    if not (18 <= age <= 65):
        return False
    
    # Rule 2: Income must be >= 30000
    if income < 30000:
        return False
    
    # Rule 3: Credit score between 300-850
    if not (300 <= credit_score <= 850):
        return False
    
    # Rule 4: Employment status affects eligibility
    if employment_status.lower() not in ["employed", "self-employed"]:
        return False
    
    # If all basic conditions are met, applicant is eligible
    # Customer type (new, existing, premium) would affect discount in a real system,
    # but for this lab we only return eligibility status
    return True
