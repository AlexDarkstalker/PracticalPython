from urllib.request import urlopen

http = urlopen("https://stepik.org/media/attachments/lesson/209719/2.html").read().decode("utf-8")
text = str(http)
codeStrings = dict()
state = 0
maxValue = 0
maxStrings = list()
while text.find("<code>") != -1:
    posCode = text.find("<code>")
    posEnd = text.find("</code>", posCode)
    codeString = text[posCode + len("<code>"): posEnd]
    text = text[posEnd:]
    if codeStrings.keys().__contains__(codeString):
        codeStrings[codeString] += 1
        if codeStrings[codeString] == maxValue:
            maxStrings.append(codeString)
        elif codeStrings[codeString] > maxValue:
            maxStrings = []
            maxValue = codeStrings[codeString]
            maxStrings.append(codeString)
    else:
        codeStrings[codeString] = 1
print(sorted(maxStrings), maxValue)
