first = input("enter your first number : ")
operator = input("entwr operator (+,-,*,/, %): ")
second = input("enter your second number : ")

if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second)
elif operator == "/":
    print(first / second)
elif operator == "%":
    print(first % second)
else:
    print("invalid operation")