import random
import os
class Cell:
    def __init__(self, value):
        self.value = value
        self.flipped = False

    def is_flipped(self):
        return self.flipped  

    def flip(self):
        self.flipped = not self.flipped
        return self.flipped
    
    def __str__(self):
        return self.value if self.flipped else '*'

class Memory_Game(Cell):
    def __init__(self):
        self.size = 2
        self.grid = []
        self.__score = 0
        self.__turns = 0

    def inc_score(self):
        self.__score += 1

    def inc_turns(self):
        self.__turns += 1

    def create_grid(self):
        max_num = self.size ** 2 // 2
        ls = [j for i in range(2) for j in range(1, max_num + 1)]
        random.shuffle(ls)
        grid = [Cell(ls[i * self.size + j]) for i in range(self.size) for j in range(self.size)]
        grid = [grid[i * self.size: (i + 1) * self.size] for i in range(self.size)]
        self.grid = grid

    def display_grid(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.grid[i][j].__str__(), end = ' ')
            print()

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        try:
            if type(size) != int:
                raise TypeError('Size must be integer')
            elif size < 2:
                raise ValueError('Size must be greater than one.')
            elif size % 2 != 0:
                raise ValueError('Size must be even number.')
        except ValueError as e:
            print(f'Error: {e}')
        self.__size = size

    def flip_card(self, row, col):
        if self.grid[row][col].is_flipped():
            raise IndexError('This card already is open')
        elif row < 0 or row >= self.size or col < 0 or col >= self.size:
            raise ValueError(f'Row and column index must be in [0, {self.size + 1}] range. ')
        else: 
            self.grid[row][col].flip()
            return self.grid[row][col].value

    def play(self):
        in_size = input('Enter the grid size (e.g., 4 for 4x4): ')
        
        try:
            self.size = int(in_size)
        except:
            TypeError('Size must be integer.')

        self.create_grid()
        print('Current grid:')
        self.display_grid()
        print(f'\nScore: {self.__score}, Turns: {self.__turns}')

        max_circle = self.size**2 * 1.5
        print(f'{max_circle:}')
        while self.__score != self.size**2 // 2 and self.__turns <= max_circle:
            try:
                row1, col1 = map(int, input('Flip the first card (row col): ').split())
                row2, col2 = map(int, input('Flip the second card (row col): ').split())
            except:
                ValueError('Invalid input.')
            c1_val = self.flip_card(row1, col1)
            c2_val = self.flip_card(row2, col2)
            self.inc_turns()
            self.display_grid()
            if c1_val != c2_val:
                self.grid[row1][col1].flip()
                self.grid[row2][col2].flip()
            # os.system('clear')
            else:
                self.inc_score()
                print("It's the match.")
            print(f'\nScore: {self.__score}, Turns: {self.__turns}')

        print("You win") if self.__score == self.size else print("You failed. Try again.")

            

m = Memory_Game()
m.play()