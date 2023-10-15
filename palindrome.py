
def isPalindrome(x: int) -> bool:
    
    if x < 0:     # if its negative its not a palindrome
        return False
    
    reversed_num = 0
    temp = x
    
    while temp != 0:
        digit = temp % 10
        reversed_num = reversed_num * 10 + digit
        temp //= 10
    
    return reversed_num == x 

result = isPalindrome(13311)
print(result)

