def fibonacci():
    yield 1
    i = 0
    j = 1
    this = 0

    while True:
        this = i + j
        i = j
        j = this
        yield this

for n, f in enumerate(fibonacci()):
    if len(str(f)) == 1000:
        print n+1, f
        break
