# --- Day 2: Gift Shop ---
from math import ceil
with open("input02.txt") as file:
    ranges = [x.split("-") for x in file.read().strip().split(",")]

# Part one
total_one = 0
subtotal_two = 0
for item in ranges:
    item = [int(x) for x in item]
    for i in range(item[0], item[1] + 1):
        str_item = str(i)
        half_index = len(str_item) // 2
        if str_item[:half_index] == str_item[half_index:]:
            total_one += i
        else:
            length = len(str_item)
            stop = length // 2 + 1
            for x in range(1, stop):
                reps = str_item.count(str_item[:x])
                if reps == ceil(length / x):
                    subtotal_two += i

total_two = subtotal_two + total_one
print(f"Part one answer --> Total sum of invalid ids: {total_one}") 
print(f"Part two answer --> Total sum of invalid ids: {total_two}") 