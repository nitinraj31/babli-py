str1=input ("enter thestring to check whecther the  string is palindrome or not:")
str2=str1[::-1]
if str1==str2:
    print("the given string is palindrome") 
else:
    print("the given string is not palindrome")
