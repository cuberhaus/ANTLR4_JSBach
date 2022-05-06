grammar jsbach;

root: bloc EOF;

// this statement is needed because we have to call blocks from code and root has EOF, we only want one EOF
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

lectura: '<?>' ID ;
escriptura: '<!>' (expr|STRING)+;
usar_procediment: ID definir_parametres;
definir_procediment : ID usar_parametres '|:' bloc ':|';
usar_parametres : expr* ;
definir_parametres: ID*;
if : 'if' condicio '|:' bloc ':|' (else)? ; // else pot estar o pot no ser-hi
else : 'else' '|:' bloc ':|';
while : 'while' condicio '|:' bloc ':|';
condicio: expr ('=' | '/=' | '<' | '>' | '<=' | '>=') expr;
assign: ID '<-' expr; // x <- 12

ID: [a-zA-Z]+; // match identifiers
NUM: [0-9]+;
STRING : '"' .*? '"' ;
WS: [ \t\n]+ -> skip; // skip spaces, tabs, newlines, \r (windows)
COMMENT : '~~~' .*? '~~~' -> skip ;

DIV: '/';
MOD: '%';
MES: '+';
MINUS: '-';
MULT: '*';
POT: '^';
// NEWLINE :'\r'? '\n' ; // return newlines to parser (end-statement signal)
