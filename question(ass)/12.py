str1 = input("Enter first string: ").lower()
str2 = input("Enter second string: ").lower()

if sorted(str1) == sorted(str2):
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")
