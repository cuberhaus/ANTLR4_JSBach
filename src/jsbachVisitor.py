# Generated from jsbach.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .jsbachParser import jsbachParser
else:
    from jsbachParser import jsbachParser

# This class defines a complete generic visitor for a parse tree produced by jsbachParser.

class jsbachVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by jsbachParser#root.
    def visitRoot(self, ctx:jsbachParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#bloc.
    def visitBloc(self, ctx:jsbachParser.BlocContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#statement.
    def visitStatement(self, ctx:jsbachParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#pot.
    def visitPot(self, ctx:jsbachParser.PotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#div_mult_mod.
    def visitDiv_mult_mod(self, ctx:jsbachParser.Div_mult_modContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#num.
    def visitNum(self, ctx:jsbachParser.NumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#mes_minus.
    def visitMes_minus(self, ctx:jsbachParser.Mes_minusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#id.
    def visitId(self, ctx:jsbachParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#definir_procediment.
    def visitDefinir_procediment(self, ctx:jsbachParser.Definir_procedimentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#parametros.
    def visitParametros(self, ctx:jsbachParser.ParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#if.
    def visitIf(self, ctx:jsbachParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#else_condition.
    def visitElse_condition(self, ctx:jsbachParser.Else_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#while.
    def visitWhile(self, ctx:jsbachParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#condicio.
    def visitCondicio(self, ctx:jsbachParser.CondicioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#assign.
    def visitAssign(self, ctx:jsbachParser.AssignContext):
        return self.visitChildren(ctx)



del jsbachParser