# Generated from Expr.g by ANTLR 4.10.1
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
        4,1,9,50,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,4,0,10,8,0,11,0,12,
        0,11,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,21,8,1,1,2,1,2,1,2,3,2,26,8,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,40,8,2,10,
        2,12,2,43,9,2,1,3,1,3,1,3,1,3,1,3,1,3,0,1,4,4,0,2,4,6,0,0,53,0,9,
        1,0,0,0,2,20,1,0,0,0,4,25,1,0,0,0,6,44,1,0,0,0,8,10,3,2,1,0,9,8,
        1,0,0,0,10,11,1,0,0,0,11,9,1,0,0,0,11,12,1,0,0,0,12,13,1,0,0,0,13,
        14,5,0,0,1,14,1,1,0,0,0,15,16,3,4,2,0,16,17,5,4,0,0,17,21,1,0,0,
        0,18,21,3,6,3,0,19,21,5,4,0,0,20,15,1,0,0,0,20,18,1,0,0,0,20,19,
        1,0,0,0,21,3,1,0,0,0,22,23,6,2,-1,0,23,26,5,3,0,0,24,26,5,2,0,0,
        25,22,1,0,0,0,25,24,1,0,0,0,26,41,1,0,0,0,27,28,10,6,0,0,28,29,5,
        9,0,0,29,40,3,4,2,6,30,31,10,5,0,0,31,32,5,8,0,0,32,40,3,4,2,6,33,
        34,10,4,0,0,34,35,5,7,0,0,35,40,3,4,2,5,36,37,10,3,0,0,37,38,5,6,
        0,0,38,40,3,4,2,4,39,27,1,0,0,0,39,30,1,0,0,0,39,33,1,0,0,0,39,36,
        1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,5,1,0,0,0,43,
        41,1,0,0,0,44,45,5,2,0,0,45,46,5,1,0,0,46,47,3,4,2,0,47,48,5,4,0,
        0,48,7,1,0,0,0,5,11,20,25,39,41
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<-'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'+'", "'-'", "'*'", "'^'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "ID", "NUM", "NEWLINE", 
                      "WS", "MES", "MINUS", "MULT", "POT" ]

    RULE_root = 0
    RULE_statement = 1
    RULE_expr = 2
    RULE_assign = 3

    ruleNames =  [ "root", "statement", "expr", "assign" ]

    EOF = Token.EOF
    T__0=1
    ID=2
    NUM=3
    NEWLINE=4
    WS=5
    MES=6
    MINUS=7
    MULT=8
    POT=9

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

        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatementContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatementContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = ExprParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.statement()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExprParser.ID) | (1 << ExprParser.NUM) | (1 << ExprParser.NEWLINE))) != 0)):
                    break

            self.state = 13
            self.match(ExprParser.EOF)
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

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def NEWLINE(self):
            return self.getToken(ExprParser.NEWLINE, 0)

        def assign(self):
            return self.getTypedRuleContext(ExprParser.AssignContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ExprParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 20
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.expr(0)
                self.state = 16
                self.match(ExprParser.NEWLINE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.assign()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 19
                self.match(ExprParser.NEWLINE)
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

        def NUM(self):
            return self.getToken(ExprParser.NUM, 0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def POT(self):
            return self.getToken(ExprParser.POT, 0)

        def MULT(self):
            return self.getToken(ExprParser.MULT, 0)

        def MINUS(self):
            return self.getToken(ExprParser.MINUS, 0)

        def MES(self):
            return self.getToken(ExprParser.MES, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ExprParser.NUM]:
                self.state = 23
                self.match(ExprParser.NUM)
                pass
            elif token in [ExprParser.ID]:
                self.state = 24
                self.match(ExprParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 41
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 39
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 27
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 28
                        self.match(ExprParser.POT)
                        self.state = 29
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 30
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 31
                        self.match(ExprParser.MULT)
                        self.state = 32
                        self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 33
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 34
                        self.match(ExprParser.MINUS)
                        self.state = 35
                        self.expr(5)
                        pass

                    elif la_ == 4:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 36
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 37
                        self.match(ExprParser.MES)
                        self.state = 38
                        self.expr(4)
                        pass

             
                self.state = 43
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def NEWLINE(self):
            return self.getToken(ExprParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = ExprParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(ExprParser.ID)
            self.state = 45
            self.match(ExprParser.T__0)
            self.state = 46
            self.expr(0)
            self.state = 47
            self.match(ExprParser.NEWLINE)
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
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         




