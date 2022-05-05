import sys
from antlr4 import *
from jsbachLexer import jsbachLexer
from jsbachParser import jsbachParser
from TreeVisitor import TreeVisitor

# input_stream = InputStream(input('? '))
input_stream = FileStream(sys.argv[1])
lexer = jsbachLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = jsbachParser(token_stream)
tree = parser.root()
visitor = TreeVisitor()
visitor.visit(tree)
