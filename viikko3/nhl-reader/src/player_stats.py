from player_reader import PlayerReader

class PlayerStats:
    def __init__(self, reader: PlayerReader):
        self.reader = reader
        
        
    def top_scorers_by_nationality(self, nationality: str):
        return sorted(list(filter(lambda x: (x.nationality == nationality), self.reader.players())), key=lambda x: x.points(),reverse=True)