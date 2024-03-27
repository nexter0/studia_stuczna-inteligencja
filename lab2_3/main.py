def terminal_state_table():
    return [[3, 12, 8], [2, 4, 6], [14, 5, 2]]


def min_player(value, alpha, beta, depth=0):
    if depth == 0:
        print(" " * depth, "MIN reached leaf node with value:", value)
    if depth > 0:
        print(" " * depth, "MIN choosing from:", value)
    if isinstance(value, list):
        min_val = float('inf')
        for num in value:
            min_val = min(min_val, max_player(num, alpha, beta, depth + 1))
            beta = min(beta, min_val)
            if beta <= alpha:
                print(" " * depth, "Beta cutoff at:", beta)
                break
        if depth > 0:
            print(" " * depth, "MIN chosen value:", min_val)
        return min_val
    else:
        if depth > 0:
            print(" " * depth, "MIN reached leaf node with value:", value)
        return value


def max_player(value, alpha, beta, depth=0):
    if depth == 0:
        print(" " * depth, "MAX reached root node with value:", value)
    if depth > 0:
        print(" " * depth, "MAX choosing from:", value)
    if isinstance(value, list):
        max_val = float('-inf')
        for num in value:
            max_val = max(max_val, min_player(num, alpha, beta, depth + 1))
            alpha = max(alpha, max_val)
            if beta <= alpha:
                print(" " * depth, "Alpha cutoff at:", alpha)
                break
        if depth > 0:
            print(" " * depth, "MAX chosen value:", max_val)
        return max_val
    else:
        if depth > 0:
            print(" " * depth, "MAX reached leaf node with value:", value)
        return value


def find_solution():
    state = terminal_state_table()
    max_choice = max([min_player(subarray, float('-inf'), float('inf')) for subarray in state])
    return max_choice


solution = find_solution()
print("The solution is:", solution)
