def char_position(letter):
    return ord(letter) - 97


def pos_to_char(pos):
    return chr(pos + 97)


def is_valid1(passwd):
    seq = 0
    last = -42
    for p in passwd:
        if p == last + 1:
            seq += 1
            if seq == 3:
                return True
        else:
            seq = 1
        last = p
    return False


def is_valid2(passwd):
    return char_position("i") not in passwd and char_position("l") not in passwd and char_position("o") not in passwd


def is_valid3(passwd):
    pairs = 0
    last = -42
    for p in passwd:
        if p == last:
            pairs += 1
            last  = -42
        else:
            last = p

    return pairs >= 2

def increment(passwd, postition=7):
    if postition < 0:
        return passwd
    if passwd[postition] == char_position("z"):
        increment(passwd, postition - 1)
    passwd[postition] = (passwd[postition] + 1)% 26
    return passwd



s = "hepxcrrq"
s = "hepxxyzz"
s = map(char_position, s)

while True:
    increment(s)
    if is_valid2(s) and is_valid1(s) and is_valid3(s):
        print "".join(map(pos_to_char, s))
        break
