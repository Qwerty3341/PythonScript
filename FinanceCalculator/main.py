def calculate_left_salary() -> None:
    pass


def calculate_finances(monthly_income: float, tax_rate: float, currency: str) -> None:
    monthly_tax: float = monthly_income * (tax_rate / 100)
    monthly_net_income: float = monthly_income - monthly_tax
    yearly_salary: float = monthly_income * 12
    yearly_tax: float = monthly_tax * 12
    yearly_net_income: float = yearly_salary - yearly_tax
    
    print('------------------------------------------------')
    print(f'Monthly income: {currency} {monthly_income:,.2f}')
    print(f'Tax rate: {tax_rate:,.0f}%')
    print(f'Monthly tax: {currency} {monthly_tax:,.2f}')
    print(f'Monthly net income: {currency} {monthly_net_income:,.2f}')
    print(f'Yearly salary: {currency} {yearly_salary:,.2f}')
    print(f'Yearly tax paid: {currency} {yearly_tax:,.2f}')
    print(f'Yearly net income: {currency} {yearly_net_income:,.2f}')
    print('------------------------------------------------')

    
def main() -> None:
    monthly_income: float = float(input('Monthly salary: '))
    while not isinstance(monthly_income, float):
        print('Put a float value!')
        monthly_income: float = float(input('Monthly salary: '))

    tax_rate: float = float(input('Tax rate (%): '))
    while not isinstance(monthly_income, float):
        print('Put a float value!')
        tax_rate: float = float(input('Tax rate (%): '))

    calculate_finances(monthly_income, tax_rate, currency='MX')


if __name__ == '__main__':
    main()