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

        invalid = False

        for length in range(1, mid+1):
            repeated_num = string_num[:length]
            repeated_count = string_num.count(repeated_num)
            if (len(string_num) / length) == repeated_count:
                invalid = True

        if invalid:
            print("Found invalid ID: " + i)
            count += i

print("Sum of invalid IDs: " + count)

