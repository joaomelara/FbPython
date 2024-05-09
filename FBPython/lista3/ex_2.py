counter = 0
for i in range (500):
    if (i % 3 == 0 and i % 2 != 0):
        counter += i
        print(counter)
print(counter)