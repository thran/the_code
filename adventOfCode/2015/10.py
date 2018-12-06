source = "3113322113"

def look_and_say(number):
    output = ""
    actual = ""
    count = None
    for s in number:
        if s != actual:
            if count is not None:
                output += str(count) + actual
            actual = s
            count = 1
        else:
            count +=1
    output += str(count) + actual

    return output

for i in range(50):
    source = look_and_say(source)
    print i, len(source)