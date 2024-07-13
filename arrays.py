import numpy as np

name = 'Tom'
name2 = 'Jane'
bet_coin=30
bet_cell=3
# print(name1 + ' and ' + name2 + ' are friends.')
# print('{} and {} are friends. '.format(name1,name2))

# print(name + ' bet ' + str(bet_coin) + ' coin(s) to ' + str(bet_cell)
# + '.' )

# print('{} bet {} coin(s) to {} .'.format(name,bet_coin,bet_cell))
# friends = ['Tom','Jane','Brain']
friends = np.array(['Tom','Jane','Brian','Carol','Jack'])
for i , friend in enumerate(friends):
    # print(i,friend)
    print(f"{i}: {friend}")
# i=0
# for friend in friends:
#     print(f"{i}:{friend}")
#     i+=1

