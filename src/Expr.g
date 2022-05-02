grammar Expr;
root : statement+ EOF ;

statement : expr NEWLINE #expression
    // | ID '<-' expr NEWLINE
    | assign    # assign_id
    | NEWLINE   # newline
    ;
expr :	<assoc=right> expr POT expr #pot
	| expr MULT expr    #mult
	| expr MINUS expr   #minus
	| expr MES expr     #mes
	| NUM               #num
    | ID                #id
;
assign : ID '<-' expr NEWLINE; // x <- 12

ID : [a-zA-Z]+ ; // match identifiers
NUM : [0-9]+ ;
NEWLINE :'\r'? '\n' ; // return newlines to parser (end-statement signal)
WS : [ \t]+ -> skip ; // skip spaces, tabs, newlines, \r (windows)
MES : '+' ;
MINUS : '-' ;
MULT : '*' ;
POT : '^' ;
// COMMENT : '~~~' .*? '~~~' -> skip ;
