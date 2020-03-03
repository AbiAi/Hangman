import random

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ' \
        'ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda ' \
        'parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider ' \
        'stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()
guessedLetters = []
bad_guesses = []
good_guesses = []
total_guesses_made = 0
total_wrong_guesses = 0
hangman_levels = [''' 
  +---+ 

      | 

      | 

      | 

     ===''', ''' 

  +---+ 

  O   | 

      | 

      | 

     ===''', ''' 

  +---+ 

  O   | 

  |   | 

      | 

     ===''', ''' 

  +---+ 

  O   | 

 /|   | 

      | 

     ===''', ''' 

  +---+ 

  O   | 

 /|\  | 

      | 

     ===''', ''' 

  +---+ 

  O   | 

 /|\  | 

 /    | 

     ===''', ''' 

  +---+ 

  O   | 

 /|\  | 

 / \  | 

     ===''']


def run():
    game()


def game():
    global word, wordToGuessAsList, total_guesses_made, total_wrong_guesses, bad_guesses, good_guesses

    word = random.choice(words)
    wordToGuessAsList = list(word)
    print(wordToGuessAsList)

    while True:
        print('\n---MENU---',
              '\nChoose one of the following options to access the menu',
              '\n1: Get no. of guesses made',
              '\n2: Get all letters I have guessed',
              '\n3: Get the last letter I guessed',
              '\n4: Get Hangman status',
              '\nquit: End game')
        print('\nGuess the word by entering a letter between A and Z\n')

        entry = input()

        try:
            val = int(entry)

            if 0 < val < 6:
                getMenu(val)
            else:
                print("Sorry! That menu option is not available.")

        except ValueError:
            if entry == 'quit':
                break
            elif len(entry) != 1:
                print('Please enter one LETTER between A and Z!')
            else:
                entry = entry.lower()
                current_guess = entry
                guessedLetters.append(current_guess)
                total_guesses_made += 1

                if current_guess in getWordToGuess():
                    if current_guess not in good_guesses:
                        good_guesses.append(current_guess)
                        wordToGuessAsList[:] = [x for x in wordToGuessAsList if x != current_guess]

                        print('Good job! ' + current_guess + ' is in my mystery word.\n' 'Guess another letter!\n')

                    else:
                        print('You already guessed the letter', current_guess,
                              '. It was correct and added to the GOOD GUESS LIST')
                else:
                    if current_guess not in bad_guesses:
                        total_wrong_guesses += 1
                        bad_guesses.append(current_guess)

                        print('Bad guess m8! ' + current_guess + ' is NOT in my mystery word.\n' 'Guess another '
                                                                 'letter!\n')
                        print('Total Wrong Guesses Now: ', total_wrong_guesses)

                    else:
                        print('You already guessed the letter', current_guess,
                              '. It was correct and added to the BAD GUESS LIST')
            if total_wrong_guesses == 7:
                print('You have guessed TOO many wrong answers, Sonny! GAME OVER\n',
                      getHangmanLevel())
                break
            if not wordToGuessAsList:
                print('YOU WON!!!\n The word to guess was ', getWordToGuess())
                break


def getMenu(request):
    if total_wrong_guesses == 0:
        print('Please make your first guess')
    else:
        menu = {
            '5': getWordToGuess(),
            '1': getNoGuessesMade(),
            '2': getAllLettersGuessed(),
            '3': getlastLetterGuessed(),
            '4': getHangmanLevel()
        }
        toString = str(request)
        print(menu.get(toString))


def getWordToGuess():
    return word


def getlastLetterGuessed():
    return guessedLetters[-1]


def getAllLettersGuessed():
    return guessedLetters


def getNoGuessesMade():
    return total_guesses_made


def getHangmanLevel():
    print('\nYou have ', len(hangman_levels) - total_wrong_guesses, ' guesses left!')
    return hangman_levels[total_wrong_guesses - 1]
