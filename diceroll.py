import random

def main():                     ##function to set up game
    player1 = 0                 ##call in player 1
    player2 = 0                 ##call in player 2
    round = 1                   ##set round to 1

    while round != 5:                ##test to see if round is at three
        print("Round " + str(round))              ##set each round to roll dice
        player1 = dice_Roll()
        print("Player 1 rolled: ",player1)
        player2 = dice_Roll()
        print("Player 2 rolled: ",player2)

        if player1 > player2:           ##test roll to see who rolled the highest number
            print("Player 1 wins")
        elif player1 < player2:
            print("Player 2 wins")
        else:
            print("It's a draw!")
        
        
        round = round + 1                ##add each round
        
def dice_Roll():
    diceRoll =  random.randint(1,6)         ##roll dice between 1 and 6
    return diceRoll

main()
    
