import json

from netcat import Netcat


def get_map():
    m = {}
    nc = Netcat('88.99.13.190', 36348)

    def code(inp):
        nc.read_until('\n')
        nc.write('aa' + inp + '\n')
        nc.read_until('\n')
        return nc.read_until('\n')[4:-1]

    for i in range(33, 127):
        inp = chr(i)
        output = code(inp)
        print(inp, output)
        m[inp] = output
        for j in range(32, 127):
            inp = chr(i) + chr(j)
            output = code(inp)
            print(inp, output)
            m[inp] = output

    return m

# json.dump(get_map(), open('map.json', 'w'))
cipher = '4b795162425d5e1e1e757544726f6669797f7c63756f4249461e4f464d44754f425e534f5975585f75197d797e1b62696e6f5e751b424d4475595a5f4b7548755e434b754b424b424d755e4f1b75155e2a57'

m = json.load(open('map.json'))
mm = {v:k for k, v in m.items()}

r = ''
for i in range(len(cipher) / 4):
    c = cipher[4*i:4 * (i + 1)]
    if c in mm:
        r += mm[c]

print(r)