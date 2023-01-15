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

program : left_curly_bracket compound_statement right_curly_bracket {printf("program : left_curly_bracket compound_statement right_curly_bracket\n");}
declaration : simple_declaration | array_declaration {printf("declaration : simple_declaration | array_declaration\n");}
simple_declaration : type space IDENTIFIER {printf("simple_declaration : type space IDENTIFIE\n");}
type : INTEGER | STRING | BOOLEAN {printf("type : INTEGER | STRING | BOOLEAN\n");}
array_declaration : ARRAY left_array_bracket type right_array_bracket IDENTIFIER {printf("array_declaration : ARRAY left_array_bracket type right_array_bracket IDENTIFIER\n");}
compound_statement : statement semicolon AUX {printf("compound_statement : statement semicolon AUX\n");}
AUX : /*Empty*/ | compound_statement {printf("AUX : /*Empty*/ | compound_statement\n");}
statement : simplstmt | structstmt {printf("statement : simplstmt | structstmt\n");}
simplstmt : assignstmt | iostmt | declaration {printf("simplstmt : assignstmt | iostmt | declaration\n");}
structstmt : compound_statement | ifstmt | whilestmt {printf("structstmt : compound_statement | ifstmt | whilestmt\n");}
ifstmt : IF condition left_curly_bracket compound_statement right_curly_bracket | IF condition left_curly_bracket compound_statement right_curly_bracket ELSE left_curly_bracket compound_statement right_curly_bracket {printf("ifstmt : IF condition left_curly_bracket compound_statement right_curly_bracket | IF condition left_curly_bracket compound_statement right_curly_bracket ELSE left_curly_bracket compound_statement right_curly_bracket\n");}
whilestmt : WHILE condition left_curly_bracket compound_statement right_curly_bracket {printf("whilestmt : WHILE condition left_curly_bracket compound_statement right_curly_bracket\n");}
assignstmt : IDENTIFIER equal_sign expression {printf("assignstmt : IDENTIFIER equal_sign expression\n");}
expression : expression plus_sign term | expression minus_sign term | term {printf("expression : expression plus_sign term | expression minus_sign term | term\n");}
term : term multiplication_sign factor | term division_sign factor | term modulus_sign factor | factor {printf("term : term multiplication_sign factor | term division_sign factor | term modulus_sign factor | factor\n");}
factor : left_round_bracket expression right_round_bracket | IDENTIFIER | INTEGER_CONSTANT {printf("factor : left_round_bracket expression right_round_bracket | IDENTIFIER | INTEGER_CONSTANT\n");}
iostmt : INPUT_INTEGER left_round_bracket IDENTIFIER right_round_bracket| INPUT_STRING left_round_bracket IDENTIFIER right_round_bracket | PRINT left_round_bracket IDENTIFIER right_round_bracket | PRINT left_round_bracket STRING_CONSTANT right_round_bracket {printf("iostmt : INPUT_INTEGER left_round_bracket IDENTIFIER right_round_bracket| INPUT_STRING left_round_bracket IDENTIFIER right_round_bracket | PRINT left_round_bracket IDENTIFIER right_round_bracket | PRINT left_round_bracket STRING_CONSTANT right_round_bracket \n");}
condition : left_round_bracket expression RELATION expression right_round_bracket {printf("condition : left_round_bracket expression RELATION expression right_round_bracket\n");}
RELATION : space SIGN space {printf("RELATION : space SIGN space\n");}
SIGN : less_than_check | less_or_equal_than_check | equal_check | more_than_check | more_or_equal_than_check | logical_and | logical_or | logical_not {printf("SIGN : less_than_check | less_or_equal_than_check | equal_check | more_than_check | more_or_equal_than_check | logical_and | logical_or | logical_not\n");}
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