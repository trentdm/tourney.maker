import unittest
from roster import Roster

class TestRoster(unittest.TestCase):
  def setUp(self):
    roster_data = {"players" : [
                    {"name" : "Kalpesh Shah", "skill" : 3, "division": "West"},
                    {"name" : "Larry Ward", "skill" : 3, "division": "West"},
                    {"name" : "Justin Long", "skill" : 3, "division": "East"},
                    {"name" : "Joe Au", "skill" : 2, "division": "East"},
                    {"name" : "Kevin Dahl", "skill" : 2, "division": "West"},
                    {"name" : "Maria Bates", "skill" : 1, "division": "East"}
                  ]}
    self.roster = Roster(roster_data)

  def tearDown(self):
    self.roster = None

  def test_roster_has_player_data(self):
    self.assertEqual('Kalpesh Shah', self.roster.get_players()[0].name)

  def test_roster_size(self):
    self.assertEqual(6, self.roster.get_count())

  def test_get_division_peers_count(self):
    peers = self.roster.get_division_peers(self.roster.get_players()[0])
    self.assertEqual(2, len(peers))

  def test_get_division_peers_division(self):
    player_1 = self.roster.get_players()[0]
    peers = self.roster.get_division_peers(player_1)
    for peer in peers:
      self.assertEqual(player_1.division, peer.division)