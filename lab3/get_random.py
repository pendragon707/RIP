import random

def get_random(num_count, begin, end):
    for _ in range(num_count):
        yield random.randint(begin, end)
