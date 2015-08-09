import json
import os.path

def write_tournament(tournament, path):
  target_directory = os.path.dirname(path)

  if(not os.path.exists(target_directory)):
    os.makedirs(target_directory)

  with open(path, 'w+') as file:
    json.dumps(tournament.__dict__)