from core import core

map = core.Map()
map.place_snake(snake_index=0, position=core.Position(2, 0))
map.place_snake(snake_index=1, position=core.Position(3, 0))
map.place_snake(snake_index=2, position=core.Position(6, 2))

map.find_possible_moves(0)