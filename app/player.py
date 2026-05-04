class Player:
    def __init__(self, uid, name, score=0):
        self.__uid = uid # unique ID
        self.__name = name # The name of the player
        self.__score = score # The score of the player

    @property
    def uid(self):
        return self.__uid
    @property
    def name(self):
        return self.__name
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError("Score must be an integer.")
        if value < 0:
            raise ValueError("Score must be a non-negative integer.")
        self.__score = value


    def __str__(self):
        return f"ID: {self.__uid}, Name: {self.__name}"

    def __repr__(self):
        return f"Player(name='{self.name}', uid='{self.__uid}', score={self.__score})"

