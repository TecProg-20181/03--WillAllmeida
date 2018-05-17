import random
import string

WORDLIST_FILENAME = "palavras.txt"

class Guess:

    def __init__(self):
        self.guesses = 8

    def isWordGuessed(self, secretWord, lettersGuessed):

        for letter in secretWord:
            if letter in lettersGuessed:
                pass
            else:
                return False

        return True

    def getGuessedWord(self):

         guessed = ''

         return guessed

    def isGuessedWord(self, letter, lettersGuessed, guessed):
        for letter in secretWord:
            if letter in lettersGuessed:
                guessed += letter
            else:
                guessed += '_'

        return guessed

    def getGuesses(self):

        return self.guesses

    def decreaseGuesses(self):
        self.guesses = self.getGuesses() - 1


def loadWords():

    print "Loading word list from file..."

    inFile = open(WORDLIST_FILENAME, 'r', 0)
    line = inFile.readline()
    wordList = string.split(line)

    print "  ", len(wordList), "words loaded."

    return random.choice(wordList)

class Letter:

    def __init__(self):

        self.available = string.ascii_lowercase

    def getAvailableLetters(self):

        return self.available

    def manageAvailableLetters(self, lettersGuessed):
        for letter in self.available:
            if letter in lettersGuessed:
                self.available = self.available.replace(letter, '')

        print 'Available letters', self.available
        print '------------'


def showWelcomeMessage(secretWord):

    print 'Welcome to the game, Hangam!'
    print 'I am thinking of a word that is', len(secretWord), ' letters long.'
    print '-------------'


def hangman(secretWord):
    guess = Guess()
    letters = Letter()

    lettersGuessed = []

    showWelcomeMessage(secretWord)


    while guess.isWordGuessed(secretWord, lettersGuessed) == False and guess.getGuesses() >0:

        print 'You have ', guess.getGuesses() , 'guesses left.'

        guessed = guess.getGuessedWord()
        available = letters.getAvailableLetters()

        letters.manageAvailableLetters(lettersGuessed)

        letter = raw_input('Please guess a letter: ')
        print '------------'

        if letter in lettersGuessed:

            guessed = guess.isGuessedWord(letter, lettersGuessed, guessed)
            print 'Oops! You have already guessed that letter: ', guessed

        elif letter in secretWord:

            lettersGuessed.append(letter)

            guessed = guess.isGuessedWord(letter, lettersGuessed, guessed)

            print 'Good Guess: ', guessed

        else:
            guess.decreaseGuesses()
            lettersGuessed.append(letter)

            guessed = guess.isGuessedWord(letter, lettersGuessed, guessed)

            print 'Oops! That letter is not in my word: ',  guessed
            print '------------'

    else:

        if guess.isWordGuessed(secretWord, lettersGuessed) == True:
            print 'Congratulations, you won!'

        else:
            print 'Sorry, you ran out of guesses. The word was ', secretWord, '.'


secretWord = loadWords().lower()
hangman(secretWord)
