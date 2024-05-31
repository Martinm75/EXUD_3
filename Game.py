
import random


class Game:
    __slots__ = ['__player1', '__player2', '__rounds']

    def __init__(self, player1, player2, rounds):
        self.__player1 = player1
        self.__player2 = player2
        self.__rounds = rounds
    def playRound(self):
        num1 = random.randint
        while 25 < num1 < -25:
            num1 = random.randint

        self.__player1.boost(num1)
        num2= random.randint
        while 25 < num2 < -25:
            num2 = random.randint

        self.__player2.boost(num2)

        print("[("+num1+","+self.__player1.boost(num1)+"),("+num2,+","+self.__player2.boost(num2)+")]" )