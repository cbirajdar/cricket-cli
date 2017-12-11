import unittest

from cricket.rankings import IccRankingsParser
from cricket.commands import TEAM_STANDINGS_URL
from cricket.commands import PLAYER_RANKINGS_URL


class IccRankingsParserTestCase(unittest.TestCase):
    def test_team_standing(self):
        standings = IccRankingsParser(TEAM_STANDINGS_URL).team_standings()
        for championship in standings.iterkeys():
            self.assertTrue(championship in self._icc_championships())

    @staticmethod
    def _icc_championships():
        return [
            'ICC Test Championship',
            'ICC ODI Championship',
            'ICC Twenty20 Championship',
            'ICC Women\'s Championship'
        ]

    def test_player_rankings(self):
        rankings = IccRankingsParser(PLAYER_RANKINGS_URL).player_rankings()
        for category in rankings.iterkeys():
            self.assertTrue(category in self._icc_player_ranking_categories())

    @staticmethod
    def _icc_player_ranking_categories():
        return [
            'Test Batsmen',
            'Test Bowlers',
            'Test Allrounders',
            'ODI Batsmen',
            'ODI Bowlers',
            'ODI Allrounders',
            'Twenty20 Batsmen',
            'Twenty 20 Bowlers',
            'Twenty20 Allrounders',
            'Women\' s ODI Batting',
            'Women\'s ODI Bowling',
            'Women\'s ODI Allrounders',
            'Women\'s T20 Batting',
            'Women\'s T20 Bowling',
            'Women\'s T20 Allrounders'
        ]
