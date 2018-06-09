import turnArray
def Read():
    inputs=[]
    outputs=[]
    try:
        text_file=open("testValues.txt", "r")
        lines=text_file.read().split('\n')
    except:
        return []
    for line in lines:
        line=line.split(':')
        tempLine=[float(i) for i in line[0].split(',')]
        inputs.append(tempLine)
        tempLine=[float(i) for i in line[1].split(',')]
        outputs.append(tempLine)
    lines=[]
    lines.append(inputs)
    lines.append(outputs)
    inputs=turnArray.Turn(lines[0])
    zeros=[1.0 for i in range(len(inputs[0]))]
    inputs.reverse()
    inputs.append(zeros)
    inputs.reverse()
    outputs=turnArray.Turn(lines[1])
    return inputs,outputs
    
