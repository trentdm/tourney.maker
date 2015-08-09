import roster_file_importer
from tournament import Tournament
import tournament_file_exporter

roster = roster_file_importer.get_roster('resources\\roster.json')
tournament = Tournament(roster)
tournament_file_exporter.write_tournament(tournament, 'bin\\tournament.json')