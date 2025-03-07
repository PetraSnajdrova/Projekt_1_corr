# TODO imports
import os

# TODO main function
def calculator() -> str:
    selection = ('+', '-', '*', '/', 'pow', 'avg', 'quit')

    while True:
        show_selection(selection)
        choice = input('Select operation: ')
        os.system('cls')

        if choice == 'quit':
            print('Good bye')
            break
        elif choice in ('+', '-', '*', '/'):
            calculate_arithmetic_op()
        elif choice in 'pow':
            power()
        elif choice in 'avg':
            count_average()



# TODO Selection listing
def show_selection(*args) -> str:
    """
    Description:
    Connects values from *args with .join method.
    Then adds separator before and after parameters.

    Example:
    args = ("a", "b", "c")

    Result:
    ---------
    a | b | c
    ---------
    """
    joined = ' | '.join(*args)
    separator = "-" * len(joined)
    print(separator, joined, separator, sep="\n")


# TODO power
def power() -> None:
    """
    Description:
    Takes two inputs as parameters:
    1. input is base
    2. input is exponent

    Example:
    input1 = 5
    input2 = 2

    Result:
    5 ** 2 = 25
    """
    input1 = int(input('Base: '))
    input2 = int(input('Exponent: '))
    print(f'{input1} ** {input2} = {input1 ** input2}')


# TODO Average
def count_average() -> None:
    """
    Description:
    Takes values from input and stores them to list.
    Values must be numeric.
    If input '=', func calculates average as sum/lengh of list.

    Example:
    numbers = [1, 2, 3, 4, 5]

    Result:
    Average = 3
    """
    # numbers = list()

    # while (value := input('Number: ')) != '=':
    #     if value.isnumeric():
    #         numbers.append(int(value))

    # result = sum(numbers) / len(numbers)

    # print(f'Average is {result}')
    numbers = list()
    value = int()
    while value != "quit":
        value = input('Value: ')
        if value.isnumeric():
            numbers.append(int(value))

    result = sum(numbers) / len(numbers)

    print(f'Average is {result}')


# TODO Basic arithmetic operators
def calculate_arithmetic_op() -> None:
    entry = ''

    while True:
        button = input('Select number or operator, "=" for result: ')

        if button.isnumeric() or button in ('+', '-', '*', '/'):
            entry += button
        elif button == '=':
            print(f'{entry} = {eval(entry)}')
            break


if __name__ == '__main__':
    calculator()