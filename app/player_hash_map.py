# Step 2: Implement the Hash Map - assessment part 2
from app.player_list import PlayerList
from app.player import Player


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

    def get_index(self, key):
        """
        Calculates the index for a player key.
        """
        return Player.hash(key) % self.SIZE

    def put(self, key, name):
        """
        Adds a player to the correct PlayerList bucket.

        :param key: The player's unique ID.
        :param name: The player's name.
        """
        player_list = self.__hashmap[self.get_index(key)]
        existing_player = player_list.find_by_key(key)

        if existing_player:
            existing_player.name = name
        else:
            player = Player(key, name)
            player_list.insert_tail(player)
            self.__player_count += 1

