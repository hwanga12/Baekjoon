def solution(skill, skill_trees):
    a = 0
    ay = {}
    
    for i in range(len(skill)):
        ay[skill[i]] = i 
    
    
    for i in range(len(skill_trees)):
        answer = []
        result = "".join(char for char in skill_trees[i] if char in skill)
        for j in result:
            answer.append(ay[j])
        
        hey = True
        for k in range(len(answer)):
             if answer[k] != k:
                    hey = False
        if hey is True:
            a += 1
    return a