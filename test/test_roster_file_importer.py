import unittest
import roster_file_importer

class TestRosterFileImporter(unittest.TestCase):
  def setUp(self):
    self.roster = roster_file_importer.get_roster('resources/test_data.json')

  def tearDown(self):
    self.roster = None
  
  def test_roster_has_players(self):
    self.assertEqual(14, len(self.roster.get_players()))