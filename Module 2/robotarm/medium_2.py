from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.medium import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[2],0)

# your code starts here:

for x in range(5):
    for i in range(6):
        robotArm.moveRight()
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
    if x < 4:
        for i in range(2):
            robotArm.moveRight()
    else:
        robotArm.moveRight()
    
# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()