import math

def get_optimized_matches(matches):
  optimized_matches = []
  match_limit = get_match_limit(matches)
  player_game_limit = get_player_game_limit(matches)
  player_game_counts = get_player_game_counts(matches)

  for current_skill_difference in range(match_limit):
    for match in matches:
      if(is_current_skill_diff(match, current_skill_difference)
         and is_unique_match(optimized_matches, match)
         and players_not_over_assigned(match, player_game_counts, player_game_limit)):

        increment_game_counts(match, player_game_counts)
        optimized_matches.append(match)

        if(len(optimized_matches) == match_limit):
          return optimized_matches

  return optimized_matches

def get_match_limit(matches):
  division_player_count = len(get_players(matches)) / 2
  team_size = 2
  match_limit = math.factorial(division_player_count) / \
                (math.factorial(team_size) * math.factorial(division_player_count - team_size))
  return match_limit


def get_player_game_limit(matches):
  return (len(get_players(matches)) / 2) - 1

def get_players(matches):
  players = []

  for match in  matches:
    for team in match.teams:
      for player in team.players:
        if(player not in players):
          players.append(player)

  return players

def get_player_game_counts(matches):
  player_game_counts = {}

  for match in matches:
    for team in match.teams:
      for player in team.players:
        if(player.name not in player_game_counts):
          player_game_counts[player.name] = 0

  return player_game_counts

def is_current_skill_diff(match, current_skill_difference):
  return math.fabs(match.get_skill_difference()) == current_skill_difference

def is_unique_match(matches, match):
  return match not in matches

def players_not_over_assigned(match, player_game_counts, player_game_limit):
  for team in match.teams:
    for player in team.players:
      if(player_game_counts[player.name] >= player_game_limit):
        return False

  return True

def increment_game_counts(match, player_game_counts):
  for team in match.teams:
    for player in team.players:
      player_game_counts[player.name] += 1