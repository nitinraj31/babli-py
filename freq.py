s=input("enter a string:")
freq={}
for ch in s:
    freq[ch]=freq.get (ch,0)+1
print("character frequency:",freq)
for k,v in freq.items():
 print(k,":",v)