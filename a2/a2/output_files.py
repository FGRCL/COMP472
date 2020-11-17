from a2.game_node import Node


def write_no_solution(solution_file):
    solution_file.write("no solution")


def write_solution_file(final_node: Node, solution_file, exec_time):
    solution_file_line_template = "{} {} {}\n"
    node_stack = stack_nodes(final_node)

    solution_cost = 0
    while node_stack:
        current_node = node_stack.pop()
        solution_file.write(solution_file_line_template.format(current_node.moved_token, current_node.cost, get_state_string(current_node)))
        solution_cost = current_node.total_cost
    solution_file.write('{} {}\n'.format(solution_cost, exec_time))


def write_search_file(closed_list, search_file):
    search_file_line_template = "{} {} {} {}\n"

    for node in closed_list:
        search_file.write(search_file_line_template.format(node.f, node.total_cost, node.heuristic_score, get_state_string(node)))


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
