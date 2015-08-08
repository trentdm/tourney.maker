class Player(object):
  def __init__(self, player_data):
    self.name = player_data['name']
    self.skill = player_data['skill']
    self.division = player_data['division']