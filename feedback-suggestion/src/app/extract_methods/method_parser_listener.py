# Generated from JavaParser.g4 by ANTLR 4.11.1
from antlr4 import *

from .method_node import MethodNode

JAVA_METHOD_DECLARATIONS = ["methodDeclaration", "constructorDeclaration", "genericMethodDeclaration",
                            "genericConstructorDeclaration"]


def capitalize_first_letter(s: str):
    return s[0].upper() + s[1:]


class MethodParserListener(ParseTreeListener):
    def __init__(self, method_declarations):
        self.methods = []
        for method_name in method_declarations:
            name = f"enter{capitalize_first_letter(method_name)}"
            setattr(self, name, self.make_enter(method_name))

    def make_enter(self, name):
        def enter(ctx=None):
            me = MethodNode(
                start_line=ctx.start.line,
                stop_line=ctx.stop.line,
                source_code=ctx.getText()
            )
            self.methods.append(me)

        return enter
