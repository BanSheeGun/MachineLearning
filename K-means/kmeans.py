def list_equal(a, b, n):
    for i in range(n):
        if a[i][0] != b[i][0] or a[i][1] != b[i][1] :
            return False
    return True


def learn(x, m, n, middle):
    c = [0 for _ in range(m)]
    md = []
    while True:
        md.append(middle)
        new_middle = [[0, 0] for _ in range(n)]
        tmp = [0 for _ in range(n)]
        index = 0
        for xe in x:
            distance = [(xe[0] - me[0]) ** 2 + (xe[1] - me[1]) ** 2 for me in middle]
            minindex = 0
            for i in range(n):
                if distance[minindex] > distance[i]:
                    minindex = i
            new_middle[minindex][0] += xe[0]
            new_middle[minindex][1] += xe[1]
            tmp[minindex] += 1
            c[index] = minindex
            index += 1

        for i in range(n):
            if tmp[i] != 0:
                new_middle[i][0] /= tmp[i]
                new_middle[i][1] /= tmp[i]
        if list_equal(middle, new_middle, n):
            break
        middle = new_middle
    return md, c


def main():
    print("Hello world")


if __name__ == '__main__':
    main()
