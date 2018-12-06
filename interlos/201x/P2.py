input = "SNOOTORTTEOSNNSILRRLLNSLLITREILNROLSRLNRNOLRSILRNNSTSTLETTTIOEELSNOERSNOINRLESRRNLTRITSRSOEIOINOSLNTSOORNIOTSTRNTOTOETEORILRONOSIRERELNNNIELISOTNLSILRNNNSLESNOENOSLEIONSSOORREEIELSRNILOIINRSETIOOLNOTRLIOSTTISRTSLEORISIEINREENNTNTTTOEEIREERSSRNRNLSESLINTINTNORLSLEESIRSOTSOLLINTTRRNIOOSTSTSROLIONIRISSLOSTTOELLITEOSNSRTOTITSTITOLNNIOOESNERSINLRNLRTSNOTORTRNORLESTTRLEOLEERIORRNNLERNRTLENLISOTRLOSEELINSRSLILSTNNNENLSNNLSRSITTRNRLTNOELTNLIETRLERLSIOIEIREOLRLLLNTLNESSLIIONILIIELNNLOTEETINRONLTLSTIRRTTO"

output = []
SSOSSOSLLSLLLSLLSSSLOSSLSOSSSLSOOLOLLSOSLOLOSLLOOOLLLLLLLSLLLOOOLSLOOLOLLLLLOOLOOSOLLLLOSOLLSOOOLLSLLOSSSSSSLOSLSLLLSLLLSLLLLLLLO

def T(p):
    if p == "L": return "S"
    if p == "S": return "L"
    return "O"

def R(p):
    return [p, p]

def E(p1, p2):
    return [p2, p1]

def I(p1, p2):
    if p1 == "L" or p2 == "L":
        return "L"
    if p1 == p2:
        return "O"
    return "S"

def N(p1, p2):
    if (p1 == "L" and p2 == "L") or (p1 == "S" and p2 == "O") or (p1 == "O" and p2 == "S"):
        return "L"
    if (p1 == "L" and p2 == "O") or (p1 == "O" and p2 == "L") or (p1 == "S" and p2 == "S"):
        return "O"
    return "S"


for p in input[::-1]:
    if p in "LOS":
        output.append(p)
    if p == "T":
        output.append(T(output.pop()))
    if p == "R":
        output += R(output.pop())
    if p == "E":
        output += E(output.pop(), output.pop())[::-1]
    if p == "I":
        output.append(I(output.pop(), output.pop()))
    if p == "N":
        output.append(N(output.pop(), output.pop()))

    print "".join(output)[::-1]