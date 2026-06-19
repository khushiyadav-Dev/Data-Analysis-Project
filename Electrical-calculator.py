def ohms_law_calculator():
    print("--- Fundamental of Electrical Engineering Calculator ---")
    print("Choose what you want to calculate:")
    print("1. Voltage (V = I * R)")
    print("2. Current (I = V / R)")
    print("3. Resistance (R = V / I)")
    print("4. Electrical Power (P = V * I)")
    
    choice = input("\nEnter choice (1/2/3/4): ")

    if choice == '1':
        i = float(input("Enter Current (I) in Amperes: "))
        r = float(input("Enter Resistance (R) in Ohms: "))
        print(f"Result: Voltage (V) = {i * r} Volts")

    elif choice == '2':
        v = float(input("Enter Voltage (V) in Volts: "))
        r = float(input("Enter Resistance (R) in Ohms: "))
        if r != 0:
            print(f"Result: Current (I) = {v / r} Amperes")
        else:
            print("Error: Resistance cannot be zero!")

    elif choice == '3':
        v = float(input("Enter Voltage (V) in Volts: "))
        i = float(input("Enter Current (I) in Amperes: "))
        if i != 0:
            print(f"Result: Resistance (R) = {v / i} Ohms")
        else:
            print("Error: Current cannot be zero!")

    elif choice == '4':
        v = float(input("Enter Voltage (V) in Volts: "))
        i = float(input("Enter Current (I) in Amperes: "))
        print(f"Result: Power (P) = {v * i} Watts")

    else:
        print("Invalid choice!")

if __name__ == "__main__":
    while True:
        ohms_law_calculator()
        cont = input("\nDo you want to calculate again? (y/n): ").lower()
        if cont != 'y':
            print("Thank you for using the FEE Calculator!")
            break
