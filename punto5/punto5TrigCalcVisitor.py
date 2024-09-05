# Generated from punto5TrigCalc.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .punto5TrigCalcParser import punto5TrigCalcParser
else:
    from punto5TrigCalcParser import punto5TrigCalcParser

# This class defines a complete generic visitor for a parse tree produced by punto5TrigCalcParser.

class punto5TrigCalcVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by punto5TrigCalcParser#prog.
    def visitProg(self, ctx:punto5TrigCalcParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by punto5TrigCalcParser#printExpr.
    def visitPrintExpr(self, ctx:punto5TrigCalcParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by punto5TrigCalcParser#SinFunction.
    def visitSinFunction(self, ctx:punto5TrigCalcParser.SinFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by punto5TrigCalcParser#CosFunction.
    def visitCosFunction(self, ctx:punto5TrigCalcParser.CosFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by punto5TrigCalcParser#TanFunction.
    def visitTanFunction(self, ctx:punto5TrigCalcParser.TanFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by punto5TrigCalcParser#int.
    def visitInt(self, ctx:punto5TrigCalcParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by punto5TrigCalcParser#float.
    def visitFloat(self, ctx:punto5TrigCalcParser.FloatContext):
        return self.visitChildren(ctx)



del punto5TrigCalcParser