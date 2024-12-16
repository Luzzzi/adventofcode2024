with open("input.txt", "r") as fd:
    lines = fd.readlines()
    lines = [line.rstrip() for line in lines] 

    listA = []
    listB = []
for line in lines :
    separate_numbers = line.split()
    listA.append(separate_numbers[0])
    listB.append(separate_numbers[-1])

listA.sort()
listB.sort()

totalDistance = []
for number in range(len(listA)):
    totalDistance.append(abs(int(listA[number]) - int(listB[number])))

    
result = sum(totalDistance)
print(result)