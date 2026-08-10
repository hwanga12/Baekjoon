def solution(id_list, report, k):
    reported_count = {name: 0 for name in id_list}
    reported_by = {name: set() for name in id_list}

    for r in report:
        a, b = r.split()

        if b not in reported_by[a]:
            reported_by[a].add(b)
            reported_count[b] += 1

    answer = []

    for name in id_list:
        mail_count = 0

        for reported in reported_by[name]:
            if reported_count[reported] >= k:
                mail_count += 1

        answer.append(mail_count)

    return answer