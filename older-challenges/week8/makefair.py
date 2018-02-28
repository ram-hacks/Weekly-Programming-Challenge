makefair = lambda s: ''.join(p[0] for p in zip(s[::2], s[1::2]) if p[0]!=p[1])
