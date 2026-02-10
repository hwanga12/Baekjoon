import sys
input = sys.stdin.readline

s = input().strip()
n = len(s)

# 26개 알파벳에 대해 각각 문자열 길이만큼의 리스트 생성
# prefix_sum[알파벳번호][위치]
prefix_sum = [[0] * (n + 1) for _ in range(26)]

for i in range(n):
    # 현재 문자가 어떤 알파벳인지 번호 확인 (0~25)
    now_char_idx = ord(s[i]) - ord('a')
    
    # 모든 알파벳(0~25)의 이전 누적합을 현재 칸으로 복사
    for j in range(26):
        prefix_sum[j][i+1] = prefix_sum[j][i]
    
    # 현재 해당하는 알파벳만 개수 1 증가
    prefix_sum[now_char_idx][i+1] += 1

# 이제 질문(q)이 들어오면 O(1)로 바로 계산 가능!
q = int(input())
for _ in range(q):
    alpha, l, r = input().split()
    l, r = int(l), int(r)
    idx = ord(alpha) - ord('a')
    
    # r+1 위치 값에서 l 위치 값을 빼면 구간 내 개수 등장!
    print(prefix_sum[idx][r+1] - prefix_sum[idx][l])