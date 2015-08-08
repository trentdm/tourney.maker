import unittest
from player import Player

class TestPlayer(unittest.TestCase):
  def setUp(self):
    player_data = {'name' : 'Kalpesh Shah', 'skill' : 3, 'division' : 'West'}
    self.player = Player(player_data)

  def tearDown(self):
    self.roster = None

  def test_player_name(self):
    self.assertEqual('Kalpesh Shah', self.player.name)

  def test_player_skill(self):
    self.assertEqual(3, self.player.skill)

  def test_player_division(self):
    self.assertEqual("West", self.player.division)