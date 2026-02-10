'''
This module contains the unit tests for the loan_calculator.py module.
Students will add their black box test cases here.
'''
import unittest
from loan_calculator import is_eligible_for_loan

class TestLoanEligibility(unittest.TestCase):
    """
    Test suite for the is_eligible_for_loan function using Black Box Testing
    techniques.
    """
    # --- Example Test Cases (Students will add many more based on EP, BVA, DTT) ---
    def test_valid_applicant_employed_new(self):
        """
        Test case for a valid applicant who is employed and a new customer.
        Expected: True (eligible)
        """
        self.assertTrue(is_eligible_for_loan(
            age=30, 
            income=45000, 
            credit_score=750,
            employment_status='employed', 
            customer_type='new'
            ))

    def test_invalid_age_below_min(self):
        """
        Test case for an applicant with age below the minimum required (EP/BVA).
        Expected: False (ineligible)
        """
        self.assertFalse(is_eligible_for_loan(
            age=17, 
            income=45000, 
            credit_score=750,
            employment_status='employed', 
            customer_type='new'
            ))

    # TODO: Add many more test cases here based on your EP, BVA, and DTT analysis!
    def test_invalid_income_below_min(self):
        """
        Test case for an applicant with income below the minimum required (EP).
        Expected: False (ineligible)
        """
        self.assertFalse(is_eligible_for_loan(
            age=30, 
            income=14999, 
            credit_score=750,
            employment_status='employed', 
            customer_type='new'
            ))

    def test_invalid_credit_score_above_max(self):
        """
        Test case for an applicant with credit score above the maximum allowed (EP).
        Expected: False (ineligible)
        """
        self.assertFalse(is_eligible_for_loan(
            age=30, 
            income=45000, 
            credit_score=851,
            employment_status='employed', 
            customer_type='new'
            ))
        
    def test_invalid_employment_status_unemployed(self):
        """
        Test case for an applicant who is unemployed (EP).
        Expected: False (ineligible)
        """
        self.assertFalse(is_eligible_for_loan(
            age=30, 
            income=45000, 
            credit_score=750,
            employment_status='unemployed', 
            customer_type='new'
            ))

if __name__ == '__main__':
    unittest.main()