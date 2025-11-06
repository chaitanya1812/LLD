
from enum import Enum
import time

class GameStatus(Enum):
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETE = "COMPLETE"
    IMPOSSIBLE = "IMPOSSIBLE"

class Game:

    default_char = "_"
    inds_to_nums = {} # no updates to this
    nums_to_inds = {} # no updates to this
    symbols = ['X', 'Y']


    def __init__(self, size=3):
        print("\nStarting New Game 3X3 Tic Tac Toe!")
        self.size = size
        self.selections = {} # -1: empty/free;  0: p1 selections; 1: p2 selections
        self.state = None
        self._set_default_state()
        self.curr_player = 0
        self.status = GameStatus.IN_PROGRESS

        
    
    def _set_default_state(self):
        s = self.size
        self.state = [[self.default_char]*s for _ in range(s)]
        self.selections[-1] = set()
        self.selections[0] = set()
        self.selections[1] = set()
        count = 1
        for i in range(s):
            for j in range(s):
                k = (i,j)
                self.inds_to_nums[k] = count
                self.nums_to_inds[count] = k
                self.selections[-1].add(count)
                count += 1

    def display_game_state(self):
        print()
        for i in range(self.size):
            print(self.state[i])
    
    def display_options_to_select(self):
        print("\nchoose the number for the selection: Player : ", self.get_current_player_symbol())
        s = self.size
        for i in range(s):
            for j in range(s):
                if self.state[i][j] == self.default_char:
                    print(self.inds_to_nums[(i,j)], end = " ") 
                else:
                    print(self.state[i][j], end = " ") 

            print()

    def is_selection_valid(self, num):
        return num in self.selections[-1] # num should be in empty selections


    def enter_valid_number(self):
        print(f"Enter Valid number. Select one of : ", list(self.selections[-1]))

    def switch_player(self):
        self.curr_player = 1 - self.curr_player
    
    def get_current_player_symbol(self):
        return self.symbols[self.curr_player]

    def update_state(self, selected_num):
        s = selected_num
        self.selections[-1].remove(s) # remove from empty/free spots
        self.selections[self.curr_player].add(s) # add to corresponding player selection
        i, j = self.nums_to_inds[s]
        self.state[i][j] = self.get_current_player_symbol()

    def upsert_game_status(self):
        # completed
        if self.is_complete():
            self.status = GameStatus.COMPLETE
            return
        
        # no cells left to select: impossible to complete
        if len(self.selections[-1]) == 0:
            self.status = GameStatus.IMPOSSIBLE
            return
        



    def is_complete(self):
        sz = self.size
        s = self.state # current board/state
        # rows:
        for i in range(sz):
            if (s[i][1] != self.default_char and 
                s[i][0] == s[i][1] and 
                s[i][1] == s[i][2]): return True
        
        # columns:
        for j in range(sz):
            if (s[1][j] != self.default_char and
                s[0][j] == s[1][j] and 
                s[1][j] == s[2][j]): return True
        
        # +ve diagonal:
        if (s[1][1] != self.default_char and
            s[1][1] == s[0][2] and 
            s[1][1] == s[2][0]): return True

        # -ve diagonal:
        if (s[1][1] != self.default_char and
            s[1][1] == s[0][0] and 
            s[1][1] == s[2][2]): return True

        return False

    def diaplay_winner(self):
        print(f"Player {self.get_current_player_symbol()} Wins!")
    
    def diaplay_impossible(self):
        print(f"Game Over! Both Players Win!")




    
def startGame():
    game =  Game()

    def start_new_game():
        nonlocal game
        game = Game()
    
    while True:
        # game.display_game_state()
        game.display_options_to_select()
        num = 0
        while True:
            num = int(input("select a number from above choices : "))
            if game.is_selection_valid(num): break
            game.enter_valid_number()
        
        game.update_state(num)
        game.upsert_game_status()

        match game.status:
            case GameStatus.COMPLETE:
                game.diaplay_winner()
                game.display_game_state()
                time.sleep(3)
                start_new_game()
            case GameStatus.IMPOSSIBLE:
                game.diaplay_impossible()
                game.display_game_state()
                time.sleep(3)
                start_new_game()
            case _:
                game.switch_player() # swith player


if __name__ == "__main__": startGame()
