from core.position import Position

class Snake:
    def __init__(self, length) -> None:
        self.positions = []
        self.length = length

    def __eq__(self, __o: object) -> bool:
        return __o.x == self.x and __o.y == self.y
    
    def move(self, position: Position):
        self.positions.append(position)

    def get_head(self) -> Position:
        return self.positions[len(self.positions) - 1]