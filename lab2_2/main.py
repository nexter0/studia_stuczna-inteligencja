class PuzzleNode:
    def __init__(self, state, parent=None, g_score=0):
        self.state = state  # The current state of the puzzle.
        self.parent = parent  # Reference to the parent node.
        self.g_score = g_score  # The cost from the start node to this node.

    def generate_children(self):
        # Method to generate child nodes from the current node.
        # Returns a list of PuzzleNode objects representing the child nodes.
        children = []
        x, y = self.find_empty_tile()
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy  # Calculate new coordinates after moving.
            if 0 <= new_x < 3 and 0 <= new_y < 3:  # Check if the new position is valid.
                # Create a new state by swapping the empty tile with the neighboring tile.
                new_state = [row[:] for row in self.state]
                new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
                # Create a new PuzzleNode with the new state, set its parent and g_score, and append to children.
                children.append(PuzzleNode(new_state, parent=self, g_score=self.g_score + 1))
        return children

    def find_empty_tile(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == ' ':
                    return i, j

    def is_goal(self):
        return self.state == [['1', '2', '3'], ['4', '5', '6'], ['7', '8', ' ']]

    def manhattan_distance(self):
        # Method to calculate the Manhattan distance heuristic.
        # Returns the sum of Manhattan distances for each tile from its goal position.
        distance = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != ' ':
                    row, col = divmod(int(self.state[i][j]) - 1, 3)
                    distance += abs(row - i) + abs(col - j)
        return distance


def print_solution(node):
    # Function to print the solution path from the initial state to the goal state.
    moves = []  # Initialize a list to store the states along the solution path.
    while node.parent:
        moves.append(node.state)
        node = node.parent
    moves.reverse()
    for state in moves:
        for row in state:
            print(row)
        print()


def a_star(start_state):
    # A* algorithm
    open_list = [PuzzleNode(start_state)]
    closed_set = set()  # visited nodes.

    while open_list:
        open_list.sort(key=lambda x: x.g_score + x.manhattan_distance())  # Sort the open list by f-score.
        current_node = open_list.pop(0)  # Remove and get the node with the lowest f-score.

        if current_node.is_goal():  # Check if the current node is the goal state.
            print_solution(current_node)  # Print the solution path.
            return

        closed_set.add(current_node)  # Add the current node to the closed set.

        children = current_node.generate_children()  # Generate children of the current node.
        for child in children:
            if child in closed_set:  # Skip children already visited.
                continue
            if child not in open_list:  # Add newly generated children to the open list.
                open_list.append(child)


if __name__ == "__main__":
    start_state = [[' ', '1', '3'], ['4', '2', '5'], ['7', '8', '6']]
    print("Initial State:")
    for row in start_state:
        print(row)
    print("\nSolving...\n")
    a_star(start_state)
