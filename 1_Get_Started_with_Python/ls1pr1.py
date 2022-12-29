# ls1pr1.py
#
# This is a ROCK-PAPER-SCISSORS simulation
# 1. Open Terminal by pullining it up from the bottom of the VSCode (Shown in the video)
# 2. start ipython (if the PATH is already added) or cd into the location of Script of the python shown in the vid
# 3. cd into the directory that contains this file.
# 4. type 
# - run ls1pr1.py
# - rps()
# 5. It print "Choose your weapon:". Then, you may type 
# - rock
# - paper
# - scissors 
# 6. The computer will random one of those three
# 7. The winner or tie is announced.
# 8. You have to fix it, so it announce the correct winner. 
# 
import random          # imports the library named random
# library is a package that contains ready-to-use programe. In this case, random takes a list of elements then return one of the element randomly
# Green colored texts are comments which are descriptions. They will not be exucuted.

def rps():
    """This plays a game of rock-paper-scissors
       (or a variant of that game)
       Arguments: none     (prompted text doesn't count as an argument)
       Results: none       (printing doesn't count as a result)
    """
    #Show a prompt for user.
    user = input("Choose your weapon(rock or paper or scissors): ")
    comp = random.choice(['rock', 'paper', 'scissors'])
    
    #start a newline
    print()

    #Show the weapon of the user and comp
    print('The user (you)   chose', user)
    print('The computer (I) chose', comp)
    print()

    # if
    # if (Ture), then the actions under if will be executed
    # if (1+1==2):
    #     print("YES")
    # "YES" is printed
    # if (False), then the actions under if will not be executed
    # if (1+1==3):
    #     print("YES")
    # nothing is printed
    # REMARK: == is used to compare, = is used to assign value to variable

    # if, else
    # if (Ture), then the actions under if will be executed and actions under else will not be executed.
    # if (1+1==2):
    #   print("YES")
    # else:
    #   print("NO")
    # "YES" is printed
    # if (False), then the actions under if will be executed and actions under else will not be executed.
    # if (1+1==3):
    #   print("YES")
    # else:
    #   print("NO")
    # "NO" is printed

    # if, elseif
    # if (Ture), then the actions under if will be executed and actions under else will not be executed.
    # if (1+1==2):
    #   print("YES!")
    # elseif (1+1==3):
    #   print("YES!!")
    # elseif (1+1==4):
    #   print("YES!!!")
    # "YES!" is printed
    #
    # if (1+2==2):
    #   print("YES!")
    # elseif (1+2==3):
    #   print("YES!!")
    # elseif (1+2==4):
    #   print("YES!!!")
    # "YES!!" is printed
    #
    # if (1+3==2):
    #   print("YES!")
    # elseif (1+3==3):
    #   print("YES!!")
    # elseif (1+3==4):
    #   print("YES!!!")
    # "YES!!!" is printed


    #Find out who is the winner by comparing the weapon of the use and comp using if, elseif

    if user == 'rock' and comp == 'scissors':
        print('Ha! I actually chose paper, which annihilates your rock.')

    elif user == 'rock' and comp == 'paper':
        print('I won! Your rock is dust!')
    
    #TASK: add all the results of the combination between weapon of user and comp (If struck, see video or ls1pr1_sol.py)




    print("Better luck next time...")