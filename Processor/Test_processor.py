import unittest
import processor_16bit
# import numpy as np
import random
import math

def gen_num(maxbit):
    return [(int)(random.random()*1.5) for i in range(maxbit)]

def to_binary(val):
    retval = ""
    for i in val:
        retval += str(i)
    return retval


def bin2dec(bin):
    val =0;
    for i in range(len(bin)):
        val += bin[(len(bin)-1)-i]*(2**i);
    return val

def dec2bin(n,k): 
    initbin = bin(n).replace("0b","")
    b = [ int(initbin[i]) if i >= 0 else 0 for i in range(len(initbin)-k,len(initbin))]
    return b 


def andt(i1,i2):
    return [ i1[i] and i2[i] for i in range(len(i1))]

def ort(i1,i2):
    return [ i1[i] or i2[i] for i in range(len(i1))]

def nott(inp):
    return [1-inp[i] for i in range(len(inp))]

class TestCalc(unittest.TestCase):

    def test_transistor(self):
        #{in = switch = 0/1 power = 1} {out = 0/1}
        test_result = Gates_refactored.Transistor(0,1).output()
        self.assertEqual(test_result,0)

        test_result = Gates_refactored.Transistor(1).output()
        self.assertEqual(test_result,1)

        # Testing POWER input:
        # if Power is 0 then the output should be 0
        test_result = Gates_refactored.Transistor(1,0).output()
        self.assertEqual(test_result,0)



    def test_NAND(self):

        test_result = Gates_refactored.NAND(0,0,1).output()
        self.assertEqual(test_result,1)

        test_result = Gates_refactored.NAND(0,1,1).output()
        self.assertEqual(test_result,1)

        test_result = Gates_refactored.NAND(1,0,1).output()
        self.assertEqual(test_result,1)

        test_result = Gates_refactored.NAND(1,1,1).output()
        self.assertEqual(test_result,0)

        # Testing POWER input:
        test_result = Gates_refactored.NAND(1,0,0).output()
        self.assertEqual(test_result,0)

    def test_NOT(self):

        test_result = Gates_refactored.NOT(0,1).output()
        self.assertEqual(test_result,1)

        test_result = Gates_refactored.NOT(1,1).output()
        self.assertEqual(test_result,0)

        # Testing Power input:
        test_result = Gates_refactored.NOT(1,0).output()
        self.assertEqual(test_result,0)


    def test_AND(self):

        test_result = Gates_refactored.AND(0,0,1).output()
        self.assertEqual(test_result,0)

        test_result = Gates_refactored.AND(0,1,1).output()
        self.assertEqual(test_result,0)

        test_result = Gates_refactored.AND(1,0,1).output()
        self.assertEqual(test_result,0)

        test_result = Gates_refactored.AND(1,1,1).output()
        self.assertEqual(test_result,1)

        # Testing POWER input:
        test_result = Gates_refactored.AND(1,1,0).output()
        self.assertEqual(test_result,0)


    def test_OR(self):

        test_result = Gates_refactored.OR(0,0,1).output()
        self.assertEqual(test_result,0)

        test_result = Gates_refactored.OR(0,1,1).output()
        self.assertEqual(test_result,1)

        test_result = Gates_refactored.OR(1,0,1).output()
        self.assertEqual(test_result,1)

        test_result = Gates_refactored.OR(1,1,1).output()
        self.assertEqual(test_result,1)

        # Testing POWER input:
        test_result = Gates_refactored.OR(1,1,0).output()
        self.assertEqual(test_result,0)



    def test_NOR(self):

        test_result = Gates_refactored.NOR(0,0,1).output()
        self.assertEqual(test_result,1)

        test_result = Gates_refactored.NOR(0,1,1).output()
        self.assertEqual(test_result,0)

        test_result = Gates_refactored.NOR(1,0,1).output()
        self.assertEqual(test_result,0)

        test_result = Gates_refactored.NOR(1,1,1).output()
        self.assertEqual(test_result,0)

        # Testing POWER input:
        test_result = Gates_refactored.NOR(0,0,0).output()
        self.assertEqual(test_result,0)

    def test_XOR(self):

        test_result = Gates_refactored.XOR(0,0,1).output()
        self.assertEqual(test_result,0)

        test_result = Gates_refactored.XOR(0,1,1).output()
        self.assertEqual(test_result,1)

        test_result = Gates_refactored.XOR(1,0,1).output()
        self.assertEqual(test_result,1)

        test_result = Gates_refactored.XOR(1,1,1).output()
        self.assertEqual(test_result,0)

        # Testing POWER input:
        test_result = Gates_refactored.XOR(1,0,0).output()
        self.assertEqual(test_result,0)

    def test_XNOR(self):

        test_result = Gates_refactored.XNOR(0,0,1).output()
        self.assertEqual(test_result,1)

        test_result = Gates_refactored.XNOR(0,1,1).output()
        self.assertEqual(test_result,0)

        test_result = Gates_refactored.XNOR(1,0,1).output()
        self.assertEqual(test_result,0)

        test_result = Gates_refactored.XNOR(1,1,1).output()
        self.assertEqual(test_result,1)

        # Testing POWER input:
        test_result = Gates_refactored.XNOR(0,0,0).output()
        self.assertEqual(test_result,0)


    def test_MUX(self):

        test_result = Gates_refactored.MUX(0,0,0,1).output()
        self.assertEqual(test_result,0)

        test_result = Gates_refactored.MUX(0,1,0,1).output()
        self.assertEqual(test_result,0)

        test_result = Gates_refactored.MUX(1,0,0,1).output()
        self.assertEqual(test_result,1)

        test_result = Gates_refactored.MUX(1,1,0,1).output()
        self.assertEqual(test_result,1)


        test_result = Gates_refactored.MUX(0,0,1,1).output()
        self.assertEqual(test_result,0)

        test_result = Gates_refactored.MUX(0,1,1,1).output()
        self.assertEqual(test_result,1)

        test_result = Gates_refactored.MUX(1,0,1,1).output()
        self.assertEqual(test_result,0)

        test_result = Gates_refactored.MUX(1,1,1,1).output()
        self.assertEqual(test_result,1)

        #Testing POWER input:
        test_result = Gates_refactored.MUX(1,1,1,0).output()
        self.assertEqual(test_result,0)

    def test_DMUX(self):
        test_result = Gates_refactored.DMUX(0,0,1).output()
        self.assertEqual(test_result,[0,0])

        test_result = Gates_refactored.DMUX(0,1,1).output()
        self.assertEqual(test_result,[0,0])

        test_result = Gates_refactored.DMUX(1,0,1).output()
        self.assertEqual(test_result,[1,0])

        test_result = Gates_refactored.DMUX(1,1,1).output()
        self.assertEqual(test_result,[0,1])

        # Testing Power input;
        test_result = Gates_refactored.DMUX(1,0,0).output()
        self.assertEqual(test_result,[0,0])

        test_result = Gates_refactored.DMUX(1,1,0).output()
        self.assertEqual(test_result,[0,0])


   # Testing 16 Bit Variants

    def test_MUX16(self):

        test_result = Gates_refactored.Mux16([0,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1],[0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],0,1).output()
        self.assertEqual(test_result,[0,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1])

        test_result = Gates_refactored.Mux16([0,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1],[0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],1,1).output()
        self.assertEqual(test_result,[0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1])

        #Testing Power input;
        test_result = Gates_refactored.Mux16([0,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1],[0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1],0,0).output()
        self.assertEqual(test_result,[0]*16)

        test_result = Gates_refactored.Mux16([0,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1],[0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1],1,0).output()
        self.assertEqual(test_result,[0]*16)

    def test_AND16(self):
        # generating random inputs for the tests
        inputs = [gen_num(16),gen_num(16)]
        # print("\n\n inputs:",inputs,"\n\n")
        test_result = Gates_refactored.And16(inputs[0],inputs[1],Power=1).output()

        # comparing the results using built-in "and" operator
        self.assertEqual(test_result,andt(inputs[0],inputs[1]));

        test_result = Gates_refactored.And16(inputs[1],inputs[0],Power=1).output()
        #same but reversed inputs
        self.assertEqual(test_result,andt(inputs[0],inputs[1]));

        #testing Power input:
        test_result = Gates_refactored.And16(inputs[1],inputs[0],Power=0).output()
        self.assertEqual(test_result,[0]*16)

    def test_OR16(self):
        inputs = [gen_num(16),gen_num(16)]

        test_result = Gates_refactored.Or16(inputs[0],inputs[1],Power=1).output()
        self.assertEqual(test_result,ort(inputs[0],inputs[1]))

        test_result = Gates_refactored.Or16(inputs[1],inputs[0],Power=1).output()
        self.assertEqual(test_result,ort(inputs[0],inputs[1]))

        #testing Power input:
        test_result = Gates_refactored.Or16(inputs[1],inputs[0],Power=0).output()
        self.assertEqual(test_result,[0]*16)

    def test_NOT16(self):

        inp = gen_num(16)

        test_result = Gates_refactored.Not16(inp,1).output()
        self.assertEqual(test_result,nott(inp))

        test_result = Gates_refactored.Not16(inp,1).output()
        self.assertEqual(test_result,nott(inp))

        #testing Power input:
        test_result = Gates_refactored.Not16(inp,0).output()
        self.assertEqual(test_result,[0]*16)

    # NOw testing a to n Ways Gates/devices:

    def test_or8way(self):
        inp = gen_num(8)
        test_result = Gates_refactored.Or8Way(inp,Power=1).output()
        # print("testResult: ",test_result,"\ninp: ",inp)
        self.assertEqual(test_result,max(inp))

        #Regenerating new random input just for test
        inp = gen_num(8)
        test_result = Gates_refactored.Or8Way(inp,Power=1).output()
        self.assertEqual(test_result,max(inp))

        #testing Power input:
        test_result = Gates_refactored.Or8Way(inp,Power=0).output()
        self.assertEqual(test_result,0)

    def test_mux4way16(self):
        inp = [gen_num(16),gen_num(16),gen_num(16),gen_num(16),]

        test_result = Gates_refactored.Mux4Way16(inp[0],inp[1],inp[2],inp[3],S=[0,0],Power=1).output()
        self.assertEqual(test_result,inp[0])

        test_result = Gates_refactored.Mux4Way16(inp[0],inp[1],inp[2],inp[3],S=[0,1],Power=1).output()

        # print("\n inp: ",inp,"\n\ntest_result ",test_result)
        self.assertEqual(test_result,inp[1])

        test_result = Gates_refactored.Mux4Way16(inp[0],inp[1],inp[2],inp[3],S=[1,0],Power=1).output()
        self.assertEqual(test_result,inp[2])


        test_result = Gates_refactored.Mux4Way16(inp[0],inp[1],inp[2],inp[3],S=[1,1],Power=1).output()
        self.assertEqual(test_result,inp[3])

        #Testing Power input:
        test_result = Gates_refactored.Mux4Way16(inp[0],inp[1],inp[2],inp[3],S=[0,0],Power=0).output()
        self.assertEqual(test_result,[0]*16)

    def test_Mux8Way16(self):
        inp = [gen_num(16),gen_num(16),gen_num(16),gen_num(16),gen_num(16),gen_num(16),gen_num(16),gen_num(16),]

        test_result = Gates_refactored.Mux8Way16(inp[0],inp[1],inp[2],inp[3],inp[4],inp[5],inp[6],inp[7],S=[0,0,0],Power=1).output()
        self.assertEqual(test_result,inp[0])

        test_result = Gates_refactored.Mux8Way16(inp[0],inp[1],inp[2],inp[3],inp[4],inp[5],inp[6],inp[7],S=[0,0,1],Power=1).output()
        self.assertEqual(test_result,inp[1])

        test_result = Gates_refactored.Mux8Way16(inp[0],inp[1],inp[2],inp[3],inp[4],inp[5],inp[6],inp[7],S=[0,1,0],Power=1).output()
        self.assertEqual(test_result,inp[2])

        test_result = Gates_refactored.Mux8Way16(inp[0],inp[1],inp[2],inp[3],inp[4],inp[5],inp[6],inp[7],S=[0,1,1],Power=1).output()
        self.assertEqual(test_result,inp[3])

        test_result = Gates_refactored.Mux8Way16(inp[0],inp[1],inp[2],inp[3],inp[4],inp[5],inp[6],inp[7],S=[1,0,0],Power=1).output()
        self.assertEqual(test_result,inp[4])

        test_result = Gates_refactored.Mux8Way16(inp[0],inp[1],inp[2],inp[3],inp[4],inp[5],inp[6],inp[7],S=[1,0,1],Power=1).output()
        self.assertEqual(test_result,inp[5])

        test_result = Gates_refactored.Mux8Way16(inp[0],inp[1],inp[2],inp[3],inp[4],inp[5],inp[6],inp[7],S=[1,1,0],Power=1).output()
        self.assertEqual(test_result,inp[6])

        test_result = Gates_refactored.Mux8Way16(inp[0],inp[1],inp[2],inp[3],inp[4],inp[5],inp[6],inp[7],S=[1,1,1],Power=1).output()
        self.assertEqual(test_result,inp[7])

        #Testing Power input:
        test_result = Gates_refactored.Mux8Way16(inp[0],inp[1],inp[2],inp[3],inp[4],inp[5],inp[6],inp[7],S=[0,0,1],Power=0).output()
        self.assertEqual(test_result,[0]*16)

    def test_Dmux4Way(self):

        test_result = Gates_refactored.Dmux4Way(Input=1,S=[0,0],Power=1).output()
        self.assertEqual(test_result,[1,0,0,0])

        test_result = Gates_refactored.Dmux4Way(Input=1,S=[0,1],Power=1).output()
        self.assertEqual(test_result,[0,1,0,0])

        test_result = Gates_refactored.Dmux4Way(Input=1,S=[1,0],Power=1).output()
        self.assertEqual(test_result,[0,0,1,0])

        test_result = Gates_refactored.Dmux4Way(Input=1,S=[1,1],Power=1).output()
        self.assertEqual(test_result,[0,0,0,1])

        #Testing 0 as input:
        test_result = Gates_refactored.Dmux4Way(Input=0,S=[1,0],Power=1).output()
        self.assertEqual(test_result,[0,0,0,0])

        #Testing Power input:
        test_result = Gates_refactored.Dmux4Way(Input=1,S=[0,0],Power=0).output()
        self.assertEqual(test_result,[0,0,0,0])

    def test_Dmux8Way(self):

        test_result = Gates_refactored.DMux8Way(Input=1,S=[0,0,0],Power=1).output()
        self.assertEqual(test_result,[1,0,0,0,0,0,0,0])

        test_result = Gates_refactored.DMux8Way(Input=1,S=[0,0,1],Power=1).output()
        self.assertEqual(test_result,[0,1,0,0,0,0,0,0])

        test_result = Gates_refactored.DMux8Way(Input=1,S=[0,1,0],Power=1).output()
        self.assertEqual(test_result,[0,0,1,0,0,0,0,0])

        test_result = Gates_refactored.DMux8Way(Input=1,S=[0,1,1],Power=1).output()
        self.assertEqual(test_result,[0,0,0,1,0,0,0,0])

        test_result = Gates_refactored.DMux8Way(Input=1,S=[1,0,0],Power=1).output()
        self.assertEqual(test_result,[0,0,0,0,1,0,0,0])

        test_result = Gates_refactored.DMux8Way(Input=1,S=[1,0,1],Power=1).output()
        self.assertEqual(test_result,[0,0,0,0,0,1,0,0])

        test_result = Gates_refactored.DMux8Way(Input=1,S=[1,1,0],Power=1).output()
        self.assertEqual(test_result,[0,0,0,0,0,0,1,0])

        test_result = Gates_refactored.DMux8Way(Input=1,S=[1,1,1],Power=1).output()
        self.assertEqual(test_result,[0,0,0,0,0,0,0,1])

        #Testing Power input:
        test_result = Gates_refactored.DMux8Way(Input=1,S=[0,0,0],Power=0).output()
        self.assertEqual(test_result,[0,0,0,0,0,0,0,0])


# Testing ADDERS:
    def test_halfAdders(self):

        test_result = Gates_refactored.HalfAdder(input_a=0,input_b=0,Power=1).output()
        self.assertEqual(test_result,[0,0])

        test_result = Gates_refactored.HalfAdder(input_a=0,input_b=1,Power=1).output()
        self.assertEqual(test_result,[1,0])

        test_result = Gates_refactored.HalfAdder(input_a=1,input_b=0,Power=1).output()
        self.assertEqual(test_result,[1,0])

        test_result = Gates_refactored.HalfAdder(input_a=1,input_b=1,Power=1).output()
        self.assertEqual(test_result,[0,1])

        #Testing Power input:
        test_result = Gates_refactored.HalfAdder(input_a=0,input_b=1,Power=0).output()
        self.assertEqual(test_result,[0,0])

        test_result = Gates_refactored.HalfAdder(input_a=1,input_b=1,Power=0).output()
        self.assertEqual(test_result,[0,0])

    def test_FullAdder(self):

        test_result = Gates_refactored.FullAdder(input_a=0,input_b=0,c=0,Power=1).output()
        self.assertEqual(test_result,[0,0])

        test_result = Gates_refactored.FullAdder(input_a=0,input_b=1,c=0,Power=1).output()
        self.assertEqual(test_result,[1,0])

        test_result = Gates_refactored.FullAdder(input_a=1,input_b=0,c=0,Power=1).output()
        self.assertEqual(test_result,[1,0])

        test_result = Gates_refactored.FullAdder(input_a=1,input_b=1,c=0,Power=1).output()
        self.assertEqual(test_result,[0,1])

        #Testing Carry Bit
        test_result = Gates_refactored.FullAdder(input_a=0,input_b=0,c=1,Power=1).output()
        self.assertEqual(test_result,[1,0])

        test_result = Gates_refactored.FullAdder(input_a=0,input_b=1,c=1,Power=1).output()
        self.assertEqual(test_result,[0,1])

        test_result = Gates_refactored.FullAdder(input_a=1,input_b=0,c=1,Power=1).output()
        self.assertEqual(test_result,[0,1])

        test_result = Gates_refactored.FullAdder(input_a=1,input_b=1,c=1,Power=1).output()
        self.assertEqual(test_result,[1,1])

        #Testing Power input:
        test_result = Gates_refactored.FullAdder(input_a=1,input_b=0,c=0,Power=0).output()
        self.assertEqual(test_result,[0,0])

        test_result = Gates_refactored.FullAdder(input_a=0,input_b=1,c=1,Power=0).output()
        self.assertEqual(test_result,[0,0])

    def test_Adder16(self):

        rndinp_a = gen_num(16)
        rndinp_b = gen_num(16)

        rndinp_a = [0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0] #22850
        rndinp_b = [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1] #8881
        ans_aplusb = [0,1,1,1,1,0,1,1,1,1,1,1,0,0,1,1] # answer a+b = 22850 + 8881 = 31731

        test_result = Gates_refactored.Adder16(input_a=rndinp_a,input_b=rndinp_b,Power=1).output()
        self.assertEqual(test_result,ans_aplusb)

        # testing for operation with numrical overflow :-

        rndinp_a = [1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0] #41410
        rndinp_b = [1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0] #51504
        ans_aplusb = [0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0] #correct answer upto max bit length
        # answer a+b = 41410 + 51504 = 92914
        # true ans: 010110101011110010
        # our ans:    0110101011110010

        test_result = Gates_refactored.Adder16(input_a=rndinp_a,input_b=rndinp_b,Power=1).output()
        self.assertEqual(test_result,ans_aplusb)

        # testing Power input:

        # generating random input
        rndinp_a = gen_num(16)
        rndinp_b = gen_num(16)


        test_result = Gates_refactored.Adder16(input_a=rndinp_a,input_b=rndinp_b,Power=0).output()

        self.assertEqual(test_result,[0]*16)

    def test_Neg16(self):

        inp = [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1] # 13

        # as we know in 2's compliment it is negetive 13
        ans = [1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1] # 2^16 - 13 = 65536 - 13 = 65523

        # ans = [0,0,0,1,0,1,1,0,1,0,1,1,1,0,0,0]

        test_result = Gates_refactored.Neg16(inp,Power=1).output()
        self.assertEqual(test_result,ans)

        # inp = [1,0,1,0,0,1,0,1,1,1,0,0,1,0,1,0]
        # ans = nott(inp) #using premade function for testing not gate

        # test_result = Gates_refactored.Neg16(inp,Power=1).output()
        # self.assertEqual(test_result,ans)

        # testing Power input:
        test_result = Gates_refactored.Neg16(inp,Power=0).output()
        self.assertEqual(test_result,[0]*16)


# finally testing ALU

    def test_ALU(slef):
        pass


# Testing Memory

    def test_SRFlipFlop(self):

        test_result = Gates_refactored.SRFF(S=1,R=0,tm1_Q0=0,Power=1).output()
        self.assertEqual(test_result,[0,1])

        # test_result = Gates_refactored.SRFlipFlop(S=0,R=1,tm1_Q0=0,Power=1).output()
        # self.assertEqual(test_result,[1,0])

        test_result = Gates_refactored.SRFF(S=0,R=0,tm1_Q0=0,Power=1).output()
        self.assertEqual(test_result,[0,1])

        test_result = Gates_refactored.SRFF(S=1,R=1,tm1_Q0=0,Power=1).output()
        self.assertEqual(test_result,[0,1])


        test_result = Gates_refactored.SRFF(S=0,R=1,tm1_Q0=0,Power=1).output()
        self.assertEqual(test_result,[0,1])

        # testing by changing the time step

        # TIME = 0
        test_result = Gates_refactored.SRFF(S=0,R=1,tm1_Q0=0,Power=1)

        #TIME = 1 | updating State
        test_result.update(S=1,R=0)
        self.assertEqual(test_result.output(),[1,0])

        #TIME = 2 | updating State
        test_result.update(S=0,R=0)
        self.assertEqual(test_result.output(),[0,1])

        #TIME = 3 | updating State
        test_result.update(S=1,R=1)
        self.assertEqual(test_result.output(),[0,1]);

        #TIME = 4 | updating State
        test_result.update(S=1,R=0)
        self.assertEqual(test_result.output(),[0,1]);

        #TIME = 5 | updating State
        test_result.update(S=0,R=1)
        #Note: once it is haulted because of S=1 R=1 it can never recover back. so the output will always
        # going to be 0.
        self.assertEqual(test_result.output(),[0,1]);

        # When the previous States is S=1 R=0
        # instance_Sfirst = Gates_refactored.SRFlipFlop(S=1,R=0,Power=1)
        # instance_Sfirst.update(S=1,R=0)
        # test_result = instance_Sfirst.output()

        # self.assertEqual(test_result,[0,1])

        # instance_Sfirst = Gates_refactored.SRFlipFlop(S=1,R=0,Power=1)
        # instance_Sfirst.update(S=1,R=1)
        # test_result = instance_Sfirst.output()

        # self.assertEqual(test_result,[0,1])

        #When the previous State is S=0 R=1
        # instance_Rfirst = Gates_refactored.SRFlipFlop(S=0,R=1,Power=1)
        # instance_Rfirst.update(S=0,R=1)
        # test_result = instance_Rfirst.output()

        # self.assertEqual(test_result,[1,0])

        # instance_Rfirst = Gates_refactored.SRFlipFlop(S=0,R=1,Power=1)
        # instance_Rfirst.update(S=1,R=1)
        # test_result = instance_Rfirst.output()

        # self.assertEqual(test_result,[1,0])

        # #When the previous State is S=0 R=0

        # instance_Nofirst = Gates_refactored.SRFlipFlop(S=0,R=0,Power=1)
        # instance_Nofirst.update(S=1,R=0)
        # test_result = instance_Nofirst.output()

        # self.assertEqual(test_result,[1,1])




        #testing Power input:
        # test_result = Gates_refactored.SRFlipFlop(S=0,R=1,Power=0).output()
        # self.assertEqual(test_result,[0,0])


    # def Test_RAM8(self):

    #     test_result = Gates_refactored.RAM8(S=1,R=1,tm1_Q0=0,Power=1).output()
    #     self.assertEqual(test_result,[0,1])

    def test_ClockedDFF(self):
        # Working Perfectly! :D

        # now even when we turn off the clock the data still remain intact. which we can use in next time step
        #CLK HIGH
        test_result = Gates_refactored.Clocked_DFF(data=0,clock=1,Power=1)
        self.assertEqual(test_result.output(),[0,0])

        #CLK HIGH
        test_result.update(data=1,clock=1,Power=1)
        self.assertEqual(test_result.output(),[0,1])

        test_result.update(data=1,clock=0,Power=1)
        self.assertEqual(test_result.output(),[1,0])

        # # if the clock is down then there is no output hence "0"
        test_result.update(data=0,clock=0,Power=1)
        self.assertEqual(test_result.output(),[1,0])

        #CLK HIGH
        test_result.update(data=0,clock=1,Power=1)
        self.assertEqual(test_result.output(),[1,0])

        test_result.update(data=1,clock=0,Power=1)
        self.assertEqual(test_result.output(),[0,1])

        #CLK HIGH
        test_result.update(data=1,clock=1,Power=1)
        self.assertEqual(test_result.output(),[0,1])

    def test_Reg1Bit(self):

        #LOAD
        test_result = Gates_refactored.Reg1Bit(Input_1=1,Load=1,Power=1);
        self.assertEqual(test_result.output(),0);

        #value is loaded in the register
        test_result.update(Input=0,Load=0,Power=1);
        self.assertEqual(test_result.output(),1)

        #LOAD
        test_result.update(Input=0,Load=1,Power=1);
        self.assertEqual(test_result.output(),1)

        test_result.update(Input=0,Load=0,Power=1);
        self.assertEqual(test_result.output(),0)

    def test_Reg16(self):
        test_result = Gates_refactored.Reg16(Input=[0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],Load=1,Power=1)
        self.assertEqual(test_result.output(),[0]*16);

        test_result.update(Input=[0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],Load=0,Power=1);
        self.assertEqual(test_result.output(),[0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]);

        test_result.update(Input=[0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1],Load=0,Power=1)
        self.assertEqual(test_result.output(),[0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]);

    def test_Program_Counter(self):
        test_result = Gates_refactored.ProgramCounter(Input=[0]*16,load=0,inc=1,reset=0,Power=1);
        self.assertEqual(test_result.output(),[0]*16)

        # print("program_counter: ",test_result.value_1)

        tmpInput = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]
        test_result.update(Input=tmpInput,load=1,inc=0,reset=0,Power=1)
        self.assertEqual(test_result.output(),[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])

        # print("inside PC: ",test_result.mux16_3_4_r_5.output());

        test_result.update(Input=tmpInput,load=0,inc=1,reset=0,Power=1)
        self.assertEqual(test_result.output(),[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0])

        test_result.update(Input=tmpInput,load=0,inc=0,reset=1,Power=1)
        self.assertEqual(test_result.output(),[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1])

        test_result.update(Input=tmpInput,load=1,inc=0,reset=0,Power=1)
        self.assertEqual(test_result.output(),[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

        test_result.update(Input=tmpInput,load=0,inc=1,reset=1,Power=1)
        self.assertEqual(test_result.output(),[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0])

        test_result.update(Input=tmpInput,load=1,inc=1,reset=0,Power=1)
        self.assertEqual(test_result.output(),[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])

        test_result.update(Input=tmpInput,load=1,inc=1,reset=1,Power=1)
        self.assertEqual(test_result.output(),[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1])

        test_result.update(Input=tmpInput,load=1,inc=0,reset=0,Power=1)
        self.assertEqual(test_result.output(),[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])

    def test_RAM8(self):
        test_result = Gates_refactored.RAM8(Input=[0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1],address=[0,1,1],load=1,Power=1)
        test_result.update(Input=[1]*16,address=[0,0,1],load=0,Power=1)
        test_result.update(Input=[0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1],address=[0,0,0],load=1,Power=1)
        test_result.update(Input=[0]*16,address=[0,0,0],load=0,Power=1)
        # print("RAM8: ",test_result.output())

        # self.assertEqual(test_result.output(),[0]*16)
    
    def test_RAM64(self):
        # IT FUCKIN WORKS!!

        test_result = Gates_refactored.RAM64(Input=[0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0],address=[0,0,0,0,1,1],load=1,Power=1)
        test_result.update(Input=[1]*16,address=[1,1,1,1,1,1],load=1,Power=1)
        test_result.update(Input=[1]*16,address=[0,0,0,1,1,1],load=0,Power=1)
        test_result.update(Input=[0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0],address=[1,1,1,1,1,1],load=1,Power=1)
        test_result.update(Input=[0]*16,address=[0,0,0,0,1,0],load=0,Power=1)


        print("RAM64: ",test_result.output()[7][7])

        # self.assertEqual(test_result.output(),[0]*16)
        pass

    def test_RAM512(self):
        RAMindex = 5 
        add2put = dec2bin(RAMindex,9)
        print("dec2bin: ",add2put)
        test_result = Gates_refactored.RAM512(Input=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],address=[0,0,0,0,0,0,0,0,0],load=0,Power=1)
        test_result.update(Input=[1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],address=add2put,load=1,Power=1)
        test_result.update(Input=[1]*16,address=[0,0,0,0,0,0,1,1,1],load=0,Power=1)
        print("RAM512: ",len(test_result.output()[0][0][0]));

        for i in range(18):
            address = Gates_refactored.num2locN(i,512)
            print("this is RAM512: ",test_result.output()[address[0]][address[1]][address[2]])

        # test_result.update(Input=[0]*16,address=[0,0,0],load=0,Power=1)
        # self.assertEqual(test_result.output(),[0]*16)
        pass
    def test_RAM16K(self):
        # test_result = Gates_refactored.RAM16K(Input=[1]*16,address = [0]*15,load=1);
        # test_result.update(Input=[1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],address=[1]*15,load=1,Power=1)
        pass
        
        # print("RAM16K: ",len(test_result.output()[0]),(test_result.output()[0][0][0][0]));

    def test_ALU(self):
        # input_1 = [0,0,1,1,1,1,0,1,0,1,0,0,0,1,0,1]
        # input_2 = [0,0,1,0,1,1,1,0,1,1,1,0,0,0,0,0]

        # print("dec2bin: ",dec2bin(17,16) );

        # addit = Gates_refactored.Adder16(input_1,input_2,Power=1);
        # print("add: ",addit.output());

        # ctrl_bits = [0,1,0,1,1,1]

        # test_result = Gates_refactored.ALU(input_1,input_2,ctrl_bits[0],ctrl_bits[1],ctrl_bits[2],ctrl_bits[3],ctrl_bits[4],ctrl_bits[5])
        # print("dec:" ,bin2dec(test_result.output()["out"]))
        # print(test_result.output());
        pass


    def test_CPU(self):
        # # read instruction from program
        # program = open("Assembler/program2.out","rt");

        # # Converting file lines to bits array
        # plines = [] #program Lines
        # for line in program:
        #     Iin = [];
        #     for bit in line:
        #         if (bit != "\n"):
        #             Iin.append(int(bit)) 
        #     plines.append(Iin);



        # Iin = plines[0];# Current Instruction
        # Min = [0]*16;
        # reset = 0;

        # print(Iin);
        # test_result = Gates_refactored.CPU(Iin,Min,reset=0)
        # print("\nCENTRAL PROCESSING UNIT OUTPUT:",test_result.output(),"\n");

        # Iin = plines[1];
        # # Min = 
        # test_result.update(Iin,Min,reset);
        # print("\nCENTRAL PROCESSING UNIT OUTPUT:",test_result.output(),"\n");

        # test_result.update(Iin,Min,reset);
        # print("\nCENTRAL PROCESSING UNIT OUTPUT:",test_result.output(),"\n");

    # def test_Computer(self):
    #     pass

        #Testing Computer!!:-
        # test_result = Gates_refactored.Computer();

        # print(test_result.output())

        # test_result.update();
        # print(test_result.output())

        # test_result.update();
        # print(test_result.output())

        # test_result.update();
        # print(test_result.output())


        # test_result.update();
        # print(test_result.output())
        # test_result = 0
        pass
def int2binary(n):
    pass

if __name__ =='__main__':
    unittest.main()
    # Gates_refactored.Reg1Bit(Input_1=1,Load=1,Power=1);
