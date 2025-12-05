fresh = 0
ranges = []
reading_ranges = True

# populate ranges (GET IT OUT OF THE TEXT FILE)
with open("input.txt", "r") as f:
    for line in f:
        if line == "\n":
            reading_ranges = False
            continue
        if reading_ranges:
            ranges.append(line.strip())
        else:
            num = int(line.strip())
            for rng in ranges:
                split_rng = rng.split("-")
                rng_start = int(split_rng[0])
                rng_end = int(split_rng[1])
                if num >= rng_start and num <= rng_end:
                    fresh += 1
                    break

print("# fresh: " + str(fresh))
