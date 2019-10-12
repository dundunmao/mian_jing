class Canvas:

    def __init__(self, row, col):
        self.matrix = [[] * col] * row
        self.rectangle_hash = {}
        for i in range(row):
            for j in range(col):
                cell = Cell(i, j )
                self.matrix[i][j] = cell

    def draw(self, left_top, right_bottom):
        length = self.rectangle_hash
        index = length
        rectangle = Rectangle(index, left_top, right_bottom)
        self.rectangle_hash[index] = rectangle
        for i in range(len(rectangle.filled)):
            for j in range(len(rectangle.filled[0])):
                if rectangle.filled[i][j] is True:
                    cell = self.matrix[i][j]
                    if not cell.color:
                        cell.color = True
                    cell.info.append(rectangle.index)
    def drag(self):
        self.delete()
        self.draw()
    def move_to_top(self):
        pass
    def delete(self):
        pass
    def print(self):
        pass



class Cell:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.color = False
        self.info = []

class Rectangle:
    def __init__(self, index, left_top, right_bottom):
        self.index = index
        self.left_top = left_top
        self.right_bottom = right_bottom
        self.filled = []
        for i in range(left_top[0], right_bottom[0] + 1):
            self.filled[i] = []
            for j in range(left_top[1], right_bottom[1] + 1):
                self.filled[i].append(True)

