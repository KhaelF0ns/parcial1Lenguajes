import math
from punto5TrigCalcParser import punto5TrigCalcParser
from punto5TrigCalcVisitor import punto5TrigCalcVisitor


class MyVisitor(punto5TrigCalcVisitor):

    def visitPrintExpr(self, ctx: punto5TrigCalcParser.PrintExprContext):
        return self.visit(ctx.expr())

    def visitSinFunction(self, ctx: punto5TrigCalcParser.SinFunctionContext):
        value = self.visit(ctx.expr())
        if value is None:
            raise ValueError("Expected numeric value in SinFunction")
        return round(math.sin(math.radians(value)), 1)

    def visitCosFunction(self, ctx: punto5TrigCalcParser.CosFunctionContext):
        value = self.visit(ctx.expr())
        if value is None:
            raise ValueError("Expected numeric value in CosFunction")
        return round(math.cos(math.radians(value)), 1)

    def visitTanFunction(self, ctx: punto5TrigCalcParser.TanFunctionContext):
        value = self.visit(ctx.expr())
        if value is None:
            raise ValueError("Expected numeric value in TanFunction")
        return round(math.tan(math.radians(value)), 1)

    def visitInt(self, ctx: punto5TrigCalcParser.IntContext):
        return int(ctx.getText())

    def visitFloat(self, ctx: punto5TrigCalcParser.FloatContext):
        return float(ctx.getText())
