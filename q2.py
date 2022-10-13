str = input('Enter a string: ')
cap = 0
small = 0
for i in str:
    if i.isalpha() == False:
        continue
    elif i.isupper():
        cap+=1
    elif i.islower():
        small+=1
print('Capital alphabets:',cap)
print('Small alphabets:',small)
