#This program should be a small calculator.

Character1 = float(input("Enter a number: "))
Mathop = (input("Enter a mathematical operator: "))
Character3 = float(input("Enter another number: "))

if Mathop == "+":
    print(Character1 + Character3)
elif Mathop == "-":
    print(Character1 - Character3)
elif Mathop == "*":
    print(Character1 * Character3)
elif Mathop == "/":
    print(Character1/Character3)
else:
    print("Invalid mathematical operator")





    


