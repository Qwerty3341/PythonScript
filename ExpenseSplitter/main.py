import os
import platform

def clear_terminal() -> None:
    os.system('cls' if platform.system() == 'Windows' else 'clear')


def uneven_splits(total_amount: float, number_of_people: int, currency: str = '$') -> None:
    consumption_list: list = []
    
    while True:
        # clearing the list
        consumption_list.clear()
        for i in range(number_of_people):
            try:
                consumption_list.append(float(input(f'Person {i+1} consume (%): ')))
            except ValueError as e:
                print(f'Error {e}')
                continue
            
        # Checking if the percentages of the consumption list is equals to 100
        if sum(consumption_list) == 100:
            break
        else:
            print('The sum of consumptions are not 100!')
    
    # Get the splits for each person
    clear_terminal()
    print(f'Total expense: {total_amount:,.2f}{currency}')
    print(f'Number of people: {number_of_people}')
    for i, consumption in enumerate(consumption_list, start=1):
        amount_to_pay: float = consumption * total_amount / 100
        print(f'Person {i} ({consumption}%) must pay: {amount_to_pay:.2f}{currency}')
    

def calculate_split(total_amount: float, number_of_people: int, currency: str = '$') -> None:
    if number_of_people < 1:
        raise ValueError('Number of people must be greater than zero')
    
    share_per_person: float = total_amount / number_of_people

    clear_terminal()
    print(f'Total expense: {total_amount:,.2f}{currency}')
    print(f'Number of people: {number_of_people}')
    print(f'Each person should pay: {share_per_person:,.2f}{currency}')


def main() -> None:
    while True:
        try:
            total_amount: float = float(input('Enter the total amount of the expense: '))
            number_of_people: int = int(input('Enter the number of people sharing the expense: '))

            enter_uneven_splits: str = input('Enter uneven splits? (Y/N): ').lower()
            while enter_uneven_splits not in ('y', 'n'):
                print('Enter a valid value!')
                enter_uneven_splits: str = input('Enter uneven splits? (Y/N): ').lower()
                
            if enter_uneven_splits == 'y':
                uneven_splits(total_amount, number_of_people)
            elif enter_uneven_splits == 'n':
                calculate_split(total_amount, number_of_people)
            else:
                print('Wrong choise!')

            break

        except ValueError as e:
            print(f'Error: {e}')


if __name__ == '__main__':
    main()