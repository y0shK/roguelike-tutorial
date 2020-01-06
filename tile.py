class Tile:
    """
    A tile on a map
    Might be passable, might be see-able
    """
    def __init__(self, blocked, block_sight=None):
        self.blocked = blocked

        # if a tile is blocked, it blocks sight
        if block_sight is None:
            block_sight = blocked

        self.block_sight = block_sight
        
