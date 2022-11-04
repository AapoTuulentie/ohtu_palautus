import unittest
from statistics import Statistics
from player import Player
from player_reader import PlayerReader
from sortby import SortBy

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_player_search(self):
        player = self.statistics.search("Semenko").name

        self.assertEqual(player, "Semenko")

    def test_team_search(self):
        team = self.statistics.team("PIT")[0].name

        self.assertEqual(team, "Lemieux")

    def test_player_not_in_list(self):
        player = self.statistics.search("Selanne")

        self.assertEqual(player, None)

    def test_search_top_points(self):
        top = self.statistics.top(1, SortBy.POINTS[0].name)

        self.assertEqual(top, "Gretzky")    