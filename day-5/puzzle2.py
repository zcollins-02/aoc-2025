class FreshRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

ids = 0
ranges = []

# populate ranges (GET IT OUT OF THE TEXT FILE)
with open("input.txt", "r") as f:
    for line in f:
        if line == "\n":
            break
        split_line = line.strip().split("-")
        start = int(split_line[0])
        end = int(split_line[1])
        ranges.append(FreshRange(start, end))

# Make ranges unique
ranges.sort(key=lambda r: r.start)

merged = []
for rng in ranges:
    # dont merge
    if not merged or rng.start > merged[-1].end:
        merged.append(FreshRange(rng.start, rng.end))
    # merge
    else:
        merged[-1].end = max(merged[-1].end, rng.end)

ranges = merged

for rng in ranges:
    print("start: " + str(rng.start))
    print("end: " + str(rng.end))
    ids += (rng.end + 1) - rng.start

print("# fresh ids: " + str(ids))
