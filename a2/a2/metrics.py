from typing import List

from a2.data_structure import ClosedList
from a2.game_node import Node


def print_metrics(final_nodes: List[Node], closed_lists: List[ClosedList], execution_times: List[float], puzzle_count: int, search_name: str, heuristic_name: str, output_file):
    print('Metrics for: {} {}\n'.format(search_name, heuristic_name))
    #file
    print('{},{}'.format(search_name, heuristic_name), file=output_file)

    solution_total, solution_average = compute_solution_paths(final_nodes)
    print('Solution path total: {}'.format(solution_total))
    print('Solution path average: {}'.format(solution_average))
    #file
    print('{},{}'.format('Solution path total', solution_total), file=output_file)
    print('{},{}'.format('Solution path average', solution_average), file=output_file)

    search_total, search_average = compute_search_paths(closed_lists)
    print('Search path total: {}'.format(search_total))
    print('Search path average: {}'.format(search_average))
    #file
    print('{},{}'.format('Search path total', search_total), file=output_file)
    print('{},{}'.format('Search path average', search_average), file=output_file)

    no_sol_total, no_sol_average = compute_no_solution(final_nodes, puzzle_count)
    print('No solution total: {}'.format(no_sol_total))
    print('No solution average: {}'.format(no_sol_average))
    #file
    print('{},{}'.format('No solution total', no_sol_total), file=output_file)
    print('{},{}'.format('No solution average', no_sol_average), file=output_file)

    solution_cost_total, solution_cost_average = computer_solution_cost(final_nodes)
    print('Solution cost total: {}'.format(solution_cost_total))
    print('Solution cost average {}'.format(solution_cost_average))
    #file
    print('{},{}'.format('Solution cost total', solution_cost_total), file=output_file)
    print('{},{}'.format('Solution cost average', solution_cost_average), file=output_file)

    exec_total, exec_average = compute_execution_time(execution_times)
    print('Execution time total: {}'.format(exec_total))
    print('Execution time average: {}'.format(exec_average))
    #file
    print('{},{}'.format('Execution time total', exec_total), file=output_file)
    print('{},{}'.format('Execution time average', exec_average), file=output_file)
    print('{}'.format(''), file=output_file)
    print()
    print()


def compute_solution_paths(final_nodes: List[Node]):
    successful_final_nodes = [final_node for final_node in final_nodes if final_node is not None]
    total = sum([get_solution_path_length(final_node) for final_node in successful_final_nodes])
    average = total/len(successful_final_nodes)
    return total, average


def get_solution_path_length(final_node: Node):
    count = 0
    current_node = final_node
    while current_node is not None:
        count += 1
        current_node = current_node.parent
    return count


def compute_search_paths(closed_lists: List[ClosedList]):
    successful_closed_lists = [closed_list for closed_list in closed_lists if closed_list is not None]
    total = sum([get_search_path_length(closed_list) for closed_list in successful_closed_lists])
    average = total/len(successful_closed_lists)
    return total, average


def get_search_path_length(closed_list: ClosedList):
    return len(list(closed_list))


def compute_no_solution(final_nodes: List[Node], puzzle_count: int):
    total = len([final_node for final_node in final_nodes if final_node is None])
    average = total/puzzle_count
    return total, average


def computer_solution_cost(final_nodes: List[Node]):
    successful_final_nodes = [final_node for final_node in final_nodes if final_node is not None]
    total = sum([final_node.total_cost for final_node in successful_final_nodes])
    average = total/len(successful_final_nodes)
    return total, average


def compute_execution_time(execution_times: List[float]):
    succesful_exec_time = [exec_time for exec_time in execution_times if exec_time is not None]
    total = sum(succesful_exec_time)
    average = total/len(succesful_exec_time)
    return total, average
