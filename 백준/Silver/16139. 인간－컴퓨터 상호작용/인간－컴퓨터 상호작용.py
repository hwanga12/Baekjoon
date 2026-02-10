import sys

# 1. 빠른 입력을 위한 설정
input = sys.stdin.readline

def solve():
    # 문자열 입력 (공백 제거를 위해 .strip() 사용)
    s = input().strip()
    n = len(s)
    
    # 2. 누적 합 표(리스트) 만들기
    # 각 알파벳(26개)에 대해 문자열 길이+1 만큼의 공간 확보
    # prefix_sum[알파벳번호][위치] 형태
    prefix_sum = [[0] * (n + 1) for _ in range(26)]
    
    # 문자열을 한 번만 훑으면서 모든 알파벳의 누적 합을 채움
    for i in range(n):
        now_char_idx = ord(s[i]) - ord('a')
        for j in range(26):
            # 이전 위치까지의 합을 먼저 그대로 가져옴
            prefix_sum[j][i+1] = prefix_sum[j][i]
        
        # 현재 문자에 해당하는 알파벳만 +1 추가
        prefix_sum[now_char_idx][i+1] += 1
    
    # 3. 질문 처리
    q_count = int(input())
    for _ in range(q_count):
        query = input().split()
        alpha = query[0]
        l = int(query[1])
        r = int(query[2])
        
        target_idx = ord(alpha) - ord('a')
        
        # l번째부터 r번째까지의 개수는 (r+1까지의 합) - (l까지의 합)
        # 이 한 줄로 모든 연산이 끝나서 매우 빠릅니다!
        print(prefix_sum[target_idx][r+1] - prefix_sum[target_idx][l])

solve()