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