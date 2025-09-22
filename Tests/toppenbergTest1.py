name = input("what is your name? ")
mushroom = int(input("How many mushrooms did you find? "))

if mushroom == 0:
    points = 0
elif mushroom == 1:
    points = 5
elif mushroom == 2:
    points = 10
elif mushroom == 3:
    points = 20
elif mushroom > 3:
    points = 50

print(name, end='')
print(", you have collected", mushroom, "magic mushrooms. This earns you", points, "Points!")