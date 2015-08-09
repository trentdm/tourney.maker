import math

class Optimizer(object):
  def __init__(self, matches):
    self.team_size = 2
    self.matches = matches
    self.players = self.get_players()
    self.match_limit = self.get_match_limit(self.players)
    self.player_game_limit = self.get_player_game_limit(self.players)
    self.player_game_counts = self.get_player_game_counts()

  def get_players(self):
    players = []

    for match in  self.matches:
      for team in match.teams:
        for player in team.players:
          if(player not in players):
            players.append(player)

    return players

  def get_match_limit(self, players):
    division_player_count = len(players) / 2
    match_limit = math.factorial(division_player_count) / \
                  (math.factorial(self.team_size) * math.factorial(division_player_count - self.team_size))
    return match_limit


  def get_player_game_limit(self, players):
    return (len(players) / 2) - 1

  def get_player_game_counts(self):
    player_game_counts = {}

    for match in self.matches:
      for team in match.teams:
        for player in team.players:
          if(player.name not in player_game_counts):
            player_game_counts[player.name] = 0

    return player_game_counts

  def get_optimized_matches(self):
    optimized_matches = []

    for i in range(self.match_limit):
      for match in self.matches:
        if(self.is_skill_match(match, i) and self.players_not_over_assigned(match)):
          self.increment_game_counts(match)
          optimized_matches.append(match)

          if(len(optimized_matches) == self.match_limit):
            return optimized_matches

    # print self.player_game_counts
    return optimized_matches

  def is_skill_match(self, match, current_skill_difference):
    return math.fabs(match.get_skill_difference()) == current_skill_difference

  def is_unique_match(self, match):
    return match not in self.matches

  def players_not_over_assigned(self, match):
    for team in match.teams:
      for player in team.players:
        if(self.player_game_counts[player.name] >= self.player_game_limit):
          return False

    return True

  def increment_game_counts(self, match):
    for team in match.teams:
      for player in team.players:
        self.player_game_counts[player.name] += 1