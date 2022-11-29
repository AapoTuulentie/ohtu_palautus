class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 += 1
        else:
            self.m_score2 += 1

    def get_score(self):
        score_dict = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty", 4: "Deuce"}

        if self.m_score1 == self.m_score2:
            if self.m_score1 == 4:
                score = score_dict[self.m_score1]
            else:
                score = score_dict[self.m_score1] + "-All"

        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            minus_result = self.m_score1 - self. m_score2

            if minus_result == 1:
                score = "Advantage player1"
            elif minus_result == -1:
                score = "Advantage player2"
            elif minus_result >= 2:
                score = "Win for player1"
            else:
                score = "Win for player2"
        else:
            player1 = score_dict[self.m_score1]
            player2 = score_dict[self.m_score2]
            score = player1 + "-" + player2

        return score
