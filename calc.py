def calc():
    while True:
        user_input = input("\n Please input two numbers and an arithmetic separated by a comma, +, -, /, * or 'q' to quit: ")
        if user_input == 'q':
            print("Exiting caculator program...")
            break
        arithmeic_values = ['*', '+', '/','-']
        user_input = user_input.split(',')
        removed_item = None
        for item in arithmeic_values:
            if item in user_input:
                user_input.remove(item)
                removed_item = item
                break
        if not removed_item:
            print("please input a valid arithmetic *, +, -, or /")
        
        try:
            user_input = [int(i) for i in user_input]
        except ValueError as e:
            print(f"Invalid input: all operands must be numbers and a python arithmetic operator! Details: {e}")
        
        if len(user_input) != 2:
            print('Please provide exactly two numbers, separated by a comma! \n e.g. 3,2,+ \n')
        else:
            a, b = user_input
            match removed_item:
                case '+':
                    print(f"The solution of {a} + {b} is {a + b}")
                case '*':
                    print(f"The solution of {a} * {b} is {a * b}")
                case '-':
                    print(f"The solution of {a} - {b} is {a - b}")
                case '/':
                    if b == 0:
                        print("cannot divide by zero")
                    print(f"The solution of {a} / {b} is {a / b}")
        

calc()  
              
   
