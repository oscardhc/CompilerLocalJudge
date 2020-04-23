#!/Users/oscar/opt/anaconda3/bin/python3

import os
import sys

# This script will run test for all *.mx files under 'path' EXCEPT for <arguments>
path = '/Users/oscar/Documents/Classes/1920_Spring/Compiler/Compiler-2020/local-judge/testcase/codegen/'

testcases = []
for f in os.listdir(path):
    if os.path.splitext(f)[1] == '.mx':
        testcases.append(f)
for s in sys.argv[1:]:
    testcases.remove(s + '.mx')
testcases.sort()

timeres = ''

for t in testcases:
    os.system('cp %s%s ./in.mx' % (path, t))
    with open('in.mx', 'r') as f:
        ar = f.read().split('\n')
        ip = ''
        flag = False
        for l in ar:
            if l.strip() == '=== end ===':
                flag = False
                with open('test.in', 'w') as g:
                    print(ip, file=g)
            elif flag:
                ip += (l + '\n')
            elif l.strip()  == '=== input ===':
                flag = True
        ip = ''
        flag = False
        for l in ar:
            if l.strip() == '=== end ===':
                flag = False
                with open('test.ans', 'w') as g:
                    print(ip, file=g)
            elif flag:
                ip += (l + '\n')
            elif l.strip()  == '=== output ===':
                flag = True
        print(t, ':', end='')
        if os.system('../MxSwift/.build/release/MxSwift >/dev/null'): # 1. To compiler source file 'in.mx'
            print('\033[1;35mBuild failed... \033[0m', end='')
            break
        else:
            print('\033[1;32mBuild passed... \033[0m', end='')
            if os.system('./build.sh out2 <test.in >test.out') or os.system('diff -B -b test.out test.ans > diff.out'): # 2. To compile with llc and compare output
                print('\033[1;31mx86 failed... \033[0m', end='')
                # break
            else:
                print('\033[1;32mx86 passed... \033[0m', end='')
            if os.system('./test.sh out2 2>/dev/null >ravel.out') or os.system('diff -B -b test.out test.ans'): # 3. To compile with my own backend and compare output
                print('\033[1;31mravel failed... \033[0m', end='')
                break
            else:
                with open('ravel.out', 'r') as h:
                    ar = h.read().split('\n')
                    for l in ar:
                        if l.startswith('time: '):
                            tm = l
                            timeres += (l[6:] + ',')
                            break
                print('\033[1;32mravel passed with ' + tm + '... \033[0m', end='')
        print('')
# print(timeres) # print cycle counts for all tests for statistical use
