import random
import matplotlib.pyplot as plt

# 0 → OFF
# 1 → ON
moves_list:list = []
series_dict: dict = {}
NUM_ROUNDS:int = 1000
TRIES:int = 5
SERIES_LENGTH: int = 5

class Buttons:
    def __init__(self, num_buttons):
        """ Sets the initial states of all the buttons """
        self.buttons_list = []
        for i in range(num_buttons):
            self.buttons_list.append(random.choice([0, 1]))
        if self.buttons_list == [0 for x in range(num_buttons)]:
            self.set_buttons_randomly(num_buttons)
    
    def set_buttons_randomly(self, num_buttons):
        """ Helps with setting initial button states """
        self.buttons_list = []
        for i in range(num_buttons):
            self.buttons_list.append(random.choice([0, 1]))

    def shuffle_buttons(self):
        """ Shuffles the buttons between rounds """
        final_list:list = []
        for i in range(len(self.buttons_list)):
            element = random.choice(self.buttons_list)
            final_list.append(element)
            self.buttons_list.remove(element)
        self.buttons_list = final_list

    def turn_buttons(self, quantity = [False, None], position = [False, [0, 0, 0, 0]]) -> list:
        """ Turns the buttons when it's its turn """
        if quantity[0] != True:  # Setting the number of buttons to turn
            quantity = random.randint(1, len(self.buttons_list))
        else:
            quantity = quantity[1]
        if position[0] != True:  # Setting buttons to turn
            position[1] = [0, 0, 0, 0]
            free_positions:list = [0, 1, 2, 3]  # Free positions not trying to turn yet
            for _ in range(quantity):  # Setting the turns for the right amount of buttons
                choice = random.choice(free_positions)
                position[1][choice] = 1
                free_positions.remove(choice)

        for i in range(len(self.buttons_list)):  # Turning the buttons
            if position[1][i] == 1:
                if self.buttons_list[i] == 1:
                    self.buttons_list[i] = 0
                else:
                    self.buttons_list[i] = 1

        moves_list.append(position[1])
        return moves_list
    
    def check(self):
        """ Checks whether there is a winner """
        if self.buttons_list == [0, 0, 0, 0]:
            #print(moves_list)
            #print("--------------------WIN----------------------")
            return True
        
def analyze(moves:list):
    serie = []
    for i in range(SERIES_LENGTH):
        serie.append(moves[len(moves) - SERIES_LENGTH + i])
    if str(serie) not in series_dict.keys():
        series_dict.update({str(serie):1})
    else:
        series_dict[str(serie)] += 1


wins = 0
buttons = Buttons(4)
for i in range(NUM_ROUNDS):
    i = 0
    while i < TRIES:
        buttons.shuffle_buttons()
        if i%20 == 0:
            moves = buttons.turn_buttons(quantity = [True, 3])
        else:
            moves = buttons.turn_buttons(quantity = [True, 2])
        if buttons.check() == True:
            wins+=1
            i = TRIES
            if len(moves) >= SERIES_LENGTH:
                analyze(moves)
            moves_list.clear()
        else:
            i+=1

names = list(series_dict.keys())
values = list(series_dict.values())

#plt.bar(range(len(series_dict)), values, tick_label=names)
#plt.show()

print("Wins = ", wins)
print("Out of = ", NUM_ROUNDS)