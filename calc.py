import os
import keyboard

def main():
    os.system('CLS')

    print("Select an operation to perform: ")
    print("")
    print("1. ADD")
    print("2. SUBTRACT")
    print("3. MULTIPLY")
    print("4. DIVIDE")
    print("")
    operation = input("Enter your option: ")
    print("")
    if operation == '1':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        num12 = num1 + num2
        print("")
        print(f"Result: {num1} + {num2} = {num12}")
        print("")
        print("Press F5 to continue...")
        while True:
            if keyboard.is_pressed('F5'):
                os.system('CLS')
                main()
                break
            else:
                continue
    elif operation == '2':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        num12 = num1 - num2
        print(f"Result: {num1} - {num2} = {num12}")
        print("")
        print("Press F5 to continue...")
        while True:
            if keyboard.is_pressed('F5'):
                os.system('CLS')
                main()
                break
            else:
                continue
    elif operation == '3':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        num12 = num1 * num2
        print(f"Result: {num1} * {num2} = {num12}")
        print("")
        print("Press F5 to continue...")
        while True:
            if keyboard.is_pressed('F5'):
                os.system('CLS')
                main()
                break
            else:
                continue
    elif operation == '4':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        num12 = num1 / num2
        print(f"Result: {num1} / {num2} = {num12}")
        print("")
        print("Press F5 to continue...")
        while True:
            if keyboard.is_pressed('F5'):
                os.system('CLS')
                main()
                break
            else:
                continue
    else:
        print("Invalid Entry")
        

        
main()
