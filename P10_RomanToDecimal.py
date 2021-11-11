tallies = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

def RomanToDecimal(roman):
    sum = 0
    for i in range(len(roman) - 1):
        left = roman[i]
        right = roman[i + 1]
        if tallies[left] < tallies[right]:
            sum -= tallies[left]
        else:
            sum += tallies[left]
    sum += tallies[roman[-1]]
    return sum

a=input("Enter Roman Numeral: \n")
print(RomanToDecimal(a))
