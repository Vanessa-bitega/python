import random

class Player:
    def __init__(self, name, coin):
        self.name = name
        self.coin = coin
        self.bets = {}
        self.initialize_bets()

    def initialize_bets(self):
        global table
    
        for cell in table:
            self.bets[cell.name] = 0

    def set_bet_coin(self, bet_coin, bet_cell):
        if self.coin >= bet_coin:
            self.coin -= bet_coin
            self.bets[bet_cell] += bet_coin
        else:
            print(f"Insufficient funds! You have {self.coin} coins. Please enter a lower bet.")

    def add_coins(self, amount):
       
        self.coin += amount

    def reset_table(self):
        """Reset bets to 0"""
        self.initialize_bets()

class Human(Player):
    """Human player"""
    def __init__(self, name, coin):
        super().__init__(name, coin)

    def enable_bet_coin(self, string, max_bet_coin):
        """Validates and processes bet input"""
        try:
            bet_amount = int(string)
        except ValueError:
            return False

        if 1 <= bet_amount <= max_bet_coin:
            if bet_amount > self.coin:
                print(f"Insufficient funds! You have {self.coin} coins. Please enter a lower bet.")
                return False
            else:
                return True
        else:
            return False

    def enable_bet_cell(self, string):
        """Validates the cell input"""
        if string in cells:
            return True
        return False

    def bet(self):
        """Prompts user to place a bet"""
        max_bet_coin = min(99, self.coin)
        while True:
            bet_coin = input(f"How many coins do you bet?: (1-{max_bet_coin}) ")

            if self.enable_bet_coin(bet_coin, max_bet_coin):
                bet_coin = int(bet_coin)
                while True:
                    bet_cell = input("On what do you bet?: (R, B, 1-8) ")
                    if self.enable_bet_cell(bet_cell):
                        self.set_bet_coin(bet_coin, bet_cell)
                        print(f"{self.name} bet {bet_coin} coin(s) to {bet_cell}.")
                        return
                    else:
                        pass

class Computer(Player):
    """PC player"""
    def __init__(self, name, coin):
        super().__init__(name, coin)

    def bet(self):
        """Randomly place a bet"""
        max_bet = min(self.coin, 99)
        bet_coin = random.randint(1, max_bet)

        # Select a random cell name
        bet_cell = random.choice(cells)

        self.set_bet_coin(bet_coin, bet_cell)
        print(f"{self.name} bet {bet_coin} coin(s) to {bet_cell}.")

        return

def create_players():
    """Creates instances of players"""
    global players
    players = []

    players.append(Human('MY', 500))
    for i in range(1, 4):
        players.append(Computer(f'C{i}', 500))

class ColorBase:
    RED = '\033[91m'
    GREEN = '\033[92m'
    END = '\033[0m'

class Cell:
    def __init__(self, name, rate, color):
        self.name = name
        self.rate = rate
        self.color = color

def create_table():
    global table
    table = []

    # Add Cell objects with the specified information
    table.append(Cell("R", 2, "red"))
    table.append(Cell("B", 2, "black"))
    for i in range(1, 9):
        table.append(Cell(str(i), 8, "red" if i % 2 == 1 else "black"))

def green_bar():
    return f"{ColorBase.GREEN}|{ColorBase.END}"

def color(cell):
    line = f"{cell.name}(×{cell.rate})"
    green_bar_text = green_bar()
    colored_line = f"{green_bar_text}{line}{green_bar_text}"
    if cell.color == 'red':
        return f"{ColorBase.RED}{line}{ColorBase.END}{green_bar_text}{green_bar_text}"
    return colored_line

def show_table():
    # Display the header row with player names
    headers = ['|_____|']
    for player in players:
        headers.append(f"{player.name}")
    print('|'.join(headers) + '|')

    # Display the table with bets
    for cell in table:
        colored_name = color(cell)
        row = [colored_name]
        for player in players:
            bet = str(player.bets[cell.name]).zfill(2)
            row.append(bet)
        print('|'.join(row) + '|')

def set_cells():
    global cells
    cells = ['R', 'B'] + [str(i) for i in range(1, 9)]

def bet_players():
    for player in players:
        player.bet()

def win_player(player, hit_cell_number):
    """Calculate payout and add it to winning player's coins"""
    bet_amount = player.bets[hit_cell_number]
    payout_rate = next(cell.rate for cell in table if cell.name == hit_cell_number)
    payout_amount = bet_amount * payout_rate
    player.add_coins(payout_amount)
    print(f"{player.name} won. Gained {payout_amount} coins.")

def check_hit():
    """Generate winning number and check for winning players"""
    winning_cell = random.choice(cells)
    print(f"\nWinning number is {winning_cell}.")

    for player in players:
        if player.bets[winning_cell] > 0:
            win_player(player, winning_cell)

def show_coin():
    """Display players' coins"""
    coins_info = "[Players’ coin] "
    for player in players:
        coins_info += f"{player.name}: {player.coin} / "
    print(coins_info)

def initialize():
    """Execute initial setup"""
    create_table()
    create_players()
    set_cells()

def play_once():
    """Execute a single play of the game"""
    reset_table()
    bet_players()
    show_table()
    check_hit()
    show_coin()

def is_game_end():
    """Check if the game should end (i.e., if any player has run out of coins)"""
    for player in players:
        if player.coin <= 0:
            return True
    return False

def reset_table():
    """Reset bets for all players"""
    for player in players:
        player.reset_table()

def game_end():
    """Display game end message with the player's name who has no coin"""
    for player in players:
        if player.coin <= 0:
            print(f"Game ends as {player.name} has no coin.")
            break

def play():
    initialize()
    while not is_game_end():
        play_once()
    else:
        game_end()

# Global list to store player instances and cells
players = []
cells = []

if __name__ == "__main__":
    play()
