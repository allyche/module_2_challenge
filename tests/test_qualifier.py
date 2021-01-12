# Import find_qualifying_loans
from app import find_qualifying_loans

# Import pathlib
from pathlib import Path

# Import fileio
from qualifier.utils import fileio

# Import Calculators
from qualifier.utils import calculators

# Import Filters
from qualifier.filters.max_loan_size import filter_max_loan_size
from qualifier.filters.credit_score import filter_credit_score
from qualifier.filters.debt_to_income import filter_debt_to_income
from qualifier.filters.loan_to_value import filter_loan_to_value
from qualifier.utils.fileio import save_csv

def test_save_csv():
    # @TODO: Your code here!
    # Use Path from pathlib to output the test csv to ./data/output/qualifying_loans.csv
    csvpath = Path('./data/output/qualifying_loans.csv')
    header = ["Lender", "Max Loan Amount" , "Max LTV" , "Max DTI" , "Min Credit Score", "Interest Rate"]
    qualifying_loans = ["Bank of Big - Premier Option","300000","0.85","0.47","740","3.6"]
    save_csv(csvpath, qualifying_loans, header)
    assert csvpath.exists()

def test_calculate_monthly_debt_ratio():
    assert calculators.calculate_monthly_debt_ratio(1500, 4000) == 0.375

def test_calculate_loan_to_value_ratio():
    assert calculators.calculate_loan_to_value_ratio(210000, 250000) == 0.84

def test_filters():
    bank_data = fileio.load_csv(Path('./data/daily_rate_sheet.csv'))
    current_credit_score = 750
    debt = 1500
    income = 4000
    loan = 210000
    home_value = 250000

    monthly_debt_ratio = 0.375
    loan_to_value_ratio = 0.84

    # @TODO: Test the filters code!
    # YOUR CODE HERE!
    bank_data_filtered = filter_max_loan_size(loan, bank_data)
    assert len(bank_data_filtered) == 18
    bank_data_filtered = filter_credit_score(current_credit_score, bank_data_filtered)
    assert len(bank_data_filtered) == 9
    bank_data_filtered = filter_debt_to_income(monthly_debt_ratio, bank_data_filtered)
    assert len(bank_data_filtered) == 8
    bank_data_filtered = filter_loan_to_value(loan_to_value_ratio, bank_data_filtered)
    assert len(bank_data_filtered) == 6
