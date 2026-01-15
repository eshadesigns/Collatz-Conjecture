# store sequence as an array
collatzArr = []

number = 1

# requests a positive integer input
while True:
    number = input("Enter a positive integer: ")
    try:
        number = int(number)
        if number>0:
            print("Drawing Collatz Tree...")
            break
        else:
            print("Error! The number you entered is not positive")
    except ValueError: # catches decimal and non-numerical input
        print("Error! Input is not an integer")
        
# recursive function to form the sequence
def fillArr(num):
    if num==1:
        collatzArr.append(1)
        return

    collatzArr.append(num)

    if num%2==0:
        num/=2

    else:
        num=(num*3)+1

    fillArr(int(num))

fillArr(number)

def visualize_collatz(arr):
    for i, num in enumerate(arr):
        print("  " * i + f"└─ {num}")

visualize_collatz(collatzArr)

