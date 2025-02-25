def calculate_left_salary(gross_salary: float) -> None:
    print('------------------------------------------------')
    list_of_expenses : list = input().split()

    print('Put the money that you spend in each expense')
    for expense in list_of_expenses:
        expense_value: float = float(input(f'{expense} = '))
        gross_salary -= expense_value

    print('Left salary ',gross_salary)


def calculate_finances(monthly_income: float, tax_rate: float, currency: str) -> None:
    monthly_tax: float = monthly_income * (tax_rate / 100)
    monthly_net_income: float = monthly_income - monthly_tax
    yearly_salary: float = monthly_income * 12
    yearly_tax: float = monthly_tax * 12
    yearly_net_income: float = yearly_salary - yearly_tax
    
    print('------------------------------------------------')
    print(f'Monthly income (gross): {currency} {monthly_income:,.2f}')
    print(f'Tax rate: {tax_rate:,.0f}%')
    print(f'Monthly tax: {currency} {monthly_tax:,.2f}')
    print(f'Monthly net income: {currency} {monthly_net_income:,.2f}')
    print(f'Yearly salary: {currency} {yearly_salary:,.2f}')
    print(f'Yearly tax paid: {currency} {yearly_tax:,.2f}')
    print(f'Yearly net income: {currency} {yearly_net_income:,.2f}')
    print('------------------------------------------------')

    add_expenses = input('Add expenses (Y/N)? ').lower()
    if add_expenses == 'y':
        calculate_left_salary(monthly_net_income)

    
def main() -> None:
    while True:
        try:
            monthly_income: float = float(input('Monthly salary: '))
            break
        except:
            print('Put a float value!')
        
    while True:
        try:
            tax_rate: float = float(input('Tax rate (%): '))
            break
        except:
            print('Put a float value!')
    
    calculate_finances(monthly_income, tax_rate, currency='MX')


if __name__ == '__main__':
    main()