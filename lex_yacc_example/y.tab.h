/* A Bison parser, made by GNU Bison 2.3.  */

/* Skeleton interface for Bison's Yacc-like parsers in C

   Copyright (C) 1984, 1989, 1990, 2000, 2001, 2002, 2003, 2004, 2005, 2006
   Free Software Foundation, Inc.

   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 2, or (at your option)
   any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program; if not, write to the Free Software
   Foundation, Inc., 51 Franklin Street, Fifth Floor,
   Boston, MA 02110-1301, USA.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     INTEGER = 258,
     STRING = 259,
     BOOLEAN = 260,
     WHILE = 261,
     IF = 262,
     ELSE = 263,
     INPUT_INTEGER = 264,
     INPUT_STRING = 265,
     INPUT_BOOLEAN = 266,
     PRINT = 267,
     ARRAY = 268,
     plus_sign = 269,
     minus_sign = 270,
     multiplication_sign = 271,
     division_sign = 272,
     modulus_sign = 273,
     equal_sign = 274,
     equal_check = 275,
     not_equal_check = 276,
     less_than_check = 277,
     more_than_check = 278,
     less_or_equal_than_check = 279,
     more_or_equal_than_check = 280,
     logical_and = 281,
     logical_or = 282,
     logical_not = 283,
     left_round_bracket = 284,
     right_round_bracket = 285,
     left_array_bracket = 286,
     right_array_bracket = 287,
     less_than_or_equak_check = 288,
     more_than_or_equal_check = 289,
     semicolon = 290,
     left_curly_bracket = 291,
     right_curly_bracket = 292,
     colon = 293,
     comma = 294,
     dot = 295,
     line_bottom = 296,
     space = 297,
     IDENTIFIER = 298,
     INTEGER_CONSTANT = 299,
     STRING_CONSTANT = 300,
     SIMPLSTMT = 301,
     STRUCTSTMT = 302
   };
#endif
/* Tokens.  */
#define INTEGER 258
#define STRING 259
#define BOOLEAN 260
#define WHILE 261
#define IF 262
#define ELSE 263
#define INPUT_INTEGER 264
#define INPUT_STRING 265
#define INPUT_BOOLEAN 266
#define PRINT 267
#define ARRAY 268
#define plus_sign 269
#define minus_sign 270
#define multiplication_sign 271
#define division_sign 272
#define modulus_sign 273
#define equal_sign 274
#define equal_check 275
#define not_equal_check 276
#define less_than_check 277
#define more_than_check 278
#define less_or_equal_than_check 279
#define more_or_equal_than_check 280
#define logical_and 281
#define logical_or 282
#define logical_not 283
#define left_round_bracket 284
#define right_round_bracket 285
#define left_array_bracket 286
#define right_array_bracket 287
#define less_than_or_equak_check 288
#define more_than_or_equal_check 289
#define semicolon 290
#define left_curly_bracket 291
#define right_curly_bracket 292
#define colon 293
#define comma 294
#define dot 295
#define line_bottom 296
#define space 297
#define IDENTIFIER 298
#define INTEGER_CONSTANT 299
#define STRING_CONSTANT 300
#define SIMPLSTMT 301
#define STRUCTSTMT 302




#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
# define YYSTYPE_IS_TRIVIAL 1
#endif

extern YYSTYPE yylval;

