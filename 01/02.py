with open("input.txt", "r") as fd:
    lines = fd.readlines()
    lines = [line.rstrip() for line in lines] 

    listA = []
    listB = []
for line in lines :
    separate_numbers = line.split()
    listA.append(separate_numbers[0])
    listB.append(separate_numbers[-1])

total_list = []
for numberA in listA: 
    similarity_score = 0 
    for numberB in listB: 
        if numberA == numberB:
            similarity_score += 1
    total_list.append(int(numberA) * similarity_score)

total = sum(total_list)
print(total)