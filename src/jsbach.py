import sys
import os

from antlr4 import *
from jsbachLexer import jsbachLexer

if __name__ is not None and "." in __name__:
    from jsbachParser import jsbachParser
    from jsbachVisitor import jsbachVisitor
else:
    from jsbachParser import jsbachParser
    from jsbachVisitor import jsbachVisitor

note_to_int = {}

int_to_note = {}


def initialize_int_to_note():
    """
    Initializes a dictionary which transforms a value into its corresponding string in lilypond
    :return: None
    """
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    int_to_note[0] = "a'0"
    int_to_note[1] = "b'0"
    i = 1
    n = 8
    while i < n:
        j = 0
        m = 7
        while j < m:
            int_to_note[j + ((i - 1) * 7) + 2] = letters[(j + 2) % 7] + "'" + str(i)
            j += 1
        i += 1


def initialize_note_to_int():
    """
    Initializes a dictionary which transforms notes from the programming language into its corresponding int
    :return: None
    """
    # global notes # Needed to modify global copy of notes
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    note_to_int["A0"] = 0
    note_to_int["B0"] = 1
    i = 1
    n = 8
    while i < n:
        j = 0
        m = 7
        while j < m:
            note_to_int[letters[(j + 2) % 7] + str(i)] = j + ((i - 1) * 7) + 2
            j += 1
        i += 1
    note_to_int["C8"] = 51
    note_to_int['A'] = note_to_int["A4"]
    note_to_int['B'] = note_to_int["B4"]
    note_to_int['C'] = note_to_int["C4"]
    note_to_int['D'] = note_to_int["D4"]
    note_to_int['E'] = note_to_int["E4"]
    note_to_int['F'] = note_to_int["F4"]
    note_to_int['G'] = note_to_int["G4"]


# Class has to be defined above main, like in c++
class TreeVisitor(jsbachVisitor):
    def __init__(self):
        self.nivell = 0
        # Necessitem un llistat de diccionaris per guardar els àmbits de visibilitat
        self.ids = [{}]
        self.procediments = {}
        self.notes_a_reproduir = []
        initialize_note_to_int()
        initialize_int_to_note()

    def begin_default(self):
        """
        Start the program from the "Main" function
        :return: None
        """
        function = "Main"
        if function in self.procediments:
            self.visit(self.procediments[function][1])
        else:
            raise Exception("El codi no conté el procediment " + str(function))

    def begin(self, param):
        """
        Start the program from the "param" function
        :param param:
        :return:
        """
        if param in self.procediments:
            self.visit(self.procediments[param][1])
        else:
            raise Exception("El codi no conté el procediment " + str(param))

    # Visit a parse tree produced by ExprParser#root.
    def visitRoot(self, ctx: jsbachParser.RootContext):
        children = list(ctx.getChildren())
        for i in children:
            self.visit(i)

    def visitBloc(self, ctx: jsbachParser.BlocContext):
        children = list(ctx.getChildren())
        for i in children:
            self.visit(i)

    # Visit a parse tree produced by ExprParser#assign.
    def visitAssign(self, ctx: jsbachParser.AssignContext):
        children = list(ctx.getChildren())
        if len(children) == 1:
            print("Error")
        else:
            identifier = children[0].getText()
            numero = self.visit(children[2])
            self.ids[-1][identifier] = numero
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#statement.
    def visitStatement(self, ctx: jsbachParser.StatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#pot.
    def visitPot(self, ctx: jsbachParser.PotContext):
        children = list(ctx.getChildren())
        if len(children) == 1:
            print("Error")
        else:
            numero1, numero2, op = self.get_values_from_children(children)
            return numero1 ** numero2
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#div_mult_mod.
    def visitDiv_mult_mod(self, ctx: jsbachParser.Div_mult_modContext):
        children = list(ctx.getChildren())
        if len(children) == 1:
            print("Error")
        else:
            numero1, numero2, op = self.get_values_from_children(children)
            if op == '*':
                return numero1 * numero2
            elif op == '%':
                return numero1 % numero2
            elif op == '/':
                if numero2 == 0:
                    raise Exception("Divisió per zero!")
                return numero1 / numero2
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#num.
    def visitNum(self, ctx: jsbachParser.NumContext):
        children = list(ctx.getChildren())
        num = int(children[0].getText())
        return num

    # Visit a parse tree produced by ExprParser#mes_minus.
    def visitMes_minus(self, ctx: jsbachParser.Mes_minusContext):
        children = list(ctx.getChildren())
        if len(children) == 1:
            print("error")
        else:
            numero1, numero2, op = self.get_values_from_children(children)
            if op == '+':
                return numero1 + numero2
            if op == '-':
                return numero1 - numero2
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#id.
    def visitId(self, ctx: jsbachParser.IdContext):
        children = list(ctx.getChildren())
        identifier = children[0].getText()
        return identifier

    # Visit a parse tree produced by jsbachParser#lectura.
    def visitLectura(self, ctx: jsbachParser.LecturaContext):
        children = list(ctx.getChildren())

        if len(children) == 1:
            print("Error")
        else:
            identifier = children[1].getText()
            numero = int(input())
            self.ids[-1][identifier] = numero
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
                print(segment[1:-1], end=" ")
            elif isinstance(identifier, int):
                print(identifier, end=" ")
            else:
                print(self.ids[-1][identifier], end=" ")
            current_children += 1
        print("\n", end="")  # we only need one line feed

    # Visit a parse tree produced by jsbachParser#usar_procediment.
    def visitUsar_procediment(self, ctx: jsbachParser.Usar_procedimentContext):
        children = list(ctx.getChildren())
        nom_funcio = children[0].getText()
        if nom_funcio not in self.procediments:
            raise Exception("La funció " + nom_funcio + ", no existeix.")
        argument_values = self.visit(children[1])  # definir_arguments
        argument_ids = self.procediments[nom_funcio][0]
        if len(argument_values) != len(argument_ids):
            raise Exception(
                "El nombre d'arguments en la crida de la funció " +
                nom_funcio + " no es correspon amb el nombre "
                             "d'arguments que admet.")
        procediment = self.procediments[nom_funcio][1]
        self.ids.append({})
        i = 0
        n = len(argument_ids)
        while i < n:
            argument_value = argument_values[i]
            if isinstance(argument_value, str):
                argument_value = self.ids[-2][argument_value]
            self.ids[-1][argument_ids[i]] = argument_value
            i += 1
        self.visit(procediment)
        self.ids.pop()

    # Visit a parse tree produced by jsbachParser#definir_procediment.
    def visitDeclarar_procediment(self, ctx: jsbachParser.Declarar_procedimentContext):
        children = list(ctx.getChildren())
        # El primer fill conté el nom de la funció
        nom_procediment = children[0].getText()
        if nom_procediment in self.procediments:
            raise Exception("La funció" + nom_procediment +
                            "ja ha estat declarada.")
        # El segon fill conté els arguments de la funció
        arguments = self.visit(children[1])
        variables_set = set(arguments)
        if len(arguments) != len(variables_set):
            raise Exception(
                "El procediment conté noms de paràmetres formals repetits!")
        # El 4rt fill conté el bloc de codi que conté el procediment de la funció
        procediment = children[4]
        self.procediments[nom_procediment] = [arguments, procediment]

    # Visit a parse tree produced by jsbachParser#definir_arguments.
    def visitDefinir_arguments(self, ctx: jsbachParser.Definir_argumentsContext):
        children = list(ctx.getChildren())
        argument_values = []
        for child in children:
            argument_value = self.visit(child)
            argument_values.append(argument_value)
        return argument_values

    # Visit a parse tree produced by jsbachParser#arguments.
    def visitDeclarar_arguments(self, ctx: jsbachParser.Declarar_argumentsContext):
        children = list(ctx.getChildren())
        arguments = []
        for i in children:
            arguments.append(i.getText())
        return arguments

    # Visit a parse tree produced by jsbachParser#if.
    def visitIf(self, ctx: jsbachParser.IfContext):
        children = list(ctx.getChildren())
        condition_value = self.visit(children[1])
        if condition_value:
            self.visit(children[4])
        elif len(children) == 7:
            self.visit(children[6])

    # Visit a parse tree produced by jsbachParser#else.
    def visitElse(self, ctx: jsbachParser.ElseContext):
        children = list(ctx.getChildren())
        self.visit(children[3])

    # Visit a parse tree produced by jsbachParser#while.
    def visitWhile(self, ctx: jsbachParser.WhileContext):
        children = list(ctx.getChildren())
        while self.visit(children[1]):
            self.visit(children[4])
        return self.visitChildren(ctx)

    # Visit a parse tree produced by jsbachParser#condicio.
    def visitCondicio(self, ctx: jsbachParser.CondicioContext):
        children = list(ctx.getChildren())
        if len(children) == 1:
            print("Error")
        else:
            numero1, numero2, op = self.get_values_from_children(children)
            value = 0
            if op == '=':
                value = numero1 == numero2
            elif op == "/=":
                value = numero1 != numero2
            elif op == '<':
                value = numero1 < numero2
            elif op == '>':
                value = numero1 > numero2
            elif op == "<=":
                value = numero1 <= numero2
            elif op == ">=":
                value = numero1 >= numero2
            if value:
                return 1
            return 0

    def get_values_from_children(self, children):
        """
        Returns the numbers from operations with two parameters and the operator from the children.
        :param children: children nodes of the current node
        :return: First number, second number, operator
        """
        numero1 = self.visit(children[0])
        numero2 = self.visit(children[2])
        if isinstance(numero1, str):
            numero1 = self.ids[-1][numero1]
        if isinstance(numero2, str):
            numero2 = self.ids[-1][numero2]
        op = children[1].getText()
        return numero1, numero2, op

    # Visit a parse tree produced by jsbachParser#parenthesis.
    def visitParenthesis(self, ctx: jsbachParser.ParenthesisContext):
        children = list(ctx.getChildren())
        return self.visit(children[1])

    # Visit a parse tree produced by jsbachParser#crea_llista.
    def visitCrea_llista(self, ctx: jsbachParser.Crea_llistaContext):
        children = list(ctx.getChildren())
        i = 1
        n = len(children) - 1
        valors = []
        while i < n:
            valors.append(self.visit(children[i]))
            i += 1
        return valors

    # Visit a parse tree produced by jsbachParser#append.
    def visitAppend(self, ctx: jsbachParser.AppendContext):
        children = list(ctx.getChildren())
        list_name = children[0].getText()
        if list_name not in self.ids[-1]:
            raise Exception("This list does not exist!")
        value = self.visit(children[2])
        self.ids[-1][list_name].append(value)

    # Visit a parse tree produced by jsbachParser#erase_from_list.
    def visitErase_from_list(self, ctx: jsbachParser.Erase_from_listContext):
        children = list(ctx.getChildren())
        list_name = children[1].getText()
        if list_name not in self.ids[-1]:
            raise Exception("This list does not exist!")
        index = int(children[3].getText()) - 1
        if index < 1 or index > len(self.ids[-1][list_name]):
            raise Exception("L'element està fora del rang entre 1 i n")
        self.ids[-1][list_name].pop(index)

    # Visit a parse tree produced by jsbachParser#get_list_size.
    def visitGet_list_size(self, ctx: jsbachParser.Get_list_sizeContext):
        children = list(ctx.getChildren())
        list_name = children[0].getText()
        if list_name not in self.ids[-1]:
            raise Exception("This list does not exist!")
        list_name = list_name[1:]
        size = len(self.ids[-1][list_name])
        return size

    # Visit a parse tree produced by jsbachParser#access_list.
    def visitAccess_list(self, ctx: jsbachParser.Access_listContext):
        children = list(ctx.getChildren())
        list_name = children[0].getText()
        index = self.visit(children[2])
        value = self.ids[-1][list_name][index]
        return value

    # Visit a parse tree produced by jsbachParser#nota_id.
    def visitNota_id(self, ctx: jsbachParser.Nota_idContext):
        children = list(ctx.getChildren())
        identifier = children[0].getText()
        return note_to_int[identifier]

    # Visit a parse tree produced by jsbachParser#reproduccio.
    def visitReproduccio(self, ctx: jsbachParser.ReproduccioContext):
        children = list(ctx.getChildren())
        value_nota = self.visit(children[1])
        if isinstance(value_nota, str):
            if value_nota not in self.ids[-1]:
                raise Exception("La variable no existeix!")
            value_nota = self.ids[-1][value_nota]
        if value_nota < 0 or value_nota > len(note_to_int):
            raise Exception("El valor a reproduir no és una nota!")

        self.notes_a_reproduir.append(value_nota)


def main():
    input_stream = FileStream(sys.argv[1])
    lexer = jsbachLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = jsbachParser(token_stream)
    tree = parser.root()
    visitor = TreeVisitor()
    visitor.visit(tree)

    if len(sys.argv) == 2:
        visitor.begin_default()
    elif len(sys.argv) == 3:
        visitor.begin(sys.argv[2])
    else:
        raise Exception("Incorrect number of arguments")
    input_file_name = os.path.basename(sys.argv[1])
    lilyfile1 = """\"\\version \\"2.22.1\\"
\\score { 
    \\absolute { 
        \\tempo 4 = 120\n"""
    note_strings = []
    for nota in visitor.notes_a_reproduir:
        note_strings.append(int_to_note[nota])
    string_notes = ' '.join(note_strings)
    string_notes = "        " + string_notes
    lilyfile2 = """
    } 
    \\layout {} 
    \\midi {} 
} \" """
    os.system("echo " + lilyfile1 + string_notes + lilyfile2 + " > " + input_file_name + ".lily")

    os.system("lilypond " + input_file_name + ".lily")  # THIS WORKS
    os.system("timidity -Ow -o " + input_file_name + ".wav " + input_file_name + ".midi")  # THIS DOESNT
    os.system("ffmpeg -i " + input_file_name + ".wav -codec:a libmp3lame -qscale:a 2 " + input_file_name + ".mp3")

    os.system("mplayer " + input_file_name + ".mp3")


if __name__ == '__main__':
    main()
