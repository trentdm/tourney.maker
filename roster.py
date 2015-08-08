from player import Player

class Roster(object):
  def __init__(self, roster_data):
    map_func = lambda player_data : Player(player_data)
    self.players = map(map_func,  roster_data['players'])

  def get_players(self):
    return self.players

  def get_count(self):
    return len(self.players)