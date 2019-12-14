def norm(n):
    return ((n - 1) % 26) + 1


def int_to_letter(n):
    return chr(norm(n) + ord('A') - 1)


def letter_to_int(letter):
    return ord(letter.upper()) - ord('A') + 1


def text_map(text, fce):
    output = ''
    for letter in text:
        output += int_to_letter(fce(letter_to_int(letter)))
    return output


if __name__ == '__main__':
    cipher = 'SPHADNILYIXOSYRTTGPKAPXIIFCPEIX'
    print(text_map(cipher, lambda x: 3 * x + 4))
