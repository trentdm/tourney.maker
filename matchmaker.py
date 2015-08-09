import itertools
from optimizer import Optimizer
from team import Team
from match import Match

class Matchmaker(object):
  def get_tournament_matches(self, roster):
    teams = self.get_teams(roster)
    matches = self.get_matches(teams)
    return Optimizer(matches).get_optimized_matches()

  def get_teams(self, roster):
    teams = []

    for player in roster.get_players():
      for peer in roster.get_division_peers(player):
        team = Team(player, peer)

        if(self.is_unique_team(teams, team)):
          teams.append(team)

    return teams

  def is_unique_team(self, teams, new_team):
    for team in teams:
      if(new_team.get_id() == team.get_id()):
        return False

    return True

  def get_matches(self, teams):
    matches = []
    division_groups = itertools.groupby(teams, lambda team: team.division)

    for key, division_1_group in division_groups:
      division_2_group = [team for team in teams if team.division != key]

      for div_1_team in division_1_group:
        for div_2_team in division_2_group:
          match = Match(div_1_team, div_2_team)

          if(self.is_unique_match(matches, match)):
            matches.append(match)

    return matches

  def is_unique_match(self, matches, new_match):
    for match in matches:
      if(new_match.get_id() == match.get_id()):
        return False

    return True