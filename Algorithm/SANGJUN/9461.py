from sys import stdin
input = stdin.readline

def _9461(n : int):
    P = [1, 1, 1, 2, 2] + [0] * (n - 5)

    for i in range(5, n):
        P[i] = P[i - 1] + P[i - 5]

    return P[n - 1]


if __name__ == "__main__":
    testcase = int(input())
    for _ in range(testcase):
        print(_9461(int(input())))
