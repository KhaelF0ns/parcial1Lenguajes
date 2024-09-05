grammar punto5TrigCalc;

prog:   stat+ ;

stat:   expr                        # printExpr
    ;

expr:   SIN '(' expr ')'            # SinFunction
    |   COS '(' expr ')'            # CosFunction
    |   TAN '(' expr ')'            # TanFunction
    |   INT                         # int
    |   FLOAT                       # float
    ;

INT     : [0-9]+ ;
FLOAT   : [0-9]*[.,][0-9]+ ;
WS      : [ \n\r\t]+ -> skip ;
SIN     : 'sin'|'Sin' ;
COS     : 'cos'|'Cos' ;
TAN     : 'tan'|'Tan' ;
