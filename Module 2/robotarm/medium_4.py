from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.medium import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[4],0)

# your code starts here:

for amount_blocks in range(4):
    robotArm.grab()
    for i in range(5 - amount_blocks):
        robotArm.moveRight()
    robotArm.drop()
    for i in range(5 - amount_blocks):
        robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
robotArm.moveRight()
for amount_blocks2 in range(4):
    robotArm.grab()
    for i in range(5 - 4 + amount_blocks2):
        robotArm.moveLeft()
    robotArm.drop()
    for i in range(5 - 3 + amount_blocks2):
        robotArm.moveRight()
        
# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()