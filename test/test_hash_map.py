import unittest

from app.player_hash_map import PlayerHashMap


class PlayerHashMapTest(unittest.TestCase):

    def test_hash_map_starts_with_ten_buckets(self):
        player_hash_map = PlayerHashMap()

        self.assertEqual(len(player_hash_map.hashmap), 10)

    def test_hash_map_starts_empty(self):
        player_hash_map = PlayerHashMap()

        self.assertEqual(player_hash_map.size(), 0)


if __name__ == "__main__":
    unittest.main()