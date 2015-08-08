def get_tournament(roster, team_size):
  return Tournament()

class Tournament(object):
  def __init__(self):
    pass

  def get_count(self):
    return 0

  def get_matches(self):
    return []

class Match(object):
  def __init__(self, team_1, team_2, skill_diff):
    pass

class Team(object):
  def __init__(self, player_1, player_2, skill):
    pass