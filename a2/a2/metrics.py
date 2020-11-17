from typing import List

from a2.data_structure import ClosedList
from a2.game_node import Node


def print_metrics(final_nodes: List[Node], closed_lists: List[ClosedList], execution_times: List[float], puzzle_count: int, search_name: str, heuristic_name: str):
    print('Metrics for: {} {}\n'.format(search_name, heuristic_name))

    solution_total, solution_average = compute_solution_paths(final_nodes)
    print('Solution path total: {}\n'.format(solution_total))
    print('Solution path average: {}\n'.format(solution_average))

    search_total, search_average = compute_search_paths(closed_lists)
    print('Search path total: {}\n'.format(search_total))
    print('Search path average: {}\n'.format(search_average))

    no_sol_total, no_sol_average = compute_no_solution(final_nodes, puzzle_count)
    print('No solution total: {}\n'.format(no_sol_total))
    print('No solution average: {}\n'.format(no_sol_average))

    exec_total, exec_average = compute_execution_time(execution_times)
    print('Execution time total: {}\n'.format(exec_total))
    print('Execution time average: {}\n'.format(exec_average))


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


def compute_execution_time(execution_times: List[float]):
    succesful_exec_time = [exec_time for exec_time in execution_times if exec_time is not None]
    total = sum(succesful_exec_time)
    average = total/len(succesful_exec_time)
    return total, average
