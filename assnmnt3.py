
equal=True
itsNot=False
def ThreeNumbers(number1, number2, number3):
    if int(number1)==int(number2) or int(number1)==int(number3) or int(number2)==int(number3):
        print("Are any two numbers equal ? ")
        print(equal)
    elif int(number1)!=int(number2) or int(number1)!=int(number3) or int(number2)!=int(number3):
        print("Are any two numbers equal ? ")
        print(itsNot)
    return

ThreeNumbers(3,3,4)

ThreeNumbers(3,3,3)

ThreeNumbers(2,3,4)