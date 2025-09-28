// // 2252742
// grammar MiniGo;

// @lexer::header {
// from lexererr import *
// }

// @lexer::members {
// def __init__(self, input=None, output:TextIO = sys.stdout):
//     super().__init__(input, output)
//     self.checkVersion("4.9.2")
//     self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
//     self._actions = None
//     self._predicates = None
//     self.prev_token = None
//     self.list_keyword = [self.IDENTIFIER, self.PARENTHESIS_CLOSING, self.CURLY_CLOSING, self.SQUARE_CLOSING, self.INT_LIT, self.FLOAT_LIT, self.STRING_LIT, self.TRUE, self.FALSE, self.RETURN, self.CONTINUE,self.BREAK, self.INT, self.FLOAT, self.TRUE, self.FALSE, self.STRING, self.NIL, self.COMMENT_SINGLE]

// def nextToken(self):
//     token = super().nextToken();  # Fetch the next token from input
//     return token;  # Return it as the next token

// def emit(self):
//     tk = self.type
//     if tk == self.UNCLOSE_STRING:       
//         result = super().emit();
//         raise UncloseString(result.text);
//     elif tk == self.ILLEGAL_ESCAPE:
//         result = super().emit();
//         raise IllegalEscape(result.text);
//     elif tk == self.ERROR_CHAR:
//         result = super().emit();
//         raise ErrorToken(result.text);
//     elif tk == self.NL :
//         if self.prev_token != None and self.prev_token in self.list_keyword:
//             self.prev_token = self.SEMICOLON;
//             self.type = self.SEMICOLON;
//             self.text = ';';
//             return super().emit();
//         return super().nextToken();
//     else:
//         self.prev_token = tk;
//         return super().emit();
// }

// options{
// 	language = Python3;
// }

// /*
//   CHANGE:
//   1. add struct_lit : IDENTIFIER struct_value;
// */

// program: list_decl EOF;

// list_decl: decl list_decl | decl ;

// decl: variable 
//         | array_declare 
//         | struct_decl
//         | interface_lit 
//         | function
//         | constants_stmt
//         | method_func;

// // TYPE AND VALUE, NOTE THAT: IDETIFIER IS FOR STRUCT TYPE
// type_variable: primitive_variable | IDENTIFIER;
// // primitive_variable: INT | FLOAT | STRING | BOOLEAN | STRING;
// primitive_variable: INT | FLOAT | STRING | BOOLEAN | STRING ; // redundant at string
// primitive_value:
// 	INT_LIT
// 	| FLOAT_LIT
// 	| STRING_LIT
// 	| TRUE
// 	| FALSE
//   | NIL; // 6 BUG, LACK OF NIL VALUE

// ////////////////////////////////////////////////////////////////////////

// // ARRAY TYPE 
// array_declare: VAR IDENTIFIER list_dim type_variable end_var;
//   list_dim: mono_dim list_dim | mono_dim;
//     mono_dim: SQUARE_OPENING dim SQUARE_CLOSING;
//       dim: INT_LIT | IDENTIFIER;

// // array_access: IDENTIFIER mono_dim; 1 BUG
// // array_access: IDENTIFIER list_dim; 1.1 BUG
// array_access: IDENTIFIER list_dim;

// array_lit: list_dim type_variable CURLY_OPENING array_value CURLY_CLOSING;

// array_value: array_value_sub COMMA array_value | array_value_sub;

// array_value_sub: array_value_except_array | CURLY_OPENING array_value CURLY_CLOSING ;

// // array_value_except_array: array_value_mono COMMA array_value | array_value_mono ;  // 3 BUG
// array_value_except_array: array_value_mono COMMA array_value_except_array | array_value_mono ;  // 3 BUG

// array_value_mono: primitive_value | IDENTIFIER | struct_lit ;

// ////////////////////////////////////////////////////////////////////////

// // STRUCT TYPE
// struct_decl:
// 	TYPE IDENTIFIER STRUCT CURLY_OPENING list_fields CURLY_CLOSING end_var;
//   list_fields: list_fields_init ; // can not null
//   list_fields_init: fields list_fields_init | fields;
//     fields: IDENTIFIER type_except_array end_var ;
// // struct_access: IDENTIFIER DARK_POINT IDENTIFIER ;  // 4 BUG as struct asccess can be array_access at the lhs
// struct_access: lhs ;  // 4 BUG as struct asccess can be array_access at the lhs˚¨
// // THIS IS FOR ASSIGNMENT MEANING STATEMENT OR EXPRESSION
// struct_fields_assign: struct_access ASSIGN_LOGIC expr;

// // WHERE TO PUT THIS
// struct_instance:
// 	IDENTIFIER ASSIGN_LOGIC struct_lit;
//     list_fields_value_null: list_fields_value | ;
//     list_fields_value: list_fields_value_sub ;
//   list_fields_value_sub:
// 	fields_value COMMA list_fields_value_sub
// 	| fields_value;
//     fields_value: IDENTIFIER COLON primitive_value | IDENTIFIER COLON expr;
//   struct_value: CURLY_OPENING list_fields_value_null CURLY_CLOSING;

//   struct_lit: IDENTIFIER struct_value;

// ////////////////////////////////////////////////////////////////////////

// // INTERFACE TYPE
// interface_lit:
// 	TYPE IDENTIFIER INTERFACE CURLY_OPENING list_methods CURLY_CLOSING end_var;
//   list_methods: methods list_methods | methods;
//     methods:
// 	// IDENTIFIER PARENTHESIS_OPENING list_para PARENTHESIS_CLOSING optional_return_type end_var;
// 	IDENTIFIER PARENTHESIS_OPENING (list_para | ) PARENTHESIS_CLOSING optional_return_type end_var;
//       list_para: list_para_mono COMMA list_para | list_para_mono;
//       // list_para_mono: sharing_type | common_type | ; // WHAT IF list_para is empty so in list_para: empty , empty is accept => 5 BUG
//       list_para_mono: sharing_type | common_type; // WHAT IF list_para is empty so in list_para: empty , empty is accept => 5 BUG
//         sharing_type:
// 	IDENTIFIER type_except_array COMMA sharing_type
// 	| IDENTIFIER type_except_array;
//         type_except_array:  type_variable | list_dim type_variable;
//         common_type: common_type_sub type_except_array;
//           common_type_sub: IDENTIFIER COMMA common_type_sub | IDENTIFIER;

// ////////////////////////////////////////////////////////////////////////

// // VARIABLE, CONSTANTS AND FUNCTION variables: global_var | local_var | func_para ;
// variable: global_var end_var;
// //   global_var: VAR IDENTIFIER optional_type optional_init end_var;
//     optional_type: type_except_array | ;
// //     optional_init: ASSIGN_RULE expr | ;

//     global_var: var_decl_init | var_decl_no_init;

//         var_decl_no_init: VAR IDENTIFIER type_except_array;

//         var_decl_init: VAR IDENTIFIER optional_type ASSIGN_RULE expr;

// list_expr: expr COMMA list_expr | expr;

// expr: expr OR expr1 | expr1;

// expr1: expr1 AND expr2 | expr2;

// expr2:
// 	expr2 EQUAL expr3
// 	| expr2 DIFFER expr3
// 	| expr2 LESS expr3
// 	| expr2 LESS_OR_EQUAL expr3
// 	| expr2 GREATER expr3
// 	| expr2 GREATER_OR_EQUAL expr3
// 	| expr3;

// expr3:  
//     expr3 PLUS expr4 
//     | expr3 MINUS expr4 
//     | expr4;

// expr4:
// 	expr4 ASTERISK expr5
// 	| expr4 DIVIDE expr5
// 	| expr4 MODULO expr5
// 	| expr5;

// expr5: NOT expr5 | MINUS expr5 | expr6;

// expr6:
// 	// expr6 SQUARE_OPENING expr SQUARE_CLOSING
// 	expr6 list_dim_array_access
// 	| expr6 DARK_POINT IDENTIFIER
// 	| expr6 DARK_POINT function_call
// 	| expr7;

// expr7:
// 	primitive_value
// 	// | list_fields_value // 8 BUG: WHY LIST_FIELDS_VALUE
// 	| array_lit
// 	| NIL
//   | lhs // 8 BUG: ADDING LHS for struct_access
//   | function_call
//   // | IDENTIFIER struct_value
//   // | array_access // 7 BUG: FORGET ARRAY_ACCESS
//   | struct_lit
//   | IDENTIFIER
// 	| PARENTHESIS_OPENING expr PARENTHESIS_CLOSING;

// end_var: SEMICOLON | NL;

// // local_var: ; // stmt

// // func_para: ;

// list_dim_array_access: SQUARE_OPENING expr SQUARE_CLOSING list_dim_array_access | SQUARE_OPENING expr SQUARE_CLOSING;

// constants: CONST IDENTIFIER ASSIGN_RULE expr;
// constants_stmt: constants end_var;

// function:
// 	FUNC IDENTIFIER PARENTHESIS_OPENING (list_para | ) PARENTHESIS_CLOSING optional_return_type
// 		function_body end_var;
//   optional_return_type: type_except_array | ;
//   function_body: CURLY_OPENING list_stmt CURLY_CLOSING;

// function_call:
// 	IDENTIFIER PARENTHESIS_OPENING list_para_value PARENTHESIS_CLOSING;
// // REMEMBER THAT IF THE FUNCTION CALL IS MAKE A INFINITY LOOP
//   list_para_value: list_para_value_notnull | ;
//     list_para_value_notnull:
// 	para_value COMMA list_para_value_notnull
// 	| para_value;
//   //     para_value:
// 	// primitive_value
// 	// | struct_access
// 	// | IDENTIFIER
// 	// | array_access                  // 2 BUG
//   // | IDENTIFIER struct_value
//   // | expr
//   // | method_func_call
// 	// | function_call;
//       para_value:
// 	primitive_value
// 	//| struct_access same with lhs
// 	| IDENTIFIER
// 	| lhs
//   // | IDENTIFIER struct_value
//   | struct_lit
//   | expr
//   | method_func_call
// 	| function_call;

// method_func:
// 	FUNC receiver IDENTIFIER PARENTHESIS_OPENING (list_para | ) PARENTHESIS_CLOSING optional_return_type
// 		function_body end_var;
//   receiver: PARENTHESIS_OPENING IDENTIFIER IDENTIFIER PARENTHESIS_CLOSING;

// method_func_call: expr6 DARK_POINT function_call;
// // method_func_call: IDENTIFIER DARK_POINT function_call;
// // method_func_call: expr6 DARK_POINT function_call;

// ////////////////////////////////////////////////////////////////////////

// // STATEMENTS
// stmt:
// 	variable
// 	| constants_stmt
// 	| assign_stmt
// 	// | if_stmt // CHANGE TO if_mono
//   | if_stmt_end
// 	| for_stmt
// 	| break_stmt
// 	| continue_stmt
// 	| call_stmt
// 	| return_stmt;

// list_stmt: stmt list_stmt | stmt;

// // list_stmt_all: (list_stmt | if_many_stmt) list_stmt_all | (list_stmt | if_many_stmt);

// // assign_stmt: LHS_stmt assign_op expr;
// // ADD EXPR6 TO AS ACCESS
// assign_stmt: assign_stmt_no_end end_var;

// assign_stmt_no_end: lhs assign_op expr ;
    
//     //     IDENTIFIER assign_op expr 
//     // | array_access assign_op expr 
//     // | struct_access assign_op expr 

// lhs: lhs DARK_POINT IDENTIFIER
//     | lhs SQUARE_OPENING expr SQUARE_CLOSING
//     | IDENTIFIER ;
// // example: a[2+4] 
// // lhs: lhs DARK_POINT IDENTIFIER
// //     | lhs list_dim
// //     | IDENTIFIER ;


// // REMEMBER COMPLICATED LIKE FUNCTION CALL IS AN ARRAY
// // LHS_stmt: IDENTIFIER | array_access | struct_access;

// assign_op:
// 	ASSIGN_LOGIC
// 	| PLUS_EQUAL
// 	| MINUS_EQUAL
// 	| ASTERISK_EQUAL
// 	| DIVIDE_EQUAL
// 	| MODULO_EQUAL;

// // if_stmt: else_if_stmt else_stmt end_var;
// if_stmt_end: if_stmt end_var;
// if_stmt: IF PARENTHESIS_OPENING expr PARENTHESIS_CLOSING CURLY_OPENING list_stmt CURLY_CLOSING else_stmt;

// else_stmt: ELSE CURLY_OPENING list_stmt CURLY_CLOSING | ELSE if_stmt | ;

// for_stmt: basic_form | init_form | range_form;

// basic_form: FOR condition CURLY_OPENING list_stmt CURLY_CLOSING end_var;

// condition: expr;

// init_form:
// 	FOR initilization SEMICOLON condition SEMICOLON update CURLY_OPENING list_stmt CURLY_CLOSING end_var;

// initilization: IDENTIFIER assign_op expr | var_decl_init;

// update: IDENTIFIER assign_op expr;

// range_form: FOR index COMMA value ASSIGN_LOGIC RANGE expr CURLY_OPENING list_stmt CURLY_CLOSING end_var;

// index: IDENTIFIER;

// value: IDENTIFIER;

// break_stmt: BREAK SEMICOLON;

// continue_stmt: CONTINUE SEMICOLON;

// call_stmt: function_call end_var | method_func_call end_var;

// return_stmt: RETURN return_tail end_var;

// return_tail: expr | ;

// //////////////////////////////////////////////////////////////////////////
// // ////////////////////////////////////////////////////////////////////////

// IF: 'if';
// ELSE: 'else';
// FOR: 'for';
// RETURN: 'return';
// FUNC: 'func';
// TYPE: 'type';
// STRUCT: 'struct';
// INTERFACE: 'interface';
// STRING: 'string';
// INT: 'int';
// FLOAT: 'float';
// BOOLEAN: 'boolean';
// CONST: 'const';
// VAR: 'var';
// CONTINUE: 'continue';
// BREAK: 'break';
// RANGE: 'range';
// NIL: 'nil';
// TRUE: 'true';
// FALSE: 'false';

// // FRAGMENT define here
// fragment DIGIT: [0-9];
// fragment DIGIT_NOZERO: [1-9];
// fragment SINGLEQUOTE: ['];
// fragment DOUBLEQUOTE: ["];
// fragment BINARY_PRE: '0b' | '0B';
// fragment OCTAL_PRE: '0o' | '0O';
// fragment HEXADECIMAL_PRE: '0x' | '0X';
// fragment CHAR_STR:
//     ~["\n\\] 
// 	| '\\' ('n' | 't' | 'r' | '"' | '\\') ;

// // COMMENT_SINGLE: '//' .*? ('\n' | ('\r' '\n') | EOF) -> skip;
// COMMENT_SINGLE: '//' (~[\n] | ~[\r\n])* -> skip;

// COMMENT_BLOCK: '/*' (COMMENT_BLOCK | .)*? '*/' -> skip;

// IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;

// fragment DECIMAL: [0] | DIGIT_NOZERO DIGIT*;

// fragment BINARY: BINARY_PRE [01]+;

// fragment OCTAL: OCTAL_PRE [0-7]+;

// fragment HEXADECIMAL: HEXADECIMAL_PRE [0-9a-fA-F]+;

// INT_LIT: DECIMAL | BINARY | OCTAL | HEXADECIMAL;

// // NOTE THAT: BEHIND exp signal has number start with DIGIT_NOZERO FLOAT_LIT: DIGIT+ '.' DIGIT*
// // ([eE][+-]? DIGIT_NOZERO+DIGIT*)? ;
// FLOAT_LIT: DIGIT+ '.' DIGIT* ([eE][+-]? DIGIT+)?;

// STRING_LIT: DOUBLEQUOTE CHAR_STR* DOUBLEQUOTE;

// // BOOLEAN_LIT: 'true' | 'false';

// // NIL_LIT: 'nil';

// // DEFINE TYPE here
// DIFFER: '!=';
// NOT: '!';
// AND: '&&';
// OR: '||';
// PLUS_EQUAL: '+=';
// PLUS: '+';
// MINUS_EQUAL: '-=';
// MINUS: '-';
// ASTERISK_EQUAL: '*=';
// ASTERISK: '*';
// DIVIDE_EQUAL: '/=';
// DIVIDE: '/';
// MODULO_EQUAL: '%=';
// MODULO: '%';

// EQUAL: '==';
// GREATER_OR_EQUAL: '>=';
// GREATER: '>';
// LESS_OR_EQUAL: '<=';
// LESS: '<';

// DARK_POINT: '.';

// ASSIGN_LOGIC: ':=';
// ASSIGN_RULE: '=';

// PARENTHESIS_OPENING: '(';
// PARENTHESIS_CLOSING: ')';
// SQUARE_OPENING: '[';
// SQUARE_CLOSING: ']';
// CURLY_OPENING: '{';
// CURLY_CLOSING: '}';
// COMMA: ',';
// SEMICOLON: ';';
// COLON: ':';

// // NL: '\n' -> skip; //skip newlines
// NL: '\r'* '\n';

// WS: [ \t\r\f]+ -> skip; // skip spaces, tabs 

// UNCLOSE_STRING:
// 	DOUBLEQUOTE CHAR_STR* ('\r'? '\n' | EOF ) {
//     if (len(self.text) >= 2 and self.text[-2] == '\r' and self.text[-1] == '\n'):
//         raise UncloseString(self.text[:-2])
//     elif (self.text[-1] == '\n' ):
//         raise UncloseString(self.text[:-1])
//     else: 
//         raise UncloseString(self.text)
// };

// ILLEGAL_ESCAPE:
// 	DOUBLEQUOTE CHAR_STR* ('\\' ~["rnt\\] | '\r'? '\n' | '\\' EOF | EOF) {raise IllegalEscape(self.text)};

// ERROR_CHAR: . {raise ErrorToken(self.text)};
// //UNCLOSE_STRING: '=' ~["]? DOUBLEQUOTE {raise UncloseString(self.text)} ;

//2252662
grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
prev_token = None


def emit(self):
    tk = self.type
    semi_list = [self.ID, self.RPAREN, self.RBRACE, self.RBRACK, self.INT_LIT, self.FLOAT_LIT, self.STRING_LIT, self.TRUE, self.FALSE, self.RETURN, self.CONTINUE,self.BREAK, self.INT, self.FLOAT, self.BOOL, self.STRING, self.NIL]
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        self.prev_token = self.UNCLOSE_STRING;
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        self.prev_token = self.ILLEGAL_ESCAPE;
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        self.prev_token = self.ERROR_CHAR;
        raise ErrorToken(result.text);		 
    elif tk == self.NEWLINE:
        if self.prev_token in semi_list:
            self.prev_token = self.SEMI;
            self.text = ';';
            self.type = self.SEMI;
            return super().emit();
        return super().nextToken();
    else:
        self.prev_token = tk;
        return super().emit();



}

options{
	language = Python3;
}

program: program_element_list EOF;
program_element_list:
	declaration program_element_list
	| declaration;

optional_variable_type: variable_type |;
variable_type: primitive_type | array_type;
primitive_type: INT | FLOAT | STRING | BOOL | ID;

literal:
	INT_LIT
	| FLOAT_LIT
	| STRING_LIT
	| TRUE
	| FALSE
	| array_literal
	| struct_literal
	| NIL;

array_literal: array_type LBRACE array_block RBRACE;
array_pre_element:
	INT_LIT
	| FLOAT_LIT
	| ID
	| STRING_LIT
	| TRUE
	| FALSE
	| struct_literal
	| NIL;
array_pre_element_list:
	array_pre_element COMMA array_pre_element_list
	| array_pre_element;
array_pre_element_array_lit:
	LBRACE array_pre_element_array_lit RBRACE
	| LBRACE array_pre_element_array_lit COMMA array_pre_element_array_lit RBRACE
	| array_pre_element_list;
array_element: array_pre_element | array_pre_element_array_lit;
array_block: array_element COMMA array_block | array_element;

array_type: multiple_dimension variable_type;
multiple_dimension:
	LBRACK dim_literal RBRACK multiple_dimension
	| LBRACK dim_literal RBRACK;
dim_literal: INT_LIT | ID;

struct_literal: ID LBRACE optional_field_values RBRACE;
optional_field_values: field_values |;
field_values: field_value COMMA field_values | field_value;
field_value: ID COLON expression1;

optional_list_expression: list_expression |;
list_expression:
	expression1 COMMA list_expression
	| expression1;
expression1: expression1 OR expression2 | expression2;
expression2: expression2 AND expression3 | expression3;
expression3:
	expression3 (EQ | NEQ | LT | LE | GE | GT) expression4
	| expression4;
expression4: expression4 (ADD | SUB) expression5 | expression5;
expression5:
	expression5 (MUL | DIV | MOD) expression6
	| expression6;
expression6: (SUB | NOT) expression6 | expression7;
expression7:
	expression7 LBRACK expression1 RBRACK
	| expression7 DOT ID (LPAREN optional_list_expression RPAREN)?
	// method call and struct field access
	| expression8;
expression8:
	literal
	| ID
	| function_call
	| LPAREN expression1 RPAREN;

function_call: ID LPAREN optional_list_expression RPAREN;
// lhs: lhs LBRACK expression1 RBRACK | lhs DOT ID | array_literal | struct_literal | ID; lhs: lhs
// LPAREN list_expression? RPAREN | lhs LBRACK expression1 RBRACK | lhs DOT ID | pre_lhs; pre_lhs:
// literal | ID (LPAREN list_expression? RPAREN)? | LPAREN expression1 RPAREN;

declaration:
	(
		variable_declaration
		| constant_declaration
		| func_declaration
		| type_declaration
	) SEMI;

variable_declaration: VAR ID variable_characteristic;
variable_characteristic:
	variable_type
	| optional_variable_type initialization;
initialization: ASSIGN expression1;

constant_declaration: CONST ID ASSIGN expression1;

func_declaration: function_method_declaration;
function_method_declaration:
	FUNC (LPAREN ID ID RPAREN)? ID LPAREN list_param RPAREN optional_variable_type statement_block;
list_param: no_null_list_param |;
no_null_list_param:
	parameter COMMA no_null_list_param
	| parameter;
parameter: ID COMMA parameter | ID variable_type;

type_declaration: struct_declaration | interface_declaration;

struct_declaration: TYPE ID STRUCT LBRACE list_of_fields RBRACE;
list_of_fields:
	struct_parameter SEMI list_of_fields
	| struct_parameter SEMI;
struct_parameter: ID variable_type;

interface_declaration:
	TYPE ID INTERFACE LBRACE list_of_interface_methods RBRACE;

list_of_interface_methods:
	interface_method list_of_interface_methods
	| interface_method;
interface_method:
	ID LPAREN list_param RPAREN optional_variable_type SEMI;

list_statement: statement list_statement | statement;
statement:
	(
		declaration_stmt
		| assign_statement
		| if_statement
		| for_statement
		| break_statement
		| continue_statement
		| call_statement
		| return_statement
	);

declaration_stmt: (variable_declaration | constant_declaration) SEMI;

assign_statement:
	lhs_assign (
		COLON_ASSIGN
		| ADD_ASSIGN
		| SUB_ASSIGN
		| MUL_ASSIGN
		| DIV_ASSIGN
		| MOD_ASSIGN
	) expression1 SEMI;

lhs_assign:
	lhs_assign LBRACK expression1 RBRACK
	| lhs_assign DOT ID
	| ID;
// lhs_assign: lhs_assign LBRACK expression1 RBRACK | lhs_assign DOT ID | ID;

statement_block: LBRACE list_statement RBRACE;

if_statement:
	IF LPAREN expression1 RPAREN statement_block else_if_statement? else_statement? SEMI;
else_statement: ELSE statement_block;
else_if_statement:
	ELSE IF LPAREN expression1 RPAREN statement_block else_if_statement
	| ELSE IF LPAREN expression1 RPAREN statement_block;

for_statement:
	(basic_for_loop | for_loop_icu | for_loop_range) SEMI;

basic_for_loop: FOR expression1 statement_block;

for_loop_icu:
	FOR init_statement SEMI expression1 SEMI init_assign statement_block;
init_statement: init_assign | init_declared;
init_assign:
	ID (
		COLON_ASSIGN
		| ADD_ASSIGN
		| SUB_ASSIGN
		| MUL_ASSIGN
		| DIV_ASSIGN
		| MOD_ASSIGN
	) expression1;
init_declared: VAR ID variable_type? ASSIGN expression1;

for_loop_range:
	FOR ID COMMA ID COLON_ASSIGN RANGE expression1 statement_block;

break_statement: BREAK SEMI;

continue_statement: CONTINUE SEMI;

call_statement: function_method_call_stmt SEMI;
function_method_call_stmt:
	optional_instance_stmt ID LPAREN optional_list_expression RPAREN;
// function_method_call_stmt: (lhs_assign DOT)? ID LPAREN optional_list_expression RPAREN;
optional_instance_stmt: expression7 DOT |;

return_statement: RETURN expression1? SEMI;

// Keywords
IF: 'if';
ELSE: 'else';
FOR: 'for';
RETURN: 'return';
FUNC: 'func';
TYPE: 'type';
STRUCT: 'struct';
INTERFACE: 'interface';
STRING: 'string';
INT: 'int';
FLOAT: 'float';
BOOL: 'boolean';
CONST: 'const';
VAR: 'var';
CONTINUE: 'continue';
BREAK: 'break';
RANGE: 'range';
NIL: 'nil';
TRUE: 'true';
FALSE: 'false';

// Operators
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
EQ: '==';
NEQ: '!=';
LT: '<';
LE: '<=';
GT: '>';
GE: '>=';
AND: '&&';
OR: '||';
NOT: '!';
ASSIGN: '=';
ADD_ASSIGN: '+=';
SUB_ASSIGN: '-=';
MUL_ASSIGN: '*=';
DIV_ASSIGN: '/=';
MOD_ASSIGN: '%=';
COLON_ASSIGN: ':=';
DOT: '.';

// Separators
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
LBRACK: '[';
RBRACK: ']';
COMMA: ',';
SEMI: ';';
COLON: ':';

// ID specification
ID: [a-zA-Z_][a-zA-Z0-9_]*;

// Literals

// Update not transform into decimal ones
INT_LIT: (DECIMAL_LIT | BINARY_LIT | OCTAL_LIT | HEX_LIT);
fragment DECIMAL_LIT: '0' | [1-9] [0-9]*;
fragment BINARY_LIT: '0' [bB] [01]+;
fragment OCTAL_LIT: '0' [oO] [0-7]+;
fragment HEX_LIT: '0' [xX] [0-9a-fA-F]+;

FLOAT_LIT: DECIMAL_LEAD0 '.' DECIMAL_LEAD0? EXPONENT?;
fragment DECIMAL_LEAD0: [0-9]+;
fragment EXPONENT: [eE] [+-]? DECIMAL_LEAD0;

STRING_LIT: '"' STR_CHAR* '"';
fragment STR_CHAR: ~[\r\n"\\] | ESCAPE_SEQ;
fragment ESCAPE_SEQ: '\\' [ntr"\\];
fragment ILL_ESCAPE_SEQ: '\\' ( ~[ntr"\\] | EOF);

// Whitespaces and comments NEWLINE: '\r'? '\n';
NEWLINE: '\r'? '\n';
WS: [ \t\f\r]+ -> skip; // skip spaces, tabs  
//LINE_COMMENT: '//' ~[\r\n]* -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' (BLOCK_COMMENT | .)*? '*/' -> skip;

// Error handling
UNCLOSE_STRING:
	'"' STR_CHAR* ('\r\n' | '\n' | EOF) {
    if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
        raise UncloseString(self.text[:-2])
    elif (self.text[-1] == '\n'):
        raise UncloseString(self.text[:-1])
    else:
        raise UncloseString(self.text)
};

ILLEGAL_ESCAPE:
	'"' STR_CHAR* ILL_ESCAPE_SEQ {
    raise IllegalEscape(self.text)
};

ERROR_CHAR: . {raise ErrorToken(self.text)};