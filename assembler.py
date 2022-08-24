# Binary codes for ISA
import binascii


ISA = {
    "NOP":"00000",
    "LOAD":"00001",
    "LOADINC":"00010",
    "STORE":"00011",
    "COPY":"00100",
    "JUMP":"00101",
    "JUMPNZ":"00110",
    "INC":"00111",
    "ADDI":"01000",
    "SUBI":"01001",
    "LSHI":"01010",
    "RSHI":"01011",
    "ADD":"01100",
    "SUB":"01101",
    "MUL":"01110",
    "RESET":"01111"
      
}

# binary codes for Registers
REG = {
    "R1":"00000",
    "R2":"00001",
    "R3":"00010",
    "R4":"00011",
    "R5":"00100",
    "R6":"00101",
    "R7":"00110",
    "R8":"00111",
    "R9":"01000",
    "R10":"01001",
    "R11":"01010",
    "AC":"01011",
    "MAR":"01100"
}

asmbInst = []

inCode = open("Assembly code.txt","r")
asmbInst = inCode.read().splitlines()

instCount = 0
binaryInst = ""

outCode = open("machine.txt","w")

for inst in asmbInst :

    command = inst.split(" ")

    if (len(command) == 1):                                                    # Type - I  Instructions                       
        typeI = ISA[command[0]] + "00000000000" 
        binaryInst = "M[" + str(instCount) + "] = 16'b" + typeI
        outCode.write(binaryInst + ";\n")

    elif (len(command) == 2):                                                  
        if (command[1] in REG):                                                # Type - A Instructions 
            typeA = ISA[command[0]] + "000000" +REG[command[1]]
            binaryInst = "M[" + str(instCount) + "] = 16'b" + typeA
            outCode.write(binaryInst + ";\n")

        elif (command[0] in ["LSHI" , "RSHI" , "ADDI" , "SUBI"]):                # Type - S Instructions
            val = bin(int(command[1])).replace("0b","")
            typeS = ISA[command[0]] + "000000" +("0"*(5-len(val))+val)
            binaryInst = "M[" + str(instCount) + "] = 16'b" + typeS
            outCode.write(binaryInst + ";\n")


    elif (len(command) == 3):                                                   # Type - M Instructions
        typeM = ISA[command[0]] + REG[command[1]] + "0" + REG[command[2]] 
        binaryInst = "M[" + str(instCount) + "] = 16'b" + typeM
        outCode.write(binaryInst + ";\n")

    print(binaryInst)
    instCount +=1

inCode.close()
outCode.close()

print("Compiled successfully.")