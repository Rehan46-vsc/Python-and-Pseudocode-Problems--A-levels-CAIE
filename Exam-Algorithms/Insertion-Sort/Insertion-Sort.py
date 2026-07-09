list = [7, 3, 5, 1, 8, 6, 2]

print(list)

for index in range(1, len(list)):
    key = list[index]
    place = index - 1

    while place >= 0 and list[place] > key:
        list[place + 1] = list[place]
        place -= 1

    list[place + 1] = key

print(list)

#note that the printed list before and after are different because lists in python are mutable i.e they can be changed.
