import os.path

def write_tournament(tournament, path):
  tournament_output = get_tournament_output(tournament)
  target_directory = os.path.dirname(path)

  if(not os.path.exists(target_directory)):
    os.makedirs(target_directory)

  with open(path, 'w+') as file:
    file.write(tournament_output)

def get_tournament_output(tournament):
  output = 'game,team_1,team_2,skill_difference\n'
  matches = tournament.get_matches()

  for i in range(len(matches)):
      output += '%s,%s,%s\n' % (i, matches[i].get_id(), matches[i].get_skill_difference())

  return output