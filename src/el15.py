# Title:  Project Euler 15 Solutions
#  Auth: Roan Martin-Hayden
#  Date: 12/28/2016

import getopt
import sys

def recursive(height, width):
    h_result = 0
    w_result = 0
    if height > 0:
        h_result = recursive(height - 1, width)
    if width > 0:
        w_result = recursive(height, width - 1)
    if width == 0 or height == 0:
        return 1
    return h_result + w_result

class memory_optimization:
    def __init__(self):
        self.cache = {}

    def recr(self, height, width):
        h_result = 0
        w_result = 0
        location = (height, width)
        if location in self.cache:
            return self.cache[location]
        if height > 0:
            h_result = self.recr(height - 1, width)
        if width > 0:
            w_result = self.recr(height, width - 1)
        if width == 0 and height == 0:
            return 1
        self.cache[location] = h_result + w_result
        return self.cache[location]

def main(argv):
    height = 20
    width = 20
    mr = memory_optimization()
    try:
        opts, argv = getopt.getopt(argv, 'w:h:')
    except getopt.GetoptError:
        print("I failed you")
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            height = arg
        if opt == "-w":
            width = arg

    print(mr.recr(height, width))

if __name__ == '__main__':
    main(sys.argv)
