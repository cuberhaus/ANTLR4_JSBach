grammar jsbach;

root: bloc EOF;

bloc : statement+;

statement: if
    | lectura
    | escriptura
    | definir_procediment
    | usar_procediment
    | while
    | expr
    | assign
    ;

expr: <assoc = right> expr POT expr #pot // Cannot name this expressions as separate declarations
	| expr (DIV | MULT | MOD) expr #div_mult_mod
	| expr (MES | MINUS) expr #mes_minus
	| NUM #num
	| ID #id
;

usar_procediment: ID parametres;
definir_procediment : ID parametres '|:' bloc ':|';
parametres: ID*;
if : 'if' condicio '|:' bloc ':|' (else)? ; // else pot estar o pot no ser-hi
else : 'else' '|:' bloc ':|';
while : 'while' condicio '|:' bloc ':|';
condicio: expr ('=' | '/=' | '<' | '>' | '<=' | '>=') expr;
assign: ID '<-' expr; // x <- 12

ID: [a-zA-Z]+; // match identifiers
NUM: [0-9]+;
// NEWLINE :'\r'? '\n' ; // return newlines to parser (end-statement signal)
WS: [ \t\n]+ -> skip; // skip spaces, tabs, newlines, \r (windows)
DIV: '/';
MOD: '%';
MES: '+';
MINUS: '-';
MULT: '*';
POT: '^';
COMMENT : '~~~' .*? '~~~' -> skip ;
