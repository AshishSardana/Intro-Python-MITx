def isPalindrome(aString):
    '''
    aString: a string
    '''
    # Your code here
    for j,i in enumerate(aString):
        if not(i==aString[-j-1]):
            return False
    return True
        
