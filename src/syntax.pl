capital --> ['A']. capital --> ['B']. capital --> ['C']. capital --> ['D']. capital --> ['E'].
capital --> ['F']. capital --> ['G']. capital --> ['H']. capital --> ['I']. capital --> ['J'].
capital --> ['K']. capital --> ['L']. capital --> ['M']. capital --> ['N']. capital --> ['O'].
capital --> ['P']. capital --> ['Q']. capital --> ['R']. capital --> ['S']. capital --> ['T'].
capital --> ['U']. capital --> ['V']. capital --> ['W']. capital --> ['X']. capital --> ['Y'].
capital --> ['Z'].

small --> ['a']. small --> ['b']. small --> ['c']. small --> ['d']. small --> ['e']. small --> ['f'].
small --> ['g']. small --> ['h']. small --> ['i']. small --> ['j']. small --> ['k']. small --> ['l'].
small --> ['m']. small --> ['n']. small --> ['o']. small --> ['p']. small --> ['q']. small --> ['r'].
small --> ['s']. small --> ['t']. small --> ['u']. small --> ['v']. small --> ['w']. small --> ['x'].
small --> ['y']. small --> ['z'].

digit --> ['0']. digit --> ['1']. digit --> ['2']. digit --> ['3']. digit --> ['4']. digit --> ['5'].
digit --> ['6']. digit --> ['7']. digit --> ['8']. digit --> ['9'].

number --> digit, number.
number --> digit.

alphanumeric --> capital, alphanumeric. alphanumeric --> small, alphanumeric.
alphanumeric --> number, alphanumeric. alphanumeric --> capital.
alphanumeric --> small. alphanumeric --> number.

variable --> capital, subvariable. variable --> capital.
subvariable --> alphanumeric, subvariable. subvariable --> alphanumeric.

expression --> term, ['+'], expression. expression --> term, ['-'], expression. expression --> term.
expression --> ternaryExpression.
term --> factor, ['*'], term. term --> factor, ['/'], term. term --> factor, ['%'], term. term --> factor.
factor --> ['('], expression, [')']. factor --> number. factor --> variable.
ternaryExpression --> ['('], booleanExpression, [')'], ['?'], factor, [':'], factor.
ternaryExpression --> ['('], booleanExpression, [')'], ['?'], factor, [':'], booleanTerm.
ternaryExpression --> ['('], booleanExpression, [')'], ['?'], booleanTerm, [':'], factor.
ternaryExpression --> ['('], booleanExpression, [')'], ['?'], booleanTerm, [':'], booleanTerm.

booleanExpression --> booleanTerm, boolOperator, booleanExpression.
booleanExpression --> ['!'], booleanTerm.
booleanExpression --> ['('], booleanExpression, [')'].
booleanExpression --> boolean.
booleanTerm --> ['('], booleanExpression, [')']. booleanTerm --> boolean.
boolean --> expression. boolean --> variable. boolean --> ['true']. boolean --> ['false'].
boolOperator --> ['&']. boolOperator --> ['|']. boolOperator --> ['!'].
boolOperator --> ['<']. boolOperator --> ['>']. boolOperator --> ['<='].
boolOperator --> ['>=']. boolOperator --> ['!=']. boolOperator --> ['=='].

assignment --> variable, ['='], expression. assignment --> variable, ['='], booleanExpression.
printValue --> ['#show'], variable. printValue --> ['#show'], number.

codeBlock --> ['begin'], subCodeBlock, ['end'].
subCodeBlock --> statement, subCodeBlock. subCodeBlock --> statement.

condition --> ['if'], ['('], booleanExpression, [')'], codeBlock.
condition --> ['if'], ['('], booleanExpression, [')'], codeBlock, subCondition.
condition --> subCondition.
subCondition --> ['else'], codeBlock.
subCondition --> ['elseif'], ['('], booleanExpression, [')'], codeBlock.
subCondition --> ['elseif'], ['('], booleanExpression, [')'], codeBlock, subCondition.

loop --> ['while'], ['('], booleanExpression, [')'], codeBlock.

statement --> condition. statement --> loop.
statement --> assignment, ['.']. statement --> printValue, ['.'].
code --> statement, code. code --> statement.