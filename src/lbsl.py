from subprocess import call, Popen, check_output, PIPE
import sys
import os

def main():
    path = os.getcwd()

    if sys.argv.__len__() > 1:
        file = sys.argv[1]
        try:
            file = file.split('.')
            extension = file[1]
            if extension == 'lbsl':
                filename = '.'.join(file)
            else:
                print 'File name should be *.lbsl'
                return
        except:
            print 'File name should be *.lbsl'
            return
    else:
        filename = "sample.lbsl"

    #tokenizer
    tokenizer = os.path.join(path, 'tokenizer.py')
    file = os.path.join(path, filename)
    call(["python", tokenizer, file])

    FNULL = open(os.devnull, 'w')
    # Semantic and syntactic analysis
    file = os.path.join(path, "syntaxSemantics.pl")
    ps = Popen(('echo', 'halt.'), stdout=PIPE)

    output = Popen(('swipl', file), stdin=ps.stdout, stdout=PIPE)
    error, output = output.communicate()
    # ps.wait()
    FNULL.close()

    #checking whether there's a syntax error
    file = os.path.join(path, "semantics.txt")
    file = open(file, 'r')
    line = file.readline().strip()
    if line == 'Error':
        print '\n\n'
        print 'Expected Output'
        print '************************************'
        print 'Syntactic Error'
        print '\n'
        print '************************************'
        exit(0)

    #intermediate code
    intermediate = os.path.join(path, "intermediatecode.py")
    call(["python", intermediate])
    
    #environment
    environment = os.path.join(path, "environment.py")

    print '\n\n'
    print 'Expected Output'
    print '************************************'
    call(["python", environment])
    print '\n'
    print '************************************'

if __name__ == '__main__':
	main()