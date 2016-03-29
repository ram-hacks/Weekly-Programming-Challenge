fair = { ('0','0'):'', ('0','1'):'0', ('1','0'):'1', ('1','1'):'' }
makefair = lambda s: ''.join(fair[p] for p in zip(s[::2], s[1::2]))
