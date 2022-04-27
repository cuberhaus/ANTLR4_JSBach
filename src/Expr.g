grammar Expr;
root : expr EOF ;
expr : expr MES expr
    | NUM
    ;
NUM : [0-9]+ ;
MES : '+' ;
WS : [ \n]+ -> skip ;
