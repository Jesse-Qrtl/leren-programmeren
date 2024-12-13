from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.expert import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[1],0)

# your code starts here:

for amount_rows in range(4):
    for i in range(amount_rows + 1):
        robotArm.grab()
        for i in range(5):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(5):
            robotArm.moveLeft()
    if amount_rows < 4:
        robotArm.moveRight()

# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()