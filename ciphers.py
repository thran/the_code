def caesar(text, shift, start='a', end='z'):
    e = ''
    for t in text:
        if ord(start) <= ord(t) <= ord(end):
            e += chr((ord(t) - ord(start) + shift) % (ord(end) - ord(start) + 1) + ord(start))
        else:
            e += t
    return e
