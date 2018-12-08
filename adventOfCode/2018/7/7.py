import re
from collections import defaultdict
from itertools import count


def seconds(letter, t=60):
    return t + ord(letter) - ord('A') + 1


prereqs = defaultdict(set)
jobs = {}
workers = {i: None for i in range(5)}

with open('input.txt') as f:
    for line in f:
        a, b = re.match(r'Step (\w) must be finished before step (\w) can begin\.', line.strip()).groups()
        prereqs[b].add(a)
        jobs[a] = seconds(a)
        jobs[b] = seconds(b)

for tick in count():
    for worker, job in zip([w for w, j in workers.items() if j is None], [j for j in jobs if jobs[j] > 0 and not prereqs[j] and j not in workers.values()]):
        print(worker, '->', job)
        workers[worker] = job

    for worker, job in workers.items():
        if job is None:
            continue
        jobs[job] += -1
        if jobs[job] == 0:
            workers[worker] = None
            for ps in prereqs.values():
                if job in ps:
                    ps.remove(job)
    print(jobs, workers)
    if sum(jobs.values()) == 0:
        break

print(tick + 1)