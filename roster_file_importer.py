import json
from roster import Roster

def get_roster(roster_file_path):
    with open(roster_file_path) as file:
      roster_data = json.load(file)
    return Roster(roster_data)