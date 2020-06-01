#
# Python:   3.8.3
#
# Author:   Ian Patterson
#
# Purpose:  The Tech Academy - Python Course, Creating our first program together
#           Demonstrating how to pass variables from function to function
#           while producing a function game.


def start(nice=0,mean=0,name=""):
    # get user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)
    
def describe_game(name):
    """
        check if this a new game or not.
        If it is new, get the user's name.
        If it is not a new game, thank the player for
        playing again and continue with the game.
    """
    # menaing, if we do not already have this user's name,
    # then they are a new player and we need to get their name
    if name != "":
        print(f"\nThank you for playing again, {name}")
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print(f"\nWelcome, {name}!")
                    print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean")
                    print("but ta the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
    return name

def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA stranger approaches you for a \nconversation. Will you be nice \nor mean? (N/M) \n>>>: ").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you \nmenacingly and storms off...")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) # pass the 3 variables to the score()

def show_score(nice,mean,name):
    print (f"\n{name}, your current total: \n({nice}, Nice) and ({mean}, Mean)")

def score(nice,mean,name):
    # score function is being passed the values stored within the 3 variable
    if nice > 2:    # if condition is valid, call win function passing in the variables so it can use them
        win(nice,mean,name)
    if mean > 2:    # if condition is valid, call lose function passing in the variables so it can use them
        lose(nice,mean,name)
    else:           # else, call nice_mean function passing in the variables so it can use them
        nice_mean(nice,mean,name)

def win(nice,mean,name):
    # Substitute the {} wildcards with our variable values
    print(f"\nNice job {name}, you win! \nEveryone loves you and you've \nmade lots of friends along the way!")
    # call again function and pass in our variables
    again(nice,mean,name)

def lose(nice,mean,name):
    print(f"\nAhhh too bad, game over! \n{name}, you live in a dirty beat-up \nvan by the river, wretched and alone!")
    again(nice,mean,name)

def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (Y/N) :\n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter (Y) for 'Yes', (N) for 'No':\n>>>")

def reset(nice,mean,name):
    nice = 0
    mean = 0
    start(nice,mean,name)


if __name__ == "__main__":
    start()
