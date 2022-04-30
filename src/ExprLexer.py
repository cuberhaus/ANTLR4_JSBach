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
        4,0,7,49,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,1,0,1,0,1,0,1,0,1,0,5,0,21,8,0,10,0,12,0,24,9,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,1,3,1,33,8,1,1,1,1,1,1,2,4,2,38,8,2,11,2,12,2,39,
        1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,22,0,7,1,1,3,2,5,3,7,4,9,5,11,
        6,13,7,1,0,1,1,0,48,57,51,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,
        7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,1,15,1,0,0,0,3,32,
        1,0,0,0,5,37,1,0,0,0,7,41,1,0,0,0,9,43,1,0,0,0,11,45,1,0,0,0,13,
        47,1,0,0,0,15,16,5,126,0,0,16,17,5,126,0,0,17,18,5,126,0,0,18,22,
        1,0,0,0,19,21,9,0,0,0,20,19,1,0,0,0,21,24,1,0,0,0,22,23,1,0,0,0,
        22,20,1,0,0,0,23,25,1,0,0,0,24,22,1,0,0,0,25,26,5,126,0,0,26,27,
        5,126,0,0,27,28,5,126,0,0,28,29,1,0,0,0,29,30,6,0,0,0,30,2,1,0,0,
        0,31,33,5,13,0,0,32,31,1,0,0,0,32,33,1,0,0,0,33,34,1,0,0,0,34,35,
        5,10,0,0,35,4,1,0,0,0,36,38,7,0,0,0,37,36,1,0,0,0,38,39,1,0,0,0,
        39,37,1,0,0,0,39,40,1,0,0,0,40,6,1,0,0,0,41,42,5,43,0,0,42,8,1,0,
        0,0,43,44,5,45,0,0,44,10,1,0,0,0,45,46,5,42,0,0,46,12,1,0,0,0,47,
        48,5,94,0,0,48,14,1,0,0,0,4,0,22,32,39,1,6,0,0
    ]

class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT = 1
    NEWLINE = 2
    NUM = 3
    MES = 4
    MINUS = 5
    MULT = 6
    POT = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'^'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "NEWLINE", "NUM", "MES", "MINUS", "MULT", "POT" ]

    ruleNames = [ "COMMENT", "NEWLINE", "NUM", "MES", "MINUS", "MULT", "POT" ]

    grammarFileName = "Expr.g"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


