def initialize_or_increment(dictionary: dict, key, init_value, increment):
    if key not in dictionary:
        dictionary[key] = init_value
    else:
        dictionary[key] += increment


def safe_init(dictionary: dict, key, init_value):
    if key not in dictionary:
        dictionary[key] = init_value
