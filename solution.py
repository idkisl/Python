def pascal_triangle():
    line = [1]
    yield 1
    while True:
        line_next = [1]
        for i in range(0, len(line) - 1):
            line_next += [line[i+1] + line[i]]

        line_next += [1]
        line = []
        for i in line_next:
            line += [i]
        for i in line:
            yield i
