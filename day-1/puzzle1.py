dial = 50
count = 0

with open("input.txt", "r") as f:
    for line in f:
        num = int(line[1:].strip())
        if "L" in line:
            dial = (dial - num) % 100
        else:
            dial = (dial + num) % 100

        if dial == 0:
            count += 1

print(count)