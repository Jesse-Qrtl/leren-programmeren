from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.beginner import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[4],0)

# your code starts here:

robotArm.moveRight()
for i in range(6):
    robotArm.grab()
    color = robotArm.scan()
    if color == 'red':
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
    elif color == 'white':
        robotArm.moveLeft()
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