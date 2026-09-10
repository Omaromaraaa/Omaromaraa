print("| Welcome To Calculater App |")
num1 = float(input("Enter The First Number: "))
operator = print("Choose an operator (+ , - , * , / , ^ , %)")
operator = input("Enter The Operator: ")
num2 = float(input("Enter The Second Number: "))

if operator == "+":
    result = num1+num2
    print(num1, "+" ,num2, "= ",result)
elif operator == "-":
    result = num1-num2
    print(num1, "-" ,num2, "= ",result)
elif operator == "*":
    result = num1*num2
    print(num1, "*" ,num2, "= ",result)
elif operator == "/":
    result = num1/num2
    print(num1, "/" ,num2, "= ",result)
elif operator == "^":
    result = num1**num2
    print(num1, "**" ,num2, "= ",result)   
elif operator == "%":
    result = num1%num2
    print(num1, "%" ,num2, "= ",result)
else:
    print("Wrong operator please try again")  