class Broad:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.matrix = [[None * col] * row]
        for i in range(self.row):
            for j in range(self.col):
                cell = Cell('yellow', self.row, self.col)
    def move(self):
        self.clean()
        self.add()
        pass
    def clean(self):

        pass
    def add(self):
        if nothing there:
            add color
            add num
        else:
            if num == num:
                double num
                change color
                if num == 2046:
                    alert WIN
            else:
                alert
                do nothing
class Cell:
    def __init__(self, color, row, col):
        self.number = number
        self.color = color
        self.row = row
        self.col = col
class Number:
    def __init__(self, num):
        self.num = num
class Color:
    def __init__(self, color):
        self.color = color
