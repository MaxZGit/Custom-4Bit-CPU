<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

This is a small custom multy cycle 4 bit CPU that is programmable via a UART interface.

### Architecture

The system consists of five main components:

1. **Control Unit**: Serves a brain of the CPU, controlling the data flow using control signals, decoding instructions
and tracking the current program counter and program state.

2. **Memory**: 16x4 bit memory for storing instructions and data.

3. **Registers**: Different registers for storing the current instruction (Instr), operand OPND and memory data (MDR).
Additionally, one working register (A) is also included.

4. **ALU**: The ALU performs the 4 bit arithmetic calculations a+b and a-b as well as incrementing and decrementing
by 1. Also included is a bitwise AND, OR and XOR.

5. **Programmer (including UART RX)**: The programmer can receive data via a UART interface (only RX)
and can be used to program instruction codes into the memory.

[[!CPU_Architecture]]
### Instruction Set

Following instructions are supported:

| Abbreviation | OP-Code | Operand | Operation                                 |
| ------------ | ------- | ------- | ----------------------------------------- |
| NOP          | 0000    | –       | $\text{No Operation}$                     |
| XOR          | 0001    | addr    | $A \leftarrow A \oplus \text{MEM[addr]}$  |
| AND          | 0010    | addr    | $A \leftarrow A \land \text{MEM[addr]}$   |
| OR           | 0011    | addr    | $A \leftarrow A \lor \text{MEM[addr]}$    |
| ADD          | 0100    | addr    | $A \leftarrow A + \text{MEM[addr]}$       |
| INC          | 0101    | –       | $A \leftarrow A + 1$                      |
| DEC          | 0110    | –       | $A \leftarrow A - 1$                      |
| SUB          | 0111    | addr    | $A \leftarrow A - \text{MEM[addr]}$       |
| JMP          | 1000    | addr    | $PC \leftarrow addr$                      |
| JZ           | 1001    | addr    | $\text{if } z == 1 :\ PC \leftarrow addr$ |
| JC           | 1010    | addr    | $\text{if } c == 1 :\ PC \leftarrow addr$ |
| LD           | 1011    | addr    | $A \leftarrow \text{MEM[addr]}$           |
| ST           | 1100    | addr    | $\text{MEM[addr]} \leftarrow A$           |
| IN           | 1101    | –       | $A \leftarrow \text{IN}$                  |
| OUT          | 1110    | –       | $\text{OUT} \leftarrow A$                 |
| LDI          | 1111    | imm     | $A \leftarrow \text{imm}$                 |

One instruction consists of a 4 bit op-code and an optional 4 bit operand, making them 4 or 8 bits long. The op-code
and operand are stored directly in succession, with the opcode preceding the operand. All possible Instructions are
listed in Table 1.
`A` is the A register, `MEM[]` represents the memory, `IN` and `OUT` are the in and out registers, `PC` is the program counter
and c or z refer to the carry or zero flag of the last ALU result.

### Operation Principle
The Control Unit starts reading the first data nibble from the memory (at address 0) and writes it into the instruction
register. After decoding the instruction, the CPU starts executing the instruction in multiple steps depending on the
active instruction. During those steps, the OPND and MDR registers are used to cache the instruction operand or memory
data if needed. The A register serves as the main working register (accumulator), the input data and the result of an
operation are always stored in this register. For example, the instruction ADD, adds the data in the A register and
the data in the MDR register together using the ALU and stores the result in A. Some instructions relay on logical or
arithmetical operations performed by the ALU. After a instruction is done, the program counter is increased by one
and the next instruction is read, starting the cycle from the beginning. The next few chapters will explain this flow
in more detail. The Control Unit has one extra state (active when the p_program_i is pulled high externally) that
enables the Programmer to write directly to the memory. In this mode, incoming data from the UART RX is streamed
directly into the memory to enable loading different programs. To interact with the CPU, the project includes an IN
and an OUT register with the according IN and OUT instructions. This enables external peripherals to communicate
with the CPU.

### Default Program
``` Verilog
MEM[0] <= OUT_INSTR;
MEM[1] <= INC_INSTR;
MEM[2] <= JMP_INSTR;
MEM[3] <= 4'b0000;
MEM[4-15] <= NOP_INSTR;
```
This is the default program stored in the memory after a reset. It counts up indefinitely
and outputs every result to the output pins.

### Programming
To try different programs, use the UART interface to send the instructions to the CPU. Following UART configuration must be used:
- data length: 8 bit
- baud rate: 19200
- parity bit: NO
- Stop bit: 1 stop bit

To start the programming procedure, pull the `p_program_i` low to enable the programming mode of the CPU. Now send 8 UART packets containing the 4 bit OP-Code and optional the 4 bit Operand. The 8 bit UART packets are split into two 4 bit blocks, each 4 bit block is stored in one 4 bit memory location. The data sent first will be located at the first memory location (`MEM[0]`).

## How to test

To test the CPU, just enable the correct tile and the CPU should start executing the default program. To test custom program codes, refer to the Programming section above.

## External hardware

**UART controller** to try custom programs
  - Connect the CPU RX (`uo[3]`) to controller's TX

In addition, some visualization tool will be helpful to see what the output of the CPU does. For this, some LEDs (with resistor) can be used or alternatively an Oscilloscope. 
