s=input("enter a string: ")
vowels="aeiou AEIOU"
for ch in s:
    if ch  in vowels:
        result+=ch
        print("string whiouting vowels:",result)