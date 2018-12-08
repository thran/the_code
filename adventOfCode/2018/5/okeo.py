
file = open('input.txt','r')
text = file.read()

def delete(text,index):
    return text[:index]+text[index+2:]

def doit(text):
    for i,letter in enumerate(text):
        try:
            if letter.swapcase() == text[i+1]:
                text = delete(text,i)
                return doit(text)
        except Exception as e:
            print(e)
            break
    return text

changed = True
while changed:
    new_text = doit(text)
    changed = text != new_text
    text = new_text

print(len(text))

exit()

file = open('input.txt', 'r')
text = file.read()


def delete(text, index):
    return text[:index] + text[index+2:]


def doit(text):
    for i, letter in enumerate(text):
        if i + 1 == len(text):
            break
        if letter.swapcase() == text[i+1]:
            text = delete(text,i)
            return text
    return text


changed = True
while changed:
    new_text = doit(text)
    changed = text != new_text
    text = new_text

print(len(text))
