from ast import For
from traceback import format_exc
import unittest
from statistics import Statistics
from player import Player


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

    def test_search_with_right_name(self):
        self.assertEqual(self.statistics.search("Semenko").name, "Semenko")
        self.assertEqual(self.statistics.search("Semenko").team, "EDM")
        self.assertEqual(self.statistics.search("Semenko").goals, 4)
        self.assertEqual(self.statistics.search("Semenko").assists, 12)

    def test_search_with_wrong_name(self):
        self.assertEqual(self.statistics.search("jaska"), None)


    def test_top_three_scorers_result_size(self):
        top_scorers = self.statistics.top_scorers(3)
        self.assertEqual(len(top_scorers), 3)

    def test_top_three_scorers_right_names(self):
        top_scorers = self.statistics.top_scorers(3)
        self.assertEqual(top_scorers[0].name, "Gretzky")
        self.assertEqual(top_scorers[1].name, "Lemieux")
        self.assertEqual(top_scorers[2].name, "Yzerman")


    def test_team_size(self):
        team = self.statistics.team("EDM")
        self.assertEqual(len(team), 3)

    def test_team(self):
        team = self.statistics.team("EDM")
        for player in team:
            self.assertEqual(player.team, "EDM")