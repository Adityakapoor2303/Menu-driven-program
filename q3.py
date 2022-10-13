name = input('Enter your full name: ')
list = name.rsplit()
if len(list)==2:
    firstname = list[0]
    lastname = list[1]
    print(firstname[0].upper()+'.',lastname.title())
else:
    firstname = list[0]
    middlename = list[1]
    lastname = list[-1]
    print(firstname[0].upper()+'.',middlename[0].upper()+'.',lastname.title())
