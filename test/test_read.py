import unittest
import read

class TestRead(unittest.TestCase):
  def setUp(self):
    self.roster = read.get_roster('resources/test_data.json')

  def tearDown(self):
    self.roster = None
  
  def test_player_count(self):
    self.assertEqual(14, len(self.roster.players))

  def test_player_name(self):
    self.assertEqual('Kalpesh Shah', self.roster.players[0].name)

  def test_player_skill(self):
    self.assertEqual(3, self.roster.players[0].skill)