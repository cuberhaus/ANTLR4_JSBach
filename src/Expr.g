grammar Expr;
root : statement+ EOF ;

statement : expr NEWLINE
    | ASSIGN 
    | NEWLINE
    ;
expr :	<assoc=right> expr POT expr
	| expr MULT expr
	| expr MINUS expr
	| expr MES expr
	| NUM 
;

ASSIGN: ID '<-' expr ; // x <- 12
COMMENT : '~~~' .*? '~~~' -> skip ;
NEWLINE:'\r'? '\n' ; // return newlines to parser (end-statement signal)
ID: [a-zA->]+ ; // match identifiers
NUM : [0-9]+ ;
MES : '+' ;
MINUS : '-' ;
MULT : '*' ;
POT : '^' ;
WS : [ \t\r]+ -> skip ; // skip spaces, tabs, newlines, \r (windows)
