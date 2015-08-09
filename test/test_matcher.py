import unittest
from matchmaker import Matchmaker
from roster import Roster

class TestMatcher(unittest.TestCase):
  def setUp(self):
    roster_data = {
                    "players" : [
                      {"name" : "Kalpesh Shah", "skill" : 3, "division": "West"},
                      {"name" : "Larry Ward", "skill" : 3, "division": "West"},
                      {"name" : "Trent Miller", "skill" : 3, "division": "West"},
                      {"name" : "Katrina Brinkley", "skill" : 2, "division": "West"},
                      {"name" : "Dan Doepner", "skill" : 2, "division": "West"},
                      {"name" : "Kevin Dahl", "skill" : 2, "division": "West"},
                      {"name" : "Doug Nufer", "skill" : 1, "division": "West"},
                      {"name" : "Bill Schaefermeyer", "skill" : 3, "division": "East"},
                      {"name" : "James Morris", "skill" : 3, "division": "East"},
                      {"name" : "Justin Long", "skill" : 3, "division": "East"},
                      {"name" : "Joe Au", "skill" : 2, "division": "East"},
                      {"name" : "Joseph Hoyal", "skill" : 2, "division": "East"},
                      {"name" : "Eric Prusse", "skill" : 2, "division": "East"},
                      {"name" : "Maria Bates", "skill" : 1, "division": "East"}
                    ]
                  }
    roster = Roster(roster_data)
    self.matchmaker = Matchmaker()
    self.teams = self.matchmaker.get_teams(roster)
    self.matches = self.matchmaker.get_matches(self.teams)
    self.optimized_matches = self.matchmaker.get_tournament_matches(roster)

  def tearDown(self):
    self.tourney = None

  def test_team_count(self):
    self.assertEqual(42, len(self.teams))

  def test_match_count(self):
    self.assertEqual(441, len(self.matches))

  def test_optimized_match_count(self):
    self.assertEqual(21, len(self.optimized_matches))

  def test_tourney_has_match(self):
    self.assertEqual("Bill SchaefermeyerJames MorrisKalpesh ShahLarry Ward", self.matches[0].id)