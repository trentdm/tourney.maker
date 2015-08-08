import unittest
import reader

class TestRead(unittest.TestCase):
  def setUp(self):
    self.roster = reader.get_roster('resources/test_data.json')

  def tearDown(self):
    self.roster = None
  
  def test_roster_has_players(self):
    self.assertEqual(14, len(self.roster.get_players()))