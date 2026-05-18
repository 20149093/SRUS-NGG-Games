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

    # Add hash method to player - preparing to implementing get index() - assessment part 2

    @classmethod
    def hash(cls, key):
        """
        Creates a numeric hash from a player UID.
        """
        total = 0

        for character in key:
            total += ord(character)

        return total




    def __str__(self):
        return f"ID: {self.__uid}, Name: {self.__name}"

    def __repr__(self):
        return f"Player(name='{self.name}', uid='{self.__uid}', score={self.__score})"

    def __eq__(self, other):
        if not isinstance(other, Player):
            return NotImplemented
        return self.uid == other.uid and self.name == other.name and self.score == other.score

    def __lt__(self, other):
        if not isinstance(other, Player):
            return NotImplemented
        return self.score < other.score

    def __hash__(self):
        return self.hash(self.uid)

    @classmethod
    def sort_quickly(cls, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        left = []
        right = []
        for x in arr[1:]:
            if x > pivot:
                left.append(x)
            else:
                right.append(x)
        return cls.sort_quickly(left) + [pivot] + cls.sort_quickly(right)