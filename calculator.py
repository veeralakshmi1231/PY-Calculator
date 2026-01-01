a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Choose operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice = input("Enter choice (1/2/3/4): ")
if choice == '1':
    print("Result:", a + b)
elif choice == '2':
    print("Result:", a - b)
elif choice == '3':
    print("Result:", a * b)
elif choice == '4':
    print("Result:", a / b)
else:
    print("Invalid choice")
