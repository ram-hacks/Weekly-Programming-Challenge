import enum
import argparse

_ops = ['PUSH', 'DUP', 'SWAP', 'POP',
        'ADD', 'SUB', 'MUL', 'DIV', 'MOD',
        'LD', 'STR',
        'LABEL', 'CALL', 'JMP', 'JZ', 'JNEG', 'RET', 'EXIT',
        'OCHR', 'OINT', 'ICHR', 'IINT',
       ]

OP = enum.Enum('OPS', _ops)

_toks = ['IMF_STACK', 'IMF_HEAP', 'IMF_ARITH', 'IMF_FLOW', 'IMF_IO',
         'OP_PUSH', 'OP_DUP', 'OP_SWAP', 'OP_POP', 'OP_LD',
         'OP_ADD', 'OP_SUB', 'OP_MUL', 'OP_DIV', 'OP_MOD',
         'OP_STR', 'OP_LABEL', 'OP_CALL', 'OP_JMP', 'OP_JZ',
         'OP_JNEG', 'OP_RET', 'OP_EXIT', 'OP_OCHR', 'OP_OINT',
         'OP_ICHR', 'OP_IINT', 'INT_IMMED', 'LABEL', 'LF',
]

TOK = enum.Enum('TOK', _toks)

_toks_map = {
        TOK.IMF_STACK: ' ',
        TOK.IMF_HEAP: '\t\t',
        TOK.IMF_ARITH: '\t ',
        TOK.IMF_FLOW: '\n',
        TOK.IMF_IO: '\t\n',
        TOK.OP_PUSH: ' ',
        TOK.OP_DUP: '\n ',
        TOK.OP_SWAP: '\n\t',
        TOK.OP_POP: '\n\n',
        TOK.OP_LD: '\t',
        TOK.OP_STR: ' ',
        TOK.OP_ADD: '  ',
        TOK.OP_SUB: ' \t',
        TOK.OP_MUL: ' \n',
        TOK.OP_DIV: '\t ',
        TOK.OP_MOD: '\t\t',
        TOK.OP_LABEL: '  ',
        TOK.OP_CALL: ' \t',
        TOK.OP_JMP: ' \n',
        TOK.OP_JZ: '\t ',
        TOK.OP_JNEG: '\t\t',
        TOK.OP_RET: '\t\n',
        TOK.OP_EXIT: '\n\n',
        TOK.OP_OCHR: '  ',
        TOK.OP_OINT: ' \t',
        TOK.OP_ICHR: '\t ',
        TOK.OP_IINT: '\t\t',
        TOK.LABEL: ('\t', ' '),
        TOK.INT_IMMED: ('\t', ' '),
        TOK.LF: '\n'
}

_parse_rules = {
    OP.PUSH: (TOK.IMF_STACK, TOK.OP_PUSH, TOK.INT_IMMED, TOK.LF),
    OP.DUP: (TOK.IMF_STACK, TOK.OP_DUP),
    OP.SWAP: (TOK.IMF_STACK, TOK.OP_SWAP),
    OP.POP: (TOK.IMF_STACK, TOK.OP_POP),

    OP.ADD: (TOK.IMF_ARITH, TOK.OP_ADD),
    OP.SUB: (TOK.IMF_ARITH, TOK.OP_SUB),
    OP.MUL: (TOK.IMF_ARITH, TOK.OP_MUL),
    OP.DIV: (TOK.IMF_ARITH, TOK.OP_DIV),
    OP.MOD: (TOK.IMF_ARITH, TOK.OP_MOD),

    OP.STR: (TOK.IMF_HEAP, TOK.OP_STR),
    OP.LD: (TOK.IMF_HEAP, TOK.OP_LD),

    OP.LABEL: (TOK.IMF_FLOW, TOK.OP_LABEL, TOK.LABEL, TOK.LF),
    OP.CALL: (TOK.IMF_FLOW, TOK.OP_CALL, TOK.LABEL, TOK.LF),
    OP.JMP: (TOK.IMF_FLOW, TOK.OP_JMP, TOK.LABEL, TOK.LF),
    OP.JZ: (TOK.IMF_FLOW, TOK.OP_JZ, TOK.LABEL, TOK.LF),
    OP.JNEG: (TOK.IMF_FLOW, TOK.OP_JNEG, TOK.LABEL, TOK.LF),
    OP.RET: (TOK.IMF_FLOW, TOK.OP_RET),
    OP.EXIT: (TOK.IMF_FLOW, TOK.OP_EXIT),

    OP.OCHR: (TOK.IMF_IO, TOK.OP_OCHR),
    OP.OINT: (TOK.IMF_IO, TOK.OP_OINT),
    OP.ICHR: (TOK.IMF_IO, TOK.OP_ICHR),
    OP.IINT: (TOK.IMF_IO, TOK.OP_IINT),
}

class FileInputStream(object):
    """
    Read tokens from a file-like object.
    """
    def __init__(self, fh):
        self._fh = fh
        self._eof = False
        self._buf = ''
        self._blocksize = 512
        self._consumed = 0

    def has_more(self):
        """ True iff there are unconsumed tokens. """
        self._buffer()
        return len(self._buf) > 0

    def _buffer(self):
        if not self._eof:
            data = self._fh.read(self._blocksize)
            self._buf += data

            if len(data) < self._blocksize:
                self._eof = True

    def get_next(self, l=1):
        old_size = len(self._buf)

        # if there are < l chars buffered, read more from the file
        while len(self._buf) < l and not self._eof:
            self._buffer()

        if len(self._buf) >= l:
            part = self._buf[:l]
            self._buf = self._buf[l:]
            ret = ''.join(part)
            self._consumed += len(ret)

            return ret
        else:
            return None

    def push(self, st):
        """
        Push tokens back into the buffer.
        """
        self._buf = st + self._buf
        self._consumed -= len(st)

class Op(object):
    def __init__(self, op, num, arg=None):
        self.op = op
        self.arg = arg
        self.num = num

def _parse_int(val, unsigned=False):
    """
    Parse a whitespace integer into an actual integer.
    """
    chars = list(val)

    assert len(chars) >= 2
    sign_char = chars.pop(0)
    sign = 1 if sign_char == ' ' else -1

    accum = 0
    power = 1
    while len(chars):
        if chars.pop(-1) == '\t':
            accum += sign * power
        power <<= 1

    return accum

class Program(object):
    def __init__(self, ops, labels):
        self._ops = ops
        self._labels = labels
        self._relocate = 0

    def __getitem__(self, addr):
        return self._ops[addr - self._relocate]

    def lookup_label(self, label):
        return self._labels[label] + self._relocate

    def __str__(self):
        buf = ''
        i = 0
        for op in self._ops:
            buf += '%3d: %s' % (i, op.op.name)
            if op.arg:
                buf += ' '
                if op.op in (OP.JMP, OP.CALL, OP.JZ, OP.JMP, OP.JNEG):
                    buf += str(self.lookup_label(op.arg))
                else:
                    buf += str(op.arg)
            buf += '\n'
            i += 1

        return buf

class VM(object):
    """
    The actual whitespace executor.
    """
    def __init__(self):
        self._pc = 0
        self._stack = []
        self._heap = {}
        self._call_stack = []
        self._running = False

        self._pgm_mem = None

    def load(self, program):
        """
        Load the given program into address 0.
        """
        self._program = program

    def start(self, entry=0):
        """ Begin execution at the given entry point. """
        self._running = True
        self._pc = entry

        self._run()

    def _run(self):
        while self._running:
            opcode = self._program[self._pc]
            fn_name = '_op_' + opcode.op.name

            pc_pre = self._pc

            if hasattr(self, fn_name):
                fn = getattr(self, '_op_' + opcode.op.name)
                fn(opcode)
            else:
                raise ValueError('Illegal operation:', opcode.op.name)

            # Increment only if the instruction did not change the PC
            if self._pc == pc_pre:
                self._pc += 1

    def _op_EXIT(self, opcode):
        self._running = False

    def _op_PUSH(self, opcode):
        self._stack.append(opcode.arg)

    def _op_DUP(self, opcode):
        self._stack.append(self._stack[-1])

    def _op_SWAP(self, opcdoe):
        self._stack += [self._stack.pop(-1), self._stack.pop(-1)]

    def _op_POP(self, opcode):
        self._stack.pop(-1)

    def _op_ADD(self, opcode):
        self._stack = self._stack[:-2] + [sum(self._stack[-2:])]

    def _op_SUB(self, opcode):
        right = self._stack.pop(-1)
        left = self._stack.pop(-1)
        self._stack.append(left - right)

    def _op_MUL(self, opcode):
        self._stack.append(self._stack.pop(-1) * self._stack.pop(-1))

    def _op_DIV(self, opcode):
        right = self._stack.pop(-1)
        left = self._stack.pop(-1)
        self._stack.append(left//right)

    def _op_MOD(self, opcode):
        right = self._stack.pop(-1)
        left = self._stack.pop(-1)
        self._stack.append(left % right)

    def _op_STR(self, opcode):
        val = self._stack.pop(-1)
        addr = self._stack.pop(-1)
        self._heap[addr] = val

    def _op_LD(self, opcode):
        self._stack.append(self._heap[self._stack.pop(-1)])

    def _op_CALL(self, opcode):
        self._call_stack.append(self._pc + 1)
        self._op_JMP(opcode)

    def _op_JMP(self, opcode):
        self._pc = self._program.lookup_label(opcode.arg)

    def _op_JZ(self, opcode):
        if self._stack.pop(-1) == 0:
            self._op_JMP(opcode)

    def _op_JNEG(self, opcode):
        if self._stack.pop(-1) < 0:
            self._op_JMP(opcode)

    def _op_RET(self, opcdoe):
        self._pc = self._call_stack.pop(-1)

    def _op_OINT(self, opcode):
        print(self._stack.pop(-1), end='')

    def _op_OCHR(self, opcode):
        print(chr(self._stack.pop(-1)), end='')

    def _op_IINT(self, opcode):
        addr = self._stack.pop(-1)
        self._heap[addr] = int(input(''))

def _format_ws(ws):
    trans = {'\t': 'tab', ' ': 'space', '\n': 'lf'}
    toks = []
    for char in ws:
        toks.append('#' + trans[char])

    return ' '.join(toks)

def assemble(stream):
    """
    A shitty parser.
    """
    def _match_str(stream, part):
        match = stream.get_next(len(part))
        if match == part:
            return match
        else:
            stream.push(match)
            return False

    def _match_chars(stream, part):

        match = ''
        while stream.has_more():
            c = stream.get_next()
            if c in part:
                match += c
            else:
                stream.push(c)
                break

        if match:
            return match
        else:
            return False

    def _match_tok(stream, tok):
        matched = False

        if not tok in _toks_map:
            raise ValueError('No definition for token: ', tok)
        else:
            rule = _toks_map[tok]

            if isinstance(rule, str):
                return _match_str(stream, rule)

            # match some chars
            elif isinstance(rule, tuple):
                return _match_chars(stream, rule)

            else:
                raise ValueError('Invalid match.')

    def _match_rule(stream):
        for op in _parse_rules:
            toks = []

            matched = True
            for match_tok in _parse_rules[op]:
                match = _match_tok(stream, match_tok)

                if match is False:
                    matched = False
                    break
                else:
                    toks.append((match_tok, match))

            if matched:
                return op, toks
            else:
                for tok, match in toks[::-1]:
                    stream.push(match)

        raise ValueError('no rule matched:'+ _format_ws(stream.get_next(5)))

    labels = {}
    paddr = 0
    num = 0
    program = []

    while stream.has_more():
        op, toks = _match_rule(stream)

        # if there are args, they start after IMF and OP
        args = toks[2:]

        num += 0

        if op == OP.LABEL:
            arg_tok, arg_val = args[0]
            labels[arg_val] = paddr
        else:
            if op is OP.PUSH:
                arg = _parse_int(args[0][1])
            elif op in (OP.JMP, OP.JZ, OP.JNEG, OP.CALL):
                arg = args[0][1]
            else:
                arg = None

            program.append(Op(op, num, arg))
            paddr += 1

            assert paddr == len(program)

    return Program(program, labels)

parser = argparse.ArgumentParser(description="A really shitty interpreter for whitespace. Don't use this. It's bad.")
parser.add_argument('file', metavar='F', type=str)
parser.add_argument('--disassemble', action='store_true', default=False)

args = parser.parse_args()


pgm = None
with open(args.file) as fh:
    stream = FileInputStream(fh)
    pgm = assemble(stream)

if args.disassemble:
    print(pgm)
else:
    vm = VM()

    # load the program into the VM
    vm.load(pgm)

    # Jump to address 0 and gogogo
    vm.start(0)
