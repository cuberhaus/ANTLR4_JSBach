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

/* COMMENT: '%' ~[\r\n]* '\r'? '\n'; */ 
COMMENT : '~~~' .*? '~~~' -> skip ;
NEWLINE:'\r'? '\n' ; // return newlines to parser (end-statement signal)
NUM : [0-9]+ ;
MES : '+' ;
MINUS : '-' ;
MULT : '*' ;
POT : '^' ;
WS : [ \t]+ -> skip ;
