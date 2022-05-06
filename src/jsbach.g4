grammar jsbach;

root: bloc EOF;

// this statement is needed because we have to call blocks from code and root has EOF, we only want one EOF
bloc: statement+;

statement:
	if
	| lectura
	| escriptura
	| definir_procediment
	| usar_procediment
	| while
	// | expr
	| assign;

expr:
	'(' expr ')'					# parenthesis
	| <assoc = right> expr POT expr	# pot // Cannot name this expressions as separate declarations
	| expr (DIV | MULT | MOD) expr	# div_mult_mod
	| expr (MES | MINUS) expr		# mes_minus
	| NUM							# num
	| VARIABLE_ID					# id;

newlines: NEWLINE+;
lectura: '<?>' VARIABLE_ID newlines;
escriptura: '<!>' (expr | STRING)+ newlines;
usar_procediment: FUNCTION_ID definir_arguments newlines;
definir_procediment:
	FUNCTION_ID arguments '|:' newlines bloc ':|' newlines;
definir_arguments: expr*;
arguments: VARIABLE_ID*;
if:
	'if' condicio '|:' newlines bloc ':|' (newlines | else); // el else és opcional 
else: 'else' '|:' newlines bloc ':|' newlines;
while: 'while' condicio '|:' newlines bloc ':|' newlines+;
condicio: expr ('=' | '/=' | '<' | '>' | '<=' | '>=') expr;
assign: VARIABLE_ID '<-' (expr | condicio) newlines;

FUNCTION_ID:
	[A-Z] [a-zA-Z]*; // functions start with a capital letter
VARIABLE_ID:
	[a-z] [a-zA-Z]*; // variables start with a lower-case letter
NUM: [0-9]+;
STRING: '"' .*? '"';
WS: [ \t]+ -> skip; // skip spaces, tabs, newlines, \r (windows)
COMMENT: '~~~' .*? '~~~' -> skip;
NEWLINE:
	'\r'? '\n'; // return newlines to parser (end-statement signal)

DIV: '/';
MOD: '%';
MES: '+';
MINUS: '-';
MULT: '*';
POT: '^';
