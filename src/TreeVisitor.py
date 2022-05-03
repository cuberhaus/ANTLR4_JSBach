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

    # def visitExpr(self, ctx):
    #     l = list(ctx.getChildren())
    #     if len(l) == 1:
    #         print(
    #             "  " * self.nivell
    #             + ExprParser.symbolicNames[l[0].getSymbol().type]
    #             + "("
    #             + l[0].getText()
    #             + ")"
    #         )
    #     elif len(l) > 1:
    #         if l[1].getText() == "^":
    #             print("  " * self.nivell + "POT(^)")
    #         elif l[1].getText() == "*":
    #             print("  " * self.nivell + "MULT(*)")
    #         elif l[1].getText() == "+":
    #             print("  " * self.nivell + "MES(+)")
    #         elif l[1].getText() == "-":
    #             print("  " * self.nivell + "MINUS(-)")

    #         self.nivell += 1
    #         # for i in l:
    #         #     print(i.getText())
    #         self.visit(l[0])
    #         self.visit(l[2])
    #         self.nivell -= 1

    # Visit a parse tree produced by ExprParser#assign.
    def visitAssign(self, ctx:ExprParser.AssignContext):
        l = list(ctx.getChildren())
        
        # id = ctx.getText()
        # value = self.visit(l[2])
        for i in l:
            print(l)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#statement.
    def visitStatement(self, ctx:ExprParser.StatementContext):
        l = list(ctx.getChildren())
        if len(l) == 1:
            numero1 = self.visit(l[0])
            print(numero1)
        else:
            print("Error")
            
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#pot.
    def visitPot(self, ctx:ExprParser.PotContext):
        l = list(ctx.getChildren())

        if len(l) == 1:
            print("Error")
        else:
            numero1 = self.visit(l[0])
            numero2 = self.visit(l[2])
            op = l[1].getText()
            return numero1 ** numero2
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#div_mult_mod.
    def visitDiv_mult_mod(self, ctx:ExprParser.Div_mult_modContext):
        l = list(ctx.getChildren())
        if len(l) == 1:
            print("Error")
        # elif len(l) == 3:
        else:
            numero1 = self.visit(l[0])
            numero2 = self.visit(l[2])
            op = l[1].getText()
            if op == '*':
                return numero1 * numero2
            elif op == '%':
                return numero1 % numero2
            elif op == '/':
                return numero1 / numero2
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#num.
    def visitNum(self, ctx:ExprParser.NumContext):
        l = list(ctx.getChildren())
        # num = self.visit(l[0])
        num = int(l[0].getText())
        return num
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#mes_minus.
    def visitMes_minus(self, ctx:ExprParser.Mes_minusContext):
        l = list(ctx.getChildren())
        if len(l) == 1:
            print("error")
        else:
            numero1 = self.visit(l[0])
            numero2 = self.visit(l[2])
            op = l[1].getText()
            # print(op)
            # op = op.getText()
            if op == '+':
                return numero1 + numero2
            if op == '-':
                return numero1 - numero2
        # return numero1 + numero2
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#id.
    def visitId(self, ctx:ExprParser.IdContext):
        l = list(ctx.getChildren())
        identifier = l[0]
        number = ids[identifier]
        return number
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#assign.
    def visitAssign(self, ctx:ExprParser.AssignContext):
        l = list(ctx.getChildren())
        return self.visitChildren(ctx)
