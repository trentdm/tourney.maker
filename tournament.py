from matchmaker import Matchmaker

class Tournament(object):
  def __init__(self, roster):
    self.roster = roster
    self.matches = Matchmaker().get_tournament_matches(self.roster)
    self.count = len(self.matches)

  def get_count(self):
    return self.count

  def get_matches(self):
    return self.matches