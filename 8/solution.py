from enum import Enum

'''
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
'''

class InstructionType(Enum):
    NOP = 'nop'
    ACC = 'acc'
    JMP = 'jmp'

INSTR = 0
ACCUM = 0

def nop_processor(val):
    global INSTR
    INSTR += 1

def acc_processor(val):
    global ACCUM, INSTR
    ACCUM += val
    INSTR += 1

def jmp_processor(val):
    global INSTR
    INSTR += val

INSTR_PROCESSORS = {
    "nop": nop_processor,
    "acc": acc_processor,
    "jmp": jmp_processor,
}

def run_program(instructions):
    visited = set()
    while INSTR not in visited:
        visited.add(INSTR)
        INSTR_PROCESSORS[instructions[INSTR][0]](instructions[INSTR][1])
    return ACCUM

if __name__ == '__main__':
    with open('./8/input.txt') as f:
        lines = f.read().splitlines()
    instructions = [(line[:3], int(line[4:])) for line in lines]

    # Part 1
    print(run_program(instructions))
