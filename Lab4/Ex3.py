# Manipulate a list in various ways

responseValues = [5, 7, 3, 8,]
responseValues.append(0)

responseValues = responseValues[0:2] + [6] + responseValues[2:]


print(responseValues)