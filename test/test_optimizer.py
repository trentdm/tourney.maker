import unittest
import optimizer
import matcher
from roster import Roster

class TestOptimizer(unittest.TestCase):
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
    teams = matcher.get_teams(roster)
    self.matches = matcher.get_matches(teams)

  def tearDown(self):
    self.matches = None

  def test_matches_count(self):
    optimized_matches = optimizer.get_optimized_matches(self.matches)
    self.assertEqual(21, len(optimized_matches))

  def test_match_skill_difference(self):
    optimized_matches = optimizer.get_optimized_matches(self.matches)

    for match in optimized_matches:
      self.assertEqual(0, match.get_skill_difference())
