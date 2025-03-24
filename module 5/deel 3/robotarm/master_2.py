from RobotArm import RobotArm
from collections import Counter

# Import the challenges (in this case challenges/example.py)
from challenges.master import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[2],0)

# your code starts here:
kleuren = []

for i in range(3):
    robotArm.moveRight()

for i in range(6):
    robotArm.moveRight()
    robotArm.grab()

    kleur = robotArm.scan()
    kleuren.append(kleur)

    robotArm.drop()

for i in range(5):
    robotArm.moveLeft()

aantal_kleuren = Counter(kleuren)

for blocks in range(6):
    robotArm.grab()
    kleur = robotArm.scan()

    if aantal_kleuren[kleur] == 3:
        for i in range(4 + blocks):
            robotArm.moveLeft()
        robotArm.drop()
        for i in range(5 + blocks):
            robotArm.moveRight()

    elif aantal_kleuren[kleur] == 2:
        for i in range(3 + blocks):
            robotArm.moveLeft()
        robotArm.drop()
        for i in range(4 + blocks):
            robotArm.moveRight()
            
    else:  
        for i in range(2 + blocks):
            robotArm.moveLeft()
        robotArm.drop()
        for i in range(3 + blocks):
            robotArm.moveRight()

# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

