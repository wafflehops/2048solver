import tkinter as tk
import random
import colors as c
from src.find_path import *
from time import sleep
class Game(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title('2048 solver')
        self.main_grid = tk.Frame(
            self, bg=c.GRID_COLOR, bd=3, width=400, height=400)
        self.main_grid.grid(pady=(80, 0))
        self.make_GUI()
        self.mainloop()


    def make_GUI(self):
        self.cells = []
        self.matrix = [[0] * 4 for _ in range(4)]
        for i in range(4):
            row = []
            for j in range(4):
                cell_frame = tk.Frame(
                    self.main_grid,
                    bg=c.EMPTY_CELL_COLOR,
                    width=100,
                    height=100,
                )
                cell_frame.pack_propagate(False)
                cell_frame.grid(row=i, column=j, padx=5, pady=5)
                cell_number = tk.Label(cell_frame, text="").place(relx=.5, rely=.5, anchor="center")
                cell_data = {"frame": cell_frame, "number": cell_number}
                cell_frame.bind("<Button-1>", self.click_frame)
                row.append(cell_data)
            self.cells.append(row)
        
        start_button = tk.Button(self, text="start", command=self.solve).place(relx=0.5, y=40, anchor="center")
        
    def solve(self):
        shortest_path = find_path(self.matrix)
        print(shortest_path)
        self.play(shortest_path)
        
    def play(self, path):
        for move in path:
            if move == '1':
                self.up()
            if move == '2':
                self.right()
            if move == '3':
                self.down()
            if move == '4':
                self.left()


    def update_matrix(self):
        for i in range(4):
            for j in range(4):
                label = self.cells[i][j]["frame"].winfo_children()[0]
                self.matrix[i][j] = 0 if label.cget('text') == "" else int(label.cget('text'))

    def click_frame(self, event):
        label = event.widget.winfo_children()[0]
        frame = event.widget
        label.configure(
            text=self.next_number(label.cget('text'))
        )
        number = 0 if label.cget('text') == "" else int(label.cget('text'))
        if number == 0:
                    frame.configure(bg=c.EMPTY_CELL_COLOR)
                    label.configure(
                        bg=c.EMPTY_CELL_COLOR, text="")
        else:
            frame.configure(
                bg=c.CELL_COLORS[number])
            label.configure(
                bg=c.CELL_COLORS[number],
                fg=c.CELL_NUMBER_COLORS[number],
                font=c.CELL_NUMBER_FONTS[number],
                text=str(number))

        self.update_matrix()
        
    def next_number(self, current_number):
        if current_number == "":
            return "2"
        elif current_number != "2048":
            return str(int(current_number) * 2)
        else:
            return ""
        
        
    def update_GUI(self):
        for i in range(4):
            for j in range(4):
                cell_value = self.matrix[i][j]
                if cell_value == 0:
                    self.cells[i][j]["frame"].configure(bg=c.EMPTY_CELL_COLOR)
                    self.cells[i][j]["frame"].winfo_children()[0].configure(
                        bg=c.EMPTY_CELL_COLOR, text="")
                else:
                    self.cells[i][j]["frame"].configure(
                        bg=c.CELL_COLORS[cell_value])
                    self.cells[i][j]["frame"].winfo_children()[0].configure(
                        bg=c.CELL_COLORS[cell_value],
                        fg=c.CELL_NUMBER_COLORS[cell_value],
                        font=c.CELL_NUMBER_FONTS[cell_value],
                        text=str(cell_value))
        self.update_idletasks()


    def left(self):
        self.matrix = move_board_left(self.matrix)
        self.update_GUI()
   


    def right(self):
        self.matrix = move_board_right(self.matrix)
        self.update_GUI()
        


    def up(self):
        self.matrix = move_board_up(self.matrix)
        self.update_GUI()
       


    def down(self):
        self.matrix = move_board_down(self.matrix)
        self.update_GUI()
    
    def next_color(self, current_color):
        if current_color == c.EMPTY_CELL_COLOR:
            return c.CELL_COLORS[2]
        if current_color == c.CELL_COLORS[2]:
            return c.CELL_COLORS[4]
        if current_color == c.CELL_COLORS[4]:
            return c.CELL_COLORS[8]
        if current_color == c.CELL_COLORS[8]:
            return c.CELL_COLORS[16]
        if current_color == c.CELL_COLORS[16]:
            return c.CELL_COLORS[32]
        if current_color == c.CELL_COLORS[32]:
            return c.CELL_COLORS[64]
        if current_color == c.CELL_COLORS[64]:
            return c.CELL_COLORS[128]
        if current_color == c.CELL_COLORS[128]:
            return c.CELL_COLORS[256]
        if current_color == c.CELL_COLORS[256]:
            return c.CELL_COLORS[512]
        if current_color == c.CELL_COLORS[512]:
            return c.CELL_COLORS[1024]
        if current_color == c.CELL_COLORS[1024]:
            return c.CELL_COLORS[2048]
        if current_color == c.CELL_COLORS[2048]:
            return c.EMPTY_CELL_COLOR
  


   

def main():
    Game()


if __name__ == "__main__":
    main()