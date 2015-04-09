import random

#checks if the player chooses to continue the game
Gameover = None

def guessing_game(best_game):

    # generates a random number
    rannum = random.randint(1,100)
    print rannum

    print "Hello, Player!"
    name = raw_input("What is your name?")

    # checks if the guessed number matches the random number
    found = False
    count = 1
    
    isint = True

    while not found:
        guess = raw_input("What's your guess, %s?" % (name)) 

        # try except loop check if the input enter is a real number. If a
        # Value error occurs, program will ask for a real number.
        try:
            guess = int(guess)
            # if the guess doesn't match the number
            if guess != rannum:
                # checks if the guessed number is between 1-100
                if guess < 1 or guess > 100:
                    print """You thought that was between 1 and 100? Silly! Enter a
                    a real guess!"""
                # checks if number is too low or too high
                elif guess > rannum:
                    print "Your guess is too high"
                elif guess < rannum:
                    print "Your guess is too low"
            else:
                # found set to true to exit the loop
                found = True

                # append the amount of times you guessed to best_game and finds
                # your lowest score
                best_game.append(count) 
                minimum = min(best_game)
                print "Congrats! You found it!!! Your best game is % s" % (minimum)
                
                # asks if you want to play again
                Gameover  = raw_input("Do you want to play again, yes or no?")
                if Gameover.lower() == "yes":
                    guessing_game(best_game)
                else:
                    print "bye bye"
            count += 1
        # the user didn't enter a real number
        except ValueError:
            print "Please enter a real numberrrr!!!!!!!!!!"

# pass an empty array as an argument to cache all previous scores
guessing_game([])