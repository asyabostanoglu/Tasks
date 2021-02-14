#########################################################
#Title  : Simulate the Game "Rock, Paper, Scissors"
#Author : Asya Bostanoğlu
#Date   : 11.02.2021
#########################################################


#announce the game
print("--------------------Welcome to Rock Paper Scissors Game--------------------")


#get players nicknames
Player1_Nickname = input("Player1 please enter your nickname:")
Player2_Nickname = input("Player2 please enter your nickname:")


#take the inputs
Player1_Choice = input("Enter your choice '1' for rock, '2' for paper, '3' for scissors\n{}:".format(Player1_Nickname))
Player2_Choice = input("Enter your choise '1' for rock, '2' for paper, '3' for scissors\n{}:".format(Player2_Nickname))


#decide and announce the winner
if (Player1_Choice) == (Player2_Choice):
    print ("It's tie!")
elif Player1_Choice == '1' and Player2_Choice == '2':
    print ("Paper covers rock! {} is winner!".format(Player2_Nickname))
elif Player1_Choice == '1' and Player2_Choice == '3':
    print ("Rock smashes scissors! {} is winner!".format(Player1_Nickname))
elif Player1_Choice == '2' and Player2_Choice == '1':
    print ("Paper covers rock! {} is winner!".format(Player1_Nickname))
elif Player1_Choice == '2' and Player2_Choice == '3':
    print ("Scissors cuts paper! {} is winner!".format(Player2_Nickname))
elif Player1_Choice == '3' and Player2_Choice == '1':
    print ("Rock smashes scissors! {} is winner!".format(Player2_Nickname))
elif Player1_Choice == '3' and Player2_Choice == '2':
    print ("Scissors cuts paper! {} is winner!".format(Player1_Nickname))



#########################################################