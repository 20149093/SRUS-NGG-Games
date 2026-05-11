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

    def test_get_returns_player(self):
        player_hash_map = PlayerHashMap()

        player_hash_map.put("1", "Baltimore")

        found_player = player_hash_map.get("1")

        self.assertEqual(found_player.name, "Baltimore")


        # This checks missing players

    def test_get_returns_none_when_player_not_found(self):
        player_hash_map = PlayerHashMap()

        found_player = player_hash_map.get("999")

        self.assertIsNone(found_player)

    def test_remove_deletes_player(self):
        player_hash_map = PlayerHashMap()
        player_hash_map.put("1", "Baltimore")

        removed_player = player_hash_map.remove("1")

        self.assertEqual(removed_player.name, "Baltimore")
        self.assertIsNone(player_hash_map.get("1"))
        self.assertEqual(player_hash_map.size(), 0)

# Create collision test - I need two keys and same bucket/index

    def test_collision_handling(self):
        player_hash_map = PlayerHashMap()

        player_hash_map.put("AB", "Baltimore")
        player_hash_map.put("BA", "John")

        first_player = player_hash_map.get("AB")
        second_player = player_hash_map.get("BA")

        self.assertEqual(first_player.name, "Baltimore")
        self.assertEqual(second_player.name, "John")
        self.assertEqual(player_hash_map.size(), 2)

    def test_display_does_not_crash(self):
        player_hash_map = PlayerHashMap()
        player_hash_map.put("AB", "Baltimore")
        player_hash_map.put("BA", "John")

        player_hash_map.display()



if __name__ == "__main__":
    unittest.main()