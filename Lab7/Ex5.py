# Combine the tuples Years and Respondents into a single dictionary

Years = (1980, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989)
Respondents = (17, 35, 26, 26, 25, 27, 35, 21, 19)

listlen = len(Years)
MyDict = {}
index = 0

while index < listlen:
    MyDict[Years[index]] = Respondents[index]
    index += 1

print(MyDict)