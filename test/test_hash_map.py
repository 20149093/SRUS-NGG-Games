import unittest

from app.player_hash_map import PlayerHashMap


class PlayerHashMapTest(unittest.TestCase):

    def test_hash_map_starts_with_ten_buckets(self):
        player_hash_map = PlayerHashMap()

        self.assertEqual(len(player_hash_map.hashmap), 10)

    def test_hash_map_starts_empty(self):
        player_hash_map = PlayerHashMap()

        self.assertEqual(player_hash_map.size(), 0)

    def test_get_index_returns_valid_index(self):
        player_hash_map = PlayerHashMap()

        index = player_hash_map.get_index("ABC123")

        self.assertTrue(0 <= index < 10)

    def test_put_adds_player(self):
        player_hash_map = PlayerHashMap()

        player_hash_map.put("1", "Baltimore")

        self.assertEqual(player_hash_map.size(), 1)


if __name__ == "__main__":
    unittest.main()