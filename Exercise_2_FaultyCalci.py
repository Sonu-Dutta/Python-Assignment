# Exercise 2 - Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator and the two numbers as input from the user
# and then return the result


print("Enter the first Number :")
num1 = int(input())
print("Enter the second Number :")
num2 = int(input())
print("Choose the operation you want to perform" +'+,-,*,/,%')
num3 =input()

if num1 ==45 and num2==3 and num3=='*':
    print("555")
elif num1 == 56 and num2 == 9 and num3 == '+':
        print("77")
elif num1 == 56 and num2 == 6 and num3 == '/':
        print("4")
elif num3 == '+':
    add=num2+num1
    print(add)
elif num3 == '-':
    sub=num2-num1
    print(sub)
elif num3=='*' :
    mul=num1*num2
    print(mul)    
elif num3 == '/':
    div=num2/num1
    print(div)
elif num3 == '%':
    mod=num2%num1
    print(mod)
else:
    print("Error! Please check your input")