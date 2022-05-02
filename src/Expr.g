grammar Expr;
root: statement+ EOF;

statement: expr | assign;
expr:
	<assoc = right> expr POT expr	# pot
	| expr (DIV | MULT | MOD)		# div_mult_mod
	| expr (MES | MINUS) expr		# mes_minus
	| NUM							# num
	| ID							# id;
assign: ID '<-' expr; // x <- 12

ID: [a-zA-Z]+; // match identifiers
NUM: [0-9]+;
// NEWLINE :'\r'? '\n' ; // return newlines to parser (end-statement signal)
WS:
	[ \t\n]+ -> skip; // skip spaces, tabs, newlines, \r (windows)
DIV: '/';
MOD: '%';
MES: '+';
MINUS: '-';
MULT: '*';
POT: '^';
COMMENT : '~~~' .*? '~~~' -> skip ;
