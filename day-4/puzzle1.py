rolls = 0
rows = []

# populate 2D array (GET IT OUT OF THE TEXT FILE)
with open("input.txt", "r") as f:
    for row, line in enumerate(f):
        rows.append([])
        for col, char in enumerate(line.strip()):
            rows[row].append(char)

height = len(rows)
width = len(rows[0])

# Don't throw an error when doing edge cases
def safe_get(rows, i, j):
    if 0 <= i < len(rows) and 0 <= j < len(rows[0]):
        return rows[i][j]
    return None

for i, row in enumerate(rows):
    for j, col in enumerate(row):
        if col != "@":
            continue
        
        # safely check 8 surrounding spots
        adjacent = [
            safe_get(rows, i, j+1),
            safe_get(rows, i, j-1),
            safe_get(rows, i+1, j),
            safe_get(rows, i-1, j),
            safe_get(rows, i+1, j+1),
            safe_get(rows, i-1, j-1),
            safe_get(rows, i-1, j+1),
            safe_get(rows, i+1, j-1),
        ]

        if adjacent.count("@") < 4:
            rolls += 1


print("# of accessible rolls: " + str(rolls))
