import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from punto5TrigCalcLexer import punto5TrigCalcLexer
from punto5TrigCalcParser import punto5TrigCalcParser
from MyVisitor import MyVisitor


def process_line(line, visitor):
    input_stream = InputStream(line)
    lexer = punto5TrigCalcLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = punto5TrigCalcParser(token_stream)
    tree = parser.stat()  # Parsear como 'stat' para procesar línea a línea
    result = visitor.visit(tree)

    if result is not None:
        print(result)


if __name__ == '__main__':
    visitor = MyVisitor()

    if len(sys.argv) > 1:
        # Procesar archivo línea por línea
        with open(sys.argv[1], 'r') as file:
            for line in file:
                process_line(line.strip(), visitor)
    else:
        # Modo interactivo
        while True:
            try:
                line = input(">> ")
                if line.strip() == "":
                    break
                process_line(line, visitor)
            except EOFError:
                break