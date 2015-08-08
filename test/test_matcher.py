import unittest
import matcher
from roster import Roster

class TestMatcher(unittest.TestCase):
  def setUp(self):
    roster = Roster()
    self.matches = matcher.get_division_matches(roster, 2)

  def tearDown(self):
    self.roster = None