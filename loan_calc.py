python
def calculate_loan_payment(principal, annual_interest_rate, loan_term_years):
    """
    Calculates the monthly payment for a loan.

    Args:
        principal (float): The present value of the loan (the amount borrowed).
        annual_interest_rate (float): The annual interest rate as a percentage
                                     (e.g., 5 for 5%).
        loan_term_years (int): The term of the loan in years.

    Returns:
        float: The monthly loan payment. Returns None if inputs are invalid.
    """
    if principal <= 0 or annual_interest_rate < 0 or loan_term_years <= 0:
        raise ValueError("Principal and loan term must be positive, and interest rate cannot be negative.")

    # Convert annual interest rate from percentage to decimal and then to monthly
    monthly_interest_rate = (annual_interest_rate / 100) / 12

    # Convert loan term from years to months
    number_of_payments = loan_term_years * 12

    if monthly_interest_rate == 0:
        # Special case for 0% interest rate
        monthly_payment = principal / number_of_payments
    else:
        # Standard loan payment formula
        numerator = monthly_interest_rate * (1 + monthly_interest_rate)**number_of_payments
        denominator = (1 + monthly_interest_rate)**number_of_payments - 1
        monthly_payment = principal * (numerator / denominator)

    return monthly_payment

if __name__ == '__main__':
    # Example usage:
    # Loan amount: $200,000
    # Annual interest rate: 5%
    # Loan term: 30 years
    principal_amount = 200000
    interest_rate_percent = 5
    term_in_years = 30

    try:
        payment = calculate_loan_payment(principal_amount, interest_rate_percent, term_in_years)
        print(f"Loan Principal: ${principal_amount:,.2f}")
        print(f"Annual Interest Rate: {interest_rate_percent}%")
        print(f"Loan Term: {term_in_years} years")
        print(f"Monthly Payment: ${payment:,.2f}")

        # Another example: 0% interest
        principal_amount_zero = 10000
        interest_rate_zero = 0
        term_in_years_zero = 10
        payment_zero = calculate_loan_payment(principal_amount_zero, interest_rate_zero, term_in_years_zero)
        print(f"\nLoan Principal: ${principal_amount_zero:,.2f}")
        print(f"Annual Interest Rate: {interest_rate_zero}%")
        print(f"Loan Term: {term_in_years_zero} years")
        print(f"Monthly Payment (0% interest): ${payment_zero:,.2f}")

    except ValueError as e:
        print(f"Error: {e}")