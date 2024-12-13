from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.expert import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[2],0)

# your code starts here:

for i in range(8):
    robotArm.moveRight()
for red_row in range(9):
    robotArm.grab()
    color = robotArm.scan()
    if color == 'red':
        for amount_rows_moved in range(red_row + 1):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(amount_rows_moved + 1):
            robotArm.moveLeft()
    else:
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