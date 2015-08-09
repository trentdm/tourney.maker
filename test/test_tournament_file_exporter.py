import unittest
import os.path
import tournament_file_exporter
from tournament import Tournament
from roster import Roster

class TestTournamentFileExporter(unittest.TestCase):
  def setUp(self):
    self.output_path = 'bin/tournament.json'
    roster_data = {"players" : [
                    {"name" : "Kalpesh Shah", "skill" : 3, "division": "West"},
                    {"name" : "Larry Ward", "skill" : 3, "division": "West"},
                    {"name" : "Justin Long", "skill" : 3, "division": "East"},
                    {"name" : "Joe Au", "skill" : 2, "division": "East"},
                    {"name" : "Kevin Dahl", "skill" : 2, "division": "West"},
                    {"name" : "Maria Bates", "skill" : 1, "division": "East"}
                  ]}
    self.tournament = Tournament(Roster(roster_data))

  def tearDown(self):
    self.roster = None
  
  def test_tournament_written(self):
    tournament_file_exporter.write_tournament(self.tournament, self.output_path)
    self.assertTrue(os.path.exists)