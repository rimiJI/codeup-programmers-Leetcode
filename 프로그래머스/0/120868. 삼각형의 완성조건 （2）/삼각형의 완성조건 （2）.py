def solution(sides):
    sides.sort()
    return ((sides[1] + sides[0]) - (sides[1] - sides[0]) - 1)

#가장 긴변은 작은변들의 합보다 작아야 한다. 