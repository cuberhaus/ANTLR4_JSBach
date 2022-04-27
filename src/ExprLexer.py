# Generated from Expr.g by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\5")
        buf.write("\27\b\1\4\2\t\2\4\3\t\3\4\4\t\4\3\2\6\2\13\n\2\r\2\16")
        buf.write("\2\f\3\3\3\3\3\4\6\4\22\n\4\r\4\16\4\23\3\4\3\4\2\2\5")
        buf.write("\3\3\5\4\7\5\3\2\4\3\2\62;\4\2\f\f\"\"\2\30\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\3\n\3\2\2\2\5\16\3\2\2\2\7")
        buf.write("\21\3\2\2\2\t\13\t\2\2\2\n\t\3\2\2\2\13\f\3\2\2\2\f\n")
        buf.write("\3\2\2\2\f\r\3\2\2\2\r\4\3\2\2\2\16\17\7-\2\2\17\6\3\2")
        buf.write("\2\2\20\22\t\3\2\2\21\20\3\2\2\2\22\23\3\2\2\2\23\21\3")
        buf.write("\2\2\2\23\24\3\2\2\2\24\25\3\2\2\2\25\26\b\4\2\2\26\b")
        buf.write("\3\2\2\2\5\2\f\23\3\b\2\2")
        return buf.getvalue()


class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NUM = 1
    MES = 2
    WS = 3

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'" ]

    symbolicNames = [ "<INVALID>",
            "NUM", "MES", "WS" ]

    ruleNames = [ "NUM", "MES", "WS" ]

    grammarFileName = "Expr.g"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


