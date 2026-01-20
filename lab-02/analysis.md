# Black Box Testing Analysis for Loan Eligibility Calculator
This document outlines the Equivalence Partitioning, Boundary Value Analysis, and
Decision Table Testing applied to the `is_eligible_for_loan` function.
## 1. Equivalence Partitioning (EP)
Identify valid and invalid equivalence classes for each input parameter.
### Age
| Equivalence Class | Description | Representative Value | Result |
|-------------------|-------------|----------------------| ----------------|
| Valid (18-65) | Ages within the eligible range | `40` | Pass |
| Invalid (<18) | Ages below the minimum | `10` | Fail |
| Invalid (>65) | Ages above the maximum | `70` | Fail |

### Income
| Equivalence Class | Description | Representative Value | Result |
|-------------------|-------------|----------------------| ----------------|
| Valid (>=30000) | Incomes at or above minimum | `50000` | Pass |
| Invalid (<30000) | Incomes below minimum | `20000` |  Fail |
### Credit Score
| Equivalence Class | Description | Representative Value |  Result |
|-------------------|-------------|----------------------|  ----------------|
| Valid (300-850) | Scores within eligible range | `600` |  Pass |
| Invalid (<300) | Scores below minimum | `250` |   Fail |
| Invalid (>850) | Scores above maximum | `900` |   Fail |
## 2. Boundary Value Analysis (BVA)
Identify boundary values for each numerical input parameter.
### Age
| Boundary Value | Description | Expected Outcome | 
|----------------|-------------|------------------|
| `17` | Min - 1 | Ineligible |
| `18` | Min | Eligible |
| `65` | Max | Eligible |
| `66` | Max + 1 | Ineligible |
### Income
| Boundary Value | Description | Expected Outcome |
|----------------|-------------|------------------|
| `29999` | Min - 1 | Ineligible |
| `30000` | Min | Eligible |
### Credit Score
| Boundary Value | Description | Expected Outcome |
|----------------|-------------|------------------|
| `299` | Min - 1 | Ineligible |
| `300` | Min | Eligible |
| `850` | Max | Eligible |
| `851` | Max + 1 | Ineligible |
## 3. Decision Table Testing (DTT)
Analyze rules involving `employment_status` and `customer_type`.
**Conditions:**
- C1: Age, Income, Credit Score are all valid (pre-conditions met)
- C2: Employment Status is 'employed' or 'self-employed'
- C3: Customer Type is 'premium'
- C4: Customer Type is 'existing' (and not premium)
**Actions:**
- A1: Eligible for Loan
- A2: Apply Premium Discount (e.g., 5% off interest)
- A3: Apply Existing Customer Discount (e.g., 2% off interest)

| Rule # | C1 | C2 | C3 | C4 | A1 | A2 | A3 | Notes |
|--------|----|----|----|----|----|----|----|-------|
| 1 | Y | Y | Y | N | X | X | | Employed, Premium Customer |
| 2 | Y | Y | N | Y | X | | X | Employed, Existing Customer |
| 3 | Y | Y | N | N | X | | | Employed, New Customer |
| 4 | Y | N | - | - | | | | Not Employed (e.g., unemployed, student)
|
| 5 | N | - | - | - | | | | Age/Income/Credit invalid (any one
fails) |
*Note: For the purpose of this lab, the `is_eligible_for_loan` function only returns
`True` or `False`. The