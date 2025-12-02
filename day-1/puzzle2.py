dial = 50
count = 0

with open("input.txt", "r") as f:
    for line in f:
        num = int(line[1:].strip())
        if num > 100:
            count += num // 100
            num = num % 100

        if "L" in line:
            if (dial - num) < 0 and dial != 0:
                print("line: " + line.strip())
                print("dial: " + str(dial))
                count += 1
            dial = (dial - num) % 100
        else:
            if (dial + num) > 100 and dial != 0:
                print("line: " + line.strip())
                print("dial: " + str(dial))
                count += 1
            dial = (dial + num) % 100

        if dial == 0:
            count += 1

print(count)