# function which return reverse of a string
# This uses the sequence of the word to check

def reverse(x):
    return x[::-1]
# It holds word together

def isPalindrome(s):
    # Calling reverse function
    rev = reverse(s)

#It flips it
    
    # Checking if both string are equal or not
    if (x == rev):
        return True
    return False


# Driver code
x = raw_input("Is it a palindrome? ")
ans = isPalindrome(x)

if ans == 1:
    print("Yes")
else:
    print("No")
