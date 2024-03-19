BOARD_SIZE = 8

def under_attack(col, queens):
    left = right = col
    for r, c in reversed(queens):
        left, right = left-1, right+1
        if c in (left, col, right):
            return True
    return False

def solve(n):
    if n == 0: return [[]]
    smaller_solutions = solve(n-1)
    solutions = []
    for i in range(BOARD_SIZE):
        for solution in smaller_solutions:
            if not under_attack(i+1, solution):
                solutions.append(solution + [(n,i+1)])
    return solutions

for answer in solve(BOARD_SIZE):
    if len(answer) == BOARD_SIZE:
        print(answer)
        break

# Print chessboard with queens
for i in range(8):
    for j in range(8):
        if (i+1, j+1) in answer:
            print('Q', end=' ')
        else:
            print('-', end=' ')
    print('\n')
