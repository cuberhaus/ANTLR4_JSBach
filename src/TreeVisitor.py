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
        self.procediments = {}

    def begin(self, param):
        if param in self.procediments:
            self.visit(self.procediments[param][1])
        else:
            raise Exception("El codi no conté el procediment " + str(param))

    def begin_default(self):
        function = "Main"
        if function in self.procediments:
            self.visit(self.procediments[function][1])
        else:
            raise Exception("El codi no conté el procediment " + str(function))

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
        # children = list(ctx.getChildren())
        # if len(children) == 1:
        #     numero1 = self.visit(children[0])
        #     print(numero1)
        # else:
        #     print("Error")
        #
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
    def visitLectura(self, ctx: jsbachParser.LecturaContext):
        children = list(ctx.getChildren())

        if len(children) == 1:
            print("Error")
        else:
            identifier = children[1].getText()
            numero = int(input())
            self.ids[identifier] = numero
        return self.visitChildren(ctx)

    # Visit a parse tree produced by jsbachParser#escriptura.
    def visitEscriptura(self, ctx: jsbachParser.EscripturaContext):
        children = list(ctx.getChildren())
        n = len(children)
        current_children = 1
        found_newline = False
        while current_children < n and not found_newline:
            identifier = self.visit(children[current_children])
            segment = children[current_children].getText()
            if segment == "\n":
                found_newline = True
            elif segment.startswith("\"") and segment.endswith("\""):
                print(segment[1:-1], end="")
            else:
                print(self.ids[identifier], end="")
            current_children += 1
        print("\r")
        # return self.visitChildren(ctx)

    # Visit a parse tree produced by jsbachParser#usar_procediment.
    def visitUsar_procediment(self, ctx: jsbachParser.Usar_procedimentContext):
        children = list(ctx.getChildren())
        nom_funcio = children[0].getText()
        if nom_funcio not in self.procediments:
            raise Exception("La funció " + nom_funcio + ", no existeix.")
        else:
            argument_values = self.visit(children[1]) # definir_arguments
            if len(argument_values) != len(self.procediments[nom_funcio][0]):
                raise Exception("El nombre d'arguments en la crida de la funció" + nom_funcio + " no es correspon amb el nombre d'arguments que admet")
            else:
                #self.procediments[nom_funcio][0] = argument_values
        return self.visitChildren(ctx)

    # Visit a parse tree produced by jsbachParser#definir_procediment.
    def visitDefinir_procediment(self, ctx: jsbachParser.Definir_procedimentContext):
        children = list(ctx.getChildren())
        n = len(children)
        nom_procediment = children[0].getText()  # El primer fill conté en nom de la funció
        if nom_procediment in self.procediments:
            raise Exception("La funció" + nom_procediment + "ja ha estat declarada.")
        else:
            variables = self.visit(children[1])  # El segon fill conté els arguments de la funció
            variables_set = set(variables)
            if len(variables) != len(variables_set):
                raise Exception("El procediment conté variables amb noms repetits!")
            procediment = children[4]  # El 4 fill conté el bloc de codi que conté el procediment de la funció
            self.procediments[nom_procediment] = [variables, procediment]
        # return self.visitChildren(ctx)

    # Visit a parse tree produced by jsbachParser#definir_arguments.
    def visitDefinir_arguments(self, ctx: jsbachParser.Definir_argumentsContext):
        children = list(ctx.getChildren())
        argument_values = []
        for child in children:
            argument_value = self.visit(child)
            argument_values.append(argument_value)
        return argument_values
        # return self.visitChildren(ctx)

    # Visit a parse tree produced by jsbachParser#arguments.
    def visitArguments(self, ctx: jsbachParser.ArgumentsContext):
        children = list(ctx.getChildren())
        arguments = []
        for i in children:
            arguments.append(i.getText())
        return arguments

    # Visit a parse tree produced by jsbachParser#if.
    def visitIf(self, ctx: jsbachParser.IfContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by jsbachParser#else.
    def visitElse(self, ctx: jsbachParser.ElseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by jsbachParser#while.
    def visitWhile(self, ctx: jsbachParser.WhileContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by jsbachParser#condicio.
    def visitCondicio(self, ctx: jsbachParser.CondicioContext):
        return self.visitChildren(ctx)
