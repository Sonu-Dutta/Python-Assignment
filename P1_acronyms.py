#short form (WWW - World Wide Web)
phrase = input("Enter a Phrase: ")
text = phrase.split()
a = " "
# print(text)

for i in text:
    # print(str(i[0]))
    a = a+str(i[0]).upper()
print(a)



