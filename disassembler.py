
# Operation code to mnemonic dictionary
# You can use this to lookup the machine code
# and translate it to the mnemonic instruction
INS_REF = {
    1: "ADD",
    2: "SUB",
    3: "STA",
    5: "LDA",
    6: "BRA",
    7: "BRZ",
    8: "BRP"
}

def disassemble(operation_code):
    if(operation_code == 000):
        return "END"
    else:
        operation_code = str(operation_code)
        if(operation_code == "901"):
            return "INP"
        elif(operation_code == "902"):
            return "OUT"
        else:
            codeList = list(operation_code)
            determine = codeList.pop(0)
            rest = "".join(codeList)
            for i in INS_REF:
                if(i == int(determine)):
                    return INS_REF[i] + " " + rest
    
    # this function should take in an integer operation code
    # and convert it to a LMC mnemonic instruction and return
    # it as a string
    pass

def main():
    operation = "0"
    listOp = []
    decoded = []
    while(operation != "000"):
        operation = input("Enter an operation in the format xxx: ")
        listOp.append(operation)
    for i in listOp:
        decoded.append(disassemble(int(i)))
    print(decoded)
    for i in decoded:
        print(i)
    
    # The main function should read all operation codes from the
    # user until the HLT instruction is read. Once it is read,
    # all operation codes should be disassembled using "disasassembled"
    # and then printed out to the user
    pass

if __name__ == "__main__":
    main()
