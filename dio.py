import fileinput, sys, os, re

def io():
    files = [k for k in sys.argv[1:] if os.path.exists(k)]
    return fileinput.input(files)

def now(func=None):
    re_arg = re.compile(r'\-\-([\w]+)=([\w\.]+)')
    
    func = func or sys.argv[1]
    func = getattr(sys.modules['__main__'], func)
    

    args = dict(re_arg.findall(k)[0] for k in sys.argv[1:] if re_arg.match(k)) 
#    print args

    return func(**args)
