def solution(cards):
    n = len(cards)
    visited = [False] * n

    def find_group(start):
        group = []
        current = start
        while not visited[current]:
            visited[current] = True
            group.append(current)
            current = cards[current] - 1
        return group

    groups = []
    for i in range(n):
        if not visited[i]:
            group = find_group(i)
            groups.append(len(group))

    if len(groups) < 2:
        return 0

    groups.sort(reverse=True)
    return groups[0] * groups[1]
