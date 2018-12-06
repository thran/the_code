import hashlib

c = 'uqwqemis'
# c = 'abc'

found = 0
i = 0
size = 8
password = [' '] * size

while True:
    hash = hashlib.md5((c + str(i)).encode('utf-8')).hexdigest()
    if hash.startswith('00000'):
        print(hash[5])
        try:
            position = int(hash[5])
            if 0 <= position < size and password[position] == ' ':
                password[position] = hash[6]
                found += 1
                print(password)
        except ValueError:
            pass

        if found >= size:
            break
    i += 1

print(''.join(password))
