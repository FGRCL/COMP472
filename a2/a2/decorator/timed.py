import time


def timedfunction(func):
    def wrapper(state, goals, heuristic):
        start_time = time.time()
        result = func(state, goals, heuristic)
        stop_time = time.time() - start_time
        return result + (stop_time, )
    return wrapper