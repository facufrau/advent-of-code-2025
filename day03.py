# --- Day 3: Lobby ---

with open("input03.txt") as file:
    total_one = 0
    total_two = 0
    for line in file:
        # Part one
        first, second = "-1", "-1"
        line_lst = list(line.strip()[:])
        reference = "-1"
        for i, c in enumerate(line_lst):
            if i != (len(line_lst) - 1) and c > first:
                first = c
                reference = i
        for i, c in enumerate(line_lst):
            if c > second and i > reference:
                second = c
        num = int(first + second)
        total_one += num

        # Part two
        MAX_BATT = 12
        index = -1
        volt = ""
        for num in range(0, MAX_BATT):
            best = 0
            stop = len(line_lst) + 1 - 12 + num
            for j in range(index + 1, stop):
                if best == 9:
                    break
                elif int(line_lst[j]) > best:
                    best = int(line_lst[j])
                    index = j
            volt += str(best)
        total_two += int(volt)

    
print(f"Part one answer --> {total_one}") 
print(f"Part two answer --> {total_two}") 