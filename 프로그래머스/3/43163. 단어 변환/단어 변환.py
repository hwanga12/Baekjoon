from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    queue = deque([(begin, 0)])
    visited = set([begin]) 
    
    while queue:
        current_word, steps = queue.popleft()
        
        if current_word == target:
            return steps
        
        for word in words:
            if word not in visited:
                diff_count = 0
                for i in range(len(current_word)):
                    if current_word[i] != word[i]:
                        diff_count += 1
            
                if diff_count == 1:
                    visited.add(word)
                    queue.append((word, steps + 1))
                    
    return 0