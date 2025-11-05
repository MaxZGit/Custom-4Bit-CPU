# Instructions
NOP_INSTR = "0000"
XOR_INSTR = "0001"
AND_INSTR = "0010"
OR_INSTR = "0011"
ADD_INSTR = "0100"
INC_INSTR = "0101"
DEC_INSTR = "0110"
SUB_INSTR = "0111"
JMP_INSTR = "1000"
JZ_INSTR = "1001"
JC_INSTR = "1010"
LD_INSTR = "1011"
ST_INSTR = "1100"
IN_INSTR = "1101"
OUT_INSTR = "1110"
LDI_INSTR = "1111"

############################
# Example programs to send:
############################

# Program to decrement output value indefinitely
dec_program = [
    OUT_INSTR, #0
    DEC_INSTR, #1
    JMP_INSTR, #2
    "0000",    #3
    NOP_INSTR, #4
    NOP_INSTR, #5
    NOP_INSTR, #6
    NOP_INSTR, #7

    NOP_INSTR, #8
    NOP_INSTR, #9
    NOP_INSTR, #10
    NOP_INSTR, #11
    NOP_INSTR, #12
    NOP_INSTR, #13
    NOP_INSTR, #14
    NOP_INSTR, #15
]

# Program to increment output value indefinitely
inc_program = [
    OUT_INSTR, #0
    INC_INSTR, #1
    JMP_INSTR, #2
    "0000",    #3
    NOP_INSTR, #4
    NOP_INSTR, #5
    NOP_INSTR, #6
    NOP_INSTR, #7

    NOP_INSTR, #8
    NOP_INSTR, #9
    NOP_INSTR, #10
    NOP_INSTR, #11
    NOP_INSTR, #12
    NOP_INSTR, #13
    NOP_INSTR, #14
    NOP_INSTR, #15
]

# Program to shift left output value indefinitely
shift_left_program = [
    IN_INSTR, #0
    OUT_INSTR, #1
    ST_INSTR, #2
    "1111",    #3
    ADD_INSTR, #4
    "1111", #5
    JC_INSTR, #6
    "1010", #7

    JMP_INSTR, #8
    "0001", #9
    INC_INSTR, #10
    JMP_INSTR, #11
    "0001", #12
    NOP_INSTR, #13
    NOP_INSTR, #14
    "0001", #15
]

# Program to toggle all output bits using LDI
toggle_LDI_program = [
    LDI_INSTR, #0
    "1111", #1
    OUT_INSTR, #2
    LDI_INSTR,    #3
    "0000", #4
    OUT_INSTR, #5
    JC_INSTR, #6
    "0000", #7

    NOP_INSTR, #8
    NOP_INSTR, #9
    INC_INSTR, #10
    JMP_INSTR, #11
    NOP_INSTR, #12
    NOP_INSTR, #13
    NOP_INSTR, #14
    NOP_INSTR, #15
]

# Program to toggle all output bits using LDI
toggle_program = [
    LDI_INSTR, #0
    "1111", #1
    OUT_INSTR, #2
    LDI_INSTR,    #3
    "0000", #4
    OUT_INSTR, #5
    JC_INSTR, #6
    "0000", #7

    NOP_INSTR, #8
    NOP_INSTR, #9
    INC_INSTR, #10
    JMP_INSTR, #11
    NOP_INSTR, #12
    NOP_INSTR, #13
    NOP_INSTR, #14
    NOP_INSTR, #15
]

# Program to count down from 3
toggle_program = [
    LDI_INSTR, #0
    "0011", #1
    OUT_INSTR, #2
    DEC_INSTR,    #3
    JZ_INSTR, #4
    "0000", #5
    JMP_INSTR, #6
    "0010", #7

    NOP_INSTR, #8
    NOP_INSTR, #9
    INC_INSTR, #10
    JMP_INSTR, #11
    NOP_INSTR, #12
    NOP_INSTR, #13
    NOP_INSTR, #14
    NOP_INSTR, #15
]

# Program to continuiously add two input numbers together and output the result
toggle_program = [
    IN_INSTR, #0
    ST_INSTR, #1
    "1111", #2
    IN_INSTR,    #3
    ADD_INSTR, #4
    "1111", #5
    OUT_INSTR, #6
    JMP_INSTR, #7

    "0000", #8
    NOP_INSTR, #9
    INC_INSTR, #10
    JMP_INSTR, #11
    NOP_INSTR, #12
    NOP_INSTR, #13
    NOP_INSTR, #14
    NOP_INSTR, #15
]

# Program to continuiously subtract two input numbers and output the result
toggle_program = [
    IN_INSTR, #0
    ST_INSTR, #1
    "1111", #2
    IN_INSTR,    #3
    SUB_INSTR, #4
    "1111", #5
    OUT_INSTR, #6
    JMP_INSTR, #7

    "0000", #8
    NOP_INSTR, #9
    INC_INSTR, #10
    JMP_INSTR, #11
    NOP_INSTR, #12
    NOP_INSTR, #13
    NOP_INSTR, #14
    NOP_INSTR, #15
]