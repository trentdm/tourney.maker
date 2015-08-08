import unittest
import reader

class TestRead(unittest.TestCase):
  def setUp(self):
    self.roster = reader.get_roster('resources/test_data.json')

  def tearDown(self):
    self.roster = None
  
  def test_player_count(self):
    self.assertEqual(14, len(self.roster.get_players()))

  def test_player_name(self):
    self.assertEqual('Kalpesh Shah', self.roster.get_players()[0].name)

  def test_player_skill(self):
    self.assertEqual(3, self.roster.get_players()[0].skill)

  def test_player_division(self):
    self.assertEqual("West", self.roster.get_players()[0].division)

  def test_roster_size(self):
    self.assertEqual(14, self.roster.get_size())