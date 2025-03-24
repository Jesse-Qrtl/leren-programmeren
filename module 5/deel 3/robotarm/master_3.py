from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.master import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[3],0)

# your code starts here:
kleuren = []
teller = 0

for i in range(3):
    robotArm.moveRight()

for blocks in range(16):
    robotArm.grab()
    kleur = robotArm.scan()

    if kleur not in kleuren:
        kleuren.append(kleur)

    kleur_index = kleuren.index(kleur)

    if kleur_index < 2:
        for i in range(3 + teller - kleur_index):
            robotArm.moveLeft()
        robotArm.drop()
        for i in range(3 + teller - kleur_index):
            robotArm.moveRight()
            
    else:   
        for i in range(1):
            for i in range(8 - (kleur_index + teller)):
                robotArm.moveRight()
            robotArm.drop()
            for i in range(8 - (kleur_index + teller)):
                robotArm.moveLeft()
    
    if (blocks + 1) % 4 == 0:
        robotArm.moveRight()
        teller += 1
        
# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

