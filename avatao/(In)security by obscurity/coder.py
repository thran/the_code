import subprocess

cipher = 'ahv%FL]mt7XCYz47Lm}/Ef|.?`jm"(Wx^io1<R3TO`w,MUcfo1<Qr)$59/+0~o&8G; kyl yh'

def code(msg):
    with open('PlainText.txt', 'w') as input:
        input.write(msg)

    subprocess.Popen('java -jar StreamCipherProgram.jar', shell=True).wait()

    with open('CipherText.txt') as output:
        return output.read()

n = 126 - 32 + 1

# for m, in ['a', 'b', 'c', 'd', 't', 'u', 'x', 'y', 'z']:
#     m = ' ' + m
#     c = code(m)
#     print m, c, map(ord, m), map(ord, c)

# m = 'b' * len(cipher)
# c = code(m)

# s = 0
# for before, after in zip(m, c):
#     s += ord(before)
#     shift = (ord(after) - s) % n
#     print shift

message = ''

s = 0
for i, c in enumerate(cipher):
    m = (ord(c) - (10 + i) - s - 32) % n + 32
    s += m
    message += chr(m)

print(message)
print(code(message))
print(cipher)
