# Title:  Project Euler 15 Solutions
#  Auth: Roan Martin-Hayden
#  Date: 12/28/2016

import getopt
import sys
import progressbar

bar = progressbar.ProgressBar(maxval=20 ** 20).start()
i = 0


def recursive(height, width):
    global i
    h_result = 0
    w_result = 0
    if height > 0:
        h_result = recursive(height - 1, width)
    if width > 0:
        w_result = recursive(height, width - 1)
    if width == 0 or height == 0:
        i += 1
        bar.update(i)
        return 1
    i += 1
    bar.update(i)
    return h_result + w_result


def main(argv):
    height = 20
    width = 20
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

    print(recursive(height, width))

if __name__ == '__main__':
    main(sys.argv)
