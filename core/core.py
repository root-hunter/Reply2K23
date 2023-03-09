

from core.file_parser import parse_file
from core.position import Position
from core.snake import Snake
from core.wormhall import Wormhall


class Map:
    def __init__(self) -> None:
        parsed_data = parse_file()

        self.matrix_point = parsed_data["matrix"]
        self.snakes = [Snake(length=snake) for snake in parsed_data["snakes"]]
        self.wormhalls = [Wormhall(position=Position(wormhall[0], wormhall[1])) for wormhall in parsed_data["wormhall"]]

        self.R = parsed_data["R"]
        self.C = parsed_data["C"]

    def __str__(self) -> str:
        return str(self.matrix_point)

    def place_snake(self, snake_index, position: Position):
        self.snakes[snake_index].positions.append(Position(position.x, position.y))

    def move_snake(self, snake_index):
        pass

    def find_main_axies_movements(self, snake_index: int, head: Position):
        possible_moves = []

        left_move = head.x - 1

        if left_move < 0:
            left_move = self.C - 1

        move = Position(left_move, head.y)
        if not self.check_overlap(snake_index=snake_index, move=move):
            possible_moves.append(move)

        right_move = head.x + 1

        if right_move > self.C - 1:
            right_move = 0

        move = Position(right_move, head.y)
        if not self.check_overlap(snake_index=snake_index, move=move):
            possible_moves.append(move)

        up_move = head.y - 1

        if up_move < 0:
            up_move = self.R - 1

        move = Position(head.x, up_move)
        if not self.check_overlap(snake_index=snake_index, move=move):
            possible_moves.append(move)

        down_move = head.y + 1

        if down_move > self.R - 1:
            down_move = 0

        move = Position(head.x, down_move)
        if not self.check_overlap(snake_index=snake_index, move=move):
            possible_moves.append(move)

        return possible_moves

    def find_possible_moves(self, snake_index: int):
        snake = self.snakes[snake_index]
        head = snake.positions[len(snake.positions) - 1]

        possible_moves = self.find_main_axies_movements(head=head, snake_index=snake_index)

        for move in possible_moves:
            if self.check_if_wormhall(move):
                wormhall_positions = self.get_all_wormhall_exclude_itself(move)
                for wormhall_position in wormhall_positions:
                    for x in self.find_main_axies_movements(head=wormhall_position, snake_index=snake_index):
                        if not self.check_overlap(snake_index=snake_index, move=x):
                            possible_moves.append(x)

        print([str(x) for x in possible_moves])

        #TODO
       
        

    def get_all_wormhall_exclude_itself(self, wormhall_position: Position):
        tmp = []
        for wormhall in self.wormhalls:
            if wormhall.position.x != wormhall_position.x and wormhall.position.y != wormhall_position.y:
                tmp.append(wormhall.position)

        return tmp

    def check_if_wormhall(self, position: Position):
        for wormhall in self.wormhalls:
            if wormhall.position.x == position.x and wormhall.position.y == position.y:
                return True
            
        return False
    
    def check_overlap(self, snake_index: int, move: Position):
        for i in range(len(self.snakes)):
            if i != snake_index:
                for position in self.snakes[i].positions:
                    if move.x == position.x and move.y == position.y:
                        print("NOT VALID MOVE: Overlap on ({}, {})".format(move.x, move.y))
                        return True
        
        return False

