def max_joltage_k_digits(sequence, k):
    n = len(sequence)
    if k > n:
        return None
    if k == n:
        return sequence
    
    to_remove = n - k
    stack = []
    
    for i, digit in enumerate(sequence):
        remaining = n - i
        
        # Keep removing from the stack while we can get better numbers in their place
        while stack and to_remove > 0 and stack[-1] < digit:
            stack.pop()
            to_remove -= 1
        
        stack.append(digit)
    
    return ''.join(stack[:k])

total_joltage = 0

with open("input.txt", "r") as f:
    for line in f:
        input_line = line.strip()
        joltage_str = max_joltage_k_digits(input_line, 12)
        joltage_val = int(joltage_str)
        print(f"{input_line} has max joltage: {joltage_str}")
        total_joltage += joltage_val

print("Your total joltage is: " + str(total_joltage))