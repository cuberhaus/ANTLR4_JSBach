grammar Expr;
root : expr EOF ;
expr :	<assoc=right> expr POT expr
	| expr MULT expr
	| expr MINUS expr
	| expr MES expr
	| NUM
;
NUM : [0-9]+ ;
MES : '+' ;
MINUS : '-' ;
MULT : '*' ;
POT : '^' ;
WS : [ \n]+ -> skip ;
