# You have to find the next palindrome corresponding to the input number, taken from the user. 
# Output:
# Next palindrome for 342 is 343
# Next palindrome for 95 is 99


def next_palindrome(n):
    n = n+1
    while not is_palindrome(n):
        n += 1
    return n


def is_palindrome(n):
    return str(n) == str(n)[::-1]


# if __name__ == "__main__":
n = int(input("Enter the number of test cases\n"))
numbers = []
for i in range(n):
    no = int(input("Enter the number:\n"))
    numbers.append(no)

for i in range(n):
    print(f"Next palindrome for {numbers[i]} is {next_palindrome(numbers[i])}")
