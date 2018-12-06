import hashlib

input = "bgvyzdsv"

number = 1
while not hashlib.md5(input + str(number)).hexdigest().startswith("000000"):
    number +=1

print number
