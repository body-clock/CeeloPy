import random

#beginning balance
playerBalance = 5
enemyBalance = 5

playerScore = 0
enemyScore = 0

playerBet = 0
enemyBet = 0

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
    global playerBet

#runs while this condition is true & until it is broken by 'break'
    while True:
        playerBet = int(input('Enter your bet: '))
        print('.')
        #try loop is accounting for ValueError - in case the user inputs something besides a number
        try:
            if int(playerBet) <= 5:
                print('Your bet is $' + str(playerBet))
                bal-=int(playerBet)
                break
            elif int(playerBet) < 1:
                print('You have to bet something!')
            else:
                print("You can't bet that much.")
        except ValueError:
            print('Enter a number please.')

    print('You have $' + str(bal) + ' left')
    print('.')

def SetEnemyBet(bal):
    global enemyBet

    enemyBet = random.randint(0,5)
    bal-=enemyBet
    print('Your opponent bet $' + str(enemyBet) + '.')
    print('They have $' + str(bal) + ' left.')
    print('.')

#dice roll function
def RollDice():
    return [random.randint(1,6) for _ in range(3)]

#analyze the roll list
def AnalyzeRoll(inputRoll):
    global playerScore
    global enemyScore

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
                playerScore = inputRoll[2]
                print('Your score is: ' + str(playerScore))
            else:
                enemyScore = inputRoll[2]
                print("Your opponent's score is: " + str(enemyScore))
            again = False
            return(inputRoll[2])
        elif inputRoll[0] != inputRoll[1]:
            #right pair
            if isPlayerTurn:
                playerScore = inputRoll[0]
                print('Your score is: ' + str(inputRoll[0]))
            else:
                enemyScore = inputRoll[0]
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
    global playerRoll
    global enemyRoll

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
        if isPlayerTurn:
            playerRoll = RollDice()
        else:
            enemyRoll = RollDice()
    else:
        again = False

def CompareScores(p,e):
    global playerBalance
    global enemyBalance

    if p>e:
        playerBalance+=playerBet+enemyBet
    elif e>p:
        enemyBalance+=enemyBet+playerBet
    else:
        print('A tie?')
    print('Your new total is $' + str(playerBalance))
    print("Your opponent's new total is $" + str(enemyBalance))

SetPlayerBet(playerBalance)
SetEnemyBet(enemyBalance)
playerRoll = RollDice()
while again is True:
    scorecode = AnalyzeRoll(playerRoll)
    UpdateScore(scorecode)

isPlayerTurn = False
again = True
enemyRoll = RollDice()
while again is True:
    scorecode = AnalyzeRoll(enemyRoll)
    UpdateScore(scorecode)

#comparison not working properly - probably something to do with
#the scope of the score or balance variables
CompareScores(playerScore, enemyScore)
