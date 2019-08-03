import random

#beginning balance
playerBalance = 5
enemyBalance = 5
again = True

isPlayerTurn = True

while True:
    response = input('Are you ready to play ceelo?: ')
    #continue if user enters yes
    if response=='yes' or response=='y':
        print('You have $' + str(playerBalance))
        break
    elif response=='no' or response=='n' or response=='nope':
        exit()
    else:
        print('Not really what I wanted to hear.')

def SetPlayerBet(bal):
#runs while this condition is true & until it is broken by 'break'
    while True:
        bet = input('Enter your bet: ')
        print('.')
        #try loop is accounting for ValueError - in case the user inputs something besides a number
        try:
            if int(bet) <= 5:
                print('Your bet is $' + str(bet))
                bal-=int(bet)
                break
            elif int(bet) < 1:
                print('You have to bet something!')
            else:
                print("You can't bet that much.")
        except ValueError:
            print('Enter a number please.')

    print('You have $' + str(bal) + ' left')
    print('.')

def SetEnemyBet(bal):
    b = random.randint(0,5)
    bal-=b
    print('Your opponent bet $' + str(b) + '.')
    print('They have $' + str(bal) + ' left.')
    print('.')

#dice roll function
def RollDice():
    return [random.randint(1,6) for _ in range(3)]

#analyze the roll list
def AnalyzeRoll(inputRoll):
    inputRoll.sort()
    if isPlayerTurn:
        print('Your roll is: ' + str(inputRoll))
    else:
        print("Your opponent's roll is: " + str(inputRoll))
    if inputRoll == [4,5,6] or len(set(inputRoll)) == 1:
        #456 or triple - auto win
        return(-1)
    elif inputRoll[0] == inputRoll[1] or inputRoll[1] == inputRoll[2]:
        if inputRoll[2] == 6 and inputRoll[1] != inputRoll[2]:
            #pair of non 6 and 6 - auto win
            return(-1)
        elif inputRoll[0] == 1 and inputRoll[0] != inputRoll[1]:
            #pair of non 1 and 1 - auto lose
            return(-2)
        elif inputRoll[1] != inputRoll[2]:
            #left pair
            if isPlayerTurn:
                print('Your score is: ' + str(inputRoll[2]))
            else:
                print("Your opponent's score is: " + str(inputRoll[2]))
            again = False
            return(inputRoll[2])
        elif inputRoll[0] != inputRoll[1]:
            #right pair
            if isPlayerTurn:
                print('Your score is: ' + str(inputRoll[0]))
            else:
                print("Your opponent's score is: " + str(inputRoll[0]))
            again = False
            return(inputRoll[0])
    elif inputRoll == [1,2,3]:
        #auto lose 123
        return(-2)
    else:
        #special case code - no valid roll
        return(-3)

def UpdateScore(score):
    global again
    global playerScore
    global r

    if score == -1:
        if isPlayerTurn:
            print('You win everything!')
        else:
            print('Your opponent takes it all!')
        again = False
    elif score == -2:
        if isPlayerTurn:
            print('You lose everything!')
        else:
            print('You take it all!')
        again = False
    elif score == -3:
        print('Rolling...')
        r = RollDice()
    else:
        again = False

SetPlayerBet(playerBalance)
SetEnemyBet(enemyBalance)
playerRoll = RollDice()
while again is True:
    scorecode = AnalyzeRoll(playerRoll)
    UpdateScore(scorecode)

#trying to roll for the enemy - not sure about how to handle this
#after the again variable is set to false in the above loop
#i would include it in the above loop, but it requires isPlayerTurn
#to be false in ordef to succeed
isPlayerTurn = False
enemyRoll = RollDice()
while True:
    scorecode = AnalyzeRoll(enemyRoll)
    UpdateScore(scorecode)
