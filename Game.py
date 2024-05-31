from player import Player
import random



class Game:
    def __init__(self, player1, player2, rounds):
        self.__player1= player1
        self.__player2= player2
        self.__rounds= rounds

    def playRound(self):
        charge1 = random.randint(-25, 25)
        charge2 = random.randint(-25, 25)

        result1 = self.__player1.boost(charge1)
        result2 = self.__player2.boost(charge2)

        return [result1, result2]

    def winner(self):
        if self.__player1.getEnergy() > self.__player2.getEnergy():
            max= self.__player1
        elif self.__player2.getEnergy() > self.__player1.getEnergy():
            max= self.__player2
        return max

    def play(self):
        for round_number in range(1, self.__rounds + 1):
            round_result = self.playRound()
            print(f"Round {round_number}: {round_result}")

