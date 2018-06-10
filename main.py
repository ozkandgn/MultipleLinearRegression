import add
import read
from Gauss import gauss
import cloneNode as clone
array=[]
output=[]
inp=[]

inputs,outputs=read.Read()
min=len(inputs)

if len(inputs)>len(inputs[0]):
    min=len(inputs[0])
    
for i in range(len(inputs)):
    array.append([])
    for j in range(min):
        array[i].append(round(add.MulAdd(inputs[i],inputs[j]),4))

for i in range(len(outputs)):
    output.append([])
    for j in range(len(inputs)):
        output[i].append(round(add.MulAdd(outputs[i],inputs[j]),4))
array[0][0]=float(len(inputs[0]))

for o in range(len(output)):
    print("\nRegression",o+1," Complate!!")
    for i in range(len(array)):
        tempString=""
        for j in range(len(array[i])):
            if not j is len(array[i])-1:
                tempString+=str(array[i][j])+"x"+str(j+1)+" + "
            else:
                tempString+=str(array[i][j])+"x"+str(j+1)
        print(tempString,"=",str(output[o][i]))

try:
    for i in range(len(output)):
        inp.append(gauss.GaussJCalculate\
            (clone.CloneAll(array),clone.CloneAll(output[i])))
        print("\nTraining",i+1," Complate!!!")
        print("Reg  Value=",inp[i][0])
        for j in range(1,len(inp[i])):
            print("X",j," Value=",inp[i][j])
    print("\n")
    values=[]
    stop=""
    while not stop is "e":
        for i in range(len(inp[0])-1):
            print("Please Enter ",i+1,". Value")
            temp=input("")
            values.append(temp)
        for ou in range(len(inp)):
            total=inp[ou][0]
            for i in range(1,len(inp[ou])):
                total+=float(inp[ou][i])*float(values[i-1])
            print("Total Result(Output)=",ou+1,"=",total)
        stop=input("If Your Close Press 'e'(If Your Continue Press Enter)")
        values=[]

except KeyboardInterrupt:
    print("Closing With 'e'!!!")
except:
    print("Values Not Enough!!!")
