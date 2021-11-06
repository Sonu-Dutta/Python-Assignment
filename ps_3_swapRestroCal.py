# You visited a restaurant called CodeWithHarry, and the food items in that restaurant are sorted, based on their amount of calories. 
# You have to reserve this list of food items containing calories.
# You have to use the following three methods to reserve a list:
# Inbuild method of python
# List name [::-1] slicing trick
# Swap the first element with the last one and second element with second last one and so on like,
# [6 7 8 34 5] -> [5 34 8 7 6]
# Input:
# Take a list as an input from the user
# [5, 4, 1]
# Output:
# [1, 4, 5]
# [1, 4, 5]
# [1, 4, 5]
# All three methods give the same results!


# Take the size of the list from the user
print("Enter the numbers of the list one by one\n")
size = int(input("Enter size of list\n"))

# Initialize a blank list
mylist = []

# Take the input from the user one by one
for i in range(size):
    mylist.append(int(input("Enter list element\n")))

# mylist = [7,3,2, 34, 1,0]
print(f"Your list is {mylist}\n")

reverse1 = mylist[:]# here --> :  is to reverse the elements from starting index to last index.
reverse1.reverse()

reverse2 = mylist[::2]
print(f"My First reversed list of {mylist} is {reverse1}")
print(f"My Second reversed list of {mylist} is {reverse2}")
reverse3 = mylist[:]
for i in range(len(reverse3)//2):
    reverse3[i], reverse3[len(reverse3) -i -1] = reverse3[len(reverse3) -i -1], reverse3[i] 
    # print(f"the reversed list at i={i} is {reverse3}")
    

print(f"My Third reversed list of {mylist} is {reverse3}")
if reverse1 == reverse2 and reverse2 == reverse3:
    print("All three methods give same result\n")