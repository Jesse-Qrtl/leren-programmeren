from RobotArm import RobotArm
from collections import Counter

# Import the challenges (in this case challenges/example.py)
from challenges.master import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[1],0)

# your code starts here:
kleuren = []

for i in range(10):
    robotArm.grab()

    kleur = robotArm.scan()
    kleuren.append(kleur)
    
    robotArm.drop()

    if i < 9:
        robotArm.moveRight()

for i in range(9):
    robotArm.moveLeft()

aantal_kleuren = Counter(kleuren)
laagste_kleur = min(aantal_kleuren, key=aantal_kleuren.get)
index_minste = kleuren.index(laagste_kleur)

for i in range(index_minste):
    robotArm.moveRight()
robotArm.grab()

# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

