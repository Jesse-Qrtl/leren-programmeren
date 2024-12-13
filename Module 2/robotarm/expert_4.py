from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.expert import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[4],0)

# your code starts here:

for i in range(9):
    robotArm.moveRight()
robotArm.grab()
for i in range(3):
    robotArm.moveLeft()
robotArm.drop()
for i in range(2):
    robotArm.moveRight()
robotArm.grab()
for i in range(2):
    robotArm.moveLeft()
robotArm.drop()
robotArm.moveRight()
robotArm.grab()
robotArm.moveLeft()
robotArm.drop()
for x in range(9):
    for i in range(6 - x):
        robotArm.moveLeft()
    robotArm.grab()
    color = robotArm.scan()
    for i in range(6 - x):
        robotArm.moveRight()
    if color == 'blue':
        for i in range(3):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(3):
            robotArm.moveLeft()
    elif color == 'green':
        for i in range(2):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(2):
            robotArm.moveLeft()
    else:
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()

# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()