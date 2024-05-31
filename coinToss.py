import random

def start_message():
    print("Start 'coin toss'")
def is_correct_input(number):
    return number in (0,1)

def get_side_name(side):
    if side == 0:
        return 'heads'
    else:
    
       return 'tails'


def get_coin_side():
    coin_side = random.randint(0,1)
    return coin_side

def view_side(bet_side,coin_side):
    print("My bet is:", get_side_name(bet_side))
    print("Coin is:", get_side_name(coin_side))
def get_result( coin_side,bet_side):
    if coin_side == bet_side:
        return 'you win'

    else:
        return 'you loses'
def view_result(result):
    print("Result: " + result)
def play():
    start_message()
   
    while True:  
        user_input = input("Enter your bet side \n 0: heads, 1: tails: ") 
        if user_input.isdigit():  
            bet_side = int(user_input)
            if is_correct_input(bet_side):
                break  
     
    coin_side = get_coin_side()
    view_side(bet_side,coin_side)
    result = get_result(coin_side,bet_side)
    view_result(result)

play()