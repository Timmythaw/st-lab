'''
This module contains the unit tests for the loan_calculator.py module.
'''
import pytest
from loan_calculator import is_eligible_for_loan


def test_valid_applicant_employed_new():
    """
    Test case for a valid applicant who is employed and a new customer.
    Expected: True (eligible)
    """
    assert is_eligible_for_loan(
        age=30, 
        income=45000, 
        credit_score=750,
        employment_status='employed', 
        customer_type='new'
    ) == True


def test_invalid_age_below_min():
    """
    Test case for an applicant with age below the minimum required (EP/BVA).
    Expected: False (ineligible)
    """
    assert is_eligible_for_loan(
        age=17, 
        income=45000, 
        credit_score=750,
        employment_status='employed', 
        customer_type='new'
    ) == False


def test_invalid_income_below_min():
    """
    Test case for an applicant with income below the minimum required (EP).
    Expected: False (ineligible)
    """
    assert is_eligible_for_loan(
        age=30, 
        income=14999, 
        credit_score=750,
        employment_status='employed', 
        customer_type='new'
    ) == False


def test_invalid_credit_score_above_max():
    """
    Test case for an applicant with credit score above the maximum allowed (EP).
    Expected: False (ineligible)
    """
    assert is_eligible_for_loan(
        age=30, 
        income=45000, 
        credit_score=851,
        employment_status='employed', 
        customer_type='new'
    ) == False


def test_invalid_employment_status_unemployed():
    """
    Test case for an applicant who is unemployed (EP).
    Expected: False (ineligible)
    """
    assert is_eligible_for_loan(
        age=30, 
        income=45000, 
        credit_score=750,
        employment_status='unemployed', 
        customer_type='new'
    ) == False


# ==============================================
# PARAMETERIZED VERSION OF ALL TESTS ABOVE
# ==============================================

@pytest.mark.parametrize("age,income,credit_score,employment_status,customer_type,expected", [
    # Valid applicant
    (30, 45000, 750, 'employed', 'new', True),
    
    # Invalid cases
    (17, 45000, 750, 'employed', 'new', False),  # Age below min
    (30, 14999, 750, 'employed', 'new', False),  # Income below min
    (30, 45000, 851, 'employed', 'new', False),  # Credit score above max
    (30, 45000, 750, 'unemployed', 'new', False),  # Unemployed
])
def test_loan_eligibility_all_cases(age, income, credit_score, employment_status, customer_type, expected):
    """Parameterized test covering all test cases above"""
    assert is_eligible_for_loan(age, income, credit_score, employment_status, customer_type) == expected
