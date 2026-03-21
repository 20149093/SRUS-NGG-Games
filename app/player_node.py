# Step 4 create a class PlayerNode passing player then 3 private instances two of them = None
# Set getters and setters as necessary then create a property call key which returns uid for the player object

class PlayerNode:
    def __init__(self, player):
        self.__player = player
        self.__previous_player = None
        self.__next_player = None

    @property
    def player(self):
        return self.__player

    @property
    def previous_player(self):
        return self.__previous_player

    @previous_player.setter
    def previous_player(self, node):
        self.__previous_player = node

    @property
    def next_player(self):
        return self.__next_player

    @next_player.setter
    def next_player(self, node):
        self.__next_player = node

    @property
    def key(self):
        return self.__player.uid

    def __str__(self):
        return f"Node(Player: {self.__player.name})"




