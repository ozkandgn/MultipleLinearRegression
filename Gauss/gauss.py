def GaussJCalculate(array,output):
    array=Combine(array,output)
    for i in range(len(array)):
        for j in range(i):
            tempValue=array[i][j]/array[j][j]
            for k in range(len(array[j])):
                array[i][k]-=(array[j][k]*tempValue)
    for i in range(len(array)):
        tempValue=array[i][i]
        for j in range(len(array[i])):
            array[i][j]/=tempValue
    for i in reversed(range(1,len(array))):
        for j in reversed(range(i,len(array[i])-1)):
            if i is j:
                for k in range(i):
                    tempValue=array[k][i]/array[i][i]
                    for l in range(i,len(array[i])):
                        array[k][l]-=array[j][l]*tempValue
    newArray=[]  
    for i in range(len(array)):
        newArray.append([])
    for i in range(len(array)):
        for j in range(len(array[i])-1):
            if int(array[i][j]) is 1:
                newArray[j]=round(array[i][-1],15)
    return newArray

def Combine(array,output):
    for i in range(len(array)):
        array[i].append(output[i])
    return array
