'''
Title: Rock - Paper - Scissor Game
Author: Gloria Dwomoh	
Date: 9/18/2014

Description: Game that simulates rock, paper, scissor game.
             The user plays against the computer.
			 
contact: http://github.com/blossomica

'''

#generating a random choice for seed
from random import choice

while 1:
    name = raw_input("Enter your name : ")
    if  name:
        break

print "\n"
    
print "Rules: Rock breaks Scissors, Scissors cuts Paper, Paper beats Rock\n"
rps = ['r','p','s']

#Here are the score counters for the user, the computer and the round
u = 0
c = 0
round = 0
#Here is the while loop, which will continue till break. The below text is intended to fit into the while loop.
while 1:
    round+=1
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "[--- ROUND #",round,"---]\n"
  
    
    print "R: Rock,      P: Paper,     S: Scissor"
    user = raw_input("Enter your choice among the three : ")   
    user = user.lower()
    py = choice(rps)
    
    print "\n"
    
    if user == py:
        print "You chose ",user
        print "I chose ",py
        print "Hence a Tie!\n"
      

#Here I check the various scenarios, rock, paper, scissor could take and I increase the appropriate counter.
    elif user == 'r' and py == 's':
        print '- You entered Rock. I had Scissor. You win!\n'
        u+=1
    elif user == 'r' and py == 'p':
        print '- You entered Rock. I had Paper. You lose!\n'
        c+=1
    elif user == 's' and py == 'p':
        print 'You entered Scissor. I had Paper. You win!\n'
        u+=1
    elif user == 's' and py == 'r':
        print '- You entered Scissor. I had Rock. You lose!\n'
        c+=1
    elif user == 'p' and py == 's':
        print '- You entered Paper. I had Scissor. You lose\n!'
        c+=1
    elif user == 'p' and py == 'r':
        print '- You entered Paper. I had Rock. You win!\n'
        u+=1
    else:
        print '- Not a valid input. Please try again\n'

    print "So far you have won ",u," times, and lost ",c," times"
    
    if c == 5:
        #Print computer won
        print "\n*** You Played ",round," rounds! ***\n"
        print "Sorry. The computer won the game! Thanks for playing."
        break
    #If user won:
    elif u == 5:
        print "\n*** You Played ",round," rounds! ***\n"
        print " \o/ Congrats! You won " +name+ ". Thanks for playing."
        break
  

