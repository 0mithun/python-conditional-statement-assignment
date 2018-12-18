number1 = int(input("Pleae Enter First Number: "))
number2 = int(input("Pleae Enter Second Number: "))
number3 = int(input("Pleae Enter Third Number: "))

if((number1 > number2) and (number1 > number3)):
    print("Greater Number is: {}".format(number1))
elif(number2 > number3):
    print("Greater Number is: {}".format(number2))
else:
    print("Greater Number is: {}".format(number3))
