/*
grammar test
Grammar of simple mathematical expressions. Without any attribute and action.
Test grammar for demo and education porpuse.
- Example of input which accepts by the grammar:
-- x = a + b * c

Written by: Morteza Zakeri
*/
grammar main;

start:
    prog EOF
    ;

prog: prog assign| assign;

assign: Id '=' expr Newline?;

expr:
    expr '+' term #rule_plus
    | expr '-' term  #rule_minus
    | term #rule3
    ;

term:
    term '*' fact
    | term '/' fact
    | fact
    ;

fact:
    BComment
    | Comment
    | Id
    | Number
    | '('expr')'
    ;

Comment: COMMENT -> channel(HIDDEN);
BComment: BLOCK_COMMENT -> channel(HIDDEN);

/* Lexical rules*/
OP: '(';
CP: ')';
Plus: '+';
MINUS: '-';
MUL: '*';
DIVIDE: '/';
ASSIGN: '=';


Id: IDENTIFIER;
Number: NUMBER;


fragment COMMENT: '//' .*? '\r'? '\n';
fragment BLOCK_COMMENT	:'/*' .*? '*/' ;
fragment IDENTIFIER: [a-zA-Z][a-zA-Z]* | [?*]+;
fragment NUMBER: [0-9]+;

Newline: '\n' -> channel(HIDDEN);
Whitespace: [ \t\r]+ -> channel(HIDDEN);