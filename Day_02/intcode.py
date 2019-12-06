inputRaw = """1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,6,19,23,1,13,23,27,1,6,27,31,1,31,10,35,1,35,6,39,1,39,13,43,2,10,43,47,1,47,6,51,2,6,51,55,1,5,55,59,2,13,59,63,2,63,9,67,1,5,67,71,2,13,71,75,1,75,5,79,1,10,79,83,2,6,83,87,2,13,87,91,1,9,91,95,1,9,95,99,2,99,9,103,1,5,103,107,2,9,107,111,1,5,111,115,1,115,2,119,1,9,119,0,99,2,0,14,0"""
testInputRaw = """1,9,10,3,2,3,11,0,99,30,40,50"""
inputList = inputRaw.split(',')
inputList = [int(i) for i in inputList]

def runCompute(inputList):
    for index in range(0, len(inputList), 4):
        if(inputList[index] == 1):
            inputList[inputList[index+3]] = inputList[inputList[index+1]] + inputList[inputList[index+2]]
        elif(inputList[index] == 2):
            inputList[inputList[index+3]] = inputList[inputList[index+1]] * inputList[inputList[index+2]]
        elif(inputList[index] == 99):
            break
        else:
            return -1
            #raise Exception('unknown opcode value: {}'.format(inputList[index]))
    return inputList[0]


# BAD SOLUTION HERE!!!!!!
# FOR THIS TO BE GOOD, WE SHOULD ACTUALLY ALLOW FOR MORE INSTRUCTION TYPES
# AND AVOID BRUTE-FORCING
# (but this should still work so hopefully good enough for now)

for i in range(0, 100):
    for j in range(0, 100):
        tempInputList = inputList[:]
        tempInputList[1] = i
        tempInputList[2] = j
        if(runCompute(tempInputList) == 19690720):
            print(100*i + j)