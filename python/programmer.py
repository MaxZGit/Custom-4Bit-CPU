import serial
import programm_lib

# uart configuration
port = 'COM5'
baudrate = 19200
timeout = 2

# select the program to send
program = programm_lib.shift_left_program

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

