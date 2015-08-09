from player import Player

class Roster(object):
  def __init__(self, roster_data):
    map_func = lambda player_data : Player(player_data)
    self.players = map(map_func, roster_data['players'])

  def get_players(self):
    return self.players

  def get_count(self):
    return len(self.players)

  def get_division_peers(self, player):
    flt = lambda p: p.division == player.division and p.name != player.name
    return filter(flt, self.players)