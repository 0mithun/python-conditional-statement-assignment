year = int(input("Please enter Year: "))

if(year%100 != 0 ) and (year%4 ==0):
    print("leap Year")
elif(year % 100 == 0) and (year % 400 == 0):
    print("leap Year")
else:
    print("Not Leap Year")
