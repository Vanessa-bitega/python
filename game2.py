import random
def start_msg():
    print("Start 'coin toss'")

def is_corrrect_input(number):
    return number in ('0','1')

def get_coin_side():
   
    return str(random.randint(0,1))

def get_side_name(side):
    if side == '0':
       return 'heads'
    else:
        return 'tails'
def view_side(mybet,coin):
    print('my bet is ' + get_side_name(mybet))
    print('coin is ' , get_side_name(coin))

def get_result(mybet,coin):
    if mybet == coin:
        return 'win'
  
    else:
        return 'looseeee'
def view_result(ans):
    print(ans)

def play():
    start_msg()
    mybet=input('Enter your bet \n 0:heads 1:tails: ') 
    coin=get_coin_side()
    view_side(mybet, coin)
    result =get_result(mybet, coin)
    view_result(result)

play()
