import random

player = {'A', 'B', 'C', 'D', 'E', 'F', 'G'}

game = random.sample(player, 4)
print(game)
priority = player.difference(game)
print(priority)
