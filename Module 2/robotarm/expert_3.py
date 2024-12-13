from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.expert import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[3],0)

# your code starts here:

teller = 0
robotArm.grab()
while True:
    teller += 1
    for i in range(teller):
        robotArm.moveRight()
    robotArm.drop()
    for i in range(teller):
        robotArm.moveLeft()
    robotArm.grab()
    if robotArm.stackEmpty():
        for i in range(teller + 1):
            robotArm.moveRight()
        robotArm.drop()
        break

# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()