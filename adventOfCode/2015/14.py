import re
from collections import defaultdict

source = [
    # "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.",
    # "Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.",
    "Rudolph can fly 22 km/s for 8 seconds, but then must rest for 165 seconds.",
    "Cupid can fly 8 km/s for 17 seconds, but then must rest for 114 seconds.",
    "Prancer can fly 18 km/s for 6 seconds, but then must rest for 103 seconds.",
    "Donner can fly 25 km/s for 6 seconds, but then must rest for 145 seconds.",
    "Dasher can fly 11 km/s for 12 seconds, but then must rest for 125 seconds.",
    "Comet can fly 21 km/s for 6 seconds, but then must rest for 121 seconds.",
    "Blitzen can fly 18 km/s for 3 seconds, but then must rest for 50 seconds.",
    "Vixen can fly 20 km/s for 4 seconds, but then must rest for 75 seconds.",
    "Dancer can fly 7 km/s for 20 seconds, but then must rest for 119 seconds.",
]

seconds = 2503
# seconds = 1000

# for deer in source:
#     g = re.match(r'(\w+) .* (\d+) km/s for (\d+) .* (\d+) seconds.', deer).groups()
#     name = g[0]
#     speed = int(g[1])
#     run = int(g[2])
#     rest = int(g[3])
#     print name, (seconds / (run + rest) * speed * run) + (min(seconds % (run + rest), run) * speed)

deers = []
for deer in source:
    g = re.match(r'(\w+) .* (\d+) km/s for (\d+) .* (\d+) seconds.', deer).groups()
    deers.append({
        "name": g[0],
        "speed": int(g[1]),
        "run": int(g[2]),
        "rest": int(g[3]),
        "points": 0,
    })


for second in range(1, seconds + 1):
    state = defaultdict(list)
    for deer in deers:
        state[
            (second / (deer["run"] + deer["rest"]) * deer["speed"] * deer["run"]) + \
                (min(second % (deer["run"] + deer["rest"]), deer["run"]) * deer["speed"])
        ].append(deer)
    for deer in state[max(state.keys())]:
        deer["points"] += 1

for deer in deers:
    print deer["name"], deer["points"]
