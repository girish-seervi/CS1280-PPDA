def temperature_converter():
    print("Temperature Converter")
    temp = float(input("Enter temperature: "))
    
    print("Select input unit:")
    print("1. Celsius (°C)\n2. Fahrenheit (°F)\n3. Kelvin (K)")
    choice = input("Enter choice (1/2/3): ")

    if choice == '1':  # Celsius to Fahrenheit & Kelvin
        fahrenheit = (temp * 9/5) + 32
        kelvin = temp + 273.15
        print(f"{temp}°C is {fahrenheit}°F and {kelvin}K")
    
    elif choice == '2':  # Fahrenheit to Celsius & Kelvin
        celsius = (temp - 32) * 5/9
        kelvin = celsius + 273.15
        print(f"{temp}°F is {celsius}°C and {kelvin}K")
    
    elif choice == '3':  # Kelvin to Celsius & Fahrenheit
        celsius = temp - 273.15
        fahrenheit = (celsius * 9/5) + 32
        print(f"{temp}K is {celsius}°C and {fahrenheit}°F")
    
    else:
        print("Invalid input")

temperature_converter()

