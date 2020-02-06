#MQ



import random

#------------Variable Dictionary--------------
age=18          #age of the user
lotto=0         #0=false 1=true 
week=3224       #Weeks in 62 years if you stop playing at 80years old
numbers=[0,0,0,0,0,0]      #List holding the user chosen numbers
wNumbers=[0,0,0,0,0,0]     #List holds the Winning numbers
price=0         #How much money spent on playing the powerball
mostWins=0      #Highest amount of correctly chosen numbers
mostWinTimes=0  #Amount of times the users hits the highest matches
#x              The numbers that you can choose from or that the computer can choose
x=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69']
#n              The Powerball numbers that you can choose from or that the computer can choose
n=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26']
#------------Functions------------------------
def intro():
    print('You are 18 years old')
    print('If you played the Powerball every week,\n\twould you be able to win?')
    print('\nTo make life easy choose your lucky numbers now.')
    print('You can only choose a number between 1-69\n')

def chosenNumbers():
    while numbers[0] not in x:
        numbers[0]=input('1. :')
    numbers[0]=int(numbers[0])
    while numbers[1] not in x:
        numbers[1]=input('2. :')
    numbers[1]=int(numbers[1])
    while numbers[2] not in x:
        numbers[2]=input('3. :')
    numbers[2]=int(numbers[2])
    while numbers[3] not in x:
        numbers[3]=input('4. :')
    numbers[3]=int(numbers[3])
    while numbers[4] not in x:
        numbers[4]=input('5. :')
    numbers[4]=int(numbers[4])
    print('\nNow pick a powerball 1-26\n')
    while numbers[5] not in n:
        numbers[5]=input('Powerball. :')
    numbers[5]=int(numbers[5])
    return numbers

def menu():
    print('1.) Can I win the Powerball in my lifetime')
    print('2.) How long would it take to win? **Warning**I have run this for hours without winning')
    choice=0
    while choice!=1 and choice!=2:
        choice=int(input('\n1 or 2 :'))
    return choice

def winningNumbers():
    wNumbers[0]=(random.randint(1,69))
    wNumbers[1]=(random.randint(1,69))
    wNumbers[2]=(random.randint(1,69))
    wNumbers[3]=(random.randint(1,69))
    wNumbers[4]=(random.randint(1,69))
    wNumbers[5]=(random.randint(1,26))  #powerBall
    return wNumbers
#------------Program Begins-------------------

intro()
numbers=chosenNumbers()
print('Dope')
print(f'Your numbers are {numbers[0]} {numbers[1]} {numbers[2]} {numbers[3]} {numbers[4]} Powerball:{numbers[5]}')
choice=menu()
if choice==1:

    input('Hit "enter" to start the simulation')
    while week>0 and lotto==0:
        week-=1
        wNumbers=winningNumbers()
        print(wNumbers)
        price+=2
        win=0
        for i in range(0,5):
            if numbers[i]==wNumbers[i]:
                win+=1
        if win==5:
            lotto=1
        else:
            print('loss')

    if lotto==1:
        if numbers[5]==wNumbers[5]:
            age=round(18+((3224-weeks)/52))
            print(f'You Won the grand prize of $345 Million')
            print(f'It took you {age}years and ${price}Dollars')
        else:
            print('You won but not the powerball...')
            print(f'You get 1 Million dollars and it only cost you {age} years and ${price} dollars')
    else:
        print(f'After playing 3,224 games and spending ${price} you never won the lottery......')
else:
    week=0  #represents games played
    input('Hit "enter" to start the simulation')
    while lotto!=1:
        win=0
        week+=1
        age=(18+(week/52))  #Playing 1 game a week, 52 games a year and you have to be 18 to play
        if age<100:
            print(f'Games Lost:{week}\t\tYear{age:.2f}')
        else:
            print(f'Games Lost: {week}\t\tYear: {age:.2f}\t\tMoney Spent: ${price}\t\tHighest match: {mostWins}, {mostWinTimes} times')
        price+=2
        wNumbers=winningNumbers()
        for i in range(0,5):
            if numbers[i]==wNumbers[i]:
                win+=1

        if win==5:
            lotto=1
        else:
            lotto=0
            if win==mostWins:
                mostWinTimes+=1
            if win>mostWins:
                mostWins=win
                mostWinTimes=1
                    

                


    if lotto==1:
        if numbers[5]==wNumbers[5]:
            age=(18+(week/52))
            print(f'You won the grand prize of $345 Million')
            print(f'It took you {age}years and ${price}Dollars')
        else:
            print('You won 1 Million in the lottery')
            print(f'It took you, \nYears:{age}\nGames Played{week}\nMoney Spent:${price}')