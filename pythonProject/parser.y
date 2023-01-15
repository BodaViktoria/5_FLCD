%{
int yylex();
void yyerror(const char *s);
%}

%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define YYDEBUG 1
%}

%token INTEGER
%token STRING
%token BOOLEAN
%token WHILE
%token IF
%token ELSE
%token INPUT_INTEGER
%token INPUT_STRING
%token INPUT_BOOLEAN
%token PRINT
%token ARRAY

%token plus_sign
%token minus_sign
%token multiplication_sign
%token division_sign
%token modulus_sign
%token equal_sign
%token equal_check
%token not_equal_check
%token less_than_check
%token more_than_check
%token less_or_equal_than_check
%token more_or_equal_than_check
%token logical_and
%token logical_or
%token logical_not

%token left_round_bracket
%token right_round_bracket
%token left_array_bracket
%token right_array_bracket
%token less_than_or_equak_check
%token more_than_or_equal_check
%token semicolon
%token left_curly_bracket
%token right_curly_bracket
%token colon
%token comma
%token dot
%token line_bottom
%token space

%token IDENTIFIER
%token INTEGER_CONSTANT
%token STRING_CONSTANT

%start program

%nonassoc SIMPLSTMT
%nonassoc STRUCTSTMT
%right SIMPLSTMT

%%

program : left_curly_bracket compound_statement right_curly_bracket {printf("program -> 'var' decllist cmpdstmt 'end'\n");}
declaration : simple_declaration | array_declaration {printf("program -> 'var' decllist cmpdstmt 'end'\n");}
simple_declaration : type space IDENTIFIER
type : INTEGER | STRING | BOOLEAN
array_declaration : ARRAY left_array_bracket type right_array_bracket IDENTIFIER
compound_statement : statement semicolon AUX
AUX : /*Empty*/ | compound_statement
statement : simplstmt | structstmt
simplstmt : assignstmt | iostmt | declaration
structstmt : compound_statement | ifstmt | whilestmt
ifstmt : IF condition left_curly_bracket compound_statement right_curly_bracket | IF condition left_curly_bracket compound_statement right_curly_bracket ELSE left_curly_bracket compound_statement right_curly_bracket
whilestmt : WHILE condition left_curly_bracket compound_statement right_curly_bracket
assignstmt : IDENTIFIER equal_sign expression
expression : expression plus_sign term | expression minus_sign term | term
term : term multiplication_sign factor | term division_sign factor | term modulus_sign factor | factor
factor : left_round_bracket expression right_round_bracket | IDENTIFIER | INTEGER_CONSTANT
iostmt : INPUT_INTEGER left_round_bracket IDENTIFIER right_round_bracket| INPUT_STRING left_round_bracket IDENTIFIER right_round_bracket | PRINT left_round_bracket IDENTIFIER right_round_bracket | PRINT left_round_bracket STRING_CONSTANT right_round_bracket
condition : left_round_bracket expression RELATION expression right_round_bracket
RELATION : space SIGN space
SIGN : less_than_check | less_or_equal_than_check | equal_check | more_than_check | more_or_equal_than_check | logical_and | logical_or | logical_not
%%

extern FILE *yyin;

void yyerror(const char *s) {
printf("%s\n",s);
}

int main(int argc, char **argv)
{
	if(argc>1) yyin = fopen(argv[1],"r");
	if(argc>2 && !strcmp(argv[2],"-d")) yydebug = 1;
	if(!yyparse()) fprintf(stderr, "\tProgram is syntactically correct.\n");
}