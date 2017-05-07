# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    count=0
    for i in secretWord:
        for j in lettersGuessed:
            if i==j:
                count+=1
                break
    if count==len(secretWord):
        return True
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    count=''
    for i in secretWord:
        flag=0
        for j in lettersGuessed:
            if i==j:
                count=count+i
                flag=1
                break
        if flag==0:
            count=count+'_ '
    return count



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    count=''
    for i in string.ascii_lowercase:
        flag=0
        for j in lettersGuessed:
            if i==j:
                flag=1
                break
        if flag==0:
            count=count+i
    return count
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print ("Welcome to the game, Hangman!\nI am thinking of a ward that is "+str(len(secretWord))+" letters long\n----------")
    guess=8
    flag1=0
    lettersGuessed=[]
    letter=''
    alreadyGuessed=0
    while guess>0:
        flag2=0
        available=getAvailableLetters(lettersGuessed)
        print("You have "+str(guess)+" guesses left.")
        print("Available letters: " + available)
        letter=raw_input('Please guess a letter: ')
        letter=letter.lower()
        if letter in lettersGuessed:
            ans=getGuessedWord(secretWord, lettersGuessed)
            print("Oops! You've already guessed that letter: "+ ans+"\n----------")
            flag2=1
        lettersGuessed.append(letter)
        ans=getGuessedWord(secretWord, lettersGuessed)
        if flag2==0:
            if letter in secretWord:
                print("Good Guess: "+ans+"\n----------")
            else:
                print("Oops! That letter is not in my word: "+ans+"\n----------")
                guess-=1
        if isWordGuessed(secretWord, lettersGuessed):
            print"Congratulations, you won!"
            flag1=1
            break
    if flag1==0:
        print("Sorry, you ran out of guesses. The word was "+secretWord)
            
        
        
    





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
