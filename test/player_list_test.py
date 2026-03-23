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

    def test_delete_head(self):
        plist = PlayerList()
        p1 = Player("1", "First")
        p2 = Player("2", "Second")
        plist.insert_tail(p1)
        plist.insert_head(p2)

        removed_player = plist.delete_head()

        self.assertEqual(removed_player.uid, "2")
        self.assertEqual(plist._PlayerList__head.player.uid, "1")

    def test_delete_tail(self):
        plist = PlayerList()
        plist.insert_tail(Player("1", "First"))
        plist.insert_tail(Player("2", "Last"))

        removed = plist.delete_tail()
        self.assertEqual(removed.uid, "2")
        self.assertEqual(plist._PlayerList__tail.player.uid, "1")
        self.assertIsNone(plist._PlayerList__tail.next_player)


if __name__ == '__main__':
    unittest.main()

