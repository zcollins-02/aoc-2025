count = 0

with open("input.txt", "r") as f:
    data = f.read()

ranges = data.split(",")

for rng in ranges:
    split_range = rng.split("-")
    range_start = int(split_range[0])
    range_end = int(split_range[1])
    
    for i in range(range_start, range_end+1):
        string_num = str(i)
        mid = len(string_num) // 2

        left = string_num[:mid]
        right = string_num[mid:]

        if left == right:
            print("Found invalid ID: " + i)
            count += i

print("Sum of invalid IDs: " + count)

