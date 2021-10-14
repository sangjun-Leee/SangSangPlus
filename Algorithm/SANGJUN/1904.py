from sys import stdin
input = stdin.readline

# 노가다 해서 규칙 찾았는데 블로그를 찾아보니...
# 길이가 i인 수를 만드는 방법 : i - 2 번째에서 00붙혀 만들기 + i - 1 번째에서 1붙혀 만들기
def _1904(N : int):
    dp = [1, 2] + [0] * (N - 2)

    for i in range(2, N):
        dp[i] = (dp[i - 2] + dp[i - 1]) % 15746
    
    return dp[N - 1]


if __name__ == "__main__":
    N = int(input())
    print(_1904(N))
