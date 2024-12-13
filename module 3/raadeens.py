speelrondes = 0
geraden_rondes = 0
score = 0

while speelrondes < 20:
    geraden_rondes += 1
    if geraden_rondes == 10:
        speelrondes += 1
        geraden_rondes = 0