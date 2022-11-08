import tkinter as tk
import colors as c
from src.find_path import *
import functools


class Game(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title('2048 solver')
        self.main_grid = tk.Frame(
            self, bg=c.GRID_COLOR, bd=3, width=400, height=400)
        self.main_grid.grid(pady=(80, 0))
        self.make_GUI()
        self.master.bind("<Left>", self.left)
        self.master.bind("<Right>", self.right)
        self.master.bind("<Up>", self.up)
        self.master.bind("<Down>", self.down)
        self.mainloop()


    def make_GUI(self):
        self.cells = []
        self.matrix = [[0] * 4 for _ in range(4)]

        for i in range(4):
            row = []
            for j in range(4):
                cell_button = tk.Button(
                    self.main_grid,
                    bg=c.EMPTY_CELL_COLOR,
                    font=("Helvetica", 45, "bold"),
                    height=2, 
                    width=5, 
                    command=functools.partial(self.toggle_tile, i, j))
                cell_button.grid(row=i, column=j, padx=5, pady=5)
                row.append(cell_button)
            self.cells.append(row)
        
        start_button = tk.Button(self, text="start", command=self.solve).place(relx=0.5, y=40, anchor="center")
    
    def toggle_tile(self, row, col):
        button = self.cells[row][col]
        current_number = 0 if button.cget('text') == "" else int(button.cget('text'))

        if current_number == 0:
            next_number = 2
        elif current_number == 2048:
            next_number = 0
        else:
            next_number = current_number * 2

        button.configure(text="" if next_number == 0 else str(next_number))
        button.configure(bg=c.CELL_COLORS[next_number])
        button.configure(fg=c.CELL_NUMBER_COLORS[next_number])

        self.matrix[row][col] = next_number

        
    def solve(self):
       self.matrix = [[0 if self.cells[i][j].cget('text') == "" else int(self.cells[i][j].cget('text')) for j in range(4)] for i in range(4)]
       print('solved: ' + find_path(self.matrix))
    

    def update_GUI(self):
        for i in range(4):
            for j in range(4):
                cell_num = self.matrix[i][j]
                self.cells[i][j].configure(
                    bg=c.CELL_COLORS[cell_num],
                    fg=c.CELL_NUMBER_COLORS[cell_num],
                    text="" if cell_num == 0 else cell_num
                )
        self.update_idletasks()


    def left(self, event):
        self.matrix = move_board_left(self.matrix)
        self.update_GUI()


    def right(self, event):
        self.matrix = move_board_right(self.matrix)
        self.update_GUI()
        

    def up(self, event):
        self.matrix = move_board_up(self.matrix)
        self.update_GUI()
    

    def down(self, event):
        self.matrix = move_board_down(self.matrix)
        self.update_GUI()


def main():
    Game()


if __name__ == "__main__":
    main()