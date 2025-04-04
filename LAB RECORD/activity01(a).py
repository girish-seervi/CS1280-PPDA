def calculator():
    print("Simple Calculator")
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    print("Select operation:")
    print("1. Add (+)\n2. Subtract (-)\n3. Multiply (*)\n4. Divide (/)")
    print("5. Modulus (%)\n6. Exponentiation (**)\n7. Floor Division (//)")

    choice = input("Enter choice (1-7): ")
    operations = {
        '1': ("+", num1 + num2),
        '2': ("-", num1 - num2),
        '3': ("*", num1 * num2),
        '4': ("/", num1 / num2 if num2 != 0 else "Error! Division by zero"),
        '5': ("%", num1 % num2 if num2 != 0 else "Error! Modulus by zero"),
        '6': ("**", num1 ** num2),
        '7': ("//", num1 // num2 if num2 != 0 else "Error! Floor division by zero")
    }
    
    if choice in operations:
        op, result = operations[choice]
        print(f"Result: {num1} {op} {num2} = {result}")
    else:
        print("Invalid input")

calculator()
