# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#program_element_list.
    def visitProgram_element_list(self, ctx:MiniGoParser.Program_element_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#optional_variable_type.
    def visitOptional_variable_type(self, ctx:MiniGoParser.Optional_variable_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#variable_type.
    def visitVariable_type(self, ctx:MiniGoParser.Variable_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primitive_type.
    def visitPrimitive_type(self, ctx:MiniGoParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal.
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_literal.
    def visitArray_literal(self, ctx:MiniGoParser.Array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_pre_element.
    def visitArray_pre_element(self, ctx:MiniGoParser.Array_pre_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_pre_element_list.
    def visitArray_pre_element_list(self, ctx:MiniGoParser.Array_pre_element_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_pre_element_array_lit.
    def visitArray_pre_element_array_lit(self, ctx:MiniGoParser.Array_pre_element_array_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_element.
    def visitArray_element(self, ctx:MiniGoParser.Array_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_block.
    def visitArray_block(self, ctx:MiniGoParser.Array_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_type.
    def visitArray_type(self, ctx:MiniGoParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#multiple_dimension.
    def visitMultiple_dimension(self, ctx:MiniGoParser.Multiple_dimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#dim_literal.
    def visitDim_literal(self, ctx:MiniGoParser.Dim_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_literal.
    def visitStruct_literal(self, ctx:MiniGoParser.Struct_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#optional_field_values.
    def visitOptional_field_values(self, ctx:MiniGoParser.Optional_field_valuesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#field_values.
    def visitField_values(self, ctx:MiniGoParser.Field_valuesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#field_value.
    def visitField_value(self, ctx:MiniGoParser.Field_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#optional_list_expression.
    def visitOptional_list_expression(self, ctx:MiniGoParser.Optional_list_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_expression.
    def visitList_expression(self, ctx:MiniGoParser.List_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression1.
    def visitExpression1(self, ctx:MiniGoParser.Expression1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression2.
    def visitExpression2(self, ctx:MiniGoParser.Expression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression3.
    def visitExpression3(self, ctx:MiniGoParser.Expression3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression4.
    def visitExpression4(self, ctx:MiniGoParser.Expression4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression5.
    def visitExpression5(self, ctx:MiniGoParser.Expression5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression6.
    def visitExpression6(self, ctx:MiniGoParser.Expression6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression7.
    def visitExpression7(self, ctx:MiniGoParser.Expression7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression8.
    def visitExpression8(self, ctx:MiniGoParser.Expression8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#function_call.
    def visitFunction_call(self, ctx:MiniGoParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#declaration.
    def visitDeclaration(self, ctx:MiniGoParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#variable_declaration.
    def visitVariable_declaration(self, ctx:MiniGoParser.Variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#variable_characteristic.
    def visitVariable_characteristic(self, ctx:MiniGoParser.Variable_characteristicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#initialization.
    def visitInitialization(self, ctx:MiniGoParser.InitializationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#constant_declaration.
    def visitConstant_declaration(self, ctx:MiniGoParser.Constant_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#func_declaration.
    def visitFunc_declaration(self, ctx:MiniGoParser.Func_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#function_method_declaration.
    def visitFunction_method_declaration(self, ctx:MiniGoParser.Function_method_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_param.
    def visitList_param(self, ctx:MiniGoParser.List_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#no_null_list_param.
    def visitNo_null_list_param(self, ctx:MiniGoParser.No_null_list_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#parameter.
    def visitParameter(self, ctx:MiniGoParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#type_declaration.
    def visitType_declaration(self, ctx:MiniGoParser.Type_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_declaration.
    def visitStruct_declaration(self, ctx:MiniGoParser.Struct_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_of_fields.
    def visitList_of_fields(self, ctx:MiniGoParser.List_of_fieldsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_parameter.
    def visitStruct_parameter(self, ctx:MiniGoParser.Struct_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_declaration.
    def visitInterface_declaration(self, ctx:MiniGoParser.Interface_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_of_interface_methods.
    def visitList_of_interface_methods(self, ctx:MiniGoParser.List_of_interface_methodsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_method.
    def visitInterface_method(self, ctx:MiniGoParser.Interface_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_statement.
    def visitList_statement(self, ctx:MiniGoParser.List_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statement.
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#declaration_stmt.
    def visitDeclaration_stmt(self, ctx:MiniGoParser.Declaration_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assign_statement.
    def visitAssign_statement(self, ctx:MiniGoParser.Assign_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#lhs_assign.
    def visitLhs_assign(self, ctx:MiniGoParser.Lhs_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statement_block.
    def visitStatement_block(self, ctx:MiniGoParser.Statement_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#if_statement.
    def visitIf_statement(self, ctx:MiniGoParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#else_statement.
    def visitElse_statement(self, ctx:MiniGoParser.Else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#else_if_statement.
    def visitElse_if_statement(self, ctx:MiniGoParser.Else_if_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_statement.
    def visitFor_statement(self, ctx:MiniGoParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#basic_for_loop.
    def visitBasic_for_loop(self, ctx:MiniGoParser.Basic_for_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_loop_icu.
    def visitFor_loop_icu(self, ctx:MiniGoParser.For_loop_icuContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#init_statement.
    def visitInit_statement(self, ctx:MiniGoParser.Init_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#init_assign.
    def visitInit_assign(self, ctx:MiniGoParser.Init_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#init_declared.
    def visitInit_declared(self, ctx:MiniGoParser.Init_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_loop_range.
    def visitFor_loop_range(self, ctx:MiniGoParser.For_loop_rangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#break_statement.
    def visitBreak_statement(self, ctx:MiniGoParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continue_statement.
    def visitContinue_statement(self, ctx:MiniGoParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#call_statement.
    def visitCall_statement(self, ctx:MiniGoParser.Call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#function_method_call_stmt.
    def visitFunction_method_call_stmt(self, ctx:MiniGoParser.Function_method_call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#optional_instance_stmt.
    def visitOptional_instance_stmt(self, ctx:MiniGoParser.Optional_instance_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#return_statement.
    def visitReturn_statement(self, ctx:MiniGoParser.Return_statementContext):
        return self.visitChildren(ctx)



del MiniGoParser