import unittest
from roster import Roster

class TestRoster(unittest.TestCase):
  def setUp(self):
    roster_data = {"players" : [
                    {"name" : "Kalpesh Shah", "skill" : 3, "division": "West"},
                    {"name" : "Larry Ward", "skill" : 3, "division": "West"}
                  ]}
    self.roster = Roster(roster_data)

  def tearDown(self):
    self.roster = None

  def test_roster_has_player_data(self):
    self.assertEqual('Kalpesh Shah', self.roster.get_players()[0].name)

  def test_roster_size(self):
    self.assertEqual(2, self.roster.get_count())