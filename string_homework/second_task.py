while True:
    first_number = int(input('Enter the first number:'))
    second_number = int(input('Enter the second number:'))
    operation = input('Enter the operation (+, -, *, /):')
    if operation == '+':
        print(first_number + second_number)
    elif operation == '-':
        print(first_number - second_number)
    elif operation == '*':
        print(first_number * second_number)
    elif operation == '/':
        if second_number == 0:
            print('Division by zero is impossible')
        else:
            print(first_number / second_number)
    else:
        print('Invalid operation')
    user_answer = input('Do you want to continue?:')
    if user_answer != 'yes' and user_answer != 'Yes' and user_answer != 'y':
       print('Goodbye')
       break