import matcher

class Tournament(object):
  def __init__(self, roster):
    self.roster = roster
    self.matches = matcher.get_tournament_matches(self.roster)
    self.count = len(self.matches)

  def get_count(self):
    return self.count

  def get_matches(self):
    return self.matches

class Match(object):
  def __init__(self, team_1, team_2):
    self.teams = [team_1, team_2]
    self.set_id()
    self.set_skill_difference()

  def set_id(self):
    sorted_teams = sorted(self.teams, key=lambda team: team.id)
    self.id = ''.join([team.id for team in sorted_teams])

  def set_skill_difference(self):
    self.skill_difference = self.teams[0].skill - self.teams[1].skill

  def get_id(self):
    return self.id

  def get_skill_difference(self):
    return self.skill_difference


class Team(object):
  def __init__(self, player_1, player_2):
    self.set_players(player_1, player_2)
    self.set_id()
    self.set_skill()
    self.division = player_1.division

  def set_players(self, player_1, player_2):
    self.players = [player_1, player_2]

  def set_id(self):
    sorted_players = sorted(self.players, key=lambda player: player.name)
    self.id = ''.join([player.name for player in sorted_players])

  def set_skill(self):
    self.skill = sum([player.skill for player in self.players])

  def get_id(self):
    return self.id

  def get_skill(self):
    return self.skill

  def get_division(self):
    return self.division