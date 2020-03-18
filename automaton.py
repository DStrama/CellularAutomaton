import tkinter as tk
from tkinter import ttk

class Automaton:

    def __init__(self, rules, width, height):
        self.grid_values = [None] * height
        self.cells = [0] * width
        self.cells[int(len(self.cells) / 2)] = 1
        if rules == 30:
            self.ruleset = [0, 0, 0, 1, 1, 1, 1, 0]
        elif rules == 60:
            self.ruleset = [0, 0, 1, 1, 1, 1, 0, 0]
        elif rules == 90:
            self.ruleset = [0, 1, 0, 1, 1, 0, 1, 0]
        elif rules == 120:
            self.ruleset = [0, 1, 1, 1, 1, 0, 0, 0]
        elif rules == 225:
            self.ruleset = [1, 1, 1, 0, 0, 0, 0, 1]

    def transition_rules( self, left_neighbor, cell, right_neighbor) :
        if left_neighbor == 1 and cell == 1 and right_neighbor == 1:
            return self.ruleset[0]
        elif left_neighbor == 1 and cell == 1 and right_neighbor == 0:
            return self.ruleset[1]
        elif left_neighbor == 1 and cell == 0 and right_neighbor == 1:
            return self.ruleset[2]
        elif left_neighbor == 1 and cell == 0 and right_neighbor == 0:
            return self.ruleset[3]
        elif left_neighbor == 0 and cell == 1 and right_neighbor == 1:
            return self.ruleset[4]
        elif left_neighbor == 0 and cell == 1 and right_neighbor == 0:
            return self.ruleset[5]
        elif left_neighbor == 0 and cell == 0 and right_neighbor == 1:
            return self.ruleset[6]
        elif left_neighbor == 0 and cell == 0 and right_neighbor == 0:
            return self.ruleset[7]
        else:
            return 0

    def next_iteration(self) :
        next_iteration = [0] * len(self.cells)
        for i in range(1, len(self.cells)-1):
            left_neighbor = self.cells[i - 1]
            cell = self.cells[i]
            right_neighbor = self.cells[i + 1]
            next_iteration[i] = self.transition_rules(left_neighbor, cell, right_neighbor)
        self.cells = next_iteration


class Gui(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.canvas = tk.Canvas(self, width=1500, height=1500)
        self.canvas.pack()

        self.label = tk.Label(self, text="Height:")
        self.label.place(relx=0.02, rely=0.02)

        self.entry_height = tk.Entry(self, width=10)
        self.entry_height.place(relx=0.02, rely=0.05)

        self.label = tk.Label(self, text="Width:")
        self.label.place(relx=0.15, rely=0.02)

        self.entry_width = tk.Entry(self, width=10)
        self.entry_width.place(relx=0.15, rely=0.05)

        self.label = tk.Label(self, text="Condition:")
        self.label.place(relx=0.3, rely=0.020)

        self.combobox_condition = ttk.Combobox(self, values=["constant", "inconstant"], state="readonly")
        self.combobox_condition.place(relx=0.3, rely=0.05)

        self.label = tk.Label(self, text="Select Rules:")
        self.label.place(relx=0.6, rely=0.020)

        self.combobox_rules = ttk.Combobox(self, values=["30", "60", "90", "120", "225"], state="readonly")
        self.combobox_rules.place(relx=0.6, rely=0.05)

        self.button = tk.Button(self, text="Start / Stop", font=3, command=self.on_button_click)
        self.button.place(relx=0.85, rely=0.05, relwidth=0.1, relheight=0.05)


    def on_button_click(self):
        self.entry_height.get()
        self.entry_width.get()
        self.combobox_condition.get()
        self.combobox_rules.get()

        ob = Automaton(int(self.combobox_rules.get()), int(self.entry_width.get()), int(self.entry_height.get()))
        for i in range(int(self.entry_height.get())):
            ob.grid_values[i] = ob.cells
            ob.next_iteration()

        self.printing(ob.grid_values)


    def printing(self, all):
        x1 = 110
        x2 = 115
        y1 = 110
        y2 = 115

        for height, cells in enumerate(all):
            for width, cell in enumerate(cells):
                if cell == 1:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="black")
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="white")
                x1 = x1 + 5
                x2 = x2 + 5

            y1 = y1 + 5
            y2 = y2 + 5
            x1 = 110
            x2 = 115


gui = Gui()
gui.mainloop()
