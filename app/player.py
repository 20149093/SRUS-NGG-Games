class Player:
    def __init__(self, uid, name):
        self.__uid = uid # unique ID
        self.__name = name # The name of the player
    @property
    def uid(self):
        return self.__uid
    @property
    def name(self):
        return self.__name

    def __str__(self):
        return f"ID: {self.__uid}, Name: {self.__name}"