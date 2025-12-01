# --- Day 1: Secret Entrance ---

# Part one
with open("input01.txt") as file:
    zeros = 0
    arrow = 50
    for line in file:
        line = line.strip().replace("R", "").replace("L", "-")
        movement = int(line)
        arrow = (arrow + movement) % 100
        if arrow == 0: zeros += 1
    print(f"Part one answer --> Total times dial in 0: {zeros}")

# Part two
with open("input01.txt") as file:
    zeros = 0
    arrow = 50
    for line in file:
        line = line.strip().replace("R", "").replace("L", "-")
        movement = int(line)
        while movement != 0:
            if movement > 0:
                arrow += 1
                movement -= 1
            else:
                arrow -= 1
                movement += 1
            if (arrow % 100) == 0: zeros += 1
            arrow %= 100
    print(f"Part two answer --> Total times dial passed 0: {zeros}")