import re
from collections import defaultdict

import numpy as np


def iterate_guards():
    data = None
    with open('input.txt') as f:
        for line in sorted(f):
            m = re.match(r'\[15\d\d-(\d\d)-(\d\d) (\d\d):(\d\d)\] Guard #(\d+) begins shift', line.strip())
            if m:
                if data is not None:
                    yield data
                month, day, hour, minute, gid = m.groups()
                data = {
                    'id': int(gid),
                    'month': month,
                    'day': day,
                    'hour': hour,
                    'times': [int(minute) if hour == '00' else 0],
                }
            else:
                month, day, hour, minute, what = re.match(r'\[1518-(\d\d)-(\d\d) (\d\d):(\d\d)\] (\w+)', line.strip()).groups()
                data['times'].append(int(minute))
        yield data


guards = defaultdict(lambda: np.zeros(60, dtype=np.int32))
for d in iterate_guards():
    for i in range(1, len(d['times']), 2):
        guards[d['id']][d['times'][i]:d['times'][i+1]] += 1


for gid, times in sorted(guards.items(), key=lambda ts: -ts[1].sum()):
    print(gid * np.argmax(times))
    break

for gid, times in sorted(guards.items(), key=lambda ts: -ts[1].max()):
    print(gid * np.argmax(times))
    break
