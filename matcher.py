import itertools

def get_tournament(roster):
  teams = get_teams(roster)
  matches = get_matches(teams)
  optimized_matches = get_optimal_matches(matches)
  return Tournament(optimized_matches)

def get_teams(roster):
  teams = []

  for player in roster.get_players():
    for peer in roster.get_division_peers(player):
      team = Team(player, peer)

      if(is_unique_team(teams, team)):
        teams.append(team)

  return teams

def is_unique_team(teams, new_team):
  for team in teams:
    if(new_team.get_id() == team.get_id()):
      return False

  return True

def get_matches(teams):
  matches = []
  division_groups = itertools.groupby(teams, lambda team: team.division)

  for key, division_1_group in division_groups:
    division_2_group = [team for team in teams if team.division != key]

    for div_1_team in division_1_group:
      for div_2_team in division_2_group:
        match = Match(div_1_team, div_2_team)

        if(is_unique_match(matches, match)):
          matches.append(match)

  return matches

def is_unique_match(matches, new_match):
  for match in matches:
    if(new_match.get_id() == match.get_id()):
      return False

  return True

def get_optimal_matches(matches):
  return matches


class Tournament(object):
  def __init__(self, matches):
    self.matches = matches
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