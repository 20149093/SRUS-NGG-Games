from app.player_list import PlayerList


class PlayerHashMap:
    """
    Stores players across multiple PlayerList buckets.
    """

    SIZE = 10

    def __init__(self):
        self.__hashmap = [PlayerList() for _ in range(self.SIZE)]
        self.__player_count = 0

    @property
    def hashmap(self):
        """
        Returns the list of PlayerList buckets.
        """
        return self.__hashmap

    def size(self):
        """
        Returns the number of players stored in the hash map.
        """
        return self.__player_count

