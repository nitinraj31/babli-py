year=int(input("enter year:"))
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("leap year:",year)
        else:
            print("not leap year:",year)
    else:
        print("leap year:",year)
else:
    print("not leap year:",year)