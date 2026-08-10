def solution(bandage, health, attacks):
    max_health = health
    consis = 0

    dict_ = {}
    for j in range(len(attacks)):
        dict_[attacks[j][0]] = attacks[j][1]

    for i in range(1, attacks[-1][0] + 1):

        if i in dict_:
            consis = 0
            health -= dict_[i]

            if health <= 0:
                return -1

        else:
            health += bandage[1]
            consis += 1

            if consis == bandage[0]:
                health += bandage[2]
                consis = 0

            health = min(health, max_health)

    return health