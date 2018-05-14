import random
import string

WORDLIST_FILENAME = "palavras.txt"

def loadWords():

    print "Loading word list from file..."

    inFile = open(WORDLIST_FILENAME, 'r', 0)
    line = inFile.readline()
    wordList = string.split(line)

    print "  ", len(wordList), "words loaded."

    return random.choice(wordList)


def isWordGuessed(secretWord, lettersGuessed):

    for letter in secretWord:
        if letter in lettersGuessed:
            pass
        else:
            return False

    return True

def getGuessedWord():

     guessed = ''

     return guessed

def getAvailableLetters():
    import string
    # 'abcdefghijklmnopqrstuvwxyz'
    available = string.ascii_lowercase

    return available

def isGuessedWord(letter, lettersGuessed, guessed):
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed += letter
        else:
            guessed += '_'

    return guessed

def showWelcomeMessage(secretWord):

    print 'Welcome to the game, Hangam!'
    print 'I am thinking of a word that is', len(secretWord), ' letters long.'
    print '-------------'

def manageAvailableLetters(available, lettersGuessed):
    for letter in available:
        if letter in lettersGuessed:
            available = available.replace(letter, '')

    print 'Available letters', available
    print '------------'

def hangman(secretWord):

    guesses = 8
    lettersGuessed = []

    showWelcomeMessage(secretWord)


    while  isWordGuessed(secretWord, lettersGuessed) == False and guesses >0:

        print 'You have ', guesses, 'guesses left.'

        guessed = getGuessedWord()

        available = getAvailableLetters()
        manageAvailableLetters(available, lettersGuessed)

        letter = raw_input('Please guess a letter: ')
        print '------------'

        if letter in lettersGuessed:

            guessed = isGuessedWord(letter, lettersGuessed, guessed)
            print 'Oops! You have already guessed that letter: ', guessed

        elif letter in secretWord:

            lettersGuessed.append(letter)

            guessed = isGuessedWord(letter, lettersGuessed, guessed)
            print 'Good Guess: ', guessed

        else:

            guesses -=1
            lettersGuessed.append(letter)

            guessed = isGuessedWord(letter, lettersGuessed, guessed)
            print 'Oops! That letter is not in my word: ',  guessed
            print '------------'

    else:

        if isWordGuessed(secretWord, lettersGuessed) == True:
            print 'Congratulations, you won!'

        else:
            print 'Sorry, you ran out of guesses. The word was ', secretWord, '.'


secretWord = loadWords().lower()
hangman(secretWord)
