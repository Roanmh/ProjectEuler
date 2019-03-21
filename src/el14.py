# Title:  Project Euler 14 Solutions
#  Auth: Roan Martin-Hayden
#  Date: 12/28/2016

from enum import Enum
from time import time
from sys import getsizeof

N = 1000000


# Supporting Functions
def draw_array():
    # TODO: Write as needed
    pass


class CollatzLengthEfficient:
    def __init__(self):
        self.memory = [None, 0]

    def length(self, n):
        if n > self.memory.__len__() - 1 or self.memory[n] is None:
            for i in range(n - (self.memory.__len__() - 1)):
                self.memory.append(None)
            if n % 2:
                np = 3 * n + 1
            else:
                np = int(n / 2)
            self.memory[n] = self.length(np) + 1
        return self.memory[n]

    def __call__(self, *args, **kwargs):
        return self.length(*args)


def collatz_length(n):
    seq = [n]
    count = 0
    while n != 1:
        if n % 2:
            n = 3 * n + 1
        else:
            n /= 2
        count += 1
        seq.append(n)
    return count, seq


# Brute Force Method
def brute(high_n):
    max_len = 0
    for n in range(1, high_n):
        result, dev_null = collatz_length(n)
        if result > max_len:
            max_len = result
            max_n = n
    return max_len, max_n


def memory(high_n):
    collatz_length_eff = CollatzLengthEfficient()
    max_len = 0
    for n in range(1, high_n):
        result = collatz_length_eff(n)
        print(getsizeof(collatz_length_eff.memory))
        if result > max_len:
            max_len = result
            max_n = n
    return max_len, max_n


# Solution Selection
class Methods(Enum):
    BRUTE = 1
    MEMORY = 2


def main(n, method=Methods.BRUTE):
    if isinstance(Methods.MEMORY, type(method)):
        result = memory(n)
    else:
        result = brute(n)
    return "{Result(" + str(n) + " : " + str(result[0]) + "@" + str(result[1]) + "}"


# Performance Test
def performance_test():
    for method in Methods:
        start_time = time()
        result = main(N, method)
        end_time = time()
        print("Method:", method)
        print("\tResult:", result)
        print("\tRuntime:", end_time - start_time)

# Run with each with n
if __name__ == "__main__":
    performance_test()
