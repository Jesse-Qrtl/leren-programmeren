from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.master import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[5],0)

# your code starts here:
kleuren = []
teller = 0

while True:
    robotArm.grab()
    kleur = robotArm.scan()
    if kleur not in kleuren:
        teller += 1
        kleuren.append(kleur)
        robotArm.drop()
        robotArm.moveRight()
    else:
        index = kleuren.index(kleur)
        for i in range(teller - index):
            robotArm.moveLeft()
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

