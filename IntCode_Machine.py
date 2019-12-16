from enum import Enum

# Inspired by some of the solutions found on Reddit for an IntCode Machine


class OP_TYPE(Enum):
    ADD = 1
    MUL = 2
    INPUT = 3
    OUT = 4
    JUMP_TRUE = 5
    JUMP_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    ADD_RELATIVE_BASE = 9
    HALT = 99


class MODE(Enum):
    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2


class IO(Enum):
    READ = 0,
    WRITE = 1


OPS = {
    OP_TYPE.ADD: [IO.READ,IO.READ,IO.WRITE],
    OP_TYPE.MUL: [IO.READ,IO.READ,IO.WRITE],
    OP_TYPE.INPUT: [IO.WRITE,],
    OP_TYPE.OUT: [IO.READ,],
    OP_TYPE.JUMP_TRUE: [IO.READ, IO.READ],
    OP_TYPE.JUMP_FALSE: [IO.READ, IO.READ],
    OP_TYPE.LESS_THAN: [IO.READ, IO.READ, IO.WRITE],
    OP_TYPE.EQUALS: [IO.READ, IO.READ, IO.WRITE],
    OP_TYPE.ADD_RELATIVE_BASE: [IO.READ,],
    OP_TYPE.HALT: []
}


class IntCodeMachine:

    def __init__(self, memory, mode='default'):
        self.ptr = 0
        self.mem = memory.copy()
        self.rel_base = 0
        self.machine_mode = mode
        self.op = None

    def __getitem__(self, index):
        return self.mem[index]

    def __setitem__(self, index, val):
        self.mem[index] = val

    def get_args(self, op_type, modes):
        args = [None] * 4

        for i, type in enumerate(op_type):
            arg = self[self.ptr + 1 + i]
            mode = MODE(modes % 10)
            modes //= 10

            if mode is MODE.RELATIVE:
                arg += self.rel_base

            if mode in (MODE.RELATIVE, MODE.POSITION):
                if arg < 0:
                    raise Exception(f'Memory index cannot be negative: {arg}')
                # Increase memory if needed
                elif arg >= len(self.mem):
                    self.mem += [0] * (arg + 1 - len(self.mem))

                if type is IO.READ:
                    arg = self[arg]
            elif mode is MODE.IMMEDIATE:
                if type is IO.WRITE:
                    raise Exception(f'Cannot write in IMMEDIATE mode.')
            else:
                raise Exception(f'Invalid mode: {mode}')
            args[i] = arg
        return args

    def get_current_op(self):
        return self.op

    def run(self, input):
        output = []
        while True:
            instruction = self[self.ptr]

            if OP_TYPE(instruction % 100):
                self.op = OP_TYPE(instruction % 100)
            else:
                raise Exception(f'Issue occurred at instruction: {instruction}')
            modes = instruction // 100
            args = OPS[self.op]
            a, b, c, d = self.get_args(args, modes)
            self.ptr += 1 + len(args)

            if self.op is OP_TYPE.INPUT:
                self[a] = input
            elif self.op is OP_TYPE.OUT:
                output.append(a)
                if self.machine_mode is 'paint' and len(output) is 2:
                    break
            elif self.op is OP_TYPE.ADD:
                self[c] = a + b
            elif self.op is OP_TYPE.MUL:
                self[c] = a * b
            elif self.op is OP_TYPE.LESS_THAN:
                self[c] = 1 if a < b else 0
            elif self.op is OP_TYPE.EQUALS:
                self[c] = 1 if a is b else 0
            elif self.op is OP_TYPE.JUMP_TRUE:
                if a is not 0:
                    self.ptr = b
            elif self.op is OP_TYPE.JUMP_FALSE:
                if a is 0:
                    self.ptr = b
            elif self.op is OP_TYPE.ADD_RELATIVE_BASE:
                self.rel_base += a
            elif self.op is OP_TYPE.HALT:
                break
            else:
                raise Exception(f'Unknown Opcode {self.op}')
        return output


