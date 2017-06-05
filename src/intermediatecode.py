import re
import json

arr = []
rlbl = []
llbl=[]
num = 0
label = 0
ifLabel = -1
isIf = False
finalObject = []

def writeLine(row):
    global finalObject
    if len(finalObject) != 0:
        lastrow = finalObject[-1]
        if lastrow[-1] == ',':
            lastrow = lastrow[:-1]
            lastrow += row
            finalObject[-1] = lastrow
        else:
            finalObject.append(row)
    else:
        finalObject.append(row)

def alphn(n):
    i = 0
    str = ''
    while (i < len(n)):
        if n[i] == " " or n[i] == "," or n[i] == ")" or n[i] == "(":
            i += 1
        else:
            str += n[i]
            i += 1
    return str

def arithmeticExp(res,exp):
    global num, isIf, ifLabel
    if exp.startswith("add"):
        if exp[4] == "(":
            count = 1
            i = 5
            while (count != 0):
                if exp[i] == "(":
                    count += 1
                if exp[i] == ")":
                    count -= 1
                i += 1
                a = alphn(exp[5:i])
                b = exp[i + 1:-1].strip()
        else:
            a,b = exp[4:-1].split(",", 1)
            a = alphn(a)

        if b.startswith("express"):
            b = alphn(b[8:])

        num += 1
        t1 =""
        t2 = ""

        for elem in arr:
            if not a.isdigit():
                if a == elem[1]:
                    t1 = elem[2]

            if not b.isdigit():
                if b == elem[1]:
                    t2 = elem[2]

        if  not a.isdigit():
            if t1 == "":
                num += 1
                tup = ('', a, "t" + str(num))
                arr.append(tup)
                t1 = "t" + str(num)
        else:
            t1 = a

        if  not b.isdigit():
            if t1 == "":
                num += 1
                tup = ('', b, "t" + str(num))
                arr.append(tup)
                t2 = "t" + str(num)
        else:
            t2 = b

        string = "add "+t1+", "+t2+", "+res
        writeLine(string)
        # print "add "+t1+","+t2+","+res

    if exp.startswith("subtract"):
        if exp[9] == "(":
            count = 1
            i = 10
            while (count != 0):
                if exp[i] == "(":
                    count += 1
                if exp[i] == ")":
                    count -= 1
                i += 1
                a = alphn(exp[10:i])
                b = exp[i + 1:-1].strip()
        else:
            a,b = exp[9:-1].split(",", 1)
            a = alphn(a)

        if b.startswith("express"):
            b = alphn(b[8:])
        num += 1
        t1 =""
        t2 =""
        for elem in arr:
            if not a.isdigit():
                if a == elem[1]:
                    t1 = elem[2]

            if not b.isdigit():
                if b == elem[1]:
                    t2 = elem[2]

        if  not a.isdigit():
            if t1 == "":
                num += 1
                tup = ('', a, "t" + str(num))
                arr.append(tup)
                t1 = "t" + str(num)
        else:
            t1 = a

        if  not b.isdigit():
            if t1 == "":
                num += 1
                tup = ('', b, "t" + str(num))
                arr.append(tup)
                t2 = "t" + str(num)
        else:
            t2 = b

        if isIf:
            string = "J" + str(ifLabel) + ": "
            isIf = False
        string = "sub "+t1+", "+t2+", "+res
        writeLine(string)
        # print "sub "+t1+","+t2+","+res

    if exp.startswith("multiply"):
        if exp[9] == "(":
            count = 1
            i = 10
            while (count != 0):
                if exp[i] == "(":
                    count += 1
                if exp[i] == ")":
                    count -= 1
                i += 1
                a = alphn(exp[10:i])
                b = exp[i + 1:-1].strip()
        else:
            a,b = exp[9:].split(",")
            a = alphn(a)

        if b.startswith("express"):
            b = alphn(b[8:])
        else:
            b = alphn(b)

        num += 1
        t1 =""
        t2 =""
        for elem in arr:
            if not a.isdigit():
                if a == elem[1]:
                    t1 = elem[2]

            if not b.isdigit():
                if b == elem[1]:
                    t2 = elem[2]

        if  not a.isdigit():
            if t1 == "":
                num += 1
                tup = ('', a, "t" + str(num))
                arr.append(tup)
                t1 = "t" + str(num)
        else:
            t1 = a

        if  not b.isdigit():
            if t1 == "":
                num += 1
                tup = ('', b, "t" + str(num))
                arr.append(tup)
                t2 = "t" + str(num)
        else:
            t2 = b

        if isIf:
            string = "J" + str(ifLabel) + ": "
            isIf = False
        string = "mul "+t1+", "+t2+", "+res
        writeLine(string)
        # print "mul "+t1+","+t2+","+res


    if exp.startswith("divide"):

        if exp[7] == "(":
            count = 1
            i = 8
            while (count != 0):
                if exp[i] == "(":
                    count += 1
                if exp[i] == ")":
                    count -= 1
                i += 1
                a = alphn(exp[8:i])
                b = exp[i + 1:-1].strip()
        else:
            a,b = exp[7:-1].split(",", 1)
            a = alphn(a)

        if b.startswith("express"):
            b = alphn(b[8:])
        else:
            b = alphn(b)

        num += 1
        t1 = ""
        t2 = ""
        for elem in arr:
            if not a.isdigit():
                if a == elem[1]:
                    t1 = elem[2]

            if not b.isdigit():
                if b == elem[1]:
                    t2 = elem[2]

        if  not a.isdigit():
            if t1 == "":
                num += 1
                tup = ('', a, "t" + str(num))
                arr.append(tup)
                t1 = "t" + str(num)
        else:
            t1 = a

        if  not b.isdigit():
            if t1 == "":
                num += 1
                tup = ('', b, "t" + str(num))
                arr.append(tup)
                t2 = "t" + str(num)
        else:
            t2 = b

        if isIf:
            string = "J" + str(ifLabel) + ": "
            isIf = False
        string = "div "+t1+", "+t2+", "+res
        writeLine(string)
        # print "mul "+a+","+b+","+res


    if exp.startswith("modulus"):
        if exp[8] == "(":
            count = 1
            i = 9
            while (count != 0):
                if exp[i] == "(":
                    count += 1
                if exp[i] == ")":
                    count -= 1
                i += 1
                a = alphn(exp[9:i])
                b = exp[i + 1:-1].strip()
        else:
            a,b = exp[8:-1].split(",", 1)
            a = alphn(a)

        if b.startswith("express"):
            b = alphn(b[8:])
        num += 1
        t1 = ""
        t2 = ""
        for elem in arr:
            if not a.isdigit():
                if a == elem[1]:
                    t1 = elem[2]

            if not b.isdigit():
                if b == elem[1]:
                    t2 = elem[2]

        if  not a.isdigit():
            if t1 == "":
                num += 1
                tup = ('', a, "t" + str(num))
                arr.append(tup)
                t1 = "t" + str(num)
        else:
            t1 = a

        if  not b.isdigit():
            if t1 == "":
                num += 1
                tup = ('', b, "t" + str(num))
                arr.append(tup)
                t2 = "t" + str(num)
        else:
            t2 = b

        if isIf:
            string = "J" + str(ifLabel) + ": "
            isIf = False
        string = "mod "+t1+", "+t2+", "+res
        writeLine(string)
        # print "mod "+t1+","+t2+","+res


def assign(a):
    global num, isIf, ifLabel
    temp = ''
    if a.startswith("("):
        count = 1
        i = 1
        while(count != 0):
            if a[i] == "(":
                count += 1
            if a[i] == ")":
                count -= 1
            i += 1
            var = alphn(a[1:i])
            val = a[i+1:-1].strip()
    else:
        vr,val = a.split(",",1)
        var = alphn(vr)
        val = val.strip()

    for elem in arr:
        if elem[1] == var:
            temp = elem[2]

    if temp == "":
        num += 1
        tup = ('',var,"t"+str(num))
        arr.append(tup)
        temp = "t"+str(num)

    string = None
    if val.startswith("add") or val.startswith("subtract"):
        val = arithmeticExp(temp,val)
    elif val.startswith("express"):
        val = val[8:]
        if val.startswith("multiply") or val.startswith("divide") or val.startswith("modulus"):
            val = arithmeticExp(temp,val)
        else:
            string = "mov " + str(alphn(val)) + "," + temp
    elif alphn(val) == "true":
        string = "mov T, "+temp
        # print "mov T,"+temp
    elif alphn(val) == "false":
        string = "mov F, "+temp
        # print "mov F,"+temp

    if isIf:
        isIf = False
        writeLine("J" + str(ifLabel) + ": ,")
    if string:
        writeLine(string)

def booleanEx(a,op,b):
    global num, label, isIf, ifLabel
    temp1 = ''
    temp2 = b

    for elem in arr:
        if a == elem[1]:
            temp1 = elem[2]
        if b == elem[2]:
            temp2 = elem[2]

    if temp1 == "":
        num += 1
        tup = ("", a, "t" + str(num))
        arr.append(tup)
        temp1 = "t" + str(num)

    if temp2 == b and b.isalpha():
        num +=1
        tup = ("", b, "t" + str(num))
        arr.append(tup)
        temp2 = "t" + str(num)

    string = None
    if op == ">":
        string = "jle "+temp1+","+temp2+",,"
    if op == "<":
        string = "jge " + temp1 + "," + temp2 + ",,"
    if op == "<=":
        string = "jg " + temp1 + "," + temp2 + ",,"
    if op == ">=":
        string = "jl " + temp1 + "," + temp2 + ",,"
    if op == "!=":
        string = "jee " + temp1 + "," + temp2 + ",,"
    if op == "==":
        string = "jne " + temp1 + "," + temp2 + ",,"
    
    if string:
        writeLine(string)

def codeBlck(c):
    while (re.search('[a-zA-Z0-9]',c)):
        if "assign" in c:
            counter = 1
            i1 = c.find("assign")
            x1= i1 + 7
            while (counter != 0):
                if c[x1] == "(":
                    counter += 1
                if c[x1] == ")":
                    counter -= 1
                x1 += 1
            assign(c[i1+7:x1])
            c = c[:i1-1]+ c[x1:]

        if "print" in c:
            counter = 1
            i2 = c.find("print")
            x2 = i2 + 6
            while (counter != 0):
                if c[x2] == "(":
                    counter += 1
                if c[x2] == ")":
                    counter -= 1
                x2 += 1
            show(c[i2+6:x2])
            c = c[:i2] + c[x2:]
        print c


def whileOp(a):
    global label, ifLabel, isIf
    tempLabel1 = ""
    tempLabel2 = ""
    b =[]
    if a.startswith("(") and a.endswith(")"):
        a = a[1:-1]
    leng = len(a)
    while(leng != 0):
        if a.startswith("express"):
            if a[8] == "(":
                counter = 1
                i = 9
                while (counter != 0):
                    if a[i] == "(":
                        counter += 1
                    if a[i] == ")":
                        counter -= 1
                    i += 1
                b.append(alphn(a[8:i]))

        if a.startswith("codeBlock"):
            a[i] = e[10:-1]

    if isIf:
        isIf = False
        writeLine("J" + str(ifLabel) + ": ,")

    for i in llbl:
        if i == ("L" + str(label)):
            label += 1
    rlbl.append("L" + str(label))
    string = "L"+str(label)+": ,"
    writeLine(string)
    # print "L"+str(label),
    tempLabel1 = "L"+str(label)

    label += 1
    booleanEx(a[0],a[1],a[2])

    for i in rlbl:
        if i == ("L" + str(label)):
            label += 1
    llbl.append("L" + str(label))
    string = "L" + str(label)
    writeLine(string)
    # print "L" + str(label)
    tempLabel2 = "L" + str(label)

    if a[3] != "":
        codeBlck(a[3])

    string = " jmp "+ tempLabel1
    writeLine(string)
    # print " jmp "+ tempLabel1

    string = tempLabel2+":,"
    writeLine(string)
    # print tempLabel2+":",

def loopIf(a):
    global label, ifLabel, isIf
    ifList = []
    count = 0
    temp = ""
    a = a.replace("express", "")
    a = a.replace("codeBlock", "")
    if isIf:
        isIf = False
        writeLine("J" + str(ifLabel) + ": ,")
    
    for char in a:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
            if count < 0:
                count = 0
        elif char == ',' and count == 0:
            ifList.append(temp)
            temp = ""
        elif char == ',' and count != 0:
            temp += ''
        else:
            temp += char
    ifList.append(temp)

    tempList = ifList[:]
    ifList = []
    for l in tempList:
        if "print" in l:
            l = l.replace("print", "print(")
            l += ')'
        ifList.append(l)

    for i in llbl:
##        print "LLBL: ", label, llbl, rlbl
        if i == ("L" + str(label)):
            label += 1
    rlbl.append("L" + str(label))

    booleanEx(ifList[0],ifList[1],ifList[2])

##    llbl.append("L" + str(label))
    
    string = "L" + str(label)
    writeLine(string)
    # print "L" + str(label)

    if ifList[3] != "":
        codeBlck(ifList[3])
    ifLabel = ifLabel + 1
    writeLine("jmp J" + str(ifLabel))
    isIf = True

    

def loopElif(a):
    global label, ifLabel, isIf
    ifList = []
    count = 0
    temp = ""
    a = a.replace("express", "")
    a = a.replace("codeBlock", "")
    
    for char in a:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
            if count < 0:
                count = 0
        elif char == ',' and count == 0:
            ifList.append(temp)
            temp = ""
        elif char == ',' and count != 0:
            temp += ''
        else:
            temp += char
    ifList.append(temp)
##    print ifList

    tempList = ifList[:]
    ifList = []
    for l in tempList:
        if "print" in l:
            l = l.replace("print", "print(")
            l += ')'
        ifList.append(l)

    string = "L"+str(label) + ": ,"
    writeLine(string)
    # print "L"+str(label),
    tempLabel1 = "L"+str(label)

##    label += 1
    booleanEx(ifList[0],ifList[1],ifList[2])

    for i in rlbl:
##        print "RLBL: ", label, llbl, rlbl
        if i == ("L" + str(label)):
            label += 1
    llbl.append("L" + str(label))

    string = "L" + str(label)
    writeLine(string)
    # print "L" + str(label)
    tempLabel2 = "L" + str(label)

    if ifList[3] != "":
        codeBlck(ifList[3])

##    print " jmp "+ tempLabel1
    writeLine("jmp J" + str(ifLabel))
    string = tempLabel2+":,"
    writeLine(string)

def loopElse(a):
    global label, isIf, ifLabel
    ifList = []
    count = 0
    temp = ""
    a = a.replace("express", "")
    a = a.replace("codeBlock", "")
    
    for char in a:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
            if count < 0:
                count = 0
        elif char == ',' and count == 0:
            ifList.append(temp)
            temp = ""
        elif char == ',' and count != 0:
            temp += ''
        else:
            temp += char
    ifList.append(temp)

    tempList = ifList[:]
    ifList = []
    for l in tempList:
        if "print" in l:
            l = l.replace("print", "print(")
            l += ')'
        ifList.append(l)
##    print ifList

    for i in llbl:
        if i == ("L" + str(label)):
            label += 1
    rlbl.append("L" + str(label))

    label += 1
##    booleanEx(ifList[0],ifList[1],ifList[2])

    if ifList[0] != "":
        codeBlck(ifList[0])

##    print " jmp "+ tempLabel1


def show(a):
    global isIf
    var = alphn(a)
    val = ''
    for elem in arr:
        if elem[1] == var:
            val = elem[2]

    global num
    num += 1
    if val == '':
        tup = ("", var, "t" + str(num))
        arr.append(tup)
        val = "t" + str(num)
    string = "shw " + val
    writeLine(string)
    # print "show t" + str(num)


def main():
    # Opening a file
    try:
        newfile = open("semantics.txt", "r")
    except IOError as e:
        print ('File could not be found')
        return
    except Exception as e:
        print ('Error in opening the file')
    rows = newfile.readline().split("encode")

    for elements in rows[1:]:
        if elements.startswith("(looping("):
            counter = 1
            index = elements.find("looping")
            i = index + 8
            while (counter != 0):
                if elements[i] == "(":
                    counter += 1
                if elements[i] == ")":
                    counter -= 1
                i += 1
            whileOp(elements[index + 8:i])

        elif elements.startswith("(assign("):
            counter = 1
            index = elements.find("assign")
            i = index + 7
            while(counter != 0):
                if elements[i] ==  "(":
                    counter += 1
                if elements[i] == ")":
                    counter -= 1
                i += 1
            assign(elements[index+7:i])

        elif elements.startswith("(print("):
            counter = 1
            index = elements.find("print")
            i = index + 6
            while (counter != 0):
                if elements[i] == "(":
                    counter += 1
                if elements[i] == ")":
                    counter -= 1
                i += 1
            show(elements[index + 6:i])

        elif elements.startswith("(condIf("):
            counter = 1
            index = elements.find("condIf")
            i = index + 7
            while (counter != 0):
                if elements[i] == '(':
                    counter += 1
                if elements[i] == ')':
                    counter -= 1
                i += 1
            loopIf(elements[index + 8 : i - 2])
            
        elif elements.startswith("(condElif("):
            counter = 1
            index = elements.find("condElif")
            i = index + 9
            while (counter != 0):
                if elements[i] == '(':
                    counter += 1
                if elements[i] == ')':
                    counter -= 1
                i += 1
            loopElif(elements[index + 10 : i - 2])
            
        elif elements.startswith("(condElse("):
            counter = 1
            index = elements.find("condElse")
            i = index + 9
            while (counter != 0):
                if elements[i] == '(':
                    counter += 1
                if elements[i] == ')':
                    counter -= 1
                i += 1
            loopElse(elements[index + 9 : i - 1])

    newfile.close()

    #Writing the finalobject into output file

    global finalObject
    try:
        file = open("intermediate.ic", "w")
    except IOError as e:
        print 'Cannot open the file.'
    except:
        print 'Error in opening the file.'

    file.seek(0)
    file.truncate()

    for element in finalObject:
        file.write(element+'\n')

    file.close()

    #writing tokens into tokens file
    global arr
    jsonobj = {}
    for element in arr:
        jsonobj[element[2]] = element[1]

    print finalObject
    try:
        file = open("tokens.json", "w")
    except IOError as e:
        print 'Cannot open the file.'
    except:
        print 'Error in opening the file.'

    file.seek(0)
    file.truncate()

    json.dump(jsonobj, file)

    file.close()

if __name__ == '__main__':
    main()
