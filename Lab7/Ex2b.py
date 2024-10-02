evenNumbers = []
counter = 1

while len(evenNumbers) == 0 or (evenNumbers and evenNumbers[-1] < 50):
    if counter % 2 == 0:
        evenNumbers.append(counter)
    counter += 1

print(evenNumbers)
