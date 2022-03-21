class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
        if self.m_score1 == self.m_score2:
            return self.draw()
            
        if self.is_on_roundpoint():
            return self.roundpoint_score()
        
        
        return self.compose_score()

    
    
    
    def compose_score(self):
        return self.personal_score(self.m_score1) + "-" + self.personal_score(self.m_score2)
    
    def personal_score(self,score):
        if score == 0:
            return "Love"
        if score == 1:
            return "Fifteen"
        if score == 2:
            return "Thirty"
        if score == 3:
            return "Forty"
        
        return ""
    
    def is_on_roundpoint(self):
        return self.m_score1 >= 4 or self.m_score2 >= 4
    
    
    def roundpoint_score(self):
        minus_result = self.m_score1 - self. m_score2

        if minus_result == 1:
            return "Advantage player1"
        if minus_result == -1:
            return "Advantage player2"
        if minus_result >= 2:
            return "Win for player1"
        
        return "Win for player2"
        
        
    def draw(self):
        if self.m_score1 == 0:
            return "Love-All"
        if self.m_score1 == 1:
            return "Fifteen-All"
        if self.m_score1 == 2:
            return "Thirty-All"
        if self.m_score1 == 3:
            return "Forty-All"
        
        return "Deuce"