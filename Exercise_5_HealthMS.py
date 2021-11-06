# Create a food log file for each client
# Create an exercise log file for each client.
# Ask the user whether they want to log or retrieve client data.
# Health Management System
# 3 clients - Harry, Rohan and Tina

# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client

import datetime
def gettime():
    return datetime.datetime.now()
def take(a):
    if a==1:
        log=int(input("Enter:  1 for excersise\n\t2 for food\n"))
        if(log==1):
            value=input("Type here\n")
            with open("harry-exercise.txt","a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("Successfully written")
        elif(log==2):
            value = input("Type here\n")
            with open("harry-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully written")
    elif(a==2):
        log= int(input("Enter:  1 for excersise\n\t2 for food\n"))
        if (log == 1):
            value = input("Type here\n")
            with open("rohan-exercise.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully written")
        elif (log== 2):
            value = input("Type here\n")
            with open("rohan-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully written")
    elif(a==3):
        log = int(input("Enter:  1 for excersise\n\t2 for food\n"))
        if (log == 1):
            value = input("Type here\n")
            with open("tina-exercise.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully written")
        elif (log== 2):
            value = input("Type here\n")
            with open("tina-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully written")
    else:
        print("Enter valid input 1:Harry   2:Rohan   3:Tina\n")
def retrieve(a):
    if a==1:
        ret=int(input("Enter:  1 for excersise\n\t2 for food\n"))
        if(ret==1):
            with open("harry-exercise.txt") as op:
                for i in op:
                    print(i,end="")
        elif(ret==2):
            with open("harry-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(a==2):
        ret = int(input("Enter:  1 for excersise\n\t2 for food\n"))
        if (ret== 1):
            with open("rohan-exercise.txt") as op:
                for i in op:
                    print(i, end="")
        elif (ret== 2):
            with open("rohan-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(a==3):
        ret = int(input("Enter:  1 for excersise\n\t2 for food\n"))
        if (ret == 1):
            with open("tina-exercise.txt") as op:
                for i in op:
                    print(i, end="")
        elif (ret == 2):
            with open("tina-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("Enter valid input 1:Harry   2:Rohan   3:Tina\n")
print("\n*******  Health Management System *******\n ")
log_retrieve=int(input("Press:  1 to log\n\t2 to retrieve\n "))

if log_retrieve==1:
    lr = int(input("Press:  1 for Harry\n\t2 for Rohan\n\t3 for Tina\n "))
    take(lr)
else:
    lr = int(input("Press:  1 for Harry\n\t2 for Rohan\n\t3 for Tina\n"))
    retrieve(lr)