def Turn(array):
    newArray=[]
    for i in range(len(array)):
        for j in range(len(array[i])):
            if i is 0:
                newArray.append([])
            newArray[j].append(array[i][j])
    return newArray
