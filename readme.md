# About this repo

Simple python project to show a way to take experiental execution time to compare a set of algorithms (three in this case) in fair way.

## Search in sorted array

First even then odd sorting algorithms.

### Problem statement
​
The sample problem is to take a sorted list of integers, a number and find if that elements is in the list

### Time and Space complexity

| Algorithm       | Best Case       | Average Case     | Worst Case       | Space Complexity |
|---------------|---------------|----------------|----------------|----------------|
| **Linear Search** | \( O(1) \)       | \( O(n) \)        | \( O(n) \)        | \( O(1) \)        |
| **Binary Search** | \( O(1) \)       | \( O(log n) \)   | \( O(log n) \)   | \( O(1) \) (Iterative) / \( O(log n) \) (Recursive) |
| **Ternary Search** | \( O(1) \)       | \( O(log3 n) \) | \( O(log3 n) \) | \( O(1) \) (Iterative) / \( O(log n) \) (Recursive) |


# Python version
Python 3.11.0
​
# Running locally and testing

* Note: This instructions are for mac. Windows or linux may require some changes. 
* A good idea for this project, is to use a virtual environment, you could set up one with: [virtualenv](https://virtualenv.pypa.io/en/latest/).
* To create the virtual environment: `virtualenv env`
* To activate it:`source env/bin/activate`
* To install dependencies: `pip3 install -r requirements.txt`
* To run unit testing: `./test.sh`
* To try a default example, run: `: ./run.sh`. In the file ./run.sh is just an example, you can modify it. Theck the `app.py` file to get to understand how it works.

# Current coverage

Make sure you have "coverage" in your requirements.txt file and run pip install. Then run `coverage run -m unittest discover` and after that run `coverage report` to get the following table:

```
Name                            Stmts   Miss  Cover
---------------------------------------------------
arraysearch\__init__.py             0      0   100%
arraysearch\algorithms.py          34      0   100%
arraysearch\constants.py            3      0   100%
arraysearch\data_generator.py      11      1    91%
test\__init__.py                    0      0   100%
test\test_algorithms.py            24      1    96%
test\test_data_generator.py        29      1    97%
---------------------------------------------------
TOTAL                             101      3    97%
```

# Code beautifier
This code has been beautify using black: https://github.com/psf/black. 
The command to use is `black . -l 120`.
