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
            new_node.next_player= self.__head
            # the old one has someone else before him
            self.__head.previous_player= new_node
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

    # Step 7 d. add two methods - delete an item from head and one from the tail

    def delete_head(self):
        # It's removing the fist node from the list
        if self.is_empty():
            return None
        removed_node = self.__head
        if self.__head == self.__tail:
            self.__head = None
            self.__tail = None
        else:
            self.__head = self.__head.next_player
            self.__head.previous_player = None
        return removed_node.player

    def delete_tail(self):
        if self.is_empty():
            return None

        removed_node = self.__tail

        if self.__head == self.__tail:
            self.__head = None
            self.__tail = None
        else:
            self.__tail = self.__tail.previous_player
            self.__tail.next_player = None

        return removed_node.player

    def delete_by_key(self, key):
        current_node = self.__head

        while current_node:
            if current_node.key == key:
                if current_node == self.__head:
                    return self.delete_head()

                if current_node == self.__tail:
                    return self.delete_tail()

                # if it's in the middle, bridge the gap
                current_node.previous_player.next_player = current_node.next_player
                current_node.next_player.previous_player = current_node.previous_player

                return current_node.player

            current_node = current_node.next_player

        return None

    # Step 8 add display to PlayerList one argument called forward - value True

    def display(self, forward=True):
        if forward:
            current_node = self.__head
            while current_node:
                print(current_node)
                current_node = current_node.next_player
        else:
            current_node = self.__tail
            while current_node:
                print(current_node)
                current_node = current_node.previous_player






