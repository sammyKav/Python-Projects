
from PIL import Image

def start(nice=0,mean=0,name=""): # overwrites defaults later on. initilizes for later.  
    #get user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)
    


def describe_game(name):
    """
        check if this is a new game or not.
        if it is new, get the user's name.
        if it is not new , thank the player for
        playing game again and continue w game

        """
    #meaning, if we do not already have this user's name,
    # then they are a new player and we need to get their name

    if name !="":
        print("\nThank you for playing again {}".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat you named? \n>>>").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted \nby several different people. \n You can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
    return name
            
def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("n\A stranger approaches you for a \nconversation. Will you be nice \nor mena? (N/M):").lower()
        if pick =="n":
            print("n\The stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick =="m":
            print("\nThe stranger glares at you \meancingly and storms off..")
            mean = (mean + 1) 
            stop = False
        else:
            print("Please enter (N) for nice and (M) for no")
    score(nice,mean,name) # pass the 3 variables to score()


def show_score(nice,mean,name):
    print("\n{}, your current total:\n({}, Nice) and ( {}, Mean)".format(name,nice,mean))


def score(nice,mean,name):
    #score function is being passed the values  stored within 3 variables
    if nice >2: # if condition valid, call win function passing in the variables so it can use them
        win(nice,mean,name)
    if mean >2: # if condition is valid, call lose function passing in the variables so it can use them
        lose(nice,mean,name)
    else:
        nice_mean(nice,mean,name)
        
def win(nice,mean,name):
    #substitue the {} wildcards with our variable values
    myImage = Image.open("Pic1.jpg")
    print("\nNice job {}, you win! \nEveryone loves you and you've \nmade lots of friends along the way!".format(name))
    myImage.show()
    #call again() function and pass in our variables
    again(nice,mean,name)

def lose(nice,mean,name):
    #substitue the [} with our variable values
    print("\nAHHH too bad, game over!".format(name))
    # call again function and pass in our variables
    again(nice,mean,name)




def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo ou want to play again? (y/n):\n>>>").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit() # built in function
        else:
            print("\nEnter (Y) for 'YES', (N) for 'NO': \n>>>")
            
def reset(nice,mean,name):
    nice =0
    mean=0
    # don't reset name
    start(nice,mean,name)
    



if __name__ == "__main__":  #python looks at this and funs the functions listed in order
    start()
    

