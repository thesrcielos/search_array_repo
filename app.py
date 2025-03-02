import sys
from arraysearch import algorithms
from arraysearch import execution_time_gathering

if __name__ == "__main__":
    minimum_size = 100000
    maximum_size = 500000
    step = 25000
    samples_by_size = 7
    
    table = execution_time_gathering.take_execution_time(minimum_size, maximum_size, step, samples_by_size)

    print("Size | Linear Search| Binary Search | Ternany Search")
    for row in table:
        print(row)
