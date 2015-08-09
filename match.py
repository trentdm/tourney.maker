class Match(object):
  def __init__(self, team_1, team_2):
    self.teams = [team_1, team_2]
    self.set_id()
    self.set_skill_difference()

  def set_id(self):
    sorted_teams = sorted(self.teams, key=lambda team: team.id)
    self.id = ''.join([team.id for team in sorted_teams])

  def set_skill_difference(self):
    self.skill_difference = self.teams[0].get_skill() - self.teams[1].get_skill()

  def get_id(self):
    return self.id

  def get_skill_difference(self):
    return self.skill_difference