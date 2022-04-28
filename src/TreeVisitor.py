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
            print("  " * self.nivell +
                  ExprParser.symbolicNames[l[0].getSymbol().type] +
                  '(' +l[0].getText() + ')')
        elif l[1].getText() == '^':
            print('  ' *  self.nivell + 'POT(^)')
            self.nivell += 1
            # for i in l:
            #     print(i.getText())
            self.visit(l[0])
            self.visit(l[2])
            self.nivell -= 1
        elif l[1].getText() == '*':
            print('  ' *  self.nivell + 'MULT(*)')
            self.nivell += 1
            # for i in l:
            #     print(i.getText())
            self.visit(l[0])
            self.visit(l[2])
            self.nivell -= 1
        elif l[1].getText() == '+':
            print('  ' *  self.nivell + 'MES(+)')
            self.nivell += 1
            # for i in l:
            #     print(i.getText())
            self.visit(l[0])
            self.visit(l[2])
            self.nivell -= 1
        elif l[1].getText() == '-':
            print('  ' *  self.nivell + 'MINUS(-)')
            self.nivell += 1
            # for i in l:
            #     print(i.getText())
            self.visit(l[0])
            self.visit(l[2])
            self.nivell -= 1
