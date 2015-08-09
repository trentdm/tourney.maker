def get_optimized_matches(matches):
  optimized_matches = []
  current_skill_difference = 0
  player_game_limit = get_player_game_limit(matches)
  player_game_counts = get_player_game_counts(matches)

  for match in matches:
    if(is_current_skill_diff(match, current_skill_difference)
       and is_unique_match(optimized_matches, match)
       and players_not_over_assigned(match, player_game_counts, player_game_limit)):

      optimized_matches.append(match)

      for team in match.teams:
        for player in team.players:
          player_game_counts[player.name] += 1

  return optimized_matches

def get_player_game_limit(matches):
  players = []

  for match in  matches:
    for team in match.teams:
      for player in team.players:
        players.append(player)

  return (len(players) / 2) - 1

def get_player_game_counts(matches):
  player_game_counts = {}

  for match in matches:
    for team in match.teams:
      for player in team.players:
        if(player.name not in player_game_counts):
          player_game_counts[player.name] = 0

  return player_game_counts

def is_current_skill_diff(match, current_skill_difference):
  return match.get_skill_difference() == current_skill_difference

def is_eligible_optimized_match(optimized_matches, match, current_skill_difference, player_game_counts):
  return match.get_skill_difference() == current_skill_difference \
         and is_unique_match(optimized_matches, match) \
         and players_not_over_assigned(match)

def players_not_over_assigned(match, player_game_counts, player_game_limit):
  for team in match.teams:
    for player in team.players:
      if(player_game_counts[player.name] >= player_game_limit):
        return False

  return True

def is_unique_match(matches, new_match):
  for match in matches:
    if(new_match.get_id() == match.get_id()):
      return False

  return True