import sys
input = sys.stdin.readline

n = int(input())
tree = {}

# 트리 구성
for _ in range(n):
    root, left, right = input().split()
    tree[root] = (left, right)

# 전위 순회 (루트 → 왼쪽 → 오른쪽)
def preorder(node):
    if node == '.':
        return
    print(node, end='')
    left, right = tree[node]
    preorder(left)
    preorder(right)

# 중위 순회 (왼쪽 → 루트 → 오른쪽)
def inorder(node):
    if node == '.':
        return
    left, right = tree[node]
    inorder(left)
    print(node, end='')
    inorder(right)

# 후위 순회 (왼쪽 → 오른쪽 → 루트)
def postorder(node):
    if node == '.':
        return
    left, right = tree[node]
    postorder(left)
    postorder(right)
    print(node, end='')

# 항상 루트는 'A'
preorder('A')
print()
inorder('A')
print()
postorder('A')