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

