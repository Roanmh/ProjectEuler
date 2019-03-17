test_data_raw = """3
7 4
2 4 6
8 5 9 3"""

data_raw = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""


class TriNode:
    comparison_count = 0

    def __init__(self, weight, child_left, child_right, path_weight_left=None, path_weight_right=None):
		self.weight = int(weight)
		self.child_left = child_left
		self.child_right = child_right
		self.path_weight_left = path_weight_left
		self.path_weight_right = path_weight_right

    @property
    def largest_path(self):
        left = self.path_weight_left if self.path_weight_left else 0
        right = self.path_weight_right if self.path_weight_right else 0

        TriNode.comparison_count += 1
        return max(left, right)


def parse_raw(data_raw):
    return [row for row in (x.split(" ") for x in data_raw.split("\n")) if row != ['']]


def init_graph(data_raw):
    triangle_weights = parse_raw(data_raw)

    nodes_by_row = []
    row_last = []
    for row_weights in triangle_weights[::-1]:
        row = []
        for i, weight in enumerate(row_weights):
            if row_last != []:
                child_left = row_last[i]
                child_right = row_last[i + 1]
            else:
                child_left = None
                child_right = None
            row.append(TriNode(weight, child_left, child_right))
        row_last = row
        nodes_by_row.insert(0, row_last)
    return nodes_by_row # Return root Node of Triangle


def calculate_path_weights(nodes_by_row):
    for row in nodes_by_row:
        for node in row:
            if node.child_left is not None:
                node.child_left.path_weight_right = node.largest_path + node.weight
            if node.child_right is not None:
                node.child_right.path_weight_left = node.largest_path + node.weight


def triangle_largest_path(nodes_by_row):
    return max((n.largest_path + n.weight for n in nodes_by_row[-1]))


def recursive_print(root_node, level=0):
    print("\t" * level, root_node.weight)
    if root_node.child_left is not None:
        recursive_print(root_node.child_left, level + 1)
    if root_node.child_left is not None:
        recursive_print(root_node.child_right, level + 1)


def main(test_values=False):
    from sys import argv
    if argv[1] == "-t" or test_values:
        nodes_by_row = init_graph(test_data_raw)
    elif argv[1] == "-f":
        with open(argv[2]) as f:
            file_data_raw = f.read()
            nodes_by_row = init_graph(file_data_raw)
    else:
        nodes_by_row = init_graph(data_raw)

    calculate_path_weights(nodes_by_row)

    print("Largest Path At Base of Triangle: ", triangle_largest_path(nodes_by_row))

    if "-c" in argv:
        print("Comparison Count: ", TriNode.comparison_count)


if __name__ == '__main__':
    main()
