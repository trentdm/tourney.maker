from player import Player

class Roster(object):
  def __init__(self, roster_data):
    self.players = map(lambda player_data : Player(player_data),  roster_data['players'])
    self.length = len(self.players)

  def get_players(self):
    return self.players