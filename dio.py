import fileinput, sys, os

def io():
    files = [k for k in sys.argv[1:] if os.path.exists(k)]
    return fileinput.input(files)
