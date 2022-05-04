from re import L


if __name__ is not None and "." in __name__:
    from jsbachParser import jsbachParser
    from jsbachVisitor import jsbachVisitor
else:
    from jsbachParser import jsbachParser
    from jsbachVisitor import jsbachVisitor


class TreeVisitor(jsbachVisitor):
    def __init__(self):
        self.nivell = 0
        self.ids = {}
        
    # Visit a parse tree produced by ExprParser#root.
    def visitRoot(self, ctx:jsbachParser.RootContext):
        l = list(ctx.getChildren())
        for i in l:
            self.visit(i)
        # return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#assign.
    def visitAssign(self, ctx:jsbachParser.AssignContext):
        l = list(ctx.getChildren())

        if len(l) == 1:
            print("Error")
        else:
            # id = self.visit(l[0])
            id = l[0].getText()
            numero = self.visit(l[2])
            op = l[1].getText()
            
            self.ids[id] = numero
        # value = self.visit(l[2])
        # for i in l:
        #     print(l)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#statement.
    def visitStatement(self, ctx:jsbachParser.StatementContext):
        l = list(ctx.getChildren())
        if len(l) == 1:
            numero1 = self.visit(l[0])
            print(numero1)
        else:
            print("Error")
            
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#pot.
    def visitPot(self, ctx:jsbachParser.PotContext):
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
    def visitDiv_mult_mod(self, ctx:jsbachParser.Div_mult_modContext):
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
    def visitNum(self, ctx:jsbachParser.NumContext):
        l = list(ctx.getChildren())
        # num = self.visit(l[0])
        num = int(l[0].getText())
        return num
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#mes_minus.
    def visitMes_minus(self, ctx:jsbachParser.Mes_minusContext):
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
    def visitId(self, ctx:jsbachParser.IdContext):
        l = list(ctx.getChildren())
        identifier = l[0]
        number = self.ids[identifier]
        return number
        return self.visitChildren(ctx)
