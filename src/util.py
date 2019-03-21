# Project Euler Utility Functions
# Functions are named according to their potential general use, and organized by
# the earliest problem they were written for.


# 14: Collatz Length
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


# 18: Triangle Path
def parse_spc_delim_2d(data_raw):
    '''Parse a space and return delimited string into a 2 array'''
    return [row for row in (x.split(" ") for x in data_raw.split("\n")) if row != ['']]

def recursive_print(root_node, level=0):
    print("\t" * level, root_node.weight)
    if root_node.child_left is not None:
        recursive_print(root_node.child_left, level + 1)
    if root_node.child_left is not None:
        recursive_print(root_node.child_right, level + 1)
