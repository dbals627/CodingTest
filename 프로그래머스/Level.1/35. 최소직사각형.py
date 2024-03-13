def solution(sizes):
    width = []
    height = []
    for i in sizes:
        width.append(sorted(i)[0])
        height.append(sorted(i)[1])
    return max(width)*max(height)