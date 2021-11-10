import random
total_names=int(input("Enter the total number of names : \n"))
names=[]

for i in range(total_names):
    names.append(list(input().split(" ")))
print("list of names are : \n")
print(names)

surname=[]
for i in range(total_names):
    surname.append(names[i][1])
    # print(names[i][1])
# print(surname)
random.shuffle(surname)
print(surname)

print("Jumbled names are : \n")
for i in range(total_names):
    print(names[i][0]+ " " +surname[i])
    # print(names[i][0]+" "+names[random.randint(0,total_names-1)][random.randint(1,len(names[i])-1)])

    # print(names[i][0]+" "+names[random.randint(1,total_names-1)][random.randint(1,len(names[i])-1)])

    #print(names[i][0]+" "+names[random.randint(i,total_names-1)][random.randint(1,len(names[i])-1)])
