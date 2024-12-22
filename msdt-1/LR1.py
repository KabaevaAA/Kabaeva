# -*- coding: utf-8 -*-

class TennisGameDefactored1:

    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.p1points += 1
        else:
            self.p2points += 1

    def score(self):
        if self.p1points == self.p2points:
            if self.p1points < 4:
                return {
                    0: "Love-All",
                    1: "Fifteen-All",
                    2: "Thirty-All",
                    3: "Forty-All",
                }[self.p1points]
            return "Deuce"

        if self.p1points >= 4 or self.p2points >= 4:
            return self.determine_winner()

        return self.get_score()

    def determine_winner(self):
        minus_result = self.p1points - self.p2points
        if minus_result == 1:
            return "Advantage " + self.player1Name
        elif minus_result == -1:
            return "Advantage " + self.player2Name
        elif minus_result >= 2:
            return "Win for " + self.player1Name
        else:
            return "Win for " + self.player2Name

    def get_score(self):
        score_map = ["Love", "Fifteen", "Thirty", "Forty"]
        return score_map[self.p1points] + "-" + score_map[self.p2points]



class TennisGameDefactored2:
    """Класс для игры в теннис с улучшенной логикой счета."""

    def __init__(self, player1Name, player2Name):
        """Инициализация игры с двумя игроками."""
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, playerName):
        """Увеличивает очки игрока."""
        if playerName == self.player1Name:
            self.p1points += 1
        else:
            self.p2points += 1

    def score(self):
        """Возвращает текущий счет игры."""
        if self.p1points == self.p2points and self.p1points < 4:
            return self.get_tied_score()
        elif self.p1points >= 4 or self.p2points >= 4:
            return self.determine_winner()

        return self.get_score()

    def get_tied_score(self):
        """Возвращает счет при равенстве очков."""
        return {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All",
            3: "Forty-All",
        }[self.p1points]

    def determine_winner(self):
        """Определяет победителя игры."""
        minus_result = self.p1points - self.p2points
        if minus_result == 1:
            return "Advantage " + self.player1Name
        elif minus_result == -1:
            return "Advantage " + self.player2Name
        elif minus_result >= 2:
            return "Win for " + self.player1Name
        else:
            return "Win for " + self.player2Name

    def get_score(self):
        """Возвращает строку с текущим счетом."""
        score_map = ["Love", "Fifteen", "Thirty", "Forty"]
        return score_map[self.p1points] + "-" + score_map[self.p2points]


class TennisGameDefactored3:
    def __init__(self, player1Name, player2Name):
        self.p1N = player1Name
        self.p2N = player2Name
        self.p1 = 0
        self.p2 = 0

    def won_point(self, n):
        if n == self.p1N:
            self.p1 += 1
        else:
            self.p2 += 1

    def score(self):
        if (self.p1 < 4 and self.p2 < 4):
            p = ["Love", "Fifteen", "Thirty", "Forty"]
            s = p[self.p1]
            return s + "-All" if (self.p1 == self.p2) else s + "-" + p[self.p2]
        else:
            if (self.p1 == self.p2):
                return "Deuce"
            s = self.p1N if self.p1 > self.p2 else self.p2N
            return "Advantage " + s if ((self.p1 - self.p2) * (self.p1 - self.p2) == 1) else "Win for " + s


# NOTE: You must change this to point at the one of the three examples that you're working on!
TennisGame = TennisGameDefactored1