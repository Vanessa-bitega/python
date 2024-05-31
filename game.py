import random

def start_message():
    print("Start 'rock-paper-scissors'")

def is_hand(number):
    return number in [0, 1, 2]

def get_player():
    while True:
        try:
            player_choice = int(input("Input your hand \n 0:rock, 1:scissors, 2:paper: "))
            if is_hand(player_choice):
                return player_choice
        except ValueError:
            pass

def get_computer():
    computer_choice = random.randint(0, 2)
    return computer_choice

def get_hand_name(hand_number):
    hands = ['rock', 'scissors', 'paper']
    return hands[hand_number]

def view_hand(player, computer):
    print("Your hand is:", get_hand_name(player))
    print("Computer's hand is:", get_hand_name(computer))


def get_result(hand_diff):
    results = {'win': 'you win', 'lose': 'you lose', 'draw': 'draw try again'}
    if hand_diff == 1:
        return results['win']
    elif hand_diff == -1:
        return results['lose']
    else:
        return results['draw']

def view_result(hand_diff):
  result = get_result(hand_diff)
  print(result)
  if result == 'draw try again':
      play() # Recursion 

def play():
    start_message()
    player_choice = get_player()
    computer_choice = get_computer()
    view_hand(player_choice, computer_choice)
    hand_difference = (player_choice - computer_choice) % 3 
    view_result(hand_difference)

# Start the game
play()
