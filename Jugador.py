

class Jugador:
    __slots__ = ['__MAX_ENERGY', '__MIN_ENERGY']

    def __init__(self):
        self.__MAX_ENERGY = 100
        self.__MIN_ENERGY = 0

    def getMIN_ENERGY(self):
        return self.__MIN_ENERGY

    def getMAX_ENERGY(self):
        return self.__MAX_ENERGY

class Player:
    __slots__ = ['__idPlayer', '__nickName', '__energy']

    def __init__(self, id, nickName):
        self.__idPlayer = id
        self.__nickName = nickName
        self.__energy = (Jugador.getMAX_ENERGY(self)-Jugador.getMIN_ENERGY(self))/2

    def getIdPlayer(self):
        return self.__idPlayer

    def getNickName(self):
        return self.__nickName

    def getEnergy(self):
        return self.__nickName

    def setIdPlayer(self, idPlayer):
        self.__idPlayer = idPlayer

    def setNickName(self, nickName):
        self.__nickName = nickName

    def __setEnergy__(self, energy):
       self.__energy = energy

    def toString(self):
        cad = "[" + self.getIdPlayer() + ", "
        cad += str(self.getNickName()) + ", "
        cad += str(self.getEnergy()) + "]"
        return cad

    def boost(self, change):
        if Jugador.getMIN_ENERGY() <= (self.getEnergy() + change) <= Jugador.getMAX_ENERGY():
            self.__setEnergy__((self.getEnergy()+change))

        elif (self.getEnergy() + change)< Jugador.getMIN_ENERGY():
            self.__setEnergy__(Jugador.getMIN_ENERGY())

        else:
            self.__setEnergy__(Jugador.getMAX_ENERGY())

        return self.getEnergy()
    
