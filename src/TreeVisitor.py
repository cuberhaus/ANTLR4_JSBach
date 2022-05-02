from re import L


if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
    from .ExprVisitor import ExprVisitor
else:
    from ExprParser import ExprParser
    from ExprVisitor import ExprVisitor


class TreeVisitor(ExprVisitor):
    def __init__(self):
        self.nivell = 0
        self.ids = {}

    def visitExpr(self, ctx):
        l = list(ctx.getChildren())
        if len(l) == 1:
            print(
                "  " * self.nivell
                + ExprParser.symbolicNames[l[0].getSymbol().type]
                + "("
                + l[0].getText()
                + ")"
            )
        elif len(l) > 1:
            if l[1].getText() == "^":
                print("  " * self.nivell + "POT(^)")
            elif l[1].getText() == "*":
                print("  " * self.nivell + "MULT(*)")
            elif l[1].getText() == "+":
                print("  " * self.nivell + "MES(+)")
            elif l[1].getText() == "-":
                print("  " * self.nivell + "MINUS(-)")

            self.nivell += 1
            # for i in l:
            #     print(i.getText())
            self.visit(l[0])
            self.visit(l[2])
            self.nivell -= 1

    # Visit a parse tree produced by ExprParser#assign_id.
    def visitAssign_id(self, ctx:ExprParser.Assign_idContext):
        l = list(ctx.getChildren())
        # id = ctx.getText()
        # value = self.visit(l[2])
        for i in l:
            print(l)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#statement.
    def visitStatement(self, ctx:ExprParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#pot.
    def visitPot(self, ctx:ExprParser.PotContext):
        op1, op, op2 = list(ctx.getChildren())
        numero1 = self.visit(op1)
        numero2 = self.visit(op2)
        return numero1 ** numero2
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#div_mult_mod.
    def visitDiv_mult_mod(self, ctx:ExprParser.Div_mult_modContext):
        op1, op, op2 = list(ctx.getChildren())
        if op == '*':
            numero1 = self.visit(op1)
            numero2 = self.visit(op2)
            return op1 * op2
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#num.
    def visitNum(self, ctx:ExprParser.NumContext):
        num = list(ctx.getChildren())
        return num
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#mes_minus.
    def visitMes_minus(self, ctx:ExprParser.Mes_minusContext):
        op1, op, op2 = list(ctx.getChildren)
        numero1 = self.visit(op1)
        numero2 = self.visit(op2)
        if op == '+':
            return numero1 + numero2
        if op == '-':
            return numero1 - numero2
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#id.
    def visitId(self, ctx:ExprParser.IdContext):
        op1 = list(ctx.getChildren())
        number = ids[op1]
        return number
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#assign.
    def visitAssign(self, ctx:ExprParser.AssignContext):
        op1, op, op2 = list(ctx.getChildren())
        ids 
        return self.visitChildren(ctx)
