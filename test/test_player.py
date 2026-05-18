import unittest
from app.player import Player


class TestPlayer(unittest.TestCase):
    def test_player_initialisation(self):
        player = Player("101", "Nelson")
        self.assertEqual(player.uid, "101")
        self.assertEqual(player.name, "Nelson")

    def test_players_can_be_compared_by_score(self):
        alice = Player("01", "Alice", score=10)
        bob = Player("02", "Bob", score=5)

        self.assertTrue(bob < alice)

    def test_sort_players(self):
        players = [
            Player("01", "Alice", score=10),
            Player("02", "Bob", score=5),
            Player("03", "Charlie", score=15),
        ]

        sorted_players = sorted(players)
        manually_sorted_players = [
            Player("02", "Bob", score=5),
            Player("01", "Alice", score=10),
            Player("03", "Charlie", score=15),
        ]

        self.assertListEqual(sorted_players, manually_sorted_players)

    def test_sort_quickly_descending(self):
        players = [
            Player("01", "Alice", score=10),
            Player("02", "Bob", score=5),
            Player("03", "Charlie", score=15),
        ]

        sorted_players = Player.sort_quickly(players)
        manually_sorted_players = [
            Player("03", "Charlie", score=15),
            Player("01", "Alice", score=10),
            Player("02", "Bob", score=5),
        ]

        self.assertListEqual(sorted_players, manually_sorted_players)


if __name__ == "__main__":
    unittest.main()