# Generated from Expr.g by ANTLR 4.10.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,9,52,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,1,0,1,0,1,0,1,1,4,1,24,8,1,11,1,12,1,25,1,
        2,4,2,29,8,2,11,2,12,2,30,1,3,3,3,34,8,3,1,3,1,3,1,4,4,4,39,8,4,
        11,4,12,4,40,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,0,0,9,1,1,3,
        2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,1,0,3,2,0,65,90,97,122,1,0,48,
        57,2,0,9,9,32,32,55,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,
        0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,
        0,0,1,19,1,0,0,0,3,23,1,0,0,0,5,28,1,0,0,0,7,33,1,0,0,0,9,38,1,0,
        0,0,11,44,1,0,0,0,13,46,1,0,0,0,15,48,1,0,0,0,17,50,1,0,0,0,19,20,
        5,60,0,0,20,21,5,45,0,0,21,2,1,0,0,0,22,24,7,0,0,0,23,22,1,0,0,0,
        24,25,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,4,1,0,0,0,27,29,7,1,
        0,0,28,27,1,0,0,0,29,30,1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,0,31,6,
        1,0,0,0,32,34,5,13,0,0,33,32,1,0,0,0,33,34,1,0,0,0,34,35,1,0,0,0,
        35,36,5,10,0,0,36,8,1,0,0,0,37,39,7,2,0,0,38,37,1,0,0,0,39,40,1,
        0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,42,1,0,0,0,42,43,6,4,0,0,43,
        10,1,0,0,0,44,45,5,43,0,0,45,12,1,0,0,0,46,47,5,45,0,0,47,14,1,0,
        0,0,48,49,5,42,0,0,49,16,1,0,0,0,50,51,5,94,0,0,51,18,1,0,0,0,5,
        0,25,30,33,40,1,6,0,0
    ]

class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    ID = 2
    NUM = 3
    NEWLINE = 4
    WS = 5
    MES = 6
    MINUS = 7
    MULT = 8
    POT = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'<-'", "'+'", "'-'", "'*'", "'^'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "NUM", "NEWLINE", "WS", "MES", "MINUS", "MULT", "POT" ]

    ruleNames = [ "T__0", "ID", "NUM", "NEWLINE", "WS", "MES", "MINUS", 
                  "MULT", "POT" ]

    grammarFileName = "Expr.g"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


