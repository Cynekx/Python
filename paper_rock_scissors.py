'''paper > rock
rock > scissors
scissors > paper'''

''' ONE WAY TO CODE:
player_one = input("1st player's choice: ")
print("NO CHEATING!!!!!\n\n" * 20) #\n dziala jak enter
player_two = input("2nd player's choice: ")

if player_one == "paper" and player_two == "rock":
    print("Player one wins!")
elif player_one == "rock" and player_two == "scissors":
    print("Player one wins!")
elif player_one == "scissors" and player_two == "paper":
    print("Player one wins!")
elif (player_one == "paper" and player_two == "paper") or (player_one == "rock" and player_two == "rock") or (player_one == "scissors" and player_two == "scissors"):
    print("It's a draw!")
else:
    print("Player two wins!") '''


player_one = input("1st player's choice: ")
print("NO CHEATING!!!!!\n\n" * 20) #\n dziala jak enter
player_two = input("2nd player's choice: ")

if player_one == "paper":
    if player_two == "rock":
        print("Player one wins!")
    if player_two == "scissors":
        print("Player two wins!")
    if player_two == "paper":
        print("It's a draw!")
elif player_one == "scissors":
    if player_two == "paper":
        print("Player 1 wins!")
    if player_two == "rock":
        print("Player 2 wins!")
    if player_two == "scissors":
        print("It's a draw!")
elif player_one == "rock":
    if player_two == "paper":
        print("Player 2 wins!")
    if player_two == "scissors":
        print("Player 1 wins!")
    if player_two == "rock":
        print("It's a draw!")
