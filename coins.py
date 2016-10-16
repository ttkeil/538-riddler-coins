#!/usr/bin/python

coins = { n: 'Heads' for n in range(1,101) }

def flip(x):
  return 'Tails' if x == 'Heads' else 'Heads'

for i in coins:
  for j in coins:
     if j % i == 0:
       coins[j] = flip(coins[j])

for x,y in coins.items():
  print(x,y)
