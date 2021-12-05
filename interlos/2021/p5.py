numbers = ['⋅', '∶', '⋮', '∶⋮', '∶∶', '∶⋅', '⋮⋅', '⋮∶', '⋮⋮']
n = '⋮⋮⋅∶⋅⋅⋮⋅∶∶⋅⋮∶⋅∶'

def expand(A):
    l = max(map(len, A))
    C = ['⋅' * (l - len(n)) + n for n in A]
    B = ['∶' + n for n in C[::-1]]
    C = ['⋮' + n for n in C]
    return A + B + C


while n not in numbers:
    numbers = expand(numbers)
    print(len(numbers))
print(numbers.index(n))
