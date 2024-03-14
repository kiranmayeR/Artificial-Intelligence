import math

def alpha_beta_pruning(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or node.is_terminal():
        return node.evaluate()

    value = -math.inf if maximizing_player else math.inf

    for child in node.get_children():
        child_value = alpha_beta_pruning(child, depth - 1, alpha, beta, not maximizing_player)

        if maximizing_player:
            value = max(value, child_value)
            alpha = max(alpha, value)
        else:
            value = min(value, child_value)
            beta = min(beta, value)

        if beta <= alpha:
            break

    return value

# Example usage
if __name__ == "__main__":
    class Node:
        def __init__(self, value):
            self.value = value
            self.children = []

        def is_terminal(self):
            return True

        def evaluate(self):
            return self.value

        def get_children(self):
            return [Node(1), Node(2), Node(3)]

    root = Node(0)
    depth = 6

    result = alpha_beta_pruning(root, depth, -math.inf, math.inf, True)
    print("Optimal value:", result)
