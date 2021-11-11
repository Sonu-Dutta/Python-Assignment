import random
# method 1
len = int(input("Enter the length of password \n"))
str="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
# p = "".join(random.sample(str,len ))
# print(p)

# method 2

m=""
for i in range(len):
    m=m+random.choice(str)
print(m)