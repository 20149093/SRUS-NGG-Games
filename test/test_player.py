import unittest
from app.player import Player


class TestPlayer(unittest.TestCase):
    def test_player_initialisation(self):
        player = Player("101", "Nelson")
        self.assertEqual(player.uid, "101")
        self.assertEqual(player.name, "Nelson")

if __name__ == '__main__':
    unittest.main()
