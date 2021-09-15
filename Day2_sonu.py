#Ques-Write the prime no.
#Enter the no.
#output "(yes this is prime) OR (no this is not prime)"
flag = 0
n=int(input("Enter a number: "))
if(n > 1):
    for i in range(2, int((n**0.5) + 1)):
        if (n % i == 0):
            flag = 1
            break
    if (flag == 0):
        print("Yes , it is a prime number.")
    else:
        print("No , it is not a prime number.")
else:
    print("No , it is not a prime number.")