from random import randrange
n = randrange(100)
while True:
  v = int(input())
  if n == v:
    print('Ok You win!')
    break
  print('Smaller' if (n < v) else 'Bigger')