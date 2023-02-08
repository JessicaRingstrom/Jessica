from random import gauss
n = 7
values = []
frequencies = {}
while len(values) < n:
    value = gauss(3, 2)
    if 0 < value < 25:
        frequencies[int(value)] = frequencies.get(int(value), 0) + 1
        values.append(value)
print(values)