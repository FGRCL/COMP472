from a2.game_node import Node


def write_solution_file(final_node: Node, solution_file, exec_time):
    solution_file_line_template = "{} {} {}\n"
    node_stack = stack_nodes(final_node)

    while node_stack:
        current_node = node_stack.pop()
        solution_file.write(solution_file_line_template.format(current_node.moved_token, current_node.cost, get_state_string(current_node)))
    solution_file.write('{} {}\n'.format(current_node.total_cost, exec_time))


def stack_nodes(final_node: Node):
    current_node = final_node
    stack = []
    while current_node.parent is not None:
        stack.append(current_node)
        current_node = current_node.parent
    stack.append(current_node)
    return stack

def get_state_string(node: Node):
    state_string = ''
    for i in range(len(node.state)):
        for j in range(len(node.state[i])):
            state_string += str(node.state[i][j]) + ' '
    return state_string