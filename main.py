#entering a string
a=input("enter a String")
#all the functions used
print("To find length of your string type len")
print("to capitalize the first letter of your string type cap")
print("To have first letter of each word in uppercase type title")
print("To have all characters in your string in lower case type lower")
print("To have all characters in your string in upper case type upper")
print("To find number of characters type count")
print("To find number of occurrence of a letter type find")
print("To find the first occurrence of a letter type index")
print("To find if a string has specific suffix type endswith")
print("To find if a string has specific prefix type startswith")
print("To find if all characters are alpha-numeric type isalnum")
print("To find if all characters are alphabets type isalpha")
print("To find if all characters are digits type isdigit")
print("To find if all characters are in lowercase type islower")
print("To find if all characters are in uppercase type isupper")
print("To find if all characters are whitespaces type isspace")
print("To remove all the leading white spaces type Lstrip")
print("o remove all the trailing white spaces type Rstrip")
print("To remove all the white spaces type strip")
print("To replace a specific phrase with another phrase type replace")
print("To take all items in an iterable and join them in one string type join")
print("To split the string at first occurrence type partition")
print("To split the string at any occurrence type split")
b: str=str(input("enter function"))
if b == "len":
   len = len(a)
   print (f'length of your string is{len}')
elif b=="cap":
    print(a.capitalize())
elif b=="title":
    print(a.title())
elif b=="lower":
    print(a.lower())
elif b=="upper":
    print(a.upper())
elif b=="count":
    c=str(input("Letter to be counted"))
    print(a.count(c))
elif b=="find":
    d=str(input("letter to be found"))
    print(a.find(d))
elif b=="index":
    e=str(input("letter"))
    print(a.index(e))
elif b=="endswith":
    f=str(input("What does it ends with"))
    print(a.endswith(f))
elif b=="startswith":
    g = str(input("What does it starts with"))
    print(a.startswith(g))
elif b=="isalnum":
    print(a.isalnum())
elif b=="isalpha":
    print(a.isalpha())
elif b=="isdigit":
    print(a.isdigit())
elif b=="islower":
    print(a.islower())
elif b=="isupper":
    print(a.isupper())
elif b=="isspace":
    print(a.isspace())
elif b=="Lstrip":
    print(a.lstrip())
elif b=="Rstrip":
    print(a.rstrip())
elif b=="strip":
    print(a.strip())
elif b=="replace":
    h=str(input("enter the word you want to replace"))
    i=str(input("enter the word you want to replace with"))
    print(a.replace(h,i))
elif b=="join":
    j=str(input("enter your separator"))
    k=j.join(a)
    print(k)
elif b=="partition":
    l=str(input("enter the word you want for partition"))
    m=a.partition(l)
    print(m)
elif b=="split":
    n=a.split()
    print(n)










