import time
import tracemalloc
import random
from arraysearch import algorithms
from arraysearch import constants
from arraysearch import data_generator


def take_execution_time(minimum_size, maximum_size, step, samples_by_size, two=False):
    return_table = []

    for size in range(minimum_size, maximum_size + 1, step):
        print("Processing size: " + str(size))
        table_row = [size]
        times = take_times(size, samples_by_size, two)
        return_table.append(table_row + times)

    return return_table


"""
    It will return three values, one for each algorithm: The execution time for that size on each algorithm
"""


def take_times(size, samples_by_size, two):
    samples = []
    for _ in range(samples_by_size):
        samples.append(data_generator.get_random_list(size))

    if two:
        return [
            take_time_for_algorithm(samples, algorithms.binary_search),
            take_time_for_algorithm(samples, algorithms.ternary_search),
        ]
    return [
        take_time_for_algorithm(samples, algorithms.linear_search),
        take_time_for_algorithm(samples, algorithms.binary_search),
        take_time_for_algorithm(samples, algorithms.ternary_search),
    ]


"""
    Returns the median of the execution time measures for a sorting approach given in 
"""


def take_time_for_algorithm(samples_array, searching_approach):
    times = []
    memory_usage = []

    for sample in samples_array:
        tracemalloc.start()
        elem = sample[random.randint(0, len(sample))]
        start_time = time.time()
        searching_approach(sample.copy(), elem)
        end_time = time.time()
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        times.append(int(constants.TIME_MULTIPLIER * (end_time - start_time)))
        memory_usage.append(peak)

    times.sort()
    memory_usage.sort()
    return times[len(times) // 2], memory_usage[len(memory_usage) // 2]
