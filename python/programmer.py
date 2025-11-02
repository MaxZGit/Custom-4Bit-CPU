import serial

port = 'COM5'
baudrate = 19200
timeout = 2

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

program = [
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

try:
    ser = serial.Serial(port, baudrate, timeout=timeout)

    for i in range(0, len(program), 2):
        high_nibble = int(program[i], 2)
        low_nibble = int(program[i + 1], 2)
        byte_value = (high_nibble << 4) | low_nibble
        ser.write(byte_value.to_bytes(1, 'big'))
        print(f"Sent byte: {byte_value:08b} (0x{byte_value:02X})")
finally:
    ser.close()
    print("Program sent successfully.")

