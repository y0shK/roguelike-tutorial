from tile import Tile
from rect import Rect
from random import randint

class GameMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        # Tile(False) -> all walkable, Tile(True) -> not walkable
        tiles = [[Tile(True) for y in range(self.height)] for x in range(self.width)]

        return tiles

    def make_map(self, max_rooms, room_min_size, room_max_size, map_width, map_height, player):
        rooms = []
        num_rooms = 0

        for r in range(max_rooms):
            # random width and height
            w = randint(room_min_size, room_max_size)
            h = randint(room_min_size, room_max_size)

            # random position w/o leaving bounds
            x = randint(0, map_width - w - 1)
            y = randint(0, map_height - h - 1)

            # use Rect class to make rectangles
            new_room = Rect(x, y, w, h)

            # run through other rooms, do they intersect?
            for other_room in rooms:
                if new_room.intersect(other_room):
                    break
            else:
                # no intersections present, create the room!

                # paint it to the map's tiles
                self.create_room(new_room)

                # define center coordinates of room
                (new_x, new_y) = new_room.center()

                if num_rooms == 0:
                    # this is the first room, where the player starts
                    player.x = new_x
                    player.y = new_y
                else: # rooms already exist
                    # connect it to previous w/ tunnel

                    (prev_x, prev_y) = rooms[num_rooms - 1].center()

                    # random number for 0 or 1
                    if randint(0,1) == 1:
                        # move horizontally, then vertically
                        self.create_h_tunnel(prev_x, new_x, prev_y)
                        self.create_v_tunnel(prev_y, new_y, new_x)
                    else:
                        # first move vertically, then horizontally
                        self.create_v_tunnel(prev_y, new_y, prev_x)
                        self.create_h_tunnel(prev_x, new_x, new_y)

                # append the new room to the list
                rooms.append(new_room)
                num_rooms += 1

    def create_room(self, room):
        # go through rectangular tiles and make them passable
        # using class Rect
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                self.tiles[x][y].blocked = False
                self.tiles[x][y].block_sight = False

    def create_h_tunnel(self, x1, x2, y):
        for x in range(min(x1,x2), max(x1,x2) +1):
            self.tiles[x][y].blocked = False
            self.tiles[x][y].block_sight = False

    def create_v_tunnel(self, y1, y2, x):
        for y in range(min(y1,y2), max(y1,y2)+1):
            self.tiles[x][y].blocked = False
            self.tiles[x][y].block_sight = False

    def is_blocked(self, x, y):
        if self.tiles[x][y].blocked:
            return True

        return False
    
