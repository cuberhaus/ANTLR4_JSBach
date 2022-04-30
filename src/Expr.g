grammar Expr;
root : statement+ EOF ;

statement : expr NEWLINE* 
    ;
expr :	<assoc=right> expr POT expr
	| expr MULT expr
	| expr MINUS expr
	| expr MES expr
	| NUM COMMENT
	| NUM 
    | COMMENT
;

ASSIGN: ID '<-' expr ; // x <- 12
COMMENT : '~~~' .*? '~~~' -> skip ;
NEWLINE:'\r'? '\n' ; // return newlines to parser (end-statement signal)
NUM : [0-9]+ ;
MES : '+' ;
MINUS : '-' ;
MULT : '*' ;
POT : '^' ;
WS : [ \t\n\r]+ -> skip ; // skip spaces, tabs, newlines, \r (windows)
