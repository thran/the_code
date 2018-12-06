from PIL import Image


i = Image.open("P1-encoded.bmp")


def get_action(color):
    c = []
    for i, x in enumerate(color):
        c.append(str(bin(x))[-1])

    return "".join(c)

def next((x, y)):
    x += 30
    if x>= 900:
        x -= 900
        y += 30
    return x, y

def previous((x, y)):
    x -= 30
    if x< 0:
        x += 900
        y -= 30
    return x, y

def top((x, y)):
    y -= 30
    if y < 0:
        print "Konec", x, y
        return False

    return x,y

def bot((x, y)):
    y += 30
    if y >= 600:
        print "Konec", x, y
        return False

    return x,y


def get_jump((x, y)):
    if x + y == 0:
        return 1
    x, y = previous((x, y))
    global i
    if i.getpixel((x,y))[0] % 2 == 1:
        return i.getpixel((x,y))[1] % 4 + 1
    else:
        return 1

pss = []
pos = 0, 0
while True:
    pss.append(pos)
    print pos, get_jump(pos), get_action(i.getpixel(pos))
    action = get_action(i.getpixel(pos))
    for _ in range(get_jump(pos)):
        if action == "000":
            pos = next(pos)
        if action == "001":
            pos = previous(pos)
        if action == "010":
            pos = top(pos)
        if action == "011":
            pos = bot(pos)
        if action == "100":
            pos = top(pos)
            pos = next(pos)
        if action == "101":
            pos = bot(pos)
            pos = previous(pos)
        if action == "110":
            pos = bot(pos)
            pos = next(pos)
        if action == "111":
            pos = top(pos)
            pos = previous(pos)

        if pos == False:
            break
    if pos == False:
        break

for pos in pss:
    for x in range(30):
        for y in range(30):
            i.putpixel((pos[0]+x, pos[1]+y), (0,0,0))

i.show()