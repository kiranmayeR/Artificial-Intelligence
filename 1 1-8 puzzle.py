import heapq

initial_state = (1, 0, 3, 4, 2, 5, 7, 8, 6)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
moves = [1, -1, 3, -3]
open_list, closed_set = [(0, initial_state, [])], set()

while open_list:
    _, current, path = heapq.heappop(open_list)
    if current == goal:
        print("Solution Found:")
        solution_path = path + [current]
        for state in solution_path:
            matrix_format = [state[i:i+3] for i in range(0, 9, 3)]
            for row in matrix_format:
                print(row)
            print()
        break
    closed_set.add(current)
    empty = current.index(0)
    for m in moves:
        if 0 <= empty // 3 + m // 3 < 3 and m + empty in range(9):
            neighbor = list(current)
            neighbor[empty], neighbor[empty + m] = neighbor[empty + m], neighbor[empty]
            neighbor_tuple = tuple(neighbor)
            if neighbor_tuple not in closed_set:
                heapq.heappush(open_list, (len(path) + 1, neighbor_tuple, path + [current]))
