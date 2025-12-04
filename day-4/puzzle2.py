total_rolls = 0
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

def remove_rolls():
    current_rolls = 0
    rolls_to_remove = []
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
                current_rolls += 1
                rolls_to_remove.append([i,j])
    
    # remove rolls after counting
    for position in rolls_to_remove:
        i = position[0]
        j = position[1]
        rows[i][j] = 'X'

    return current_rolls

# loop to keep removing until no more can be removed
removed_rolls = -1
while(removed_rolls != 0):
    removed_rolls = remove_rolls()
    total_rolls += removed_rolls


print("# of accessible rolls: " + str(total_rolls))
