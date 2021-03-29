from mv import *
from stage import *
def demo():
    stage = Stage()
    # move to (1, 4), then to (0, 10), then to (2, 10)
    mv(stage, "simultaneous", [1, 4, 0, 10, 2, 10])
    # move to (10, 0), then to (10, 4), then to (2, 0)
    mv(stage, "separately", [10, 4, 2, 0])

if __name__ == "__main__":
    demo()
