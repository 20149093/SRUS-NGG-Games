# Step 3 PlayerList with a private instance variable = None
from player_node import PlayerNode


class PlayerList:
    def __init__(self):
        self.__head = None
        self.__tail = None # Step 6 this one is pointing to the end of the list

# Create a method that allows me to insert a new node at the head (it's empty or not) return a boolean
    def is_empty(self) -> bool:
        return self.__head is None

    def insert_head(self, player):
        # Create a vehicle for our player
        new_node = PlayerNode(player)
        # it is empty then
        if self.is_empty():
            self.__head = new_node
            self.__tail = new_node # Step 6 If it is unique  then it is head and tail at the same time
        # I got someone in the list
        else:
            # the new vehicle is pointing to the one who was before
            new_node.next = self.__head
            # the old one has someone else before him
            self.__head.prev = new_node
            # the list head is now the new node
            self.__head = new_node

    def insert_tail(self, player):
        """
        Inserts a player at the end of the list.
        :param player: The player object to add at the end of the list.
        :return:
        """
        new_node = PlayerNode(player)

        if self.is_empty():
            self.__head = new_node
            self.__tail = new_node
        else:
            new_node.previous_player = self.__tail
            self.__tail.next_player = new_node
            self.__tail = new_node