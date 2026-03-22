import unittest
from app.player import Player
from app.player_list import PlayerList

class PlayerListTest(unittest.TestCase):
    def test_insert_head_empty_list(self):
        # what I want to do here is to test inserting a player into an empty list
        plist = PlayerList()
        p1 = Player("1", "NGG")
        plist.insert_head(p1)
        self.assertIsNotNone(plist._PlayerList__tail)

    def test_insert_not_empty_list(self):
        plist = PlayerList()
        plist.insert_head(Player("1", "First"))
        plist.insert_head(Player("2", "Second"))
        # Now the head should be the second inserted player
        self.assertEqual(plist._PlayerList__head.player.name, "Second")

    def test_insert_tail_empty_list(self):
        plist = PlayerList()
        plist.insert_tail(Player("99", "Last Player"))
        self.assertEqual(plist._PlayerList__tail.player.name, "Last Player")


if __name__ == '__main__':
    unittest.main()
