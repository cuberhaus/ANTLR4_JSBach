grammar jsbach;

root: bloc EOF;

// this statement is needed because we have to call blocks from code and root has EOF, we only want one EOF
bloc: statement+;

statement:
	if
	| lectura
	| escriptura
	| declarar_procediment
	| usar_procediment
	| while
	// | expr
	| assign
	| erase_from_list
	| append;

expr:
	'(' expr ')'					# parenthesis
	| <assoc = right> expr POT expr	# pot // Cannot name this expressions as separate declarations
	| expr (DIV | MULT | MOD) expr	# div_mult_mod
	| expr (MES | MINUS) expr		# mes_minus
	| VARIABLE_ID '[' expr ']'      # access_list
	| GET_LIST_SIZE                 # get_list_size
	| NOTA_ID					    # nota_id
	| NUM							# num
	| VARIABLE_ID					# id;

//crea_llista: '{' (expr (',' expr)*)? '}'; // amb comes
crea_llista: '{' expr* '}'; // sense comes
append: VARIABLE_ID '<<' expr newlines;
erase_from_list: '8<' VARIABLE_ID '[' expr ']' newlines;
//access_list: VARIABLE_ID '[' expr ']';

GET_LIST_SIZE: '#' VARIABLE_ID ;

newlines: NEWLINE+;
lectura: '<?>' VARIABLE_ID newlines;
escriptura: '<!>' (expr | STRING)+ newlines;
usar_procediment: FUNCTION_ID definir_arguments newlines;
declarar_procediment:
	FUNCTION_ID declarar_arguments '|:' newlines bloc ':|' newlines;
definir_arguments: expr*;
declarar_arguments: VARIABLE_ID*;
if:
	'if' condicio '|:' newlines bloc ':|' (newlines | else); // el else és opcional 
else: 'else' '|:' newlines bloc ':|' newlines;
while: 'while' condicio '|:' newlines bloc ':|' newlines+;
condicio: expr ('=' | '/=' | '<' | '>' | '<=' | '>=') expr;
assign:
	VARIABLE_ID '<-' (expr | condicio | crea_llista) newlines;

NOTA_ID: ('A0' | 'B0' | [A-G][0-7] | 'C8' | [A-G]);
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
