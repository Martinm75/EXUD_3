# main.py
from player import Player,  Jugador
from game import Game

p1 = Player(1, 'a')
p2 = Player(2, 'b')

print({p1})
print({p2})

g1 = Game(p1, p2, 3)

g1.play()

winner = g1.winner()
if winner:
    print("ganador:"+winner)
else:
    print("empate.")
