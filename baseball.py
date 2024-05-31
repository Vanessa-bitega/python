import math
import random
teams = []
class Team:
 
    def __init__(self, name,attack,defense):
        self.name = name
        self.attack=attack
        self.defense=defense
        self.total_score = 0
    def info(self):
        print(self.name)
        print('Offensive Power :',self.attack)
        print('Defensive Power :',self.defense)
    def get_hit_rate(self):
        return random.randint(10,self.attack)
    def get_out_rate(self):
        return random.randint(10,self.defense)

 
def create_teams():
    global teams
    team1=Team('Attackers :',80,20)
    team2=Team('Defenders :',30,70)
    team3=Team('Averages :',50,50)
    teams=[team1,team2,team3]

def show_teams():
     index=1
     for i in teams:
          print(str(index))
          i.info()
          index=index+1
playing_teams = {
    'myself': None,
    'enemy': None
}

def choice_team(player):
    show_teams()

    while True:
            try:
                choice = int(input(f'Select {player} team (1-3): '))
                if 1 <= choice <= 3:
                    playing_teams[player] = teams[choice - 1]
                    print(f"{player.capitalize()}'s team is '{playing_teams[player].name}'")
                break  # Exit the loop if valid choice is made
            except ValueError:
                pass

def get_play_inning(inning):
    if inning == 'top':
        offense = playing_teams['myself']
        defense = playing_teams['enemy']
    else:
        offense = playing_teams['enemy']
        defense = playing_teams['myself']

    hit_rate = offense.get_hit_rate()
    out_rate = defense.get_out_rate()

    score = (hit_rate - out_rate) // 10
    return max(score, 0)

def play():
    create_teams()
    choice_team('myself')
    choice_team('enemy')

    score_board = {
        'myself': [0] * 9,
        'enemy': [0] * 9
    }

    for i in range(9):
        top_score = get_play_inning('top')
        bottom_score = get_play_inning('bottom')

        score_board['myself'][i] = top_score
        score_board['enemy'][i] = bottom_score

        playing_teams['myself'].total_score += top_score
        playing_teams['enemy'].total_score += bottom_score

        # print(f"Debug: top of {i+1} {top_score}")
        # print(f"Debug: bottom of {i+1} {bottom_score}")

    print("\nScoreboard:")
    print("Inning |", " | ".join(str(i + 1) for i in range(9)), "| Total")
    print("Myself |", " | ".join(str(score) for score in score_board['myself']), f"| {playing_teams['myself'].total_score}")
    print("Enemy  |", " | ".join(str(score) for score in score_board['enemy']), f"| {playing_teams['enemy'].total_score}")

play()