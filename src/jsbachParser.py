# Generated from jsbach.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,22,96,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,1,1,4,1,27,8,1,11,
        1,12,1,28,1,2,1,2,1,2,1,2,1,2,3,2,36,8,2,1,3,1,3,1,3,3,3,41,8,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,52,8,3,10,3,12,3,55,9,3,
        1,4,1,4,1,4,1,4,1,4,1,4,1,5,5,5,64,8,5,10,5,12,5,67,9,5,1,6,1,6,
        1,6,1,6,1,6,1,6,3,6,75,8,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,
        8,1,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,0,1,6,11,0,2,4,6,
        8,10,12,14,16,18,20,0,3,2,0,16,17,20,20,1,0,18,19,1,0,6,11,95,0,
        22,1,0,0,0,2,26,1,0,0,0,4,35,1,0,0,0,6,40,1,0,0,0,8,56,1,0,0,0,10,
        65,1,0,0,0,12,68,1,0,0,0,14,76,1,0,0,0,16,81,1,0,0,0,18,87,1,0,0,
        0,20,91,1,0,0,0,22,23,3,2,1,0,23,24,5,0,0,1,24,1,1,0,0,0,25,27,3,
        4,2,0,26,25,1,0,0,0,27,28,1,0,0,0,28,26,1,0,0,0,28,29,1,0,0,0,29,
        3,1,0,0,0,30,36,3,12,6,0,31,36,3,8,4,0,32,36,3,16,8,0,33,36,3,6,
        3,0,34,36,3,20,10,0,35,30,1,0,0,0,35,31,1,0,0,0,35,32,1,0,0,0,35,
        33,1,0,0,0,35,34,1,0,0,0,36,5,1,0,0,0,37,38,6,3,-1,0,38,41,5,14,
        0,0,39,41,5,13,0,0,40,37,1,0,0,0,40,39,1,0,0,0,41,53,1,0,0,0,42,
        43,10,5,0,0,43,44,5,21,0,0,44,52,3,6,3,5,45,46,10,4,0,0,46,47,7,
        0,0,0,47,52,3,6,3,5,48,49,10,3,0,0,49,50,7,1,0,0,50,52,3,6,3,4,51,
        42,1,0,0,0,51,45,1,0,0,0,51,48,1,0,0,0,52,55,1,0,0,0,53,51,1,0,0,
        0,53,54,1,0,0,0,54,7,1,0,0,0,55,53,1,0,0,0,56,57,5,13,0,0,57,58,
        3,10,5,0,58,59,5,1,0,0,59,60,3,2,1,0,60,61,5,2,0,0,61,9,1,0,0,0,
        62,64,5,13,0,0,63,62,1,0,0,0,64,67,1,0,0,0,65,63,1,0,0,0,65,66,1,
        0,0,0,66,11,1,0,0,0,67,65,1,0,0,0,68,69,5,3,0,0,69,70,3,18,9,0,70,
        71,5,1,0,0,71,72,3,2,1,0,72,74,5,2,0,0,73,75,3,14,7,0,74,73,1,0,
        0,0,74,75,1,0,0,0,75,13,1,0,0,0,76,77,5,4,0,0,77,78,5,1,0,0,78,79,
        3,2,1,0,79,80,5,2,0,0,80,15,1,0,0,0,81,82,5,5,0,0,82,83,3,18,9,0,
        83,84,5,1,0,0,84,85,3,2,1,0,85,86,5,2,0,0,86,17,1,0,0,0,87,88,3,
        6,3,0,88,89,7,2,0,0,89,90,3,6,3,0,90,19,1,0,0,0,91,92,5,13,0,0,92,
        93,5,12,0,0,93,94,3,6,3,0,94,21,1,0,0,0,7,28,35,40,51,53,65,74
    ]

class jsbachParser ( Parser ):

    grammarFileName = "jsbach.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'|:'", "':|'", "'if'", "'else'", "'while'", 
                     "'='", "'/='", "'<'", "'>'", "'<='", "'>='", "'<-'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'/'", "'%'", 
                     "'+'", "'-'", "'*'", "'^'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "NUM", "WS", "DIV", "MOD", "MES", 
                      "MINUS", "MULT", "POT", "COMMENT" ]

    RULE_root = 0
    RULE_bloc = 1
    RULE_statement = 2
    RULE_expr = 3
    RULE_definir_procediment = 4
    RULE_parametros = 5
    RULE_if = 6
    RULE_else_condition = 7
    RULE_while = 8
    RULE_condicio = 9
    RULE_assign = 10

    ruleNames =  [ "root", "bloc", "statement", "expr", "definir_procediment", 
                   "parametros", "if", "else_condition", "while", "condicio", 
                   "assign" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    ID=13
    NUM=14
    WS=15
    DIV=16
    MOD=17
    MES=18
    MINUS=19
    MULT=20
    POT=21
    COMMENT=22

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bloc(self):
            return self.getTypedRuleContext(jsbachParser.BlocContext,0)


        def EOF(self):
            return self.getToken(jsbachParser.EOF, 0)

        def getRuleIndex(self):
            return jsbachParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = jsbachParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.bloc()
            self.state = 23
            self.match(jsbachParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlocContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.StatementContext)
            else:
                return self.getTypedRuleContext(jsbachParser.StatementContext,i)


        def getRuleIndex(self):
            return jsbachParser.RULE_bloc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloc" ):
                return visitor.visitBloc(self)
            else:
                return visitor.visitChildren(self)




    def bloc(self):

        localctx = jsbachParser.BlocContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_bloc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 25
                self.statement()
                self.state = 28 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << jsbachParser.T__2) | (1 << jsbachParser.T__4) | (1 << jsbachParser.ID) | (1 << jsbachParser.NUM))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_(self):
            return self.getTypedRuleContext(jsbachParser.IfContext,0)


        def definir_procediment(self):
            return self.getTypedRuleContext(jsbachParser.Definir_procedimentContext,0)


        def while_(self):
            return self.getTypedRuleContext(jsbachParser.WhileContext,0)


        def expr(self):
            return self.getTypedRuleContext(jsbachParser.ExprContext,0)


        def assign(self):
            return self.getTypedRuleContext(jsbachParser.AssignContext,0)


        def getRuleIndex(self):
            return jsbachParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = jsbachParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 35
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.if_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.definir_procediment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 32
                self.while_()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 33
                self.expr(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 34
                self.assign()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return jsbachParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class PotContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.ExprContext)
            else:
                return self.getTypedRuleContext(jsbachParser.ExprContext,i)

        def POT(self):
            return self.getToken(jsbachParser.POT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPot" ):
                return visitor.visitPot(self)
            else:
                return visitor.visitChildren(self)


    class Div_mult_modContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.ExprContext)
            else:
                return self.getTypedRuleContext(jsbachParser.ExprContext,i)

        def DIV(self):
            return self.getToken(jsbachParser.DIV, 0)
        def MULT(self):
            return self.getToken(jsbachParser.MULT, 0)
        def MOD(self):
            return self.getToken(jsbachParser.MOD, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDiv_mult_mod" ):
                return visitor.visitDiv_mult_mod(self)
            else:
                return visitor.visitChildren(self)


    class NumContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(jsbachParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum" ):
                return visitor.visitNum(self)
            else:
                return visitor.visitChildren(self)


    class Mes_minusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.ExprContext)
            else:
                return self.getTypedRuleContext(jsbachParser.ExprContext,i)

        def MES(self):
            return self.getToken(jsbachParser.MES, 0)
        def MINUS(self):
            return self.getToken(jsbachParser.MINUS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMes_minus" ):
                return visitor.visitMes_minus(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(jsbachParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = jsbachParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [jsbachParser.NUM]:
                localctx = jsbachParser.NumContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 38
                self.match(jsbachParser.NUM)
                pass
            elif token in [jsbachParser.ID]:
                localctx = jsbachParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 39
                self.match(jsbachParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 53
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 51
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = jsbachParser.PotContext(self, jsbachParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 42
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 43
                        self.match(jsbachParser.POT)
                        self.state = 44
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = jsbachParser.Div_mult_modContext(self, jsbachParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 45
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 46
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << jsbachParser.DIV) | (1 << jsbachParser.MOD) | (1 << jsbachParser.MULT))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 47
                        self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = jsbachParser.Mes_minusContext(self, jsbachParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 48
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 49
                        _la = self._input.LA(1)
                        if not(_la==jsbachParser.MES or _la==jsbachParser.MINUS):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 50
                        self.expr(4)
                        pass

             
                self.state = 55
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Definir_procedimentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(jsbachParser.ID, 0)

        def parametros(self):
            return self.getTypedRuleContext(jsbachParser.ParametrosContext,0)


        def bloc(self):
            return self.getTypedRuleContext(jsbachParser.BlocContext,0)


        def getRuleIndex(self):
            return jsbachParser.RULE_definir_procediment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinir_procediment" ):
                return visitor.visitDefinir_procediment(self)
            else:
                return visitor.visitChildren(self)




    def definir_procediment(self):

        localctx = jsbachParser.Definir_procedimentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_definir_procediment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(jsbachParser.ID)
            self.state = 57
            self.parametros()
            self.state = 58
            self.match(jsbachParser.T__0)
            self.state = 59
            self.bloc()
            self.state = 60
            self.match(jsbachParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(jsbachParser.ID)
            else:
                return self.getToken(jsbachParser.ID, i)

        def getRuleIndex(self):
            return jsbachParser.RULE_parametros

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametros" ):
                return visitor.visitParametros(self)
            else:
                return visitor.visitChildren(self)




    def parametros(self):

        localctx = jsbachParser.ParametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_parametros)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==jsbachParser.ID:
                self.state = 62
                self.match(jsbachParser.ID)
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condicio(self):
            return self.getTypedRuleContext(jsbachParser.CondicioContext,0)


        def bloc(self):
            return self.getTypedRuleContext(jsbachParser.BlocContext,0)


        def else_condition(self):
            return self.getTypedRuleContext(jsbachParser.Else_conditionContext,0)


        def getRuleIndex(self):
            return jsbachParser.RULE_if

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)




    def if_(self):

        localctx = jsbachParser.IfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(jsbachParser.T__2)
            self.state = 69
            self.condicio()
            self.state = 70
            self.match(jsbachParser.T__0)
            self.state = 71
            self.bloc()
            self.state = 72
            self.match(jsbachParser.T__1)
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==jsbachParser.T__3:
                self.state = 73
                self.else_condition()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bloc(self):
            return self.getTypedRuleContext(jsbachParser.BlocContext,0)


        def getRuleIndex(self):
            return jsbachParser.RULE_else_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_condition" ):
                return visitor.visitElse_condition(self)
            else:
                return visitor.visitChildren(self)




    def else_condition(self):

        localctx = jsbachParser.Else_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_else_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(jsbachParser.T__3)
            self.state = 77
            self.match(jsbachParser.T__0)
            self.state = 78
            self.bloc()
            self.state = 79
            self.match(jsbachParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condicio(self):
            return self.getTypedRuleContext(jsbachParser.CondicioContext,0)


        def bloc(self):
            return self.getTypedRuleContext(jsbachParser.BlocContext,0)


        def getRuleIndex(self):
            return jsbachParser.RULE_while

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile" ):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)




    def while_(self):

        localctx = jsbachParser.WhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_while)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(jsbachParser.T__4)
            self.state = 82
            self.condicio()
            self.state = 83
            self.match(jsbachParser.T__0)
            self.state = 84
            self.bloc()
            self.state = 85
            self.match(jsbachParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.ExprContext)
            else:
                return self.getTypedRuleContext(jsbachParser.ExprContext,i)


        def getRuleIndex(self):
            return jsbachParser.RULE_condicio

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicio" ):
                return visitor.visitCondicio(self)
            else:
                return visitor.visitChildren(self)




    def condicio(self):

        localctx = jsbachParser.CondicioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_condicio)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.expr(0)
            self.state = 88
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << jsbachParser.T__5) | (1 << jsbachParser.T__6) | (1 << jsbachParser.T__7) | (1 << jsbachParser.T__8) | (1 << jsbachParser.T__9) | (1 << jsbachParser.T__10))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 89
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(jsbachParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(jsbachParser.ExprContext,0)


        def getRuleIndex(self):
            return jsbachParser.RULE_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = jsbachParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(jsbachParser.ID)
            self.state = 92
            self.match(jsbachParser.T__11)
            self.state = 93
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         




