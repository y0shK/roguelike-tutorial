class Entity:
    """
    a generic Python object to represent any object in the game
    """
    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx, dy):
        # move by an assigned amount
        self.x += dx
        self.y += dy
