
# Algorithm 1: Minimax
# import math

# count = 0  # counts how many leaf nodes are evaluated


# def minimax(depth, index, max_turn, scores, target):
#     global count  # needed so the function can change the outside variable

#     # Base case: we reached a leaf, so return its score
#     if depth == target:
#         count += 1
#         return scores[index]

#     # MAX's turn: evaluate both children and take the larger value
#     if max_turn:
#         return max(
#             minimax(depth + 1, index * 2,     False, scores, target),
#             minimax(depth + 1, index * 2 + 1, False, scores, target),
#         )

#     # MIN's turn: evaluate both children and take the smaller value
#     else:
#         return min(
#             minimax(depth + 1, index * 2,     True, scores, target),
#             minimax(depth + 1, index * 2 + 1, True, scores, target),
#         )


# # ---------- Driver code ----------
# scores = [3, 5, 2, 9, 3, 5, 2, 9]          # Test 1: original
# # scores = [9, 2, 5, 3, 9, 2, 5, 3]        # Test 2: reorder 1
# # scores = [2, 9, 3, 5, 2, 9, 3, 5]        # Test 3: reorder 2
# # scores = [5, 5, 5, 5, 5, 5, 5, 5]        # Test 4: edge case (all equal)

# target = int(math.log2(len(scores)))       # tree depth (8 leaves -> depth 3)

# count = 0                                  # reset before every run
# result = minimax(0, 0, True, scores, target)
# print("Minimax value:", result)
# print("Leaves evaluated:", count)


# Algorithm 2: Alpha-Beta Pruning

import math

count = 0  # counts how many leaf nodes are evaluated


def alphabeta(depth, index, max_turn, scores, target, alpha, beta):
    global count

    # alpha = best value MAX is already guaranteed (starts at -infinity)
    # beta  = best value MIN is already guaranteed (starts at +infinity)

    # Base case: we reached a leaf, so return its score
    if depth == target:
        count += 1
        return scores[index]

    # MAX's turn
    if max_turn:
        value = float('-inf')              # start with the worst possible value
        for i in range(2):                 # i = 0 is left child, i = 1 is right child
            value = max(value, alphabeta(depth + 1, index * 2 + i, False,
                                         scores, target, alpha, beta))
            alpha = max(alpha, value)      # update MAX's guaranteed value
            if alpha >= beta:              # pruning condition
                break                      # skip the remaining child
        return value

    # MIN's turn
    else:
        value = float('inf')               # start with the worst possible value
        for i in range(2):
            value = min(value, alphabeta(depth + 1, index * 2 + i, True,
                                         scores, target, alpha, beta))
            beta = min(beta, value)        # update MIN's guaranteed value
            if alpha >= beta:              # pruning condition
                break
        return value


# ---------- Driver code ----------
scores = [3, 5, 2, 9, 3, 5, 2, 9]          # Test 1: original
# scores = [9, 2, 5, 3, 9, 2, 5, 3]        # Test 2: reorder 1
# scores = [2, 9, 3, 5, 2, 9, 3, 5]        # Test 3: reorder 2
# scores = [5, 5, 5, 5, 5, 5, 5, 5]        # Test 4: edge case (all equal)

target = int(math.log2(len(scores)))

count = 0                                  # reset before every run
result = alphabeta(0, 0, True, scores, target, float('-inf'), float('inf'))
print("Alpha-beta value:", result)
print("Leaves evaluated:", count)