import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# 1. 포인터를 양 끝에 배치
left = 0
right = n - 1
max_score = 0

# 2. 두 포인터가 만날 때까지 반복
while left < right:
    # 현재 두 포인터 사이의 능력치 계산
    distance = right - left - 1
    current_min_skill = min(arr[left], arr[right])
    current_score = distance * current_min_skill
    
    # 최댓값 갱신
    max_score = max(max_score, current_score)
    
    # 3. 투 포인터 이동 로직: 더 낮은 능력치를 가진 쪽을 버린다!
    if arr[left] < arr[right]:
        left += 1
    else:
        right -= 1

print(max_score)