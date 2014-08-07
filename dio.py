import fileinput, sys, os, re

def io():
    files = [k for k in sys.argv[1:] if os.path.exists(k)]
    return fileinput.input(files)

re_i = re.compile(r'^[\d]+i$')
re_f = re.compile(r'^[\d]+\.[\d]{0,1}f$')
re_b = re.compile(r'^(True|False)$')

def convert(v):
    try:
        if re_i.match(v):
            return int(v[:-1])
        elif re_f.match(v):
            return float(v[:-1])
        elif re_b.match(v):
            return bool(v)
    except:
        pass
    
    return v

def now(func=None):
    re_arg = re.compile(r'\-\-([\w]+)=([\w\.]+)')
    
    func = func or sys.argv[1]
    func = getattr(sys.modules['__main__'], func)
    
    args = (re_arg.findall(k)[0] for k in sys.argv[1:] if re_arg.match(k)) 
    args = {k:convert(v) for k, v in args}

    return func(**args)
