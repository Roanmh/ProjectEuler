# Title:  Project Euler 15 Solutions
#  Auth: Roan Martin-Hayden
#  Date: 12/28/2016

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
