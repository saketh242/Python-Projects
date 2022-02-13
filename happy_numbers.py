"""
A program which calculates a specific number of happy numbers starting from a specified number
"""

def happy_numbers(num,length = 0):

    num = str(num)
    
    entered_num = num
    happy = 0
    checked_nums = []

    while True:

        happy = 0

        for i in num:
            happy += int(i)**2
        if happy in checked_nums:
            return False

        num = str(happy)
        if happy == 1:
            return True
        else:
            checked_nums.append(happy)

def list_happy_nums(length):
    
    while True:
        num = input("Enter the first number: ")
        length = input("Enter the number of happy numbers you want: ")
        if not num.isnumeric() or not length.isnumeric():
            continue
        else:
            num = int(num)
            length = int(length)
            break
    
    happy_nums = []
    count = 0
    while count < length:
        if happy_numbers(num):
            happy_nums.append(num)
            count += 1
            num += 1
        else:
            num += 1
    print(happy_nums)

list_happy_nums(10)

# Contact
# sp357@njit.edu


        
