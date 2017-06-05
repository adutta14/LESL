capital('A') --> ['A']. capital('B') --> ['B']. capital('C') --> ['C'].
capital('D') --> ['D']. capital('E') --> ['E']. capital('F') --> ['F'].
capital('G') --> ['G']. capital('H') --> ['H']. capital('I') --> ['I'].
capital('J') --> ['J']. capital('K') --> ['K']. capital('L') --> ['L'].
capital('M') --> ['M']. capital('N') --> ['N']. capital('O') --> ['O'].
capital('P') --> ['P']. capital('Q') --> ['Q']. capital('R') --> ['R'].
capital('S') --> ['S']. capital('T') --> ['T']. capital('U') --> ['U'].
capital('V') --> ['V']. capital('W') --> ['W']. capital('X') --> ['X'].
capital('Y') --> ['Y']. capital('Z') --> ['Z'].

small('a') --> ['a']. small('b') --> ['b']. small('c') --> ['c']. small('d') --> ['d'].
small('e') --> ['e']. small('f') --> ['f']. small('g') --> ['g']. small('h') --> ['h'].
small('i') --> ['i']. small('j') --> ['j']. small('k') --> ['k']. small('l') --> ['l'].
small('m') --> ['m']. small('n') --> ['n']. small('o') --> ['o']. small('p') --> ['p'].
small('q') --> ['q']. small('r') --> ['r']. small('s') --> ['s']. small('t') --> ['t'].
small('u') --> ['u']. small('v') --> ['v']. small('w') --> ['w']. small('x') --> ['x'].
small('y') --> ['y']. small('z') --> ['z'].

digit('0') --> ['0']. digit('1') --> ['1']. digit('2') --> ['2']. digit('3') --> ['3'].
digit('4') --> ['4']. digit('5') --> ['5']. digit('6') --> ['6']. digit('7') --> ['7'].
digit('8') --> ['8']. digit('9') --> ['9'].

number((X,Y)) --> digit(X), number(Y).
number((X)) --> digit(X).

alphanumeric((X,Y)) --> capital(X), alphanumeric(Y).
alphanumeric((X,Y)) --> small(X), alphanumeric(Y).
alphanumeric((X,Y)) --> number(X), alphanumeric(Y).
alphanumeric((X)) --> capital(X).
alphanumeric((X)) --> small(X).
alphanumeric((X)) --> number(X).

variable((X,Y)) --> capital(X), subvariable(Y).
variable((X)) --> capital(X).
subvariable((X,Y)) --> alphanumeric(X), subvariable(Y).
subvariable((X)) --> alphanumeric(X).

expression(add(X,Y)) --> term(X), ['+'], expression(Y).
expression(subtract(X,Y)) --> term(X), ['-'], expression(Y).
expression(express(X)) --> term(X).
expression((X)) --> ternaryExpression(X).
term(multiply(X,Y)) --> factor(X), ['*'], term(Y).
term(divide(X,Y)) --> factor(X), ['/'], term(Y).
term(modulus(X,Y)) --> factor(X), ['%'], term(Y).
term((X)) --> factor(X).
factor((X)) --> ['('], expression(X), [')'].
factor((X)) --> number(X).
factor((X)) --> variable(X).
ternaryExpression(ternary(X,Y,Z)) --> ['('], booleanExpression(X), [')'], ['?'], factor(Y), [':'], factor(Z).

booleanExpression((X,Y,Z)) --> booleanTerm(X), boolOperator(Y), booleanExpression(Z).
booleanExpression((X,Y)) --> not(X), booleanTerm(Y).
booleanExpression((X)) --> ['('], booleanExpression(X), [')'].
booleanExpression((X)) --> boolean(X).
booleanTerm((X)) --> ['('], booleanExpression(X), [')'].
booleanTerm((X)) --> boolean(X).
boolean((X)) --> expression(X). boolean(bool(X)) --> variable(X).
boolean('true') --> ['true']. boolean('false') --> ['false'].
not('!') --> ['!'].
boolOperator('&') --> ['&']. boolOperator('|') --> ['|']. boolOperator('<') --> ['<'].
boolOperator('>') --> ['>']. boolOperator('<=') --> ['<=']. boolOperator('>=') --> ['>='].
boolOperator('!=') --> ['!=']. boolOperator('==') --> ['=='].

assignment(assign(X,Y)) --> variable(X), ['='], expression(Y).
assignment(assign(X,Y)) --> variable(X), ['='], booleanExpression(Y).
printValue(print(X)) --> ['#show'], variable(X).
printValue(print(X)) --> ['#show'], number(X).

condition(condIf(X,Y)) --> ['if'], ['('], booleanExpression(X), [')'], codeBlock(Y).
condition(condIf(X,Y,Z)) --> ['if'], ['('], booleanExpression(X), [')'], codeBlock(Y), subCondition(Z).
condition((X)) --> subCondition(X).
subCondition(condElse(X)) --> ['else'], codeBlock(X).
subCondition(condElif(X,Y)) --> ['elseif'], ['('], booleanExpression(X), [')'], codeBlock(Y).
subCondition(condElif(X,Y,Z)) --> ['elseif'], ['('], booleanExpression(X), [')'], codeBlock(Y), subCondition(Z).

loop(looping(X,Y)) --> ['while'], ['('], booleanExpression(X), [')'], codeBlock(Y).

codeBlock(codeBlock(X)) --> ['begin'], subCodeBlock(X), ['end'].
subCodeBlock((X,Y)) --> statement(X), subCodeBlock(Y).
subCodeBlock((X)) --> statement(X).

statement((X)) --> condition(X).
statement((X)) --> loop(X).
statement((X)) --> assignment(X), ['.'].
statement((X)) --> printValue(X), ['.'].
code(encode(X,Y)) --> statement(X), code(Y).
code(encode(X)) --> statement(X).
