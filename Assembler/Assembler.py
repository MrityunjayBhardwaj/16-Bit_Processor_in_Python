"""
TODO:
insert a file
preprocess it.

"""
import re
import sys

Symbol_table = {
    "@R0": 0,
    "@R1": 1,
    "@R2": 2,
    "@R3": 3,
    "@R4": 4,
    "@R5": 5,
    "@R6": 6,
    "@R7": 7,
    "@R8": 8,
    "@R9": 9,
    "@R10": 10,
    "@R11": 11,
    "@R12": 12,
    "@R13": 13,
    "@R14": 14,
    "@R15": 15,
    "SP"  : 0,
    "LCL" : 1,
    "ARG" : 2,
    "THIS": 3,
    "THAT": 4,
    "SCREEN":16384,
    "KBD" : 24576
}

# print(Symbol_table.get("KBD"))

comp_table = {
    "0"  : [0    ,1,0,1,0,1,0],
    "1"  : [0    ,1,1,1,1,1,1],
    "-1" : [0    ,0,0,1,1,0,0],
    "D"  : [0    ,0,0,1,1,0,0],
    "A"  : [0    ,1,1,0,0,0,0],
    "M"  : [   1 ,1,1,0,0,0,0],
    "!D" : [0    ,0,0,1,1,0,1],
    "!A" : [0    ,1,1,0,0,0,1],
    "!M" : [   1 ,1,1,0,0,0,1],
    "-A" : [0    ,1,1,0,0,1,1],
    "-M" : [   1 ,1,1,0,0,1,1],
   "D+1" : [0    ,0,1,1,1,1,1],
   "A+1" : [0    ,1,1,0,1,1,1],
   "M+1" : [   1 ,1,1,0,1,1,1],
   "D-1" : [0    ,0,0,1,1,1,0],
   "A-1" : [0    ,1,1,0,0,1,0],
   "M-1" : [   1 ,1,1,0,0,1,0],
   "D+A" : [0    ,0,0,0,0,1,0],
   "D+M" : [   1 ,0,0,0,0,1,0],
   "D-A" : [0    ,0,1,0,0,1,1],
   "D-M" : [   1 ,0,1,0,0,1,1],
   "A-D" : [0    ,0,0,0,1,1,1],
   "M-D" : [   1 ,0,0,0,1,1,1],
   "D&A" : [0    ,0,0,0,0,0,0],
   "D&M" : [   1 ,0,0,0,0,0,0],
   "D|A" : [0    ,0,1,0,1,0,1],
   "D|M" : [   1 ,0,1,0,1,0,1],
}

dest_table = {
    "null" : [0,0,0],
    "M"    : [0,0,1],
    "D"    : [0,1,0],
    "MD"   : [0,1,1],
    "A"    : [1,0,0],
    "AM"   : [1,0,1],
    "AD"   : [1,1,0],
    "AMD"  : [1,1,1],
}

jump_table = {
    "null"  : [0,0,0],
    "JGT"   : [0,0,1],
    "JEQ"   : [0,1,0],
    "JGE"   : [0,1,1],
    "JLT"   : [1,0,0],
    "JNE"   : [1,0,1],
    "JLE"   : [1,1,0],
    "JMP"   : [1,1,1],
}


def dec2bin(n): 
    initbin = bin(n).replace("0b","")
    b = [ int(initbin[i]) if i >= 0 else 0 for i in range(len(initbin)-16,len(initbin))]
    return b 



def main():
    #Open The File
    f = open(str(sys.argv[1]),"rt"); # rt = read text
    # print(f.read())

    # Processing this file 
    p1 = [re.compile('\/\/').split(line)
                for line in f]
    p2 = [l[0] for l in p1]
    p3 = [];
    for line in p2:
        if(re.search(r'\w',line) != None):
            p3.append(line.replace(" ","").replace("\n",""));

    # NOTE: FIRST PASS

    # NOTE: ADD LABELS in the Symbol Table and remove lables from the lines(because they are useless while interpreting the asm code)

    lineNum = 0;
    for line in p3:
        if( re.search(r'\(',line) != None):
            currLabel = line.replace("(","").replace(")","")
        # check if its alreadly inside the symbols table
            if (Symbol_table.get(currLabel) == None):
                # then add it in the dictonary
                Symbol_table[currLabel] = lineNum;
                del p3[lineNum]
        lineNum+=1


    #NOTE: SECOND PASS
    #NOTE: Now splitting the instructions for parsing.
    # for  A instruction
    BinaryProgram = [None]*len(p3)
    # Converting Variables to Register Number(16++)
    var_index = 16 #because 0-15 are researved Registers
    lineNum =0

    for line in p3:
        if( re.search(r'@\D',line) != None):
            currVariable = line.replace("@","")
            if (Symbol_table.get(currVariable) == None):
                # add this new Variable in Symbol_table
                Symbol_table[currVariable] = var_index
                p3[lineNum] = "@"+str(var_index)
                var_index +=1
            else:
                p3[lineNum] = "@"+str(Symbol_table.get(currVariable))

        lineNum +=1

    # Write the preprocessed File
    out = open(str(sys.argv[1]).replace(".asm","")+".pre","w")
    for line in p3:
        out.write(str(line)+"\n")

    # STAGE 2 Creating Symbol table
    # NOW, Split the instruction to destination,comp,jump

    i=0
    p3split = [None]*len(p3)
    for line in p3:
        tmp = re.split(r'\=',line)
        tmp1 = re.split(r'\;',tmp[len(tmp) - 1])
        finalbits = tmp;# if len(tmp) > 1 and len(tmp1) == 1
        # A instruction split
        if (len(tmp)== 1 and len(tmp1)== 1): finalbits = [line.replace("@","")] 
        # C instruction split
        if (len(tmp)== 1 and len(tmp1) > 1): finalbits = ["null",tmp1[0],tmp1[1]] 
        if (len(tmp)> 1 and len(tmp1) == 1): finalbits = [tmp[0],tmp[1],"null"] 
        if (len(tmp)> 1 and len(tmp1) > 1) : finalbits = [tmp[0],tmp1[0],tmp1[1]] 

        p3split[i] = finalbits
        i +=1

    # print(p3split)
    # Now, finally Converting it to Binary using Symbol_table
    for i in range(0,len(p3split)):
        line = p3split[i]
        if (len(line) > 1):# filter out A instructions
            # print(line)
            dest = line[0]
            comp = line[1]
            jump = line[2]
            w = dest_table[dest]
            x = comp_table[comp]
            y = jump_table[jump]
            BinaryProgram[i] = [1,1,1,x[0],x[1],x[2],x[3],x[4],x[5],x[6],w[0],w[1],w[2],y[0],y[1],y[2]]
            continue
        print(line)
        BinaryProgram[i] = dec2bin(int(line[0]))
    p3 = BinaryProgram
    # print(BinaryProgram)

    print(Symbol_table)
    # Write out file
    out = open(str(sys.argv[1]).replace(".asm","")+".out","w")
    for line in p3:
        for i in line:
            out.write(str(i))
        out.write("\n")
        pass
    
if __name__ == '__main__':
    main()