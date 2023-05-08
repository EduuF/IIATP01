def heuristic(state):
    inversions = 0
    for i in range(len(state)-1):
        if state[i] > state[i+1]:
            inversions += 1

    return inversions * 2