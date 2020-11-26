import random
cards = ['b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'b10', 'bJ', 'bQ', 'bK', 'bA',
         'k2', 'k3', 'k4', 'k5', 'k6', 'k7', 'k8', 'k9', 'k10', 'kJ', 'kQ', 'kK', 'kA',
         'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'pJ', 'pQ', 'pK', 'pA',
         'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10', 'cJ', 'cQ', 'cK', 'cA']

turn = []
flop = []
river = []
turn  = [random.choice(cards) for i in range(3)]
for i in turn:
    cards.remove(i)

flop.extend(turn)
flop.append(random.choice(cards))
cards.remove(flop[-1])

river.extend(flop)
river.append(random.choice(cards))
cards.remove(river[-1])

print('turn ' + str(turn))
print('flop ' + str(flop))
print('river ' + str(river))
print(len(cards))

default_chance_get_suite = 100 / ( len(cards) / (len(cards) / 4) )
print(default_chance_get_suite)

