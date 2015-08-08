import json
from roster import Roster

def get_roster(roster_file_path):
    roster_json = open(roster_file_path)
    roster_dict = json.load(roster_json)
    return Roster(roster_dict)