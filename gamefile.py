#number game if u roll 1 ur points are lost however who secure 50 score will be the winner.

import random

def roll():
    min_val=1
    max_val=6
    roll=random.randint(min_val,max_val)
    return roll
    
while True:
    players=input("Enter the no of player(2-4) : ")
    if players.isdigit():
        players=int(players)
        if 2<= players<=4 :
            break
        
        print("Pls enter no of players b/w 2-4 .")
    else:
        print("Invalid, pls try again!!!")
        
print("No of players : ",players)

max_score=50
player_score=[0 for i in range(players)]
 
while max(player_score) < max_score :
    
    for player_no in range(players):
        
        print("\nplayer",player_no+1," turn has started!")
        print("ur current score is : ",player_score[player_no])
        
        current_score=0
        
        while True:
            user_roll=input("Would u like to roll (y)? : ").lower()
            if user_roll != "y":
                break
            
            value=roll()
            if value==1:
                
                print("You rolled 1 ! Turn over ")
                current_score=0
                break
            else:
                current_score+=value
                print("U rolled a: ",value)
            print("Ur current score : ",current_score)
        
        player_score[player_no]+=current_score   
        print("Ur Total score : ",player_score[player_no])
        
max_score = max(player_score)
winner= player_score.index(max_score)        
print("Player",winner+1," is the winner 🥳 with a score of : ",max_score)
