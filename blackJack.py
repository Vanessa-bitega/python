import random 
cards= []
suits = ['spades','clubs','hearts','diamonds']
ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

for Suit in suits:
        for rank in ranks:
                cards.append([Suit,rank])
def shuffle_card():
        random.shuffle(cards)

def deal(num):
        cards_dealt=[]
        for n in range(num):
                card =cards.pop()
                cards_dealt.append(card)
        return cards_dealt
shuffle_card()
cards_dealt=deal(2)
card=cards_dealt[0]
rank=card[1]
if rank == 'A':
        value=11
elif rank == 'J' or rank == 'Q' or rank == 'K':
        value=10
else:
        value= rank
rank_dict={'rank':rank,'value':value}
print(rank_dict['rank'],rank_dict['value'])
