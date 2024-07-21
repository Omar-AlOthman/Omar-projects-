def calculator():
    print("Welcome to calculator by Omar AlOthman.")

    
    while True:
        print("Choose an operator from the menu:")
        print("1. Add")
        print("2. Divide")
        print("3. Subtract")
        print("4. Multiply")
        
    
        choice = input("Choose an operator from the menu (1/add, 2/divide, 3/subtract, 4/multiply): ").strip().lower()
        
        if choice not in ['1', '2', '3', '4', 'add', 'divide', 'subtract', 'multiply']:
            print("Wrong input, please try again.")
            continue  
        
        try:
            first_num = float(input("Enter the first number: "))
            second_num = float(input("Enter the second number: "))
        except ValueError:
            print("Wrong input, please enter valid numbers.")
            continue  

        
        if choice == '1' or choice == 'add':
            print("The result is:", first_num + second_num)
        elif choice == '2' or choice == 'divide':
            if second_num == 0:
                print("Division by zero is not allowed.")
            else:
                print("The result is:", first_num / second_num)
        elif choice == '3' or choice == 'subtract':
            print("The result is:", first_num - second_num)
        elif choice == '4' or choice == 'multiply':
            print("The result is:", first_num * second_num)

        
        another_calculation = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if another_calculation != 'yes':
            break

calculator()



