from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.expert import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[5],0)

# your code starts here:

blue = 0
yellow = 0
red = 0
first_color = None

for _ in range(9):
    robotArm.moveRight()
    robotArm.grab()
    color = robotArm.scan()
    if first_color == None:
        first_color = color
    if color == 'blue':
        blue += 1
    elif color == 'yellow':
        yellow += 1
    elif color == 'red':
        red += 1
    robotArm.drop()

most_common_color = None
if blue > yellow and blue > red:
    most_common_color = 'blue'
elif yellow > blue and yellow > red:
    most_common_color = 'yellow'
elif red > blue and red > yellow:
        most_common_color = 'red'
else:
    most_common_color = first_color 

for amount_moved in range(9): 
    robotArm.grab()
    color = robotArm.scan()
    if color == most_common_color:
        for i in range(9 - amount_moved):
            robotArm.moveLeft()  
        robotArm.drop()
        for i in range(8 - amount_moved):
            robotArm.moveRight() 
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