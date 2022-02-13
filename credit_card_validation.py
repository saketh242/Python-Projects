"""
A simple program that checks if a entered credit card number is valid,
The algorithm used is found in this link: 'https://www.sapling.com/7966257/checksum-credit-card'
"""
def credit_card_validation():
    credit_card_num = list(input("Enter your Credit Card number: "))
    
    check_digit = int(credit_card_num[-1])
    
    new_sum = []
    for i in range(0,15):
        if i %2 != 0:
            new_sum.append(int(credit_card_num[i]))
        else:
            new_sum.append(2*int(credit_card_num[i]))
 
    check_sum = []
    for i in new_sum:
        if i < 10:
            check_sum.append(i)
        else:
            check_sum.append(i-9)
            
    
    if (sum(check_sum) + check_digit) % 10 == 0:
        print("The entered credit card number is a valid number")
        return True
    else:
        return False

credit_card_validation()


# Contact
# sp357@njit.edu