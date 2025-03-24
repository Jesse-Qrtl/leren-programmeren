from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.master import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[4],0)

# your code starts here:
kleuren = []

for amount_blocks in range(3):
    robotArm.grab()

    for i in range(3 - amount_blocks):
        robotArm.moveRight()
    robotArm.drop()
    for i in range(3 - amount_blocks):
        robotArm.moveLeft()

for i in range(4):
    robotArm.grab()

    kleur = robotArm.scan()
    kleuren.append(kleur)   

    robotArm.drop()
    robotArm.moveRight()
    
for i in range(3):
    robotArm.moveLeft()

for blocks in range(3):
    robotArm.grab()
    for i in range(1 + blocks):
        robotArm.moveLeft()
    robotArm.drop()
    for i in range(2 + blocks):
        robotArm.moveRight()

for i in range(2):
    robotArm.moveRight()

for order in range(4):
    for blocks in range(4):
        robotArm.grab()
        color = robotArm.scan()
        if color == kleuren[order]:
            for i in range(5 + blocks):
                robotArm.moveLeft()
            robotArm.drop()
            for i in range(5):
                robotArm.moveRight()
            break

        else:
            robotArm.drop()
            robotArm.moveRight()
            


# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

