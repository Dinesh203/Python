# # kirana shop mini calculator
# no_of_item = 0
# totalRS = 0
# print("press q to finish  shopping")
# while True:
#     button = input("add item rupees: ")
#     if button == 'q':
#         break
#     no_of_item += 1
#     try:
#         totalRS += int(button)
#     except Exception:
#         # print("pleas enter valid item Rs\n")
#         continue

#     print(f"your total bill amount is {totalRS}")

# print(f"total item is: {no_of_item}, and total Rs is:- {totalRS}")

# print("Thank you for shopping with us")



# A simple calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")
