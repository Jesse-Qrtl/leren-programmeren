from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.medium import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[5],0)

# your code starts here:

for amount_blocks in range(5): 
    robotArm.grab()
    if amount_blocks > 0:
        amount_blocks += amount_blocks
    for i in range(9 - amount_blocks):
        robotArm.moveRight()
    robotArm.drop()
    for i in range(9 - amount_blocks - 1):
        robotArm.moveLeft()

# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()