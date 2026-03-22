# Step 3 PlayerList with a private instance variable = None
from player_node import PlayerNode


class PlyerList:
    def __init__(self):
        self.__head = None
# Create a method that allows me to insert a new node at the head (it's empty or not) return a boolean
    def is_empty(self) -> bool:
        return self.__head is None

    def insert_head(self, player):
        # Create a vehicle for our player
        new_node = PlayerNode(player)
        # it is empty then
        if self.__head.is_empty():
            self.__head = new_node
        # I got someone in the list
        else:
            # the new vehicle is pointing to the one who was before
            new_node.next = self.__head
            # the old one has someone else before him
            self.__head.prev = new_node
            # the list head is now the new node
            self.__head = new_node