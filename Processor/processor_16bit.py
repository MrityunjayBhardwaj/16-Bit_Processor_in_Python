
from math import floor
from math import ceil

# Creating the gates from Scratch:

# the focus is both in the Interface level and implementation level
# Transistors:

def num2loc(n):
    return [floor(n/(4096)),floor(n/512),floor(n/64),floor(n/8),(n%8) ]
    pass

def num2locN(n,k):
    # n = number in decimal
    # r = number of ram parts
    # k = ram size
    loc = []
    w = k/8
    while w >= 8:
        loc.append(floor(n/(w)))
        w = w/8
    loc.append(n%8)
    return loc

def bin2dec(bin):
    val =0;
    for i in range(len(bin)):
        val += bin[(len(bin)-1)-i]*(2**i);
    return val


MasterClock = 1


class Transistor:
    """
    Transistors are the basic building block of any electrical appliances that we see today...
    you can learn more about transistors here:- https://en.wikipedia.org/wiki/Transistor
    and video explaination: https://www.youtube.com/watch?v=VBDoT8o4q00
    as you can see transistors consist of 3 pins 2 input pins and 1 output pins.
    so input :

        POWER supply (Source)
        GATE (main on and off Switch)

        Out:
            Output (Drain) which gives us 0 and 1 according to our inputs.
    """

    # transistor id:
    transistor_id = -1

    def __init__(self,Switch,Power=1):
        # Bydefault source is always set to 1 i.e, power suppply is always on!
        #00 = 0 10 = 0 01= 0 11 = 1

        self.switch = Switch
        self.power  = Power
        self.output_value =  self.power*self.switch

        Transistor.transistor_id += 1

    def output(self):
        # TT : 00 = 0 01 = 0 10 = 0 11 = 1
        return self.output_value


    def __repr__(self):
        return ('{self.__class__.__name__}');


class NAND():

    """
    Truth_Table
    00 = 1
    01 = 1
    10 = 1
    11 = 0


    """

    nand_id = -1

    def __init__(self,Switch_0,Switch_1,Power=1):
        # Creating 2 transisors:
        self.tr_s0_0 = Transistor(Switch_0,Power)
        self.tr_s1_1 = Transistor(Switch_1,self.tr_s0_0.output())

        self.output_value  = (1-self.tr_s1_1.output())*Power

        NAND.nand_id += 1

    def output(self):
        # because the source of tr_1 is (__connected-to__ ) the output of tr_0.
        return self.output_value

class NOT:

    """
    Truth_Table
    0 = 1
    1 = 0
    """
    not_gt_id= -1

    def __init__(self,Switch,Power=1):
        self.NAND_s_s_0 = NAND(Switch,Switch,Power)
        self.output_value = self.NAND_s_s_0.output()


    def output(self):
        return self.output_value

class AND():
    """
    Truth_Table
    00 = 0
    01 = 0
    10 = 0
    11 = 1

    """
    and_id = -1

    def __init__(self,Switch_0,Switch_1,Power=1):

        self.NAND_s0_s1_0 = NAND(Switch_0,Switch_1,Power)
        self.NOT_0_1 = NOT(self.NAND_s0_s1_0.output(),Power)

        self.output_value = self.NOT_0_1.output()
        AND.and_id += 1

    def output(self):
        # because the source of tr_1 is (__connected-to__ ) the output of tr_0.
        return self.output_value

class OR():
    """
    Truth_Table
    00 = 0
    01 = 1
    10 = 1
    11 = 1

    """
    or_id = -1

    def __init__(self,Switch_0,Switch_1,Power=1):
        # Creating 2 transisors:
        self.NOT_s0_0   = NOT(Switch_0,Power)
        self.NOT_s1_1   = NOT(Switch_1,Power)
        self.NAND_0_1_2  = NAND(self.NOT_s0_0.output(),self.NOT_s1_1.output(),Power)

        self.output_value = self.NAND_0_1_2.output()
        OR.or_id += 1

    def output(self):
        return self.output_value

class NOR():
    """
    Truth_Table
    00 = 1
    01 = 0
    10 = 0
    11 = 0
    """

    nor_id = -1

    def __init__(self,Switch_0,Switch_1,Power=1):
        # Creating 2 transisors:
        self.NOT_s0_0     = NOT (Switch_0,Power)
        self.NOT_s1_1     = NOT (Switch_1,Power)
        self.NAND_0_1_2   = NAND(self.NOT_s0_0.output(),self.NOT_s1_1.output(),Power)
        self.NOT_2_3      = NOT(self.NAND_0_1_2.output(),Power)

        self.output_value = self.NOT_2_3.output()
        NOR.nor_id += 1

    def output(self):
        return self.output_value


class XOR():
    """
    Truth_Table
    00 = 0
    01 = 1
    10 = 1
    11 = 0
    """

    xor_id = -1

    def __init__(self,Switch_0,Switch_1,Power=1):
        # Creating 2 transisors:
        self.NAND_s0_s1_0 = NAND(Switch_0,Switch_1,Power)
        self.NAND_s0_0_1 = NAND(Switch_0,self.NAND_s0_s1_0.output(),Power)
        self.NAND_0_s1_2 = NAND(self.NAND_s0_s1_0.output(),Switch_1,Power)
        self.NAND_2_1_3 = NAND(self.NAND_0_s1_2.output(),self.NAND_s0_0_1.output(),Power)

        self.output_value = self.NAND_2_1_3.output()
        XOR.xor_id += 1

    def output(self):
        return self.output_value


class XNOR():
    """
    Truth_Table
    00 = 1
    01 = 0
    10 = 0
    11 = 1

    """


    xnor_id = -1

    def __init__(self,Switch_0,Switch_1,Power=1):
        # Creating 2 transisors:
        self.NAND_s0_s1_0 = NAND(Switch_0,Switch_1,Power)
        self.NAND_s0_0_1 = NAND(Switch_0,self.NAND_s0_s1_0.output(),Power)
        self.NAND_0_s1_2 = NAND(self.NAND_s0_s1_0.output(),Switch_1,Power)
        self.NAND_2_1_3 = NAND(self.NAND_0_s1_2.output(),self.NAND_s0_0_1.output(),Power)
        self.NOR_3_4  = NOT(self.NAND_2_1_3.output(),Power)

        self.output_value = self.NOR_3_4.output()

        XNOR.xnor_id += 1

    def output(self):
        return self.output_value

class MUX():
    """
    Take 2 inputs and one switch, which decide which input should be taken as output

                Truth_Table
       Input      Selection_bit   Output
      A  |  B

      0     0        0             0
      0     1        0             0
      1     0        0             1
      1     1        0             1

      0     0        1             0
      0     1        1             1
      1     0        1             0
      1     1        1             1

    """

    mux_id = -1

    def __init__(self,Input_0,Input_1,Selection_bit,Power=1):

        self.NOT_sb_0  = NOT(Selection_bit,Power)

        self.AND_sb_i1_1 = AND(Selection_bit,Input_1,Power)
        self.AND_sb_i0_2 = AND(self.NOT_sb_0.output(),Input_0,Power)

        self.OR_1_2_3  = OR(self.AND_sb_i1_1.output(),self.AND_sb_i0_2.output())

        self.output_value = self.OR_1_2_3.output()

        MUX.mux_id += 1

    def output(self):
        return self.output_value

class DMUX():

    """

    DMUX is the complement of MUX i.e, it takes 1 input and 1 switch which decide to which output this input should go

    Truth_Table
    S     out
    0 = input_0
    1 = input_1

    """

    dmux_id = -1

    def __init__(self,Input,Selection_bit,Power=1):
        # Creating 2 transisors:
        self.NOT_sb_0   = NOT(Selection_bit,Power)

        self.AND_sb_i_1   = AND(Selection_bit,Input,Power)
        self.AND_0_i_2   = AND(self.NOT_sb_0.output(),Input,Power)

        self.output_value = [self.AND_0_i_2.output(),self.AND_sb_i_1.output()]

        DMUX.dmux_id += 1

    def output(self):
        return self.output_value


# 16 Bit Variants:

class Mux16():
    """
    this mux takes 16bit data as input and give 16bit as well it has 1 switcher
    for indepth MUX:
    http://www.zeepedia.com/read.php%3F2-input_4-bit_multiplexer_8_16-input_multiplexer_logic_function_generator_digital_logic_design%26b%3D9%26c%3D18

    """

    mux16_id = -1

    def __init__(self,Input_a,Input_b,Selection_bit,Power=1):
        # Using the basic  multiplexer layout for all the bits
        #self.NOT_0  = NOT(Selection_bit,Power)

        #self.NAND_1 = NAND(Input_0,Selection_bit,Power)
        #self.NAND_2 = NAND(self.NOT_0.output(),Input_1,Power)

        #self.NAND_3 = NAND(self.NAND_1.output(),self.NAND_2.output(),Power)

        # Using AND OR gates
        self.output_value     = []

        Selection_bit    = 1- Selection_bit
        self.AND_P_S_0   = AND(Power,Selection_bit)
        self.NOT_S_1     = NOT(Selection_bit)

        self.AND_1_P_2   = AND(self.NOT_S_1.output(),Power)

        self.AND_0_Ia0_3 = AND(self.AND_P_S_0.output(),Input_a[0])
        self.AND_2_Ib0_4 = AND(self.AND_1_P_2.output(),Input_b[0])

        self.OR_3_4_5    = OR(self.AND_0_Ia0_3.output(),self.AND_2_Ib0_4.output())


        self.output_value.append(self.OR_3_4_5.output())

        self.AND_0_Ia1_6 = AND(self.AND_P_S_0.output(),Input_a[1])
        self.AND_2_Ib1_7 = AND(self.AND_1_P_2.output(),Input_b[1])

        self.OR_6_7_8 = OR(self.AND_0_Ia1_6.output(),self.AND_2_Ib1_7 .output())
        self.output_value.append(self.OR_6_7_8.output())

        self.AND_0_Ia2_9 = AND(self.AND_P_S_0.output(),Input_a[2])
        self.AND_2_Ib2_10 = AND(self.AND_1_P_2.output(),Input_b[2])

        self.OR_9_10_11 = OR(self.AND_0_Ia2_9.output(),self.AND_2_Ib2_10 .output())
        self.output_value.append(self.OR_9_10_11.output())

        self.AND_0_Ia3_12 = AND(self.AND_P_S_0.output(),Input_a[3])
        self.AND_2_Ib3_13 = AND(self.AND_1_P_2.output(),Input_b[3])

        self.OR_12_13_14 = OR(self.AND_0_Ia3_12.output(),self.AND_2_Ib3_13 .output())
        self.output_value.append(self.OR_12_13_14.output())

        self.AND_0_Ia4_15 = AND(self.AND_P_S_0.output(),Input_a[4])
        self.AND_2_Ib4_16 = AND(self.AND_1_P_2.output(),Input_b[4])

        self.OR_15_16_17 = OR(self.AND_0_Ia4_15.output(),self.AND_2_Ib4_16 .output())
        self.output_value.append(self.OR_15_16_17.output())

        self.AND_0_Ia5_18 = AND(self.AND_P_S_0.output(),Input_a[5])
        self.AND_2_Ib5_19 = AND(self.AND_1_P_2.output(),Input_b[5])

        self.OR_18_19_20 = OR(self.AND_0_Ia5_18.output(),self.AND_2_Ib5_19 .output())
        self.output_value.append(self.OR_18_19_20.output())

        self.AND_0_Ia6_21 = AND(self.AND_P_S_0.output(),Input_a[6])
        self.AND_2_Ib6_22 = AND(self.AND_1_P_2.output(),Input_b[6])

        self.OR_21_22_23 = OR(self.AND_0_Ia6_21.output(),self.AND_2_Ib6_22 .output())
        self.output_value.append(self.OR_21_22_23.output())

        self.AND_0_Ia7_24 = AND(self.AND_P_S_0.output(),Input_a[7])
        self.AND_2_Ib7_25 = AND(self.AND_1_P_2.output(),Input_b[7])

        self.OR_24_25_26 = OR(self.AND_0_Ia7_24.output(),self.AND_2_Ib7_25 .output())
        self.output_value.append(self.OR_24_25_26.output())

        self.AND_0_Ia8_27 = AND(self.AND_P_S_0.output(),Input_a[8])
        self.AND_2_Ib8_28 = AND(self.AND_1_P_2.output(),Input_b[8])

        self.OR_27_28_29 = OR(self.AND_0_Ia8_27.output(),self.AND_2_Ib8_28 .output())
        self.output_value.append(self.OR_27_28_29.output())

        self.AND_0_Ia9_30 = AND(self.AND_P_S_0.output(),Input_a[9])
        self.AND_2_Ib9_31 = AND(self.AND_1_P_2.output(),Input_b[9])

        self.OR_30_31_32 = OR(self.AND_0_Ia9_30.output(),self.AND_2_Ib9_31 .output())
        self.output_value.append(self.OR_30_31_32.output())

        self.AND_0_Ia10_33 = AND(self.AND_P_S_0.output(),Input_a[10])
        self.AND_2_Ib10_34 = AND(self.AND_1_P_2.output(),Input_b[10])

        self.OR_33_34_35 = OR(self.AND_0_Ia10_33.output(),self.AND_2_Ib10_34 .output())
        self.output_value.append(self.OR_33_34_35.output())

        self.AND_0_Ia11_36 = AND(self.AND_P_S_0.output(),Input_a[11])
        self.AND_2_Ib11_37 = AND(self.AND_1_P_2.output(),Input_b[11])

        self.OR_36_37_38 = OR(self.AND_0_Ia11_36.output(),self.AND_2_Ib11_37 .output())
        self.output_value.append(self.OR_36_37_38.output())

        self.AND_0_Ia12_39 = AND(self.AND_P_S_0.output(),Input_a[12])
        self.AND_2_Ib12_40 = AND(self.AND_1_P_2.output(),Input_b[12])

        self.OR_39_40_41 = OR(self.AND_0_Ia12_39.output(),self.AND_2_Ib12_40 .output())
        self.output_value.append(self.OR_39_40_41.output())

        self.AND_0_Ia13_42 = AND(self.AND_P_S_0.output(),Input_a[13])
        self.AND_2_Ib13_43 = AND(self.AND_1_P_2.output(),Input_b[13])

        self.OR_42_43_44 = OR(self.AND_0_Ia13_42.output(),self.AND_2_Ib13_43 .output())
        self.output_value.append(self.OR_42_43_44.output())

        self.AND_0_Ia14_45 = AND(self.AND_P_S_0.output(),Input_a[14])
        self.AND_2_Ib14_46 = AND(self.AND_1_P_2.output(),Input_b[14])

        self.OR_45_46_47 = OR(self.AND_0_Ia14_45.output(),self.AND_2_Ib14_46 .output())
        self.output_value.append(self.OR_45_46_47.output())

        self.AND_0_Ia15_48 = AND(self.AND_P_S_0.output(),Input_a[15])
        self.AND_2_Ib15_49 = AND(self.AND_1_P_2.output(),Input_b[15])

        self.OR_48_49_50 = OR(self.AND_0_Ia15_48.output(),self.AND_2_Ib15_49 .output())
        self.output_value.append(self.OR_48_49_50.output())

        Mux16.mux16_id += 1
        # print("this is inp:",Input_b)

    def output(self):

        # print("this is self.output_value:",self.output_value)
        return self.output_value

class And16():
    """
    Truth_Table

    00 = 0
    01 = 0
    10 = 0
    11 = 1

    """
    and16_id = -1

    def __init__(self,input_a,input_b,Power=1):

        self.output_value = []

        self.AND_0 = AND(input_a[0],input_b[0],Power)
        self.output_value.append(self.AND_0.output())

        self.AND_1 = AND(input_a[1],input_b[1],Power)
        self.output_value.append(self.AND_1.output())

        self.AND_2 = AND(input_a[2],input_b[2],Power)
        self.output_value.append(self.AND_2.output())

        self.AND_3 = AND(input_a[3],input_b[3],Power)
        self.output_value.append(self.AND_3.output())

        self.AND_4 = AND(input_a[4],input_b[4],Power)
        self.output_value.append(self.AND_4.output())

        self.AND_5 = AND(input_a[5],input_b[5],Power)
        self.output_value.append(self.AND_5.output())

        self.AND_6 = AND(input_a[6],input_b[6],Power)
        self.output_value.append(self.AND_6.output())

        self.AND_7 = AND(input_a[7],input_b[7],Power)
        self.output_value.append(self.AND_7.output())

        self.AND_8 = AND(input_a[8],input_b[8],Power)
        self.output_value.append(self.AND_8.output())

        self.AND_9 = AND(input_a[9],input_b[9],Power)
        self.output_value.append(self.AND_9.output())

        self.AND_10 = AND(input_a[10],input_b[10],Power)
        self.output_value.append(self.AND_10.output())

        self.AND_11 = AND(input_a[11],input_b[11],Power)
        self.output_value.append(self.AND_11.output())

        self.AND_12 = AND(input_a[12],input_b[12],Power)
        self.output_value.append(self.AND_12.output())

        self.AND_13 = AND(input_a[13],input_b[13],Power)
        self.output_value.append(self.AND_13.output())

        self.AND_14 = AND(input_a[14],input_b[14],Power)
        self.output_value.append(self.AND_14.output())

        self.AND_15 = AND(input_a[15],input_b[15],Power)
        self.output_value.append(self.AND_15.output())

        self.and16_id += 1

    def output(self):
        # because the source of tr_1 is (__connected-to__) the output of tr_0.
        return self.output_value



class Or16:
    def __init__(self,input_a,input_b,Power):
        self.output_value = []

        self.OR_0 = OR(input_a[0],input_b[0],Power)
        self.output_value.append(self.OR_0.output())


        self.OR_1 = OR(input_a[1],input_b[1],Power)
        self.output_value.append(self.OR_1.output())

        self.OR_2 = OR(input_a[2],input_b[2],Power)
        self.output_value.append(self.OR_2.output())

        self.OR_3 = OR(input_a[3],input_b[3],Power)
        self.output_value.append(self.OR_3.output())

        self.OR_4 = OR(input_a[4],input_b[4],Power)
        self.output_value.append(self.OR_4.output())

        self.OR_5 = OR(input_a[5],input_b[5],Power)
        self.output_value.append(self.OR_5.output())

        self.OR_6 = OR(input_a[6],input_b[6],Power)
        self.output_value.append(self.OR_6.output())

        self.OR_7 = OR(input_a[7],input_b[7],Power)
        self.output_value.append(self.OR_7.output())

        self.OR_8 = OR(input_a[8],input_b[8],Power)
        self.output_value.append(self.OR_8.output())

        self.OR_9 = OR(input_a[9],input_b[9],Power)
        self.output_value.append(self.OR_9.output())

        self.OR_10 = OR(input_a[10],input_b[10],Power)
        self.output_value.append(self.OR_10.output())

        self.OR_11 = OR(input_a[11],input_b[11],Power)
        self.output_value.append(self.OR_11.output())

        self.OR_12 = OR(input_a[12],input_b[12],Power)
        self.output_value.append(self.OR_12.output())

        self.OR_13 = OR(input_a[13],input_b[13],Power)
        self.output_value.append(self.OR_13.output())

        self.OR_14 = OR(input_a[14],input_b[14],Power)
        self.output_value.append(self.OR_14.output())

        self.OR_15 = OR(input_a[15],input_b[15],Power)
        self.output_value.append(self.OR_15.output())

    def output(self):
        return self.output_value


class Not16:
    def __init__(self,Input,Power=1):

        self.output_value = []

        self.NOT_0 = NOT(Input[0],Power)
        self.output_value.append(self.NOT_0.output())

        self.NOT_1 = NOT(Input[1],Power)
        self.output_value.append(self.NOT_1.output())

        self.NOT_2 = NOT(Input[2],Power)
        self.output_value.append(self.NOT_2.output())

        self.NOT_3 = NOT(Input[3],Power)
        self.output_value.append(self.NOT_3.output())

        self.NOT_4 = NOT(Input[4],Power)
        self.output_value.append(self.NOT_4.output())

        self.NOT_5 = NOT(Input[5],Power)
        self.output_value.append(self.NOT_5.output())

        self.NOT_6 = NOT(Input[6],Power)
        self.output_value.append(self.NOT_6.output())

        self.NOT_7 = NOT(Input[7],Power)
        self.output_value.append(self.NOT_7.output())

        self.NOT_8 = NOT(Input[8],Power)
        self.output_value.append(self.NOT_8.output())

        self.NOT_9 = NOT(Input[9],Power)
        self.output_value.append(self.NOT_9.output())

        self.NOT_10 = NOT(Input[10],Power)
        self.output_value.append(self.NOT_10.output())

        self.NOT_11 = NOT(Input[11],Power)
        self.output_value.append(self.NOT_11.output())

        self.NOT_12 = NOT(Input[12],Power)
        self.output_value.append(self.NOT_12.output())

        self.NOT_13 = NOT(Input[13],Power)
        self.output_value.append(self.NOT_13.output())

        self.NOT_14 = NOT(Input[14],Power)
        self.output_value.append(self.NOT_14.output())

        self.NOT_15 = NOT(Input[15],Power)
        self.output_value.append(self.NOT_15.output())

    def output(self):
        return self.output_value





# Creating multi-way version of digital Logic Gates
class Or8Way:
    """
    in:  in[8]
    out: out

    if any input bit is 1 then it return 1 otherwise 0

    """
    or8way_id = -1

    def __init__(self,Input,Power=1):

        self.output_value = 0

        self.OR_I0_I1_0 = OR(Input[0],Input[1],Power)
        self.OR_I2_I3_1 = OR(Input[2],Input[3],Power)
        self.OR_I4_I5_2 = OR(Input[4],Input[5],Power)
        self.OR_I6_I7_3 = OR(Input[6],Input[7],Power)

        self.OR_0_1_4 = OR(self.OR_I0_I1_0.output(),self.OR_I2_I3_1.output())
        self.OR_2_3_5 = OR(self.OR_I4_I5_2.output(),self.OR_I6_I7_3.output())

        self.OR_4_5_6 = OR(self.OR_0_1_4.output(),self.OR_2_3_5.output())

        self.output_value = self.OR_4_5_6.output()
        Or8Way.or8way_id +=1

    def output(self):
        return self.output_value

class Mux4Way16:
    """
    in: a[16],b[16],c[16],d[16]   Selection_bit = s[2]
    out: out[16]
    func: Select one output out of 4 inputs using selection bit

    TT:
    s[1] s[0]  out
     0    0     a
     0    1     b
     1    0     c
     1    1     d
    """

    mux4way16_id = -1

    def __init__(self,input_a,input_b,input_c,input_d,S,Power=1):
        self.MUX_Ia_Ib_S0_0 = Mux16(input_a,input_b,S[1],Power)
        self.MUX_Ic_Id_S0_1 = Mux16(input_c,input_d,S[1],Power)

        self.MUX_0_1_S1_2   = Mux16(self.MUX_Ia_Ib_S0_0.output(),self.MUX_Ic_Id_S0_1.output(),S[0],Power)

        self.output_value = self.MUX_0_1_S1_2.output()

        Mux4Way16.mux4way16_id +=1

    def output(self):
        return self.output_value


class Mux8Way16:
    """
    in: a[16],b[16],c[16],d[16],e[16],f[16],g[16],h[16]   Selection_bits = s[3]
    out: out[16]
    func: Select one output,out of 8 inputs using selection bit

    TT:
    s[2] s[1] s[0] out
     0    0    0    a
     0    0    1    b
     0    1    0    c
     0    1    1    d
     1    0    0    e
     1    0    1    f
     1    1    0    g
     1    1    1    h
    """

    mux8way16_id = -1

    def __init__(self,input_a,input_b,input_c,input_d,input_e,input_f,input_g,input_h,S,Power=1):

        self.MUX4way_Ia_Ib_Ic_Id_S01_0 = Mux4Way16(input_a,input_b,input_c,input_d,[S[1],S[2]],Power)
        self.MUX4way_Ie_If_Ig_Ih_S01_1 = Mux4Way16(input_e,input_f,input_g,input_h,[S[1],S[2]],Power)

        # print("\nfrom mux8: ",self.MUX4way_Ia_Ib_Ic_Id_S01_0.output(),self.MUX4way_Ie_If_Ig_Ih_S01_1.output())
        self.MUX_0_1_2 = Mux16(self.MUX4way_Ia_Ib_Ic_Id_S01_0.output(),self.MUX4way_Ie_If_Ig_Ih_S01_1.output(),S[0],Power)

        self.output_value = self.MUX_0_1_2.output()

        Mux8Way16.mux8way16_id +=1

    def output(self):
        return self.output_value



class Dmux4Way:
    """
    in: inp
    Selection_bits = s[2]
    out: a,b,c,d
    func: It channels one 1-bit input into 8 1-bit output using Selection bits

    """
    dmux4way_id = -1

    def __init__(self,Input,S,Power=1):

        self.DMUX_I_S0_0 = DMUX(Input,S[1],Power)
        # print("DMUX: ",self.DMUX_I_S0_0.output())
        self.NOT_S_2     = NOT(S[1],Power)

        # Always return 0
        self.MUX_00_01_3    = MUX(self.DMUX_I_S0_0.output()[0],self.DMUX_I_S0_0.output()[1],self.NOT_S_2.output())
        self.MUX_00_3_S1_4  = MUX(self.DMUX_I_S0_0.output()[0],self.MUX_00_01_3.output(),S[0],Power)
        self.MUX_01_3_S1_5  = MUX(self.DMUX_I_S0_0.output()[1],self.MUX_00_01_3.output(),S[0],Power)
        self.MUX_3_00_S1_6  = MUX(self.MUX_00_01_3.output(),self.DMUX_I_S0_0.output()[0],S[0],Power)
        self.MUX_3_01_S1_7  = MUX(self.MUX_00_01_3.output(),self.DMUX_I_S0_0.output()[1],S[0],Power)

        self.output_value   = [self.MUX_00_3_S1_4.output(),self.MUX_01_3_S1_5.output(),self.MUX_3_00_S1_6.output(),self.MUX_3_01_S1_7.output()]
        Dmux4Way.dmux4way_id +=1

    def output(self):
        return self.output_value

class DMux8Way:
    """
    in: inp Selection_bits = [3]
    out:a,b,c,d,e,f,g,h
    func: It channels one 1-bit input into 8 1-bit output using Selection bits
    """

    dmux8way_id = -1
    def __init__(self,Input,S,Power=1):
        self.Dmux4Way_I_S01_0 = Dmux4Way(Input,[S[1],S[2]],Power)

        self.dummyBit_1       = 0

        # creating 4 bits of empty data [0,0,0,0]
        self.Dmux4Way_I_S01_2 = Dmux4Way(self.dummyBit_1,[S[1],S[2]],Power)

        # first 4 bits(a,b,c,d) selection using s[2]
        self.MUX_00_20_S2_3  = MUX(self.Dmux4Way_I_S01_0.output()[0],self.Dmux4Way_I_S01_2.output()[0],S[0],Power)
        self.MUX_01_21_S2_4  = MUX(self.Dmux4Way_I_S01_0.output()[1],self.Dmux4Way_I_S01_2.output()[1],S[0],Power)
        self.MUX_02_22_S2_5  = MUX(self.Dmux4Way_I_S01_0.output()[2],self.Dmux4Way_I_S01_2.output()[2],S[0],Power)
        self.MUX_03_23_S2_6  = MUX(self.Dmux4Way_I_S01_0.output()[3],self.Dmux4Way_I_S01_2.output()[3],S[0],Power)



        # last 4 bits (e,f,g,h)
        self.MUX_20_00_S2_7  = MUX(self.Dmux4Way_I_S01_2.output()[0],self.Dmux4Way_I_S01_0.output()[0],S[0],Power)
        self.MUX_21_01_S2_8  = MUX(self.Dmux4Way_I_S01_2.output()[1],self.Dmux4Way_I_S01_0.output()[1],S[0],Power)
        self.MUX_22_02_S2_9  = MUX(self.Dmux4Way_I_S01_2.output()[2],self.Dmux4Way_I_S01_0.output()[2],S[0],Power)
        self.MUX_23_03_S2_10  = MUX(self.Dmux4Way_I_S01_2.output()[3],self.Dmux4Way_I_S01_0.output()[3],S[0],Power)



        #output = [a,b,c,d,e,f,g,h]
        self.output_value = [self.MUX_00_20_S2_3.output(),self.MUX_01_21_S2_4.output(),self.MUX_02_22_S2_5.output(),self.MUX_03_23_S2_6.output(),self.MUX_20_00_S2_7.output(),self.MUX_21_01_S2_8.output(),self.MUX_22_02_S2_9.output(),self.MUX_23_03_S2_10.output()]

        # id
        DMux8Way.dmux8way_id +=1

    def output(self):
            return self.output_value


# now creating ADDERS!!!


# half-adder
class HalfAdder:
    """
    in: a,b
    out: [sum,carry]
    func: add a and b and store the carry bit

    TT:
        a   b   sum    carry
        0   0    0      0
        0   1    1      0
        1   0    1      0
        1   1    0      1

    ComponentUsed: XOR and AND gate
    """

    halfadder_id = -1

    def __init__(self,input_a,input_b,Power=1):
        self.xor_ia_ib_0 = XOR(input_a,input_b,Power)
        self.and_ia_ib_1 = AND(input_a,input_b,Power)

        self.output_value = [self.xor_ia_ib_0.output(),self.and_ia_ib_1.output()]

        HalfAdder.halfadder_id +=1

    def output(self):
        return self.output_value

#full Adder
class FullAdder:
    """
    in: a,b,c(carry bit from previous place addition)
    out: [sum,carrybit]
    func: add a and b and also take the carry bit from prebious operation into account for calculation

    TT:
        a   b   c  sum carry
        0   0   0   0   0
        0   1   0   1   0
        1   0   0   1   0
        1   1   0   0   1
        0   0   1   1   0
        0   1   1   0   1
        1   0   1   0   1
        1   1   1   1   1

        0   0   0   0   0
        0   0   1   1   0
        0   1   0   1   0
        0   1   1   0   1
        1   0   0   1   0
        1   0   1   0   1
        1   1   0   0   1
        1   1   1   1   1
    """

    fulladder_id = -1

    def __init__(self,input_a,input_b,c,Power=1):
        self.halfadder_ia_ib_0 = HalfAdder(input_a,input_b,Power)
        self.halfadder_c_00_1   = HalfAdder(c,self.halfadder_ia_ib_0.output()[0],Power)
        self.or_11_01 = OR(self.halfadder_ia_ib_0.output()[1],self.halfadder_c_00_1.output()[1],Power)

        self.output_value = [self.halfadder_c_00_1.output()[0],self.or_11_01.output()]

        FullAdder.fulladder_id +=1


    def output(self):
        return self.output_value



class Adder16:
    """
    """

    adder16_id = -1

    def __init__(self,input_a,input_b,Power):
        self.output_value = []

        self.halfadder_ia15_ib15_0 = HalfAdder(input_a[15],input_b[15],Power)
        self.output_value.append(self.halfadder_ia15_ib15_0.output()[0])

        # self.fulladder_ia14_ib14_01_1 = FullAdder(input_a[14],input_b[14],self.halfadder_ia15_ib15_0.output()[1],Power)
        # self.output_value.append(self.fulladder_ia1_ib1_01_1.output()[0])

        self.fulladder_ia14_ib14_01_1 = FullAdder(input_a[14],input_b[14],self.halfadder_ia15_ib15_0.output()[1],Power)
        self.output_value.append(self.fulladder_ia14_ib14_01_1.output()[0])

        self.fulladder_ia13_ib13_11_2 = FullAdder(input_a[13],input_b[13],self.fulladder_ia14_ib14_01_1.output()[1],Power)
        self.output_value.append(self.fulladder_ia13_ib13_11_2.output()[0])

        self.fulladder_ia12_ib12_21_3 = FullAdder(input_a[12],input_b[12],self.fulladder_ia13_ib13_11_2.output()[1],Power)
        self.output_value.append(self.fulladder_ia12_ib12_21_3.output()[0])

        self.fulladder_ia11_ib11_31_4 = FullAdder(input_a[11],input_b[11],self.fulladder_ia12_ib12_21_3.output()[1],Power)
        self.output_value.append(self.fulladder_ia11_ib11_31_4.output()[0])

        self.fulladder_ia10_ib10_41_5 = FullAdder(input_a[10],input_b[10],self.fulladder_ia11_ib11_31_4.output()[1],Power)
        self.output_value.append(self.fulladder_ia10_ib10_41_5.output()[0])

        self.fulladder_ia9_ib9_51_6 = FullAdder(input_a[9],input_b[9],self.fulladder_ia10_ib10_41_5.output()[1],Power)
        self.output_value.append(self.fulladder_ia9_ib9_51_6.output()[0])

        self.fulladder_ia8_ib8_61_7 = FullAdder(input_a[8],input_b[8],self.fulladder_ia9_ib9_51_6.output()[1],Power)
        self.output_value.append(self.fulladder_ia8_ib8_61_7.output()[0])

        self.fulladder_ia7_ib7_71_8 = FullAdder(input_a[7],input_b[7],self.fulladder_ia8_ib8_61_7.output()[1],Power)
        self.output_value.append(self.fulladder_ia7_ib7_71_8.output()[0])

        self.fulladder_ia6_ib6_81_9 = FullAdder(input_a[6],input_b[6],self.fulladder_ia7_ib7_71_8.output()[1],Power)
        self.output_value.append(self.fulladder_ia6_ib6_81_9.output()[0])

        self.fulladder_ia5_ib5_91_10 = FullAdder(input_a[5],input_b[5],self.fulladder_ia6_ib6_81_9.output()[1],Power)
        self.output_value.append(self.fulladder_ia5_ib5_91_10.output()[0])

        self.fulladder_ia4_ib4_101_11 = FullAdder(input_a[4],input_b[4],self.fulladder_ia5_ib5_91_10.output()[1],Power)
        self.output_value.append(self.fulladder_ia4_ib4_101_11.output()[0])

        self.fulladder_ia3_ib3_111_12 = FullAdder(input_a[3],input_b[3],self.fulladder_ia4_ib4_101_11.output()[1],Power)
        self.output_value.append(self.fulladder_ia3_ib3_111_12.output()[0])

        self.fulladder_ia2_ib2_121_13 = FullAdder(input_a[2],input_b[2],self.fulladder_ia3_ib3_111_12.output()[1],Power)
        self.output_value.append(self.fulladder_ia2_ib2_121_13.output()[0])

        self.fulladder_ia1_ib1_131_14 = FullAdder(input_a[1],input_b[1],self.fulladder_ia2_ib2_121_13.output()[1],Power)
        self.output_value.append(self.fulladder_ia1_ib1_131_14.output()[0])

        self.fulladder_ia0_ib0_141_15 = FullAdder(input_a[0],input_b[0],self.fulladder_ia1_ib1_131_14.output()[1],Power)
        self.output_value.append(self.fulladder_ia0_ib0_141_15.output()[0])



        # Reversing the order of the output i.e, make it Stack
        tmp0 = [self.output_value[(len(self.output_value)-1)-i] for i in range(len(self.output_value))]

        self.output_value = tmp0
    def output(self):
        return self.output_value

class Inc16:
    #increment the input value by one bit

    def __init__(self,Input,Power=1):
        inc_val_0 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
        self.adder16_i_0_1 = Adder16(Input,inc_val_0,Power);
        self.output_value = self.adder16_i_0_1.output();

    def output(self):
        return self.output_value

class Neg16:

    """
    in: x[16]
    out: out[16]
    func: Converting x into -x using this formula : 1 + (((2^n) -1)-x)
          basically we are finding the 2's complement version of the input x.
          which helps us to represent the negetive version of our input x
    """
    neg_num16_id = -1

    def __init__(self,Input,Power=1):
        # self.output_value = []

        #Converting input into its complements using Not16
        self.not16_I_0 = Not16(Input,Power)

        #Creating 1 in 16bit format
        self.tempvalue__1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]

        # now adding both the outputs to get our final value in 2's complement format
        self.adder16_0_1_2 = Adder16(self.not16_I_0.output(),self.tempvalue__1,Power)

        self.output_value  = self.adder16_0_1_2.output()

        Neg16.neg_num16_id += 1

    def output(self):
        return self.output_value


# FInally Creating ARITHMATIC LOGICAL UNIT

class ALU:

    """
    in:   x[16] y[16]
          zx      // zero the x
          nx      // negate the x
          zy      // zero the y
          ny      // negate the u
          f       // 1 = add 0 = and
          no      // negate the output

    out:  out[16]
          zr      // 1 iff out == 0
          ng      // 1 iff out < 0

    func: if zx then x = 0 // 16-bit zero Constant
          if nx then x = !x // bit-wise negation
          if zy then y = 0  // 16-bit zero constant
          if ny then y = !y // bit-wise negation
          if f then out = x+y
               else out = x &y
          if no then out = !out //bit-wise negation

          if out=0 then zr=1 else zr=0 // 16-bit eq.  comparison
          if out<0 then ng=1 else ng=0 // 16-bit neg. comparison
    """

    alu_id = -1 # althought usually there is only one alu in a cpu but to follow the convension we are giving it an id

    def __init__(self,input_x,input_y,zx,nx,zy,ny,f,no,Power=1):

            # Creating a const zero
        self.constZero__0 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

        #if zx then x = 0 // 16-bit zero Constant
        self.mux16_ix_0_zx_1 = Mux16(input_x,self.constZero__0,zx,Power)

        #if nx then x = !x // bit-wise negation
        # print("if zx: ",self.mux16_ix_0_zx_1.output())

        #Creating !x
        self.not16_1_2 = Not16(self.mux16_ix_0_zx_1.output(),Power)
        self.mux16_1_2_nx_3 = Mux16(self.mux16_ix_0_zx_1.output(),self.not16_1_2.output(),nx,Power)

        # print("if nx: ",self.mux16_1_2_nx_3.output())

        #if zy then y = 0  // 16-bit zero constant
        self.mux16_iy_0_zy_4 = Mux16(input_y,self.constZero__0,zy,Power)

        # print("if zy: ",self.mux16_iy_0_zy_4.output())

        #if ny then y = !y // bit-wise negation
        self.not16_4_5 = Not16(self.mux16_iy_0_zy_4.output(),Power)
        self.mux16_4_5_ny_6 = Mux16(self.mux16_iy_0_zy_4.output(),self.not16_4_5.output(),ny,Power)

        # print("if ny: ",self.mux16_4_5_ny_6.output())


        #if f then out = x+y
        #else out = x &y
        self.adder16_3_6_7 = Adder16(self.mux16_1_2_nx_3.output(),self.mux16_4_5_ny_6.output(),Power)
        # print("adder: ",self.adder16_3_6_7.output())
        self.and16_3_6_8   = And16(self.mux16_1_2_nx_3.output(),self.mux16_4_5_ny_6.output(),Power)
        # print("and16 : ",self.and16_3_6_8.output())

        self.mux16_7_8_f_9 = Mux16(self.and16_3_6_8.output(),self.adder16_3_6_7.output(),f,Power)
        # print("if f ",self.mux16_7_8_f_9.output())


        #if no then out = !out //bit-wise negation
        self.not16_9_10 = Not16(self.mux16_7_8_f_9.output(),Power)
        self.mux16_9_10_no_11 = Mux16(self.mux16_7_8_f_9.output(),self.not16_9_10.output(),no,Power)

        self.out = self.mux16_9_10_no_11.output()

        # print("self.out",self.out);
        #if out=0 then zr=1 else zr=0 // 16-bit eq.  comparison
        self.or8way_ixfrom0to7_12 =  Or8Way([self.out[0],self.out[1],self.out[2],self.out[3],self.out[4],self.out[5],self.out[6],self.out[7]],Power)

        self.or8way_ixfrom8to15_13 = Or8Way([self.out[8],self.out[9],self.out[10],self.out[11],self.out[12],self.out[13],self.out[14],self.out[15]],Power)

        self.or_12_13_14 = OR(self.or8way_ixfrom0to7_12.output(),self.or8way_ixfrom8to15_13.output(),Power)

        # now this operation gives us 0 if out==1 otherwise 1 if out ==0
        self.not_14_15 = NOT(self.or_12_13_14.output(),Power)

        self.zr = self.not_14_15.output()


        #if out<0 then ng=1 else ng=0 // 16-bit neg. comparison
        # take the most significant bit(i.e, index0 because we are going from right to left) of output and if that is 1 then its negetive(i.e,ng =1) otherwise its not i.e,ng = 0
        self.ng = self.out[0]

        # now putting it all together as a final output of ALU in dictonary format.
        self.output_value = {"out":self.out,"zr":self.zr,"ng":self.ng}

        ALU.alu_id += 1

    def output(self):
        return self.output_value

class SRFF():
    #THIS IS JUST THE TEMPORARY VERSION OF SRFF USING IF... I Will Create the final logic Later

    # tm1 == time minus one. i.e, previous time step

    def __init__(self,S,R,tm1_Q0=None,Power=1):

        #initializing
        self.tm1_Q0_1 = None
        self.tm1_Q1_2 = None

        # if we dont know t-1 input i.e, when we just starting our computer
        # just think about the scenerio what if both tm1_Q0 and tm1_Q1 were '0'
        if (tm1_Q0==None) :
            if(S==1): tm1_Q0  = 0;
            if(S==0): tm1_Q0  = 1;
            self.output_value = [0,0]
        else:
            # Always outputing the previously evaluated value.
            # and because its the first state of existence of this SRFF then just output tm1_Q0 and tm1_Q1
            self.tm1_Q0_1 = tm1_Q0
            self.tm1_Q1_2 = 1-tm1_Q0 # because Q1 will always be opposite of Q1
            self.output_value = [self.tm1_Q0_1,self.tm1_Q1_2]

        self.eval_val = [self.tm1_Q0_1,self.tm1_Q1_2] #evaluated value from the current inputs and the eval_value is going to be the output_value for the next time step


        # if( S==0 and R==0 ):self.eval_val = [self.tm1_Q0_1,self.tm1_Q1_2]#then dont change the values

        if( S==0 and R==1 ):self.eval_val = [1,0]
        if( S==1 and R==0 ):self.eval_val = [0,1]

        # if( S==1 and R==1 ):self.eval_val = [None,None]


        #Now for the next time the output is going to be the currently evaluated value.
        self.tm1_Q0_1 = self.eval_val[0]
        self.tm1_Q1_2 = self.eval_val[1]

    def update(self,S,R,Power=1):
        #Call update whenever updating the time.

        # for the current time step the ouput is going to be the previously evaluated value
        self.output_value = [self.tm1_Q0_1,self.tm1_Q1_2]
        self.eval_val = [self.tm1_Q0_1,self.tm1_Q1_2]

        # if( S==0 and R==0 ):

        if( S==0 and R==1 ):self.eval_val = [1,0]
        if( S==1 and R==0 ):self.eval_val = [0,1]

        # if( S==1 and R==1 ):self.eval_val = [None,None]

        #Now for the next time the output is going to be the currently evaluated value.
        self.tm1_Q0_1 = self.eval_val[0]
        self.tm1_Q1_2 = self.eval_val[1]

    def output(self):
        return self.output_value

class Clocked_DFF:
    """
    Clocked D Flip Flop

    state[t] = function(state[t-1])  i.e, the output of current time unit is the evaluated value of the previous time unit
    """
    def __init__(self,data,clock,Power=1):
        self.not_d_0    = NOT(data,Power)
        self.nand_d_c_1 = NAND(data,clock,Power)
        self.nand_c_1_2 = NAND(clock,self.not_d_0.output(),Power)

        #Now Using SR FlipFlop \\\\\\\\\\\\\\\\\\\\\\\\\\\\USING "SRFF" temporarly/////////////////////////////////////
        self.srff_1_2_3 = SRFF(self.nand_d_c_1.output(),self.nand_c_1_2.output(),tm1_Q0=None,Power=Power)

        self.output_value = self.srff_1_2_3.output()

    def update(self,data,clock,Power=1):
        self.not_d_0    = NOT(data,Power)
        self.nand_d_c_1 = NAND(data,clock,Power)
        self.nand_c_1_2 = NAND(clock,self.not_d_0.output(),Power)

        #Now Using SR FlipFlop.update to update the values according to the new inputs
        self.srff_1_2_3.update(self.nand_d_c_1.output(),self.nand_c_1_2.output(),Power)

        self.output_value = self.srff_1_2_3.output()

    def output(self):
        return self.output_value


class Reg1Bit:
    """
    if the load bit is on then the new input_1 is going to be inserted in DFF otherwise,
    Input_0 (i.e, output of t-1) is going to persist
    """
    def __init__(self,Input_1,Load,Power=1):

        Input_0 = 0;

        # if we know the value of (t-1) then we can use that to calculate the current time output
        self.mux_i0_i1_l_0 = MUX(Input_0,Input_1,Load,Power)

        # print("self.mux_ ",self.mux_i0_i1_l_0.output());

        self.dff_0_1 = Clocked_DFF(self.mux_i0_i1_l_0.output(),1,Power)

        self.register_state = self.dff_0_1.output()[0] # now for the next t-step this output is going to be the currently evaluated value
        #if i look at the output of the system it will show me the out of the previous time step
        self.output_value = self.register_state # for current t-step the out is going to be the output in t-1 t-step which is describe by Input_1

        # print("self.output_value ",self.output_value)

    def update(self,Input,Load,Power=1):
        if (self.register_state == None):
            self.register_state = 0;

        # using the output of the previous time step as a second input for this time step

        self.mux_i0_i1_l_0 = MUX(self.register_state,Input,Load,Power)

        self.dff_0_1.update(self.mux_i0_i1_l_0.output(),Load,Power)

        # print("\n self.dff_0_1.update() ",self.dff_0_1.output());

        # for current t-step the out is going to be the output in t-1 t-step which is describe by Input_1
        self.register_state = self.dff_0_1.output()[0] # the ouput is only Q not Q`
        self.output_value = self.register_state

    def output(self):
        return self.output_value

class Reg16:
    #16-bit Register

    # TODO: Change the name Reg1Bit_i1"x"_l_0

    def __init__(self,Input,Load,Power=1):
        self.output_value = []

        Input_0 = [0]*16;

        self.Reg1Bit_i0_l_0 = Reg1Bit(Input[0],Load,Power)
        self.output_value.append(self.Reg1Bit_i0_l_0.output())

        self.Reg1Bit_i1_l_1 = Reg1Bit(Input[1],Load,Power)
        self.output_value.append(self.Reg1Bit_i1_l_1.output())

        self.Reg1Bit_i2_l_2 = Reg1Bit(Input[2],Load,Power)
        self.output_value.append(self.Reg1Bit_i2_l_2.output())

        self.Reg1Bit_i3_l_3 = Reg1Bit(Input[3],Load,Power)
        self.output_value.append(self.Reg1Bit_i3_l_3.output())

        self.Reg1Bit_i4_l_4 = Reg1Bit(Input[4],Load,Power)
        self.output_value.append(self.Reg1Bit_i4_l_4.output())

        self.Reg1Bit_i5_l_5 = Reg1Bit(Input[5],Load,Power)
        self.output_value.append(self.Reg1Bit_i5_l_5.output())

        self.Reg1Bit_i6_l_6 = Reg1Bit(Input[6],Load,Power)
        self.output_value.append(self.Reg1Bit_i6_l_6.output())

        self.Reg1Bit_i7_l_7 = Reg1Bit(Input[7],Load,Power)
        self.output_value.append(self.Reg1Bit_i7_l_7.output())

        self.Reg1Bit_i8_l_8 = Reg1Bit(Input[8],Load,Power)
        self.output_value.append(self.Reg1Bit_i8_l_8.output())

        self.Reg1Bit_i9_l_9 = Reg1Bit(Input[9],Load,Power)
        self.output_value.append(self.Reg1Bit_i9_l_9.output())

        self.Reg1Bit_i10_l_10 = Reg1Bit(Input[10],Load,Power)
        self.output_value.append(self.Reg1Bit_i10_l_10.output())

        self.Reg1Bit_i11_l_11 = Reg1Bit(Input[11],Load,Power)
        self.output_value.append(self.Reg1Bit_i11_l_11.output())

        self.Reg1Bit_i12_l_12 = Reg1Bit(Input[12],Load,Power)
        self.output_value.append(self.Reg1Bit_i12_l_12.output())

        self.Reg1Bit_i13_l_13 = Reg1Bit(Input[13],Load,Power)
        self.output_value.append(self.Reg1Bit_i13_l_13.output())

        self.Reg1Bit_i14_l_14 = Reg1Bit(Input[14],Load,Power)
        self.output_value.append(self.Reg1Bit_i14_l_14.output())

        self.Reg1Bit_i15_l_15 = Reg1Bit(Input[15],Load,Power)
        self.output_value.append(self.Reg1Bit_i15_l_15.output())

        # print("Reg16: ",self.output_value);

    def update(self,Input,Load,Power): # Input because Input_0 is the output of t-1 so we are going to reference that
        # updating the individual Register and feeding the values inside output

        # Here ofcourse i am using the previously created Register object so dont match the arguments with the names.
        self.Reg1Bit_i0_l_0.update(Input[0],Load,Power)
        self.output_value[0] = self.Reg1Bit_i0_l_0.output()

        self.Reg1Bit_i1_l_1.update(Input[1],Load,Power)
        self.output_value[1] = self.Reg1Bit_i1_l_1.output()

        self.Reg1Bit_i2_l_2.update(Input[2],Load,Power)
        self.output_value[2] = self.Reg1Bit_i2_l_2.output()

        self.Reg1Bit_i3_l_3.update(Input[3],Load,Power)
        self.output_value[3] = self.Reg1Bit_i3_l_3.output()

        self.Reg1Bit_i4_l_4.update(Input[4],Load,Power)
        self.output_value[4] = self.Reg1Bit_i4_l_4.output()

        self.Reg1Bit_i5_l_5.update(Input[5],Load,Power)
        self.output_value[5] = self.Reg1Bit_i5_l_5.output()

        self.Reg1Bit_i6_l_6.update(Input[6],Load,Power)
        self.output_value[6] = self.Reg1Bit_i6_l_6.output()

        self.Reg1Bit_i7_l_7.update(Input[7],Load,Power)
        self.output_value[7] = self.Reg1Bit_i7_l_7.output()

        self.Reg1Bit_i8_l_8.update(Input[8],Load,Power)
        self.output_value[8] = self.Reg1Bit_i8_l_8.output()

        self.Reg1Bit_i9_l_9.update(Input[9],Load,Power)
        self.output_value[9] = self.Reg1Bit_i9_l_9.output()

        self.Reg1Bit_i10_l_10.update(Input[10],Load,Power)
        self.output_value[10] = self.Reg1Bit_i10_l_10.output()

        self.Reg1Bit_i11_l_11.update(Input[11],Load,Power)
        self.output_value[11] = self.Reg1Bit_i11_l_11.output()

        self.Reg1Bit_i12_l_12.update(Input[12],Load,Power)
        self.output_value[12] = self.Reg1Bit_i12_l_12.output()

        self.Reg1Bit_i13_l_13.update(Input[13],Load,Power)
        self.output_value[13] = self.Reg1Bit_i13_l_13.output()

        self.Reg1Bit_i14_l_14.update(Input[14],Load,Power)
        self.output_value[14] = self.Reg1Bit_i14_l_14.output()

        self.Reg1Bit_i15_l_15.update(Input[15],Load,Power)
        self.output_value[15] = self.Reg1Bit_i15_l_15.output()

    def output(self):
        return self.output_value

# Counter
class ProgramCounter:
    # Program Counter
    # in[16] : input_number,load_bit and increment
    # out[16]
    # Note: it will give the currently evaluated value in the next time step

    def __init__(self,Input,load,inc,reset,Power=1):

        #initializing with 0 bit
        self.zero16_0 = [0]*16

        self.value_1 = self.zero16_0 #current counter value

        ######

        #if load  == 1
        self.mux16_0_i_l_2 = Mux16(self.value_1,Input,load,Power).output()# choose value_0 or incremented value depending on add bit

        #if reset == 1
        self.mux16_2_0_r_3 = Mux16(self.mux16_0_i_l_2,self.zero16_0,reset,Power).output()

        self.inc16_3_4 = Inc16(self.mux16_2_0_r_3,Power).output()

        self.mux16_3_4_5 = Mux16(self.mux16_2_0_r_3,self.inc16_3_4,inc,Power)

        self.eval_out = self.mux16_3_4_5.output() # output evaluate at current time step
        self.output_value = self.value_1

        self.value_1 = self.eval_out

    def update(self,Input=None,load=0,inc=1,reset=0,Power=1):


        #if load  == 1
        self.mux16_0_i_l_2 = Mux16(self.value_1,Input,load,Power).output()# choose value_0 or incremented value depending on add bit

        #if reset == 1
        self.mux16_2_0_r_3 = Mux16(self.mux16_0_i_l_2,self.zero16_0,reset,Power).output()

        self.inc16_3_4 = Inc16(self.mux16_2_0_r_3,Power).output()

        self.mux16_3_4_5 = Mux16(self.mux16_2_0_r_3,self.inc16_3_4,inc,Power)

        self.eval_out = self.mux16_3_4_5.output() # output evaluate at current time step
        self.output_value = self.value_1

        self.value_1 = self.eval_out

        # self.output_value = self.eval_out # giving the output of previous operation
        # self.eval_out = self.inc16_3_4.output() # output evaluate at current time step


    def output(self):
        return self.output_value


## Next IS RAM!!! Bitches!!! :D

class RAM8:

    """
    Input   = 16 bit
    address = 3  bit

    """
    #AWESOME!!!
    def __init__(self,Input,address,load,Power=1):

        self.final_load_path = []
        self.output_value    = []

        self.dmux_l_a0_0  =  DMUX(load,address[0],Power).output()

        self.dmux_00_a1_1 =  DMUX(self.dmux_l_a0_0[0],address[1],Power).output()
        self.dmux_01_a1_2 =  DMUX(self.dmux_l_a0_0[1],address[1],Power).output()

        # this section gives the final switch configuration for all 8 register files
        self.dmux_10_a2_3 =  DMUX(self.dmux_00_a1_1[0],address[2],Power).output()
        self.final_load_path.append(self.dmux_10_a2_3)

        self.dmux_11_a2_4 =  DMUX(self.dmux_00_a1_1[1],address[2],Power).output()
        self.final_load_path.append(self.dmux_11_a2_4)

        self.dmux_20_a2_5 =  DMUX(self.dmux_01_a1_2[0],address[2],Power).output()
        self.final_load_path.append(self.dmux_20_a2_5)

        self.dmux_21_a2_6 =  DMUX(self.dmux_01_a1_2[1],address[2],Power).output()
        self.final_load_path.append(self.dmux_21_a2_6)

        # print("RAM8-> final_load_path",self.final_load_path)

        # feeding the final configuration of load bits to the registers
        self.reg16_i_30_7  = Reg16(Input,self.dmux_10_a2_3[0],Power)
        self.reg16_i_31_8  = Reg16(Input,self.dmux_10_a2_3[1],Power)
        self.output_value.append(self.reg16_i_30_7.output())
        self.output_value.append(self.reg16_i_31_8.output())

        self.reg16_i_40_9  = Reg16(Input,self.dmux_11_a2_4[0],Power)
        self.reg16_i_41_10 = Reg16(Input,self.dmux_11_a2_4[1],Power)
        self.output_value.append(self.reg16_i_40_9.output())
        self.output_value.append(self.reg16_i_41_10.output())

        self.reg16_i_50_11 = Reg16(Input,self.dmux_20_a2_5[0],Power)
        self.reg16_i_51_12 = Reg16(Input,self.dmux_20_a2_5[1],Power)
        self.output_value.append(self.reg16_i_50_11.output())
        self.output_value.append(self.reg16_i_51_12.output())

        self.reg16_i_60_13 = Reg16(Input,self.dmux_21_a2_6[0],Power)
        self.reg16_i_61_14 = Reg16(Input,self.dmux_21_a2_6[1],Power)
        self.output_value.append(self.reg16_i_60_13.output())
        self.output_value.append(self.reg16_i_61_14.output())

    def update(self,Input,address,load,Power=1):
        self.output_value = [] # reinitializing the output_value
        self.final_load_path = [];

        self.dmux_l_a0_0  =  DMUX(load,address[0],Power).output()

        self.dmux_00_a1_1 =  DMUX(self.dmux_l_a0_0[0],address[1],Power).output()
        self.dmux_01_a1_2 =  DMUX(self.dmux_l_a0_0[1],address[1],Power).output()

        # this section gives the final switch configuration(i.e, which register is going to get the input) for all 8 register files
        self.dmux_10_a2_3 =  DMUX(self.dmux_00_a1_1[0],address[2],Power).output()
        self.final_load_path.append(self.dmux_10_a2_3)

        self.dmux_11_a2_4 =  DMUX(self.dmux_00_a1_1[1],address[2],Power).output()
        self.final_load_path.append(self.dmux_11_a2_4)

        self.dmux_20_a2_5 =  DMUX(self.dmux_01_a1_2[0],address[2],Power).output()
        self.final_load_path.append(self.dmux_20_a2_5)

        self.dmux_21_a2_6 =  DMUX(self.dmux_01_a1_2[1],address[2],Power).output()
        self.final_load_path.append(self.dmux_21_a2_6)

        # feeding the final configuration of load bits to the registers
        self.reg16_i_30_7.update(Input,self.dmux_10_a2_3[0],Power)
        self.reg16_i_31_8.update(Input,self.dmux_10_a2_3[1],Power)
        self.output_value.append(self.reg16_i_30_7.output())
        self.output_value.append(self.reg16_i_31_8.output())

        self.reg16_i_40_9.update(Input,self.dmux_11_a2_4[0],Power)
        self.reg16_i_41_10.update(Input,self.dmux_11_a2_4[1],Power)
        self.output_value.append(self.reg16_i_40_9.output())
        self.output_value.append(self.reg16_i_41_10.output())

        self.reg16_i_50_11.update(Input,self.dmux_20_a2_5[0],Power)
        self.reg16_i_51_12.update(Input,self.dmux_20_a2_5[1],Power)
        self.output_value.append(self.reg16_i_50_11.output())
        self.output_value.append(self.reg16_i_51_12.output())

        self.reg16_i_60_13.update(Input,self.dmux_21_a2_6[0],Power)
        self.reg16_i_61_14.update(Input,self.dmux_21_a2_6[1],Power)
        self.output_value.append(self.reg16_i_60_13.output())
        self.output_value.append(self.reg16_i_61_14.output())

    def output(self):
        return self.output_value

class RAM64:
    def __init__(self,Input,address,load,Power=1):
        # r64 consist of 8 RAM8 i.e, 3 more address bits 

        self.final_load_path = []
        self.output_value    = []

        self.dmux_l_a0_0  =  DMUX(load,address[0],Power).output()

        self.dmux_00_a1_1 =  DMUX(self.dmux_l_a0_0[0],address[1],Power).output()
        self.dmux_01_a1_2 =  DMUX(self.dmux_l_a0_0[1],address[1],Power).output()

        # this section gives the final switch configuration for all 8 register files
        self.dmux_10_a2_3 =  DMUX(self.dmux_00_a1_1[0],address[2],Power).output()
        self.final_load_path.append(self.dmux_10_a2_3)

        self.dmux_11_a2_4 =  DMUX(self.dmux_00_a1_1[1],address[2],Power).output()
        self.final_load_path.append(self.dmux_11_a2_4)

        self.dmux_20_a2_5 =  DMUX(self.dmux_01_a1_2[0],address[2],Power).output()
        self.final_load_path.append(self.dmux_20_a2_5)

        self.dmux_21_a2_6 =  DMUX(self.dmux_01_a1_2[1],address[2],Power).output()
        self.final_load_path.append(self.dmux_21_a2_6)

        # print("INIT: RAM64-> final_load_path",self.final_load_path)

        # feeding the final configuration of load bits to the registers

        self.spliced_address_7 = [address[3],address[4],address[5]]

        self.ram8_i_7_30_8 = RAM8(Input,self.spliced_address_7,self.dmux_10_a2_3[0])
        self.output_value.append(self.ram8_i_7_30_8.output())

        self.ram8_i_7_31_9 = RAM8(Input,self.spliced_address_7,self.dmux_10_a2_3[1])
        self.output_value.append(self.ram8_i_7_31_9.output())

        self.ram8_i_7_40_10 = RAM8(Input,self.spliced_address_7,self.dmux_11_a2_4[0])
        self.output_value.append(self.ram8_i_7_40_10.output())

        self.ram8_i_7_41_11 = RAM8(Input,self.spliced_address_7,self.dmux_11_a2_4[1])
        self.output_value.append(self.ram8_i_7_41_11.output())

        self.ram8_i_7_50_12 = RAM8(Input,self.spliced_address_7,self.dmux_20_a2_5[0])
        self.output_value.append(self.ram8_i_7_50_12.output())

        self.ram8_i_7_51_13 = RAM8(Input,self.spliced_address_7,self.dmux_20_a2_5[1])
        self.output_value.append(self.ram8_i_7_51_13.output())

        self.ram8_i_7_60_14 = RAM8(Input,self.spliced_address_7,self.dmux_21_a2_6[0])
        self.output_value.append(self.ram8_i_7_60_14.output())

        self.ram8_i_7_61_15 = RAM8(Input,self.spliced_address_7,self.dmux_21_a2_6[1])
        self.output_value.append(self.ram8_i_7_61_15.output())

    def update(self,Input,address,load,Power=1):
        # r64 consist of 8 RAM8 i.e, 3 more address bits 

        self.final_load_path = []
        self.output_value    = []

        self.dmux_l_a0_0  =  DMUX(load,address[0],Power).output()

        self.dmux_00_a1_1 =  DMUX(self.dmux_l_a0_0[0],address[1],Power).output()
        self.dmux_01_a1_2 =  DMUX(self.dmux_l_a0_0[1],address[1],Power).output()

        # this section gives the final switch configuration for all 8 register files
        self.dmux_10_a2_3 =  DMUX(self.dmux_00_a1_1[0],address[2],Power).output()
        self.final_load_path.append(self.dmux_10_a2_3)

        self.dmux_11_a2_4 =  DMUX(self.dmux_00_a1_1[1],address[2],Power).output()
        self.final_load_path.append(self.dmux_11_a2_4)

        self.dmux_20_a2_5 =  DMUX(self.dmux_01_a1_2[0],address[2],Power).output()
        self.final_load_path.append(self.dmux_20_a2_5)

        self.dmux_21_a2_6 =  DMUX(self.dmux_01_a1_2[1],address[2],Power).output()
        self.final_load_path.append(self.dmux_21_a2_6)

        # print("\n UPDATE: RAM64-> final_load_path",self.final_load_path)

        # feeding the final configuration of load bits to the registers

        self.spliced_address_7 = [address[3],address[4],address[5]]

        self.ram8_i_7_30_8.update(Input,self.spliced_address_7,self.dmux_10_a2_3[0])
        self.output_value.append(self.ram8_i_7_30_8.output())

        self.ram8_i_7_31_9.update(Input,self.spliced_address_7,self.dmux_10_a2_3[1])
        self.output_value.append(self.ram8_i_7_31_9.output())

        self.ram8_i_7_40_10.update(Input,self.spliced_address_7,self.dmux_11_a2_4[0])
        self.output_value.append(self.ram8_i_7_40_10.output())

        self.ram8_i_7_41_11.update(Input,self.spliced_address_7,self.dmux_11_a2_4[1])
        self.output_value.append(self.ram8_i_7_41_11.output())

        self.ram8_i_7_50_12.update(Input,self.spliced_address_7,self.dmux_20_a2_5[0])
        self.output_value.append(self.ram8_i_7_50_12.output())

        self.ram8_i_7_51_13.update(Input,self.spliced_address_7,self.dmux_20_a2_5[1])
        self.output_value.append(self.ram8_i_7_51_13.output())

        self.ram8_i_7_60_14.update(Input,self.spliced_address_7,self.dmux_21_a2_6[0])
        self.output_value.append(self.ram8_i_7_60_14.output())

        self.ram8_i_7_61_15.update(Input,self.spliced_address_7,self.dmux_21_a2_6[1])
        self.output_value.append(self.ram8_i_7_61_15.output())

        # print("output: ",self.output_value,"\n\n")

    def output(self):
        return self.output_value


# also need to create ram512 ram4K and ram16K

class RAM512:
    def __init__(self,Input,address,load,Power=1):
        # r512 consist of 8 RAM64 i.e, 3 more address bits  so total of 9 bits of address

        self.final_load_path = []
        self.output_value    = []

        self.dmux_l_a0_0  =  DMUX(load,address[0],Power).output()

        self.dmux_00_a1_1 =  DMUX(self.dmux_l_a0_0[0],address[1],Power).output()
        self.dmux_01_a1_2 =  DMUX(self.dmux_l_a0_0[1],address[1],Power).output()

        # this section gives the final switch configuration for all 8 register files
        self.dmux_10_a2_3 =  DMUX(self.dmux_00_a1_1[0],address[2],Power).output()
        self.final_load_path.append(self.dmux_10_a2_3)

        self.dmux_11_a2_4 =  DMUX(self.dmux_00_a1_1[1],address[2],Power).output()
        self.final_load_path.append(self.dmux_11_a2_4)

        self.dmux_20_a2_5 =  DMUX(self.dmux_01_a1_2[0],address[2],Power).output()
        self.final_load_path.append(self.dmux_20_a2_5)

        self.dmux_21_a2_6 =  DMUX(self.dmux_01_a1_2[1],address[2],Power).output()
        self.final_load_path.append(self.dmux_21_a2_6)

        # print("INIT: RAM512-> final_load_path\n\n",self.final_load_path)

        # feeding the final configuration of load bits to the registers

        self.spliced_address_7 = [address[3],address[4],address[5],address[6],address[7],address[8]]

        self.ram64_i_7_30_8 = RAM64(Input,self.spliced_address_7,self.dmux_10_a2_3[0])
        self.output_value.append(self.ram64_i_7_30_8.output())

        self.ram64_i_7_31_9 = RAM64(Input,self.spliced_address_7,self.dmux_10_a2_3[1])
        self.output_value.append(self.ram64_i_7_31_9.output())

        self.ram64_i_7_40_10 = RAM64(Input,self.spliced_address_7,self.dmux_11_a2_4[0])
        self.output_value.append(self.ram64_i_7_40_10.output())

        self.ram64_i_7_41_11 = RAM64(Input,self.spliced_address_7,self.dmux_11_a2_4[1])
        self.output_value.append(self.ram64_i_7_41_11.output())

        self.ram64_i_7_50_12 = RAM64(Input,self.spliced_address_7,self.dmux_20_a2_5[0])
        self.output_value.append(self.ram64_i_7_50_12.output())

        self.ram64_i_7_51_13 = RAM64(Input,self.spliced_address_7,self.dmux_20_a2_5[1])
        self.output_value.append(self.ram64_i_7_51_13.output())

        self.ram64_i_7_60_14 = RAM64(Input,self.spliced_address_7,self.dmux_21_a2_6[0])
        self.output_value.append(self.ram64_i_7_60_14.output())

        self.ram64_i_7_61_15 = RAM64(Input,self.spliced_address_7,self.dmux_21_a2_6[1])
        self.output_value.append(self.ram64_i_7_61_15.output())

        # print("INIT: output: ",self.output_value)
    def update(self,Input,address,load,Power=1):
        # r512 consist of 8 RAM64 i.e, 3 more address bits  so total of 9 bits of address

        self.final_load_path = []
        self.output_value    = []

        self.dmux_l_a0_0  =  DMUX(load,address[0],Power).output()

        self.dmux_00_a1_1 =  DMUX(self.dmux_l_a0_0[0],address[1],Power).output()
        self.dmux_01_a1_2 =  DMUX(self.dmux_l_a0_0[1],address[1],Power).output()

        # this section gives the final switch configuration for all 8 register files
        self.dmux_10_a2_3 =  DMUX(self.dmux_00_a1_1[0],address[2],Power).output()
        self.final_load_path.append(self.dmux_10_a2_3)

        self.dmux_11_a2_4 =  DMUX(self.dmux_00_a1_1[1],address[2],Power).output()
        self.final_load_path.append(self.dmux_11_a2_4)

        self.dmux_20_a2_5 =  DMUX(self.dmux_01_a1_2[0],address[2],Power).output()
        self.final_load_path.append(self.dmux_20_a2_5)

        self.dmux_21_a2_6 =  DMUX(self.dmux_01_a1_2[1],address[2],Power).output()
        self.final_load_path.append(self.dmux_21_a2_6)

        # print("UPDATE: RAM64-> final_load_path",self.final_load_path)

        # feeding the final configuration of load bits to the registers


        self.spliced_address_7 = [address[3],address[4],address[5],address[6],address[7],address[8]]

        self.ram64_i_7_30_8.update(Input,self.spliced_address_7,self.dmux_10_a2_3[0])
        self.output_value.append(self.ram64_i_7_30_8.output())

        self.ram64_i_7_31_9.update(Input,self.spliced_address_7,self.dmux_10_a2_3[1])
        self.output_value.append(self.ram64_i_7_31_9.output())

        self.ram64_i_7_40_10.update(Input,self.spliced_address_7,self.dmux_11_a2_4[0])
        self.output_value.append(self.ram64_i_7_40_10.output())

        self.ram64_i_7_41_11.update(Input,self.spliced_address_7,self.dmux_11_a2_4[1])
        self.output_value.append(self.ram64_i_7_41_11.output())

        self.ram64_i_7_50_12.update(Input,self.spliced_address_7,self.dmux_20_a2_5[0])
        self.output_value.append(self.ram64_i_7_50_12.output())

        self.ram64_i_7_51_13.update(Input,self.spliced_address_7,self.dmux_20_a2_5[1])
        self.output_value.append(self.ram64_i_7_51_13.output())

        self.ram64_i_7_60_14.update(Input,self.spliced_address_7,self.dmux_21_a2_6[0])
        self.output_value.append(self.ram64_i_7_60_14.output())

        self.ram64_i_7_61_15.update(Input,self.spliced_address_7,self.dmux_21_a2_6[1])
        self.output_value.append(self.ram64_i_7_61_15.output())

        # print("UPDATE: RAM512 -> output: ",self.output_value[5][6])

    def output(self):
        return self.output_value

class RAM4K:
    def __init__(self,Input,address,load,Power=1):
        # r512 consist of 8 RAM512 i.e, 3 more address bits  so total of 12 bits of address

        self.final_load_path = []
        self.output_value    = []

        self.dmux_l_a0_0  =  DMUX(load,address[0],Power).output()

        self.dmux_00_a1_1 =  DMUX(self.dmux_l_a0_0[0],address[1],Power).output()
        self.dmux_01_a1_2 =  DMUX(self.dmux_l_a0_0[1],address[1],Power).output()

        # this section gives the final switch configuration for all 8 register files
        self.dmux_10_a2_3 =  DMUX(self.dmux_00_a1_1[0],address[2],Power).output()
        self.final_load_path.append(self.dmux_10_a2_3)

        self.dmux_11_a2_4 =  DMUX(self.dmux_00_a1_1[1],address[2],Power).output()
        self.final_load_path.append(self.dmux_11_a2_4)

        self.dmux_20_a2_5 =  DMUX(self.dmux_01_a1_2[0],address[2],Power).output()
        self.final_load_path.append(self.dmux_20_a2_5)

        self.dmux_21_a2_6 =  DMUX(self.dmux_01_a1_2[1],address[2],Power).output()
        self.final_load_path.append(self.dmux_21_a2_6)

        # print("INIT: RAM4K-> final_load_path\n\n",self.final_load_path)

        # feeding the final configuration of load bits to the registers

        self.spliced_address_7 = [address[3],address[4],address[5],address[6],address[7],address[8],address[9],address[10],address[11]]

        self.ram512_i_7_30_8 = RAM512(Input,self.spliced_address_7,self.dmux_10_a2_3[0])
        self.output_value.append(self.ram512_i_7_30_8.output())

        self.ram512_i_7_31_9 = RAM512(Input,self.spliced_address_7,self.dmux_10_a2_3[1])
        self.output_value.append(self.ram512_i_7_31_9.output())

        self.ram512_i_7_40_10 = RAM512(Input,self.spliced_address_7,self.dmux_11_a2_4[0])
        self.output_value.append(self.ram512_i_7_40_10.output())

        self.ram512_i_7_41_11 = RAM512(Input,self.spliced_address_7,self.dmux_11_a2_4[1])
        self.output_value.append(self.ram512_i_7_41_11.output())

        self.ram512_i_7_50_12 = RAM512(Input,self.spliced_address_7,self.dmux_20_a2_5[0])
        self.output_value.append(self.ram512_i_7_50_12.output())

        self.ram512_i_7_51_13 = RAM512(Input,self.spliced_address_7,self.dmux_20_a2_5[1])
        self.output_value.append(self.ram512_i_7_51_13.output())

        self.ram512_i_7_60_14 = RAM512(Input,self.spliced_address_7,self.dmux_21_a2_6[0])
        self.output_value.append(self.ram512_i_7_60_14.output())

        self.ram512_i_7_61_15 = RAM512(Input,self.spliced_address_7,self.dmux_21_a2_6[1])
        self.output_value.append(self.ram512_i_7_61_15.output())

        # print("INIT: output: ",self.output_value)
    def update(self,Input,address,load,Power=1):
        # r512 consist of 8 RAM512 i.e, 3 more address bits  so total of 12 bits of address

        self.final_load_path = []
        self.output_value    = []

        self.dmux_l_a0_0  =  DMUX(load,address[0],Power).output()

        self.dmux_00_a1_1 =  DMUX(self.dmux_l_a0_0[0],address[1],Power).output()
        self.dmux_01_a1_2 =  DMUX(self.dmux_l_a0_0[1],address[1],Power).output()

        # this section gives the final switch configuration for all 8 register files
        self.dmux_10_a2_3 =  DMUX(self.dmux_00_a1_1[0],address[2],Power).output()
        self.final_load_path.append(self.dmux_10_a2_3)

        self.dmux_11_a2_4 =  DMUX(self.dmux_00_a1_1[1],address[2],Power).output()
        self.final_load_path.append(self.dmux_11_a2_4)

        self.dmux_20_a2_5 =  DMUX(self.dmux_01_a1_2[0],address[2],Power).output()
        self.final_load_path.append(self.dmux_20_a2_5)

        self.dmux_21_a2_6 =  DMUX(self.dmux_01_a1_2[1],address[2],Power).output()
        self.final_load_path.append(self.dmux_21_a2_6)

        # print("UPDATE: RAM4K-> final_load_path",self.final_load_path)

        # feeding the final configuration of load bits to the registers

        self.spliced_address_7 = [address[3],address[4],address[5],address[6],address[7],address[8],address[9],address[10],address[11]]

        self.ram512_i_7_30_8.update(Input,self.spliced_address_7,self.dmux_10_a2_3[0])
        self.output_value.append(self.ram512_i_7_30_8.output())

        self.ram512_i_7_31_9.update(Input,self.spliced_address_7,self.dmux_10_a2_3[1])
        self.output_value.append(self.ram512_i_7_31_9.output())

        self.ram512_i_7_40_10.update(Input,self.spliced_address_7,self.dmux_11_a2_4[0])
        self.output_value.append(self.ram512_i_7_40_10.output())

        self.ram512_i_7_41_11.update(Input,self.spliced_address_7,self.dmux_11_a2_4[1])
        self.output_value.append(self.ram512_i_7_41_11.output())

        self.ram512_i_7_50_12.update(Input,self.spliced_address_7,self.dmux_20_a2_5[0])
        self.output_value.append(self.ram512_i_7_50_12.output())

        self.ram512_i_7_51_13.update(Input,self.spliced_address_7,self.dmux_20_a2_5[1])
        self.output_value.append(self.ram512_i_7_51_13.output())

        self.ram512_i_7_60_14.update(Input,self.spliced_address_7,self.dmux_21_a2_6[0])
        self.output_value.append(self.ram512_i_7_60_14.output())

        self.ram512_i_7_61_15.update(Input,self.spliced_address_7,self.dmux_21_a2_6[1])
        self.output_value.append(self.ram512_i_7_61_15.output())

        # print("UPDATE: RAM512 -> output: ",self.output_value[5][6])

    def output(self):
        return self.output_value

class RAM16K:
    def __init__(self,Input,address,load,Power=1):
        # r16K consist of 4 RAM4K i.e, 2 more address bits  so total of 14 bits of address

        self.final_load_path = []
        self.output_value    = []

        self.dmux_l_a0_0  =  DMUX(load,address[0],Power).output()

        self.dmux_00_a1_1 =  DMUX(self.dmux_l_a0_0[0],address[1],Power).output()
        self.dmux_01_a1_2 =  DMUX(self.dmux_l_a0_0[1],address[1],Power).output()

        # print("INIT: RAM16K-> final_load_path\n\n",self.dmux_00_a1_1,self.dmux_01_a1_2)
        self.final_load_path.append(self.dmux_00_a1_1)
        self.final_load_path.append(self.dmux_01_a1_2)


        # print("INIT: RAM316K-> final_load_path\n\n",self.final_load_path)

        # feeding the final configuration of load bits to the registers

        self.spliced_address_7 = [address[2],address[3],address[4],address[5],address[6],address[7],address[8],address[9],address[10],address[11],address[12],address[13]]
        # self.spliced_address_7 = [address[3],address[4],address[5],address[6],address[7],address[8],address[9],address[10],address[11],address[12],address[13],address[14]]

        self.ram4k_i_7_10_8 = RAM4K(Input,self.spliced_address_7,self.dmux_00_a1_1[0])
        self.output_value.append(self.ram4k_i_7_10_8.output())

        self.ram4k_i_7_11_9 = RAM4K(Input,self.spliced_address_7,self.dmux_00_a1_1[1])
        self.output_value.append(self.ram4k_i_7_11_9.output())

        self.ram4k_i_7_20_10 = RAM4K(Input,self.spliced_address_7,self.dmux_01_a1_2[0])
        self.output_value.append(self.ram4k_i_7_20_10.output())

        self.ram4k_i_7_21_11 = RAM4K(Input,self.spliced_address_7,self.dmux_01_a1_2[1])
        self.output_value.append(self.ram4k_i_7_21_11.output())

    def update(self,Input,address,load,Power=1):
        # r16K consist of 4 RAM4K i.e, 2 more address bits  so total of 14 bits of address


        if (load):
            print("\nfromRAM loading value :",Input,"address: ",address,"\n");

        self.final_load_path = []
        self.output_value    = []

        self.dmux_l_a0_0  =  DMUX(load,address[0],Power).output()

        self.dmux_00_a1_1 =  DMUX(self.dmux_l_a0_0[0],address[1],Power).output()
        self.dmux_01_a1_2 =  DMUX(self.dmux_l_a0_0[1],address[1],Power).output()

        # print("INIT: RAM16K-> final_load_path\n\n",self.dmux_00_a1_1,self.dmux_01_a1_2)

        self.spliced_address_7 = [address[2],address[3],address[4],address[5],address[6],address[7],address[8],address[9],address[10],address[11],address[12],address[13]]

        self.final_load_path.append(self.dmux_00_a1_1)
        self.final_load_path.append(self.dmux_01_a1_2)

        self.ram4k_i_7_10_8.update(Input,self.spliced_address_7,self.dmux_00_a1_1[0])
        self.output_value.append(self.ram4k_i_7_10_8.output())

        self.ram4k_i_7_11_9.update(Input,self.spliced_address_7,self.dmux_00_a1_1[1])
        self.output_value.append(self.ram4k_i_7_11_9.output())

        self.ram4k_i_7_20_10.update(Input,self.spliced_address_7,self.dmux_01_a1_2[0])
        self.output_value.append(self.ram4k_i_7_20_10.output())

        self.ram4k_i_7_21_11.update(Input,self.spliced_address_7,self.dmux_01_a1_2[1])
        self.output_value.append(self.ram4k_i_7_21_11.output())

    def output(self):
        return self.output_value


class ROM32K:
    def __init__(self,Input,address,load,Power=1):
        # r32K consist of 8 RAM4K i.e, 3 more address bits  so total of 15 bits of address

        self.final_load_path = []
        self.output_value    = []

        self.dmux_l_a0_0  =  DMUX(load,address[0],Power).output()

        self.dmux_00_a1_1 =  DMUX(self.dmux_l_a0_0[0],address[1],Power).output()
 
        # this section gives the final switch configuration for all 8 register files
        self.dmux_10_a2_3 =  DMUX(self.dmux_00_a1_1[0],address[2],Power).output()
        self.final_load_path.append(self.dmux_10_a2_3)

        self.dmux_11_a2_4 =  DMUX(self.dmux_00_a1_1[1],address[2],Power).output()
        self.final_load_path.append(self.dmux_11_a2_4)

        self.dmux_20_a2_5 =  DMUX(self.dmux_01_a1_2[0],address[2],Power).output()
        self.final_load_path.append(self.dmux_20_a2_5)

        self.dmux_21_a2_6 =  DMUX(self.dmux_01_a1_2[1],address[2],Power).output()
        self.final_load_path.append(self.dmux_21_a2_6)


        self.dmux_01_a1_2 =  DMUX(self.dmux_l_a0_0[1],address[1],Power).output()

        # print("INIT: RAM32K-> final_load_path\n\n",self.final_load_path)

        # feeding the final configuration of load bits to the registers

        self.spliced_address_7 = [address[3],address[4],address[5],address[6],address[7],address[8],address[9],address[10],address[11],address[12],address[13],address[14]]

        self.ram4k_i_7_30_8 = RAM4K(Input,self.spliced_address_7,self.dmux_10_a2_3[0])
        self.output_value.append(self.ram4k_i_7_30_8.output())

        self.ram4k_i_7_31_9 = RAM4K(Input,self.spliced_address_7,self.dmux_10_a2_3[1])
        self.output_value.append(self.ram4k_i_7_31_9.output())

        self.ram4k_i_7_40_10 = RAM4K(Input,self.spliced_address_7,self.dmux_11_a2_4[0])
        self.output_value.append(self.ram4k_i_7_40_10.output())

        self.ram4k_i_7_41_11 = RAM4K(Input,self.spliced_address_7,self.dmux_11_a2_4[1])
        self.output_value.append(self.ram4k_i_7_41_11.output())

        self.ram4k_i_7_50_12 = RAM4K(Input,self.spliced_address_7,self.dmux_20_a2_5[0])
        self.output_value.append(self.ram4k_i_7_50_12.output())

        self.ram4k_i_7_51_13 = RAM4K(Input,self.spliced_address_7,self.dmux_20_a2_5[1])
        self.output_value.append(self.ram4k_i_7_51_13.output())

        self.ram4k_i_7_60_14 = RAM4K(Input,self.spliced_address_7,self.dmux_21_a2_6[0])
        self.output_value.append(self.ram4k_i_7_60_14.output())

        self.ram4k_i_7_61_15 = RAM4K(Input,self.spliced_address_7,self.dmux_21_a2_6[1])
        self.output_value.append(self.ram4k_i_7_61_15.output())

        # print("INIT: output: ",self.output_value)
    def update(self,Input,address,load,Power=1):
        # r32K consist of 8 RAM4K i.e, 3 more address bits  so total of 15 bits of address

        self.final_load_path = []
        self.output_value    = []

        self.dmux_l_a0_0  =  DMUX(load,address[0],Power).output()

        self.dmux_00_a1_1 =  DMUX(self.dmux_l_a0_0[0],address[1],Power).output()
        self.dmux_01_a1_2 =  DMUX(self.dmux_l_a0_0[1],address[1],Power).output()

        self.final_load_path.append(self.dmux_00_a1_1)
        self.final_load_path.append(self.dmux_00_a1_2)

        # this section gives the final switch configuration for all 8 register files
        self.dmux_10_a2_3 =  DMUX(self.dmux_00_a1_1[0],address[2],Power).output()
        self.final_load_path.append(self.dmux_10_a2_3)

        self.dmux_11_a2_4 =  DMUX(self.dmux_00_a1_1[1],address[2],Power).output()
        self.final_load_path.append(self.dmux_11_a2_4)

        self.dmux_20_a2_5 =  DMUX(self.dmux_01_a1_2[0],address[2],Power).output()
        self.final_load_path.append(self.dmux_20_a2_5)

        self.dmux_21_a2_6 =  DMUX(self.dmux_01_a1_2[1],address[2],Power).output()
        self.final_load_path.append(self.dmux_21_a2_6)



      
        # print("UPDATE: RAM32K-> final_load_path",self.final_load_path)

        # feeding the final configuration of load bits to the registers
       
        self.spliced_address_7 = [address[3],address[4],address[5],address[6],address[7],address[8],address[9],address[10],address[11],address[12],address[13],address[14]]
       
        self.ram4k_i_7_30_8.update(Input,self.spliced_address_7,self.dmux_10_a2_3[0])
        self.output_value.append(self.ram4k_i_7_30_8.output())

        self.ram4k_i_7_31_9.update(Input,self.spliced_address_7,self.dmux_10_a2_3[1])
        self.output_value.append(self.ram4k_i_7_31_9.output())

        self.ram4k_i_7_40_10.update(Input,self.spliced_address_7,self.dmux_11_a2_4[0])
        self.output_value.append(self.ram4k_i_7_40_10.output())

        self.ram4k_i_7_41_11.update(Input,self.spliced_address_7,self.dmux_11_a2_4[1])
        self.output_value.append(self.ram4k_i_7_41_11.output())

        self.ram4k_i_7_50_12.update(Input,self.spliced_address_7,self.dmux_20_a2_5[0])
        self.output_value.append(self.ram4k_i_7_50_12.output())

        self.ram4k_i_7_51_13.update(Input,self.spliced_address_7,self.dmux_20_a2_5[1])
        self.output_value.append(self.ram4k_i_7_51_13.output())

        self.ram4k_i_7_60_14.update(Input,self.spliced_address_7,self.dmux_21_a2_6[0])
        self.output_value.append(self.ram4k_i_7_60_14.output())

        self.ram4k_i_7_61_15.update(Input,self.spliced_address_7,self.dmux_21_a2_6[1])
        self.output_value.append(self.ram4k_i_7_61_15.output())

        # print("UPDATE: RAM16K -> output: ",self.output_value[5][6])

    def output(self):
        return self.output_value




#TODO : think about what naming convention to follow when using class arguments as inputs

#Fuckin Finall Creating CPU!!!
# CENTRAL PROCESSING UNIT!!!!!

class CPU:
    def __init__(self,Iin,Min,reset,Power=1):
        self.output_value = [];
        """
        input:  Min = Data from DataMemory (16)
                Iin = Instructions from InstructionMemory (16)
                reset (1)
        output: 
                Data To Data Memory:-
                    Mout (16)
                    Mwrite (1)
                    Maddress(15)
                
                Data To Instruction Memory:-
                    pc  (15)
        """

        # Maybe add Decoder later ( using Data Buses.)

        # So the input is going to be an array array


        # FOR A INSTRUCTION
#       //////_________\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        self.ALUout_tm1_0 = [0]*16; # Although there is no output of alu tm1 beacuse this init is the first time there is.

        # think of it as a data bus Iin[1 to 15]
        self.Input_1 = [0,Iin[1],Iin[2],Iin[3],Iin[4],Iin[5],Iin[6],Iin[7],Iin[8],Iin[9],Iin[10],Iin[11],Iin[12],Iin[13],Iin[14],Iin[15]];

        # FOR C INSTRUCTION
        self.Ctrlbit = [0,0,0,0,0,0,0]
        self.Jump    = [AND(Iin[0],Iin[13]).output(),
                        AND(Iin[0],Iin[14]).output(),
                        AND(Iin[0],Iin[15]).output()] #Jump Bits

        # NOTE: Maybe We have to seperate all of the components "AND(x,y).output" into seprate variable... but first we need to concrete our Style Guide for this code.

        #Calculating Comp Bits (only Appy to C instructions)
        self.Ctrlbit[0] = Iin[0] # first opcode tells weather its a A instruction or C instruction.
        self.Ctrlbit[1] = AND(Iin[0],Iin[10]).output() # if (Iin[0]) Ctrlbit[1] = Iin[10]
        self.Ctrlbit[2] = AND(Iin[0],Iin[11]).output()
        self.Ctrlbit[3] = AND(Iin[0],Iin[3]).output()  # "a" bit of C instruction
        self.Ctrlbit[4] = [AND(Iin[0],Iin[4]).output(),
                           AND(Iin[0],Iin[5]).output(),
                           AND(Iin[0],Iin[6]).output(),
                           AND(Iin[0],Iin[7]).output(),
                           AND(Iin[0],Iin[8]).output(),
                           AND(Iin[0],Iin[9]).output(),
                           ]  #All the computation bits will go in ALU
        self.Ctrlbit[5] = AND(Iin[0],Iin[12]).output()

        self.Ctrlbit[1]  = OR(NOT(Iin[0]).output(),self.Ctrlbit[1]).output() # if it is an A instruction then always set it to 1 else use the evaluated value of ctrlbit[1]

        self.mux16_1_0_c0_3 = Mux16(self.Input_1,self.ALUout_tm1_0,self.Ctrlbit[0],Power=1)

        # NOTE: when we initialize any register its initial output will go None which is not good for the further circuit insertion so we have to find a better way to do it ..... maybe set the initial output of registerst to 0?


        # A_register
        self.Reg16_3_c1_5 = Reg16(self.mux16_1_0_c0_3.output(),self.Ctrlbit[1],Power=1)

        print("A register: ",self.Reg16_3_c1_5.output());

        # D_register
        self.Reg16_0_c2_6   = Reg16(self.ALUout_tm1_0,self.Ctrlbit[2],Power=1)

        self.mux16_5_m_c3_7 = Mux16(self.Reg16_3_c1_5.output(),Min,self.Ctrlbit[3],Power=1)

        # Using ALU out[0] = evaluated value; out[1] = zr and out[2] = ng
        self.alu_6_7_c4_8 = ALU(self.Reg16_0_c2_6.output(),
                                self.mux16_5_m_c3_7.output(),
                                zx=self.Ctrlbit[4][0],
                                nx=self.Ctrlbit[4][1],
                                zy=self.Ctrlbit[4][2],
                                ny=self.Ctrlbit[4][3],
                                f=self.Ctrlbit[4][4],
                                no=self.Ctrlbit[4][5],
                                Power=1)



        #out : outM
        outM = self.alu_6_7_c4_8.output()["out"]
        self.output_value.append(outM)

        self.ALUout_tm1_0 = outM  # the output of this ALU will used as input in t+1 timestep;

        #out : writeM
        writeM = self.Ctrlbit[5]
        self.output_value.append(writeM)

        #out : addressM
        addressM = self.Reg16_3_c1_5.output()
        self.output_value.append(addressM)


        # Calculating the load bit of the program counter using Jump bits and the outputs of the ALU
        self.and_j1_82_9  = AND(self.Jump[0],self.alu_6_7_c4_8.output()["ng"])
        self.and_j2_81_10 = AND(self.Jump[1],self.alu_6_7_c4_8.output()["zr"])
        self.nor_81_82_11 = NOR(self.alu_6_7_c4_8.output()["zr"],self.alu_6_7_c4_8.output()["ng"])
        self.and_j3_10_12 = AND(self.Jump[2],self.nor_81_82_11.output())
        self.or_10_12_13  = OR(self.and_j2_81_10.output(),self.and_j3_10_12.output())
        self.or_9_13_14   = OR(self.and_j1_82_9.output(),self.or_10_12_13.output())
        self.Ctrlbit[6]   = self.or_9_13_14.output()


        """
        self.Ctrlbit[5] = OR(\
                            OR(\
                                AND(\
                                    AND(Iin[0],Iin[13]).output(),\
                                    NOR(self.alu_6_7_c4_8.output()["zr"],self.alu_6_7_c4_8.output()["ng"]).output()).output()\
                                    ,\
                                AND(\
                                    AND(Iin[0],Iin[13]).output(),\
                                    self.alu_6_7_c4_8.output()["zr"] \
                                    )\
                                    ).output()\
                                    , \
                                    AND(\
                                        AND(Iin[0],Iin[13]).output(),\
                                        self.alu_6_7_c4_8.output()["zr"]
                                    )\
                                    
                                    ).output()
        """
        self.programcounter_5_r_c5_9 = ProgramCounter(self.Reg16_3_c1_5.output(),self.Ctrlbit[6],NOT(self.Ctrlbit[6]).output(),reset,Power=1)

        # out : PC
        self.output_value.append(self.programcounter_5_r_c5_9.output())
        
    def update(self,Iin,Min,reset,Power=1):
        #INITIALIZATION
        self.output_value = []

        # for A instructions
        self.Input_1 = [0,Iin[1],Iin[2],Iin[3],Iin[4],Iin[5],Iin[6],Iin[7],Iin[8],Iin[9],Iin[10],Iin[11],Iin[12],Iin[13],Iin[14],Iin[15]];

        self.Ctrlbit = [0,0,0,0,0,0,0]
        self.Jump    = [AND(Iin[0],Iin[13]).output(),
                        AND(Iin[0],Iin[14]).output(),
                        AND(Iin[0],Iin[15]).output(),
                        ] #Jump Bits

        # if (Iin[0] == 0)1 else self.Ctrlbit[1]
        #Calculating Comp Bits
        self.Ctrlbit[0] = Iin[0] # first opcode tells weather its a A instruction or C instruction.
        self.Ctrlbit[1] = OR(  (NOT(Iin[0]).output())  , (AND(Iin[0],Iin[10]).output())  ).output() # if (Iin[0]) Ctrlbit[1] = Iin[10]
        self.Ctrlbit[2] = AND(Iin[0],Iin[11]).output()
        self.Ctrlbit[3] = AND(Iin[0],Iin[3]).output()  # "a" bit of C instruction
        self.Ctrlbit[4] = [AND(Iin[0],Iin[4]).output(),
                           AND(Iin[0],Iin[5]).output(),
                           AND(Iin[0],Iin[6]).output(),
                           AND(Iin[0],Iin[7]).output(),
                           AND(Iin[0],Iin[8]).output(),
                           AND(Iin[0],Iin[9]).output(),
                           ]  #All the computation bits will go in ALU
        self.Ctrlbit[5]  = AND(Iin[0],Iin[12]).output()
        #NOTE: self.Ctrlbit[6] required the output of ALU to calcuate the value, so we will do it later on, when we got the ALU output


        self.mux16_0_1_c0_3 = Mux16(Iin,self.ALUout_tm1_0,self.Ctrlbit[0],Power=1)


        print("-------------------inside CPU------------------")


        #######################################

        # all the sequential logic Gates should be "Ticked" samultaniously :D
        # A-register
        self.Reg16_3_c1_5.update(self.mux16_0_1_c0_3.output(),self.Ctrlbit[1],Power=1)

        # D-register 
        self.Reg16_0_c2_6.update(self.ALUout_tm1_0,self.Ctrlbit[2],Power=1)
        
        self.mux16_5_m_c3_7 = Mux16(self.Reg16_3_c1_5.output(),Min,self.Ctrlbit[3],Power=1)#using the t-1 A-register.

        # Using ALU out[0] = evaluated value; out[1] = zr and out[2] = ng
        self.alu_6_7_c4_8 = ALU(self.Reg16_0_c2_6.output(),
                                self.mux16_5_m_c3_7.output(),
                                zx=self.Ctrlbit[4][0],
                                nx=self.Ctrlbit[4][1],
                                zy=self.Ctrlbit[4][2],
                                ny=self.Ctrlbit[4][3],
                                f=self.Ctrlbit[4][4],
                                no=self.Ctrlbit[4][5],
                                Power=1)


        #out : outM
        outM = self.alu_6_7_c4_8.output()["out"]

        self.ALUout_tm1_0 = outM;


        print("\nA_register:",self.Reg16_3_c1_5.output());
        print("D_register:",self.Reg16_0_c2_6.output());

        print("\n\n###########################################################")
        print("D_input:",self.Reg16_0_c2_6.output());
        print("M/A_input:",self.mux16_5_m_c3_7.output());
        print("ALU_out:",outM);
        print("zr: ",self.alu_6_7_c4_8.output()["zr"],"ng: ",self.alu_6_7_c4_8.output()["ng"])
        print("###########################################################\n")

        print("-------------------outside CPU------------------")

        self.output_value.append(outM)

        #out : writeM
        self.output_value.append(self.Ctrlbit[5])

        #out : addressM
        addressM = self.Reg16_3_c1_5.output()
        self.output_value.append(addressM)


        # Calculating the load bit of the program counter using Jump bits and the outputs of the ALU
        self.and_j1_82_9  = AND(self.Jump[0],self.alu_6_7_c4_8.output()["ng"])
        self.and_j2_81_10 = AND(self.Jump[1],self.alu_6_7_c4_8.output()["zr"])
        self.nor_81_82_11 = NOR(self.alu_6_7_c4_8.output()["zr"],self.alu_6_7_c4_8.output()["ng"])
        self.and_j3_10_12 = AND(self.Jump[2],self.nor_81_82_11.output())
        self.or_10_12_13  = OR(self.and_j2_81_10.output(),self.and_j3_10_12.output())
        self.or_9_13_14   = OR(self.and_j1_82_9.output(),self.or_10_12_13.output())
        self.Ctrlbit[6]   = self.or_9_13_14.output()
        print("self.CTRLBIT[6]",self.Ctrlbit[6])

        if (self.Ctrlbit[6] == 1):
            print("ksadjflksjdlkfjaslkdjfasdfskfjaskdjfklsjdflkjsdlkjfklasjlkfjlksdajflksjadlfjslkadjfklsdjfklasjkdfjskladjfklasjdkflaskdjflksjadkfjalskdjflkasjdlkfjsaldkfjlaksdjflksajdfkasjdlkfjaslkdjlfksajdlfkajsldkfjaslkfjlsjfskldjflskadfjlskdfjlksdjflsdkj")

        self.programcounter_5_r_c5_9.update(self.Reg16_3_c1_5.output(),self.Ctrlbit[6],NOT(self.Ctrlbit[6]).output(),reset,Power=1)

        #out : PC
        self.output_value.append(self.programcounter_5_r_c5_9.output())

        # print("\n self.mux16_0_1_c0_3: ",self.mux16_0_1_c0_3.output(),self.Ctrlbit[1]);
        # A_register  TODO: always add the value inside A regester when we have A instruction.

        # self.Reg16_3_c1_5.update([0]*16,0,Power=1);
        # print("\n\nA register: ",self.Reg16_3_c1_5.output())

        # # D_register
        # self.Reg16_0_c2_6.update([0]*16,0,Power=1)
        # print("D register: ",self.Reg16_0_c2_6.output(),"\n\n")

    def output(self):
        return self.output_value; 

# PUTTING IT ALL TOGETHER!!!! FINALLY CREATING A  COMPUTER!!!!!!

class CPU2:
    def __init__(self,Iin,Min,reset,Power=1):
        self.output_value = [];
        """
        input:  Min = Data from DataMemory (16)
                Iin = Instructions from InstructionMemory (16)
                reset (1)
        output: 
                Data To Data Memory:-
                    Mout (16)
                    Mwrite (1)
                    Maddress(15)
                
                Data To Instruction Memory:-
                    pc  (15)
        """

        # Maybe add Decoder later ( using Data Buses.)

        # So the input is going to be an array array


        # FOR A INSTRUCTION
#       //////_________\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        self.ALUout_tm1_0 = [0]*16; # Although there is no output of alu tm1 beacuse this init is the first time there is.

        # think of it as a data bus Iin[1 to 15]
        self.Input_1 = [0,Iin[1],Iin[2],Iin[3],Iin[4],Iin[5],Iin[6],Iin[7],Iin[8],Iin[9],Iin[10],Iin[11],Iin[12],Iin[13],Iin[14],Iin[15]];

        # FOR C INSTRUCTION
        self.Ctrlbit = [0,0,0,0,0,0,0]
        self.Jump    = [AND(Iin[0],Iin[13]).output(),
                        AND(Iin[0],Iin[14]).output(),
                        AND(Iin[0],Iin[15]).output()] #Jump Bits

        # NOTE: Maybe We have to seperate all of the components "AND(x,y).output" into seprate variable... but first we need to concrete our Style Guide for this code.

        #Calculating Comp Bits (only Appy to C instructions)
        self.Ctrlbit[0] = AND(Iin[0],Iin[10]).output() # first opcode tells weather its a A instruction or C instruction.
        self.Ctrlbit[1] = AND(Iin[0],Iin[10]).output() # if (Iin[0]) Ctrlbit[1] = Iin[10]
        self.Ctrlbit[2] = AND(Iin[0],Iin[11]).output()
        self.Ctrlbit[3] = AND(Iin[0],Iin[3]).output()  # "a" bit of C instruction
        self.Ctrlbit[4] = [AND(Iin[0],Iin[4]).output(),
                           AND(Iin[0],Iin[5]).output(),
                           AND(Iin[0],Iin[6]).output(),
                           AND(Iin[0],Iin[7]).output(),
                           AND(Iin[0],Iin[8]).output(),
                           AND(Iin[0],Iin[9]).output(),
                           ]  #All the computation bits will go in ALU
        self.Ctrlbit[5] = AND(Iin[0],Iin[12]).output()

        self.Ctrlbit[1]  = OR(NOT(Iin[0]).output(),self.Ctrlbit[1]).output() # if it is an A instruction then always set it to 1 else use the evaluated value of ctrlbit[1]

        self.mux16_1_0_c0_3 = Mux16(self.Input_1,self.ALUout_tm1_0,self.Ctrlbit[0],Power=1)

        # A_register
        self.Reg16_3_c1_5 = Reg16(self.mux16_1_0_c0_3.output(),self.Ctrlbit[1],Power=1)

        print("A register: ",self.Reg16_3_c1_5.output());
        # D_register
        self.Reg16_0_c2_6   = Reg16(self.ALUout_tm1_0,self.Ctrlbit[2],Power=1)

        # M/A register
        self.mux16_5_m_c3_7 = Mux16(self.Reg16_3_c1_5.output(),Min,self.Ctrlbit[3],Power=1)
        # self.mux16_5_m_c3_7 = Mux16([0]*16,Min,self.Ctrlbit[3],Power=1)
        print("M/Aout: ",self.mux16_5_m_c3_7.output())

        # Using ALU out[0] = evaluated value; out[1] = zr and out[2] = ng
        self.alu_6_7_c4_8 = ALU(self.Reg16_0_c2_6.output(),
                                self.mux16_5_m_c3_7.output(),
                                zx=self.Ctrlbit[4][0],
                                nx=self.Ctrlbit[4][1],
                                zy=self.Ctrlbit[4][2],
                                ny=self.Ctrlbit[4][3],
                                f=self.Ctrlbit[4][4],
                                no=self.Ctrlbit[4][5],
                                Power=1)



        #out : outM
        outM = self.alu_6_7_c4_8.output()["out"]
        self.output_value.append(outM)

        self.ALUout_tm1_0 = outM  # the output of this ALU will used as input in t+1 timestep;

        #out : writeM
        writeM = self.Ctrlbit[5]
        self.output_value.append(writeM)

        #out : addressM
        addressM = self.Reg16_3_c1_5.output()
        self.output_value.append(addressM)


        # Calculating the load bit of the program counter using Jump bits and the outputs of the ALU
        self.and_j1_82_9  = AND(self.Jump[0],self.alu_6_7_c4_8.output()["ng"])
        self.and_j2_81_10 = AND(self.Jump[1],self.alu_6_7_c4_8.output()["zr"])
        self.nor_81_82_11 = NOR(self.alu_6_7_c4_8.output()["zr"],self.alu_6_7_c4_8.output()["ng"])
        self.and_j3_10_12 = AND(self.Jump[2],self.nor_81_82_11.output())
        self.or_10_12_13  = OR(self.and_j2_81_10.output(),self.and_j3_10_12.output())
        self.or_9_13_14   = OR(self.and_j1_82_9.output(),self.or_10_12_13.output())
        self.Ctrlbit[6]   = self.or_9_13_14.output()


        """
        self.Ctrlbit[5] = OR(\
                            OR(\
                                AND(\
                                    AND(Iin[0],Iin[13]).output(),\
                                    NOR(self.alu_6_7_c4_8.output()["zr"],self.alu_6_7_c4_8.output()["ng"]).output()).output()\
                                    ,\
                                AND(\
                                    AND(Iin[0],Iin[13]).output(),\
                                    self.alu_6_7_c4_8.output()["zr"] \
                                    )\
                                    ).output()\
                                    , \
                                    AND(\
                                        AND(Iin[0],Iin[13]).output(),\
                                        self.alu_6_7_c4_8.output()["zr"]
                                    )\
                                    
                                    ).output()
        """
        self.programcounter_5_r_c5_9 = ProgramCounter(self.Reg16_3_c1_5.output(),self.Ctrlbit[6],NOT(self.Ctrlbit[6]).output(),reset,Power=1)

        # updating the programcounter in the init because as we know the output of the program counter will take effect @ t+1 but we are ignoring the first time step of initializing and going straight to t=1
        # self.programcounter_5_r_c5_9.update()

        # out : PC
        self.output_value.append(self.programcounter_5_r_c5_9.output())
        
    def update(self,Iin,Min,reset,Power=1):
        #INITIALIZATION
        self.output_value = []

        print("cpu_inI: ",Iin,Iin[0],"cpu_inM: ",Min);

        # for A instructions
        self.Input_1 = [0,Iin[1],Iin[2],Iin[3],Iin[4],Iin[5],Iin[6],Iin[7],Iin[8],Iin[9],Iin[10],Iin[11],Iin[12],Iin[13],Iin[14],Iin[15]];

        self.Ctrlbit = [0,0,0,0,0,0,0]
        self.Jump    = [AND(Iin[0],Iin[13]).output(),
                        AND(Iin[0],Iin[14]).output(),
                        AND(Iin[0],Iin[15]).output(),
                        ] #Jump Bits

        # if (Iin[0] == 0)1 else self.Ctrlbit[1]
        #Calculating Comp Bits
        self.Ctrlbit[0] = AND(Iin[0],Iin[10]).output() 
        self.Ctrlbit[1] = OR(  (NOT(Iin[0]).output())  , (AND(Iin[0],Iin[10]).output())  ).output() # if (Iin[0]) Ctrlbit[1] = Iin[10] for A-register load bit
        self.Ctrlbit[2] = AND(Iin[0],Iin[11]).output() # for D-register load bit
        self.Ctrlbit[3] = AND(Iin[0],Iin[3]).output()  # "a" bit of C instruction for M/A Mux
        self.Ctrlbit[4] = [AND(Iin[0],Iin[4]).output(),
                           AND(Iin[0],Iin[5]).output(),
                           AND(Iin[0],Iin[6]).output(),
                           AND(Iin[0],Iin[7]).output(),
                           AND(Iin[0],Iin[8]).output(),
                           AND(Iin[0],Iin[9]).output(),
                           ]  #All the computation bits will go in ALU

        self.Ctrlbit[5]  = AND(Iin[0],Iin[12]).output()
        #NOTE: self.Ctrlbit[6] required the output of ALU to calcuate the value, so we will do it later on, when we got the ALU output


        self.Ctrlbit[1]  = OR(NOT(Iin[0]).output(),self.Ctrlbit[1]).output() # if it is an A instruction then always set it to 1 else use the evaluated value of ctrlbit[1]

        self.mux16_1_0_c0_3 = Mux16(self.Input_1,self.ALUout_tm1_0,self.Ctrlbit[0],Power=1)

        # # A_register
        # self.Reg16_3_c1_5.update(self.mux16_1_0_c0_3.output(),self.Ctrlbit[1],Power=1)


        # M/A register
        self.mux16_5_m_c3_7 = Mux16(self.Reg16_3_c1_5.output(),Min,self.Ctrlbit[3],Power=1)



        self.mux16_0_1_c0_3 = Mux16(Iin,self.ALUout_tm1_0,self.Ctrlbit[0],Power=1)

        # A_register
        self.Reg16_3_c1_5.update(self.mux16_1_0_c0_3.output(),self.Ctrlbit[1],Power=1)

        print("-------------------inside CPU------------------")


        #######################################

        # Using ALU out[0] = evaluated value; out[1] = zr and out[2] = ng
        self.alu_6_7_c4_8 = ALU(self.Reg16_0_c2_6.output(),
                                self.mux16_5_m_c3_7.output(),
                                zx=self.Ctrlbit[4][0],
                                nx=self.Ctrlbit[4][1],
                                zy=self.Ctrlbit[4][2],
                                ny=self.Ctrlbit[4][3],
                                f=self.Ctrlbit[4][4],
                                no=self.Ctrlbit[4][5],
                                Power=1)


        #out : outM
        outM = self.alu_6_7_c4_8.output()["out"]

        self.ALUout_tm1_0 = outM;


        # D_register
        self.Reg16_0_c2_6.update(self.ALUout_tm1_0,self.Ctrlbit[2],Power=1)

        print("\nA_register:",self.Reg16_3_c1_5.output());
        print("D_register:",self.Reg16_0_c2_6.output());

        print("\n\n###########################################################")
        print("D_input:",self.Reg16_0_c2_6.output());
        print("M/A_input:",self.mux16_5_m_c3_7.output());
        print("ALU input: ",self.Ctrlbit[4],"ALU_out:",outM);
        print("zr: ",self.alu_6_7_c4_8.output()["zr"],"ng: ",self.alu_6_7_c4_8.output()["ng"])
        print("###########################################################\n")

        print("-------------------outside CPU------------------")

        self.output_value.append(outM)

        #out : writeM
        self.output_value.append(self.Ctrlbit[5])

        #out : addressM
        addressM = self.Reg16_3_c1_5.output()
        self.output_value.append(addressM)


        # Calculating the load bit of the program counter using Jump bits and the outputs of the ALU
        self.and_j1_82_9  = AND(self.Jump[0],self.alu_6_7_c4_8.output()["ng"])
        self.and_j2_81_10 = AND(self.Jump[1],self.alu_6_7_c4_8.output()["zr"])
        self.nor_81_82_11 = NOR(self.alu_6_7_c4_8.output()["zr"],self.alu_6_7_c4_8.output()["ng"])
        self.and_j3_10_12 = AND(self.Jump[2],self.nor_81_82_11.output())
        self.or_10_12_13  = OR(self.and_j2_81_10.output(),self.and_j3_10_12.output())
        self.or_9_13_14   = OR(self.and_j1_82_9.output(),self.or_10_12_13.output())
        self.Ctrlbit[6]   = self.or_9_13_14.output()
        print("self.CTRLBIT[6]",self.Ctrlbit[6])

        if (self.Ctrlbit[6] == 1):
            print("ksadjflksjdlkfjaslkdjfasdfskfjaskdjfklsjdflkjsdlkjfklasjlkfjlksdajflksjadlfjslkadjfklsdjfklasjkdfjskladjfklasjdkflaskdjflksjadkfjalskdjflkasjdlkfjsaldkfjlaksdjflksajdfkasjdlkfjaslkdjlfksajdlfkajsldkfjaslkfjlsjfskldjflskadfjlskdfjlksdjflsdkj")

        self.programcounter_5_r_c5_9.update(self.Reg16_3_c1_5.output(),self.Ctrlbit[6],NOT(self.Ctrlbit[6]).output(),reset,Power=1)

        #out : PC
        self.output_value.append(self.programcounter_5_r_c5_9.output())

        # print("\n self.mux16_0_1_c0_3: ",self.mux16_0_1_c0_3.output(),self.Ctrlbit[1]);
        # A_register  TODO: always add the value inside A regester when we have A instruction.

        # self.Reg16_3_c1_5.update([0]*16,0,Power=1);
        # print("\n\nA register: ",self.Reg16_3_c1_5.output())

        # # D_register
        # self.Reg16_0_c2_6.update([0]*16,0,Power=1)
        # print("D register: ",self.Reg16_0_c2_6.output(),"\n\n")

    def output(self):
        return self.output_value; 


class CPU3:
    def __init__(self,Iin,Min,reset,Power=1):
        self.output_value = [];
        """
        input:  Min = Data from DataMemory (16)
                Iin = Instructions from InstructionMemory (16)
                reset (1)
        output: 
                Data To Data Memory:-
                    Mout (16)
                    Mwrite (1)
                    Maddress(15)
                
                Data To Instruction Memory:-
                    pc  (15)
        """

        # Maybe add Decoder later ( using Data Buses.)

        # So the input is going to be an array array


        # FOR A INSTRUCTION
#       //////_________\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        self.ALUout_tm1_0 = [0]*16; # Although there is no output of alu tm1 beacuse this init is the first time there is.

        # think of it as a data bus Iin[1 to 15]
        self.Input_1 = [0,Iin[1],Iin[2],Iin[3],Iin[4],Iin[5],Iin[6],Iin[7],Iin[8],Iin[9],Iin[10],Iin[11],Iin[12],Iin[13],Iin[14],Iin[15]];

        # FOR C INSTRUCTION
        self.Ctrlbit = [0,0,0,0,0,0,0]
        self.Jump    = [AND(Iin[0],Iin[13]).output(),
                        AND(Iin[0],Iin[14]).output(),
                        AND(Iin[0],Iin[15]).output()] #Jump Bits

        # NOTE: Maybe We have to seperate all of the components "AND(x,y).output" into seprate variable... but first we need to concrete our Style Guide for this code.

        #Calculating Comp Bits (only Appy to C instructions)
        self.Ctrlbit[0] = AND(Iin[0],Iin[10]).output() # first opcode tells weather its a A instruction or C instruction.
        self.Ctrlbit[1] = AND(Iin[0],Iin[10]).output() # if (Iin[0]) Ctrlbit[1] = Iin[10]
        self.Ctrlbit[2] = AND(Iin[0],Iin[11]).output()
        self.Ctrlbit[3] = AND(Iin[0],Iin[3]).output()  # "a" bit of C instruction
        self.Ctrlbit[4] = [AND(Iin[0],Iin[4]).output(),
                           AND(Iin[0],Iin[5]).output(),
                           AND(Iin[0],Iin[6]).output(),
                           AND(Iin[0],Iin[7]).output(),
                           AND(Iin[0],Iin[8]).output(),
                           AND(Iin[0],Iin[9]).output(),
                           ]  #All the computation bits will go in ALU
        self.Ctrlbit[5] = AND(Iin[0],Iin[12]).output()

        self.Ctrlbit[1]  = OR(NOT(Iin[0]).output(),self.Ctrlbit[1]).output() # if it is an A instruction then always set it to 1 else use the evaluated value of ctrlbit[1]

        self.mux16_1_0_c0_3 = Mux16(self.Input_1,self.ALUout_tm1_0,self.Ctrlbit[0],Power=1)

        # A_register
        self.Reg16_3_c1_5 = Reg16(self.mux16_1_0_c0_3.output(),self.Ctrlbit[1],Power=1)

        print("A register: ",self.Reg16_3_c1_5.output());
        # D_register
        self.Reg16_0_c2_6   = Reg16(self.ALUout_tm1_0,self.Ctrlbit[2],Power=1)

        # M/A register
        self.mux16_5_m_c3_7 = Mux16(self.Reg16_3_c1_5.output(),Min,self.Ctrlbit[3],Power=1)
        # self.mux16_5_m_c3_7 = Mux16([0]*16,Min,self.Ctrlbit[3],Power=1)
        print("M/Aout: ",self.mux16_5_m_c3_7.output())

        # Using ALU out[0] = evaluated value; out[1] = zr and out[2] = ng
        self.alu_6_7_c4_8 = ALU(self.Reg16_0_c2_6.output(),
                                self.mux16_5_m_c3_7.output(),
                                zx=self.Ctrlbit[4][0],
                                nx=self.Ctrlbit[4][1],
                                zy=self.Ctrlbit[4][2],
                                ny=self.Ctrlbit[4][3],
                                f=self.Ctrlbit[4][4],
                                no=self.Ctrlbit[4][5],
                                Power=1)



        #out : outM
        outM = self.alu_6_7_c4_8.output()["out"]
        self.output_value.append(outM)

        self.ALUout_tm1_0 = outM  # the output of this ALU will used as input in t+1 timestep;

        #out : writeM
        writeM = self.Ctrlbit[5]
        self.output_value.append(writeM)

        #out : addressM
        addressM = self.Reg16_3_c1_5.output()
        self.output_value.append(addressM)


        # Calculating the load bit of the program counter using Jump bits and the outputs of the ALU
        self.and_j1_82_9  = AND(self.Jump[0],self.alu_6_7_c4_8.output()["ng"])
        self.and_j2_81_10 = AND(self.Jump[1],self.alu_6_7_c4_8.output()["zr"])
        self.nor_81_82_11 = NOR(self.alu_6_7_c4_8.output()["zr"],self.alu_6_7_c4_8.output()["ng"])
        self.and_j3_10_12 = AND(self.Jump[2],self.nor_81_82_11.output())
        self.or_10_12_13  = OR(self.and_j2_81_10.output(),self.and_j3_10_12.output())
        self.or_9_13_14   = OR(self.and_j1_82_9.output(),self.or_10_12_13.output())
        self.Ctrlbit[6]   = self.or_9_13_14.output()


        """
        self.Ctrlbit[5] = OR(\
                            OR(\
                                AND(\
                                    AND(Iin[0],Iin[13]).output(),\
                                    NOR(self.alu_6_7_c4_8.output()["zr"],self.alu_6_7_c4_8.output()["ng"]).output()).output()\
                                    ,\
                                AND(\
                                    AND(Iin[0],Iin[13]).output(),\
                                    self.alu_6_7_c4_8.output()["zr"] \
                                    )\
                                    ).output()\
                                    , \
                                    AND(\
                                        AND(Iin[0],Iin[13]).output(),\
                                        self.alu_6_7_c4_8.output()["zr"]
                                    )\
                                    
                                    ).output()
        """
        self.programcounter_5_r_c5_9 = ProgramCounter(self.Reg16_3_c1_5.output(),self.Ctrlbit[6],NOT(self.Ctrlbit[6]).output(),reset,Power=1)

        # updating the programcounter in the init because as we know the output of the program counter will take effect @ t+1 but we are ignoring the first time step of initializing and going straight to t=1
        # self.programcounter_5_r_c5_9.update()

        # out : PC
        self.output_value.append(self.programcounter_5_r_c5_9.output())
        
    def update(self,Iin,Min,reset,Power=1):
        #INITIALIZATION
        self.output_value = []

        print("cpu_inI: ",Iin,Iin[0],"cpu_inM: ",Min);

        # for A instructions
        self.Input_1 = [0,Iin[1],Iin[2],Iin[3],Iin[4],Iin[5],Iin[6],Iin[7],Iin[8],Iin[9],Iin[10],Iin[11],Iin[12],Iin[13],Iin[14],Iin[15]];

        self.Ctrlbit = [0,0,0,0,0,0,0]
        self.Jump    = [AND(Iin[0],Iin[13]).output(),
                        AND(Iin[0],Iin[14]).output(),
                        AND(Iin[0],Iin[15]).output(),
                        ] #Jump Bits

        # if (Iin[0] == 0)1 else self.Ctrlbit[1]
        #Calculating Comp Bits
        self.Ctrlbit[0] = AND(Iin[0],Iin[10]).output() 
        self.Ctrlbit[1] = OR(  (NOT(Iin[0]).output())  , (AND(Iin[0],Iin[10]).output())  ).output() # if (Iin[0]) Ctrlbit[1] = Iin[10] for A-register load bit
        self.Ctrlbit[2] = AND(Iin[0],Iin[11]).output() # for D-register load bit
        self.Ctrlbit[3] = AND(Iin[0],Iin[3]).output()  # "a" bit of C instruction for M/A Mux
        self.Ctrlbit[4] = [AND(Iin[0],Iin[4]).output(),
                           AND(Iin[0],Iin[5]).output(),
                           AND(Iin[0],Iin[6]).output(),
                           AND(Iin[0],Iin[7]).output(),
                           AND(Iin[0],Iin[8]).output(),
                           AND(Iin[0],Iin[9]).output(),
                           ]  #All the computation bits will go in ALU

        self.Ctrlbit[5]  = AND(Iin[0],Iin[12]).output()
        #NOTE: self.Ctrlbit[6] required the output of ALU to calcuate the value, so we will do it later on, when we got the ALU output


        self.Ctrlbit[1]  = OR(NOT(Iin[0]).output(),self.Ctrlbit[1]).output() # if it is an A instruction then always set it to 1 else use the evaluated value of ctrlbit[1]



        # # A_register
        # self.Reg16_3_c1_5.update(self.mux16_1_0_c0_3.output(),self.Ctrlbit[1],Power=1)

        # M/A register
        self.mux16_5_m_c3_7 = Mux16(self.Reg16_3_c1_5.output(),Min,self.Ctrlbit[3],Power=1)


        # Printing t-1 outputs
        print("-------------------inside CPU------------------")

        print("\n\n###########################################################")
        print("D_input:",self.Reg16_0_c2_6.output());
        print("M/A_input:",self.mux16_5_m_c3_7.output());
        print("ALU input: ",self.Ctrlbit[4],"ALU_out:",self.ALUout_tm1_0);
        # print("zr: ",self.ALUout_tm1_0.output()["zr"],"ng: ",self.ALUout_tm1_0.output()["ng"])
        print("###########################################################\n")


        #######################################

        # Using ALU out[0] = evaluated value; out[1] = zr and out[2] = ng
        self.alu_6_7_c4_8 = ALU(self.Reg16_0_c2_6.output(),
                                self.mux16_5_m_c3_7.output(),
                                zx=self.Ctrlbit[4][0],
                                nx=self.Ctrlbit[4][1],
                                zy=self.Ctrlbit[4][2],
                                ny=self.Ctrlbit[4][3],
                                f=self.Ctrlbit[4][4],
                                no=self.Ctrlbit[4][5],
                                Power=1)


        #out : outM
        outM = self.alu_6_7_c4_8.output()["out"]

        self.ALUout_tm1_0 = outM;

        self.mux16_1_0_c0_3 = Mux16(self.Input_1,self.ALUout_tm1_0,self.Ctrlbit[0],Power=1)

        self.mux16_0_1_c0_3 = Mux16(Iin,self.ALUout_tm1_0,self.Ctrlbit[0],Power=1)

        # A_register
        self.Reg16_3_c1_5.update(self.mux16_1_0_c0_3.output(),self.Ctrlbit[1],Power=1)



        # D_register
        self.Reg16_0_c2_6.update(self.ALUout_tm1_0,self.Ctrlbit[2],Power=1)

        print("\nA_register:",self.Reg16_3_c1_5.output());
        print("D_register:",self.Reg16_0_c2_6.output());
        print("-------------------outside CPU------------------")


        self.output_value.append(outM)

        #out : writeM
        self.output_value.append(self.Ctrlbit[5])

        #out : addressM
        addressM = self.Reg16_3_c1_5.output()
        self.output_value.append(addressM)


        # Calculating the load bit of the program counter using Jump bits and the outputs of the ALU
        self.and_j1_82_9  = AND(self.Jump[0],self.alu_6_7_c4_8.output()["ng"])
        self.and_j2_81_10 = AND(self.Jump[1],self.alu_6_7_c4_8.output()["zr"])
        self.nor_81_82_11 = NOR(self.alu_6_7_c4_8.output()["zr"],self.alu_6_7_c4_8.output()["ng"])
        self.and_j3_10_12 = AND(self.Jump[2],self.nor_81_82_11.output())
        self.or_10_12_13  = OR(self.and_j2_81_10.output(),self.and_j3_10_12.output())
        self.or_9_13_14   = OR(self.and_j1_82_9.output(),self.or_10_12_13.output())
        self.Ctrlbit[6]   = self.or_9_13_14.output()
        print("self.CTRLBIT[6]",self.Ctrlbit[6])

        if (self.Ctrlbit[6] == 1):
            print("ksadjflksjdlkfjaslkdjfasdfskfjaskdjfklsjdflkjsdlkjfklasjlkfjlksdajflksjadlfjslkadjfklsdjfklasjkdfjskladjfklasjdkflaskdjflksjadkfjalskdjflkasjdlkfjsaldkfjlaksdjflksajdfkasjdlkfjaslkdjlfksajdlfkajsldkfjaslkfjlsjfskldjflskadfjlskdfjlksdjflsdkj")

        self.programcounter_5_r_c5_9.update(self.Reg16_3_c1_5.output(),self.Ctrlbit[6],NOT(self.Ctrlbit[6]).output(),reset,Power=1)

        #out : PC
        self.output_value.append(self.programcounter_5_r_c5_9.output())

        # print("\n self.mux16_0_1_c0_3: ",self.mux16_0_1_c0_3.output(),self.Ctrlbit[1]);
        # A_register  TODO: always add the value inside A regester when we have A instruction.

        # self.Reg16_3_c1_5.update([0]*16,0,Power=1);
        # print("\n\nA register: ",self.Reg16_3_c1_5.output())

        # # D_register
        # self.Reg16_0_c2_6.update([0]*16,0,Power=1)
        # print("D register: ",self.Reg16_0_c2_6.output(),"\n\n")

    def output(self):
        return self.output_value; 

class CPUfromhdl:
    # out: outM[16],writeM,addressM[15],pc[15]

    def __init__(self,Iin , Min,reset =0,Power=1):
        self.output_values = []

        self.ALUout = [0]*16 # we dont know ALUout just yet so we create a dummy ALUout

        self.Ainstruction = NOT(Iin[15],Power=1).output()
        self.Cinstruction = NOT(self.Ainstruction,Power=1).output()

        self.ALUtoA = AND(self.Cinstruction,Iin[10]).output() # C-instruction and destination to A-register?
        self.Aregin = Mux16(Iin,self.ALUout,self.ALUtoA).output()

        #for A register
        self.loadA = OR(self.Ainstruction,self.ALUtoA).output()
        self.Aregister  = Reg16(self.Aregin,self.loadA)

        self.Aout = self.Aregister.output()

        #for A/M Multiplexer 
        self.AMout = Mux16(self.Aout,Min,Iin[3]).output()

        #for D register
        self.loadD = AND(self.Cinstruction,Iin[11]).output()
        self.Dregister = Reg16(self.ALUout,self.loadD)
        self.Dout = self.Dregister.output()

        #ALU
        self.MyALU  = ALU(self.Dout,self.AMout,Iin[4],Iin[5],Iin[6],Iin[7],Iin[8],Iin[9]).output()
        self.ALUout = self.MyALU["out"]
        self.ZRout  = self.MyALU["zr"]
        self.NGout  = self.MyALU["ng"]

        #Set outputs for Writing memory
        self.CpuOut_outM = self.ALUout;
        self.CpuOut_writeM = Iin[12];
        self.CpuOut_addressM = self.Aout; # i.e, A register

        #calculate ProgramCounter output
        jeq = AND(self.ZRout,Iin[14],Power=1).output()
        jlt = AND(self.NGout,Iin[13],Power=1).output()
        zeroOrNeg = OR(self.ZRout,self.NGout).output()
        positive = NOT(zeroOrNeg).output()
        jgt = AND(positive,Iin[15]).output()
        jle = OR(jeq,jlt).output();
        jumpToA = OR(jle,jgt).output()
        PCload = AND(self.Cinstruction,jumpToA).output()
        PCinc = NOT(PCload).output()

        self.pc = ProgramCounter(self.Aout,PCload,PCinc,reset);

        self.CpuOut_pc = self.pc.output()

        self.output_values = [self.CpuOut_outM,self.CpuOut_writeM,self.CpuOut_addressM,self.CpuOut_pc]


    def update(self,Iin,Min,reset=0,Power=1):
        self.output_values = []

        self.Ainstruction = NOT(Iin[0],Power=1).output()
        self.Cinstruction = NOT(self.Ainstruction,Power=1).output()

        self.ALUtoA = AND(self.Cinstruction,Iin[10]).output() # C-instruction and destination to A-register?
        self.Aregin = Mux16(Iin,self.ALUout,self.ALUtoA).output()

        #for A register
        self.loadA = OR(self.Ainstruction,self.ALUtoA).output()
        self.Aregister.update(self.Aregin,self.loadA,Power) #_#

        self.Aout  = self.Aregister.output()

        #for A/M Multiplexer 
        self.AMout = Mux16(self.Aout,Min,Iin[3]).output()

        #for D register
        self.loadD = AND(self.Cinstruction,Iin[11]).output()
        self.Dregister.update(self.ALUout,self.loadD,Power) #_#
        self.Dout  = self.Dregister.output()

        print("==============inside CPU================")
        print("A-register: ",self.Aout)
        print("D-register: ",self.Dout)
        print("M/A input : ",self.AMout)
        print("ALUout: ",self.ALUout)
        print("=========================================")
        
        #ALU
        self.MyALU  = ALU(self.Dout,self.AMout,Iin[4],Iin[5],Iin[6],Iin[7],Iin[8],Iin[9]).output()
        self.ALUout = self.MyALU["out"]
        self.ZRout  = self.MyALU["zr"]
        self.NGout  = self.MyALU["ng"]


        #Set outputs for Writing memory
        self.CpuOut_outM = self.ALUout;
        self.CpuOut_writeM = Iin[12];
        self.CpuOut_addressM = self.Aout; # i.e, A register

        #calculate ProgramCounter output from ALUouts
        jeq = AND(self.ZRout,Iin[14],Power=1).output()
        jlt = AND(self.NGout,Iin[13],Power=1).output()
        zeroOrNeg = OR(self.ZRout,self.NGout).output()
        positive  = NOT(zeroOrNeg).output()
        jgt = AND(positive,Iin[15]).output()
        jle = OR(jeq,jlt).output();
        jumpToA = OR(jle,jgt).output()
        PCload  = AND(self.Cinstruction,jumpToA).output()
        PCinc   = NOT(PCload).output()

        self.pc.update(self.Aout,PCload,PCinc,reset,Power)
        self.CpuOut_pc = self.pc.output()

        self.output_values = [self.CpuOut_outM,self.CpuOut_writeM,self.CpuOut_addressM,self.CpuOut_pc]

    def output(self):
        return self.output_values;

class Computer:
    def __init__(self,progPath,reset=0,Power=1):
    #Input: it takes A file of Assembly Code from external file. and Feed it in ROM

        program = open(progPath,"rt");

        # Converting file lines to bits array
        Instructions = [] #program Lines
        for line in program:
            Iin = [];
            for bit in line:
                if (bit != "\n"):
                    Iin.append(int(bit)) 
            Instructions.append(Iin);

        #temp: Adding Vacent space
        Instructions.append([0]*16)
        Instructions.append([0]*16)
        Instructions.append([0]*16)
        Instructions.append([0]*16)
        Instructions.append([0]*16)
        Instructions.append([0]*16)

        # Adding all the Instruction into Array representation

        # output of CPU in t-1 time step is takens for calcuating the input of this time step
        self.cpu_outM  = [0]*16;
        self.cpu_addressM = [0]*15 # 15bit address(because we are using ram16K which need 14 bits of address and 1 bit is useless because most significant bit gives info about its sign)
        self.cpu_writeM = 0;
        self.cpu_pc = [0]*15;

        # input of this time step CPU
        self.cpu_inM = [0]*16;
        self.cpu_inI = [0]*16;
        self.reset = reset;

        addNbit = self.cpu_addressM[1:]

        self.output_value = [self.cpu_outM,self.cpu_addressM,self.cpu_writeM,self.cpu_pc]


        self.ROM = Instructions # AKA Instruction Memory # consist of array of instructions


        # add empty instructions 
        for i in range(5):
            self.ROM.append([0]*16)

        self.RAM = RAM512(self.cpu_outM,addNbit,self.cpu_writeM,Power=1) # AKA Data Memory
        self.reset = reset; #Computer's reset Button

        # Fetching the current Instruction of CPU to Process
        self.index_of_current_instruction = bin2dec(self.cpu_pc)
        # self.cpu_inI = self.ROM[self.index_of_current_instruction] 
        self.cpu_inI = [0]*16

        # extract only 14bits because we are using RAM16 and in the output the first bit is reserved for number sign i.e, 0 == negitive and 1 == positive

        address = num2locN(bin2dec(addNbit),512);
        # self.cpu_inM =   self.RAM.output()[address[0]][address[1]][address[2]][address[3]][address[4]]  # value inside RAM
        self.cpu_inM =   self.RAM.output()[address[0]][address[1]][address[2]]  # value inside RAM
        print("CPU IN: this is FROM COMPUTER","self.cpu_inI: ",self.cpu_inI,"self.cpu_inM: ",self.cpu_inM)

        #Central Processing Unit
        self.CPU = CPUfromhdl(self.cpu_inI,self.cpu_inM,self.reset)


        # self.CPU.update(self.cpu_inI,self.cpu_inM,self.reset)

        self.Computer_counter = 0;

        print("self.cpu_outM     ", self.cpu_outM)
        print("self.cpu_writeM   ", self.cpu_writeM)
        print("self.cpu_addressM ", self.cpu_addressM)
        print("self.cpu_pc       ", self.cpu_pc)


    def update(self,reset=0,Power=1):
        self.reset = reset

        # Updating the values using the CPU from t-1 cpu output
        self.cpu_outM       = self.CPU.output()[0]
        self.cpu_writeM     = self.CPU.output()[1]
        self.cpu_addressM   = self.CPU.output()[2]
        self.cpu_pc         = self.CPU.output()[3]


        self.output_value = [self.cpu_outM,self.cpu_addressM,self.cpu_writeM,self.cpu_pc]
        print("\n\n------------------------------------------------------------------------\n")

        print("Computer_counter: ",self.Computer_counter,"\n")

        print("self.cpu_outM     ", self.cpu_outM)
        print("self.cpu_writeM   ", self.cpu_writeM)
        print("self.cpu_addressM ", self.cpu_addressM)
        print("self.cpu_pc       ", self.cpu_pc)


        # Using the output of CPU t-1 to calcualte the inputs for current step's cpu

        # Fetching the current Instruction of CPU to Process
        self.index_of_current_instruction = bin2dec(self.cpu_pc)
        self.cpu_inI = self.ROM[self.index_of_current_instruction] 

        print("self.indexof current_instruction: ",self.index_of_current_instruction)

        # For RAM Update:-
        # addNbit = self.cpu_addressM[1:] # for 14bits of address for RAM16
        addNbit = self.cpu_addressM[7:]
        address = num2locN(bin2dec(addNbit),512)

        print("address: ",bin2dec(addNbit),len(addNbit),addNbit,"\t",address)

        self.RAM.update(self.cpu_outM,addNbit,self.cpu_writeM,Power)  # value inside RAM[self.outaddM] 
        # self.RAM.update([0]*16,[0]*15,0,Power)

        # self.cpu_inM = self.RAM.output()[address[0]][address[1]][address[2]][address[3]][address[4]]  # value inside RAM16K
        self.cpu_inM =   self.RAM.output()[address[0]][address[1]][address[2]]  # value inside RAM512

        # Print address
        print("printing RAM")
        for i in range(20):
            val    = num2locN(i,512)
            ramout = self.RAM.output()[val[0]][val[1]][val[2]]
            print(i,ramout)
        print()
        print("Cpu_inI: ",self.cpu_inI,"Cpu_inM: ",self.cpu_inM)

        self.CPU.update(self.cpu_inI,self.cpu_inM,self.reset)

        self.Computer_counter += 1

        print("\n--------------------------END-------------------------------------------")
        print("-----------------------x-x-x-x-x----------------------------------------\n")

        
    def output(self):
        return self.output_value

        

program2 ="Assembler/program/executable/program2.out";

MyComputer = Computer(progPath=program2,reset=0,Power=1) 
for i in range(20):
    MyComputer.update()
print("\n output:",MyComputer.output())

