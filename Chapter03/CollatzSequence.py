print("The Collatz sequence performs a series of mathematical operations on")
print("a number until it arrives at 1. The operation taken on the number is")
print("determined on whether or not the current number in the sequence is even or odd.")
print("Enter a number and I will show you: ")

correctInput = False
while correctInput != True:
    try:
        userNumber = int(input())
        correctInput = True
    except ValueError:
        print('Please enter an integer:')

currentNumber = userNumber

while currentNumber != 1:
    if currentNumber % 2 == 0:
        print(str(currentNumber // 2))
        currentNumber = currentNumber // 2
    else:
        print(str(currentNumber * 3 + 1))
        currentNumber = currentNumber * 3 + 1
