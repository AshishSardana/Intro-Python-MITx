low = 0
high =100
inp=''
print "Please think of a number between 0 and 100"
while (inp!='c'):
    ans = (high + low)/2
    print('Is your secret number ' + str(ans) + '?')
    inp=raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")          
    if inp=='l':
        low = ans
    elif inp=='h':
        high = ans
    elif inp=='c':
        break
    else:
        print "Sorry, I did not understand your input"
print("Game Over. Your secret number was: " + str(ans))
    
