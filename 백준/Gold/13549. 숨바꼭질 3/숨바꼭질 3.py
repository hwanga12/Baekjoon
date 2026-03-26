import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def find_time(n, m):
    # 1. 수빈이가 앞서 있거나 같은 경우
    if n >= m:
        return n - m

    # 2. 0에서 시작하는 경우 (무조건 1초 걸어서 1로 이동)
    elif n == 0:
        return 1 + find_time(1, m)

    # 3. 짝수일 때
    elif m % 2 == 0:
        return min(m - n, find_time(n, m // 2))

    # 4. 홀수일 때
    else:
        return 1 + min(find_time(n, m - 1), find_time(n, m + 1))


N, M = map(int, input().split())
print(find_time(N, M))