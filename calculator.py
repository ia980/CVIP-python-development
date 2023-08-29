print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter choice: ")
Num1 = eval(input("Enter number 1:"))
Num2 = eval(input("Enter number 2:"))
if choice == "1":
    result = Num1+Num2
    print(Num1, "+", Num2, "=", result)
elif choice == "2":
    result = Num1 - Num2
    print(Num1, "-", Num2, "=", result)
elif choice == "3":
    result = Num1 * Num2
    print(Num1, "X", Num2, "=", result)
elif choice == "4":
    result = Num1 / Num2
    print(Num1, "/", Num2, "=", result)
else:
    print("INVALID ENTRY!!")

