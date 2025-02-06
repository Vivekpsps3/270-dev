import sys

if __name__ == "__main__":
    # Predefined voltage values for students to fill in directly
    Voltage1 = 10
    Voltage2 = 20
    Voltage3 = 30
    Voltage4 = 40
    Voltage5 = 50

    if len(sys.argv) != 2:
        print("Usage: python assignment1.py <voltage_number>")
        sys.exit(1)

    voltage_number = int(sys.argv[1])

    voltages = [Voltage1, Voltage2, Voltage3, Voltage4, Voltage5]

    if 1 <= voltage_number <= 5:
        print(f"Voltage{voltage_number}: {voltages[voltage_number - 1]}")
    else:
        print("Invalid voltage number. Please enter a number between 1 and 5.")
