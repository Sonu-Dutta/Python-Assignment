# Pattern Printing
# Input = Integer n
# Boolean = True or False
#
# True n=5
# *
# **
# ***
# ****
#
# False n=5
# ****
# ***
# **
# *

# method 1

print("Pattern printing")
num = int(input("Enter the number of rows you want : "))
print("Enter 1 or 0")
bool_val = input("1 for True value or 0 for False : ")
if bool_val=="1":
    for i in range(0,num+1):
        print("*"*i)

if bool_val=="0":
    for i in range(num,0,-1):
        print("*"* i)

# Method 2

# size1 = int(input("Enter size of the rows of pattern: "))
# pattrn1 = bool(int(input("Enter : 1 for True \n\t0 for False\n ")))


# def star(size, pattrn):
#     if pattrn == 1:
#         c = 1
#         while c <= size:
#             print(c * "*")
#             c = c + 1
#     else:
#         while size > 0:
#             print(size * "*")
#             size = size - 1


# star(size1, pattrn1)