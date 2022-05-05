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
    def visitRoot(self, ctx: jsbachParser.RootContext):
        children = list(ctx.getChildren())
        for i in children:
            self.visit(i)
        # return self.visitChildren(ctx)

    def visitBloc(self, ctx: jsbachParser.BlocContext):
        children = list(ctx.getChildren())
        for i in children:
            self.visit(i)
        # return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#assign.
    def visitAssign(self, ctx: jsbachParser.AssignContext):
        children = list(ctx.getChildren())

        if len(children) == 1:
            print("Error")
        else:
            identifier = children[0].getText()
            numero = self.visit(children[2])
            # op = children[1].getText()

            self.ids[identifier] = numero
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#statement.
    def visitStatement(self, ctx: jsbachParser.StatementContext):
        children = list(ctx.getChildren())
        if len(children) == 1:
            numero1 = self.visit(children[0])
            print(numero1)
        else:
            print("Error")

        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#pot.
    def visitPot(self, ctx: jsbachParser.PotContext):
        children = list(ctx.getChildren())

        if len(children) == 1:
            print("Error")
        else:
            numero1 = self.visit(children[0])
            numero2 = self.visit(children[2])
            if isinstance(numero1, str):
                numero1 = self.ids[numero1]
            if isinstance(numero2, str):
                numero2 = self.ids[numero2]
            # op = children[1].getText()
            return numero1 ** numero2
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#div_mult_mod.
    def visitDiv_mult_mod(self, ctx: jsbachParser.Div_mult_modContext):
        children = list(ctx.getChildren())
        if len(children) == 1:
            print("Error")
        # elif len(l) == 3:
        else:
            numero1 = self.visit(children[0])
            numero2 = self.visit(children[2])
            if isinstance(numero1, str):
                numero1 = self.ids[numero1]
            if isinstance(numero2, str):
                numero2 = self.ids[numero2]
            op = children[1].getText()
            if op == '*':
                return numero1 * numero2
            elif op == '%':
                return numero1 % numero2
            elif op == '/':
                return numero1 / numero2
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#num.
    def visitNum(self, ctx: jsbachParser.NumContext):
        children = list(ctx.getChildren())
        # num = self.visit(l[0])
        num = int(children[0].getText())
        return num
        # return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#mes_minus.
    def visitMes_minus(self, ctx: jsbachParser.Mes_minusContext):
        children = list(ctx.getChildren())
        if len(children) == 1:
            print("error")
        else:
            numero1 = self.visit(children[0])
            numero2 = self.visit(children[2])
            if isinstance(numero1, str):
                numero1 = self.ids[numero1]
            if isinstance(numero2, str):
                numero2 = self.ids[numero2]
            op = children[1].getText()
            # print(op)
            # op = op.getText()
            if op == '+':
                return numero1 + numero2
            if op == '-':
                return numero1 - numero2
        # return numero1 + numero2
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#id.
    def visitId(self, ctx: jsbachParser.IdContext):
        children = list(ctx.getChildren())
        identifier = children[0].getText()
        return identifier
        # number = self.ids[identifier]
        # return number
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#lectura.
    def visitLectura(self, ctx:jsbachParser.LecturaContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by jsbachParser#escriptura.
    def visitEscriptura(self, ctx:jsbachParser.EscripturaContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by jsbachParser#usar_procediment.
    def visitUsar_procediment(self, ctx:jsbachParser.Usar_procedimentContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by jsbachParser#definir_procediment.
    def visitDefinir_procediment(self, ctx:jsbachParser.Definir_procedimentContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by jsbachParser#usar_parametres.
    def visitUsar_parametres(self, ctx:jsbachParser.Usar_parametresContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by jsbachParser#definir_parametres.
    def visitDefinir_parametres(self, ctx:jsbachParser.Definir_parametresContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by jsbachParser#if.
    def visitIf(self, ctx:jsbachParser.IfContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by jsbachParser#else.
    def visitElse(self, ctx:jsbachParser.ElseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by jsbachParser#while.
    def visitWhile(self, ctx:jsbachParser.WhileContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by jsbachParser#condicio.
    def visitCondicio(self, ctx:jsbachParser.CondicioContext):
        return self.visitChildren(ctx)
