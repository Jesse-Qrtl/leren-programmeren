from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.medium import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[1],0)

# your code starts here:

for i in range(8):
    robotArm.moveRight()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
for i in range(8):
    for i in range(2):
        robotArm.moveLeft()
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    
# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()