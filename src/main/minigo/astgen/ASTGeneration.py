# from MiniGoVisitor import MiniGoVisitor
# from MiniGoParser import MiniGoParser
# from AST import *

# # expect = Program([FuncDecl("foo",[],VoidType(),Block([
# #             If(IntLiteral(1), Block([Return(None)]), 
# #                If(IntLiteral(2), Block([Return(None)]), 
# #                   If(IntLiteral(3), Block([Return(None)]), Block([Return(None)])))),
# #             If(IntLiteral(1), Block([Return(None)]), 
# #                If(IntLiteral(2), Block([Return(None)]), 
# #                   If(IntLiteral(3), Block([Return(None)]), None)))]))
# # 		])
# # print("\n\n\n\n\n\n", str(expect), "\n\n\n\n\n\n")

# class ASTGeneration(MiniGoVisitor):

# ###########################################################
# # Visit a parse tree produced by MiniGoParser#program.
#     def visitProgram(self, ctx:MiniGoParser.ProgramContext):
#         list_decl = self.visit(ctx.list_decl())
#         return Program(list_decl)


#     # Visit a parse tree produced by MiniGoParser#list_decl.
#     def visitList_decl(self, ctx:MiniGoParser.List_declContext):
#         if ctx.getChildCount() == 1: return [self.visit(ctx.decl())]
#         return [self.visit(ctx.decl())] + self.visit(ctx.list_decl())


#     # Visit a parse tree produced by MiniGoParser#decl.
#     def visitDecl(self, ctx:MiniGoParser.DeclContext):
#         return self.visit(ctx.getChild(0))


#     # Visit a parse tree produced by MiniGoParser#type_variable.
#     def visitType_variable(self, ctx:MiniGoParser.Type_variableContext):
#         # if ctx.IDENTIFIER(): return str(Id(ctx.IDENTIFIER().getText()))
#         # return str(self.visit(ctx.primitive_variable()))
#         if ctx.IDENTIFIER(): return (Id(ctx.IDENTIFIER().getText()))
#         return (self.visit(ctx.primitive_variable()))


#     # Visit a parse tree produced by MiniGoParser#primitive_variable.
#     def visitPrimitive_variable(self, ctx:MiniGoParser.Primitive_variableContext):
#         if ctx.INT(): return IntType()
#         elif ctx.FLOAT(): return FloatType()
#         elif ctx.STRING(): return StringType()
#         elif ctx.BOOLEAN(): return BoolType()


#     # Visit a parse tree produced by MiniGoParser#primitive_value.
#     def visitPrimitive_value(self, ctx:MiniGoParser.Primitive_valueContext):
#         # if ctx.INT_LIT(): return IntLiteral(eval(ctx.INT_LIT()).getText())
#         if ctx.INT_LIT(): return IntLiteral(eval(ctx.INT_LIT().getText()))
#         elif ctx.FLOAT_LIT(): return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
#         elif ctx.STRING_LIT(): return StringLiteral(ctx.STRING_LIT().getText())
#         elif ctx.TRUE(): return BooleanLiteral(True)
#         elif ctx.FALSE(): return BooleanLiteral(False)
#         elif ctx.NIL(): return NilLiteral()
        

#     # Visit a parse tree produced by MiniGoParser#array_declare.
#     def visitArray_declare(self, ctx:MiniGoParser.Array_declareContext):
#         array_type = ctx.getChild(3).getText()
#         array_name = ctx.getChild(0).getText()
#         # list_dim = [self.visit(i) for i in self.visit(ctx.list_dim())]
#         list_dim = self.visit(ctx.list_dim())
#         return VarDecl(array_name, ArrayType(list_dim, array_type),None)


#     # Visit a parse tree produced by MiniGoParser#list_dim.
#     def visitList_dim(self, ctx:MiniGoParser.List_dimContext):
#         if ctx.getChildCount() == 1 : return [self.visit(ctx.mono_dim())]
#         return [self.visit(ctx.mono_dim())] + self.visit(ctx.list_dim())
        

#     # Visit a parse tree produced by MiniGoParser#mono_dim.
#     def visitMono_dim(self, ctx:MiniGoParser.Mono_dimContext):
#         return self.visit(ctx.dim())


#     # Visit a parse tree produced by MiniGoParser#dim.
#     def visitDim(self, ctx:MiniGoParser.DimContext):
#         if ctx.INT_LIT() : return IntLiteral(eval(ctx.INT_LIT().getText()))
#         # return str(Id(ctx.IDENTIFIER().getText()))
#         return (Id(ctx.IDENTIFIER().getText()))


#     # Visit a parse tree produced by MiniGoParser#array_access.
#     def visitArray_access(self, ctx:MiniGoParser.Array_accessContext):
#         # expr = str(Id(ctx.IDENTIFIER().getText()))
#         expr = (Id(ctx.IDENTIFIER().getText()))
#         list_dim = self.visit(ctx.list_dim())
#         # return ArrayCell(expr, list_dim)
#         return [(expr, list_dim)]


#     # Visit a parse tree produced by MiniGoParser#array_lit.
#     def visitArray_lit(self, ctx:MiniGoParser.Array_litContext):
#         list_dim = self.visit(ctx.list_dim())
#         type_variable = self.visit(ctx.type_variable())
#         array_value = self.visit(ctx.array_value()) # visitArray_value_except_array has return the list
#         return ArrayLiteral(list_dim, type_variable, array_value)


#     # Visit a parse tree produced by MiniGoParser#array_value.
#     def visitArray_value(self, ctx:MiniGoParser.Array_valueContext):
#         return self.visit(ctx.array_value_sub()) if ctx.getChildCount() == 1 else self.visit(ctx.array_value_sub()) + self.visit(ctx.array_value())
#     # visitArray_value_except_array has return the list

#     # Visit a parse tree produced by MiniGoParser#array_value_sub.
#     def visitArray_value_sub(self, ctx:MiniGoParser.Array_value_subContext):
#         return self.visit(ctx.array_value_except_array()) if ctx.getChildCount() == 1 else [self.visit(ctx.array_value())]


#     # Visit a parse tree produced by MiniGoParser#array_value_except_array.
#     def visitArray_value_except_array(self, ctx:MiniGoParser.Array_value_except_arrayContext):
#         return [self.visit(ctx.array_value_mono())] if ctx.getChildCount() == 1 else [self.visit(ctx.array_value_mono())] + self.visit(ctx.array_value_except_array())


#     # Visit a parse tree produced by MiniGoParser#array_value_mono.
#     def visitArray_value_mono(self, ctx:MiniGoParser.Array_value_monoContext):
#         if ctx.IDENTIFIER(): return Id(ctx.IDENTIFIER().getText())
#         elif ctx.primitive_value() : return self.visit(ctx.primitive_value())
#         return self.visit(ctx.struct_lit())


#     # Visit a parse tree produced by MiniGoParser#struct_decl.
#     def visitStruct_decl(self, ctx:MiniGoParser.Struct_declContext):
#         struct_name = ctx.IDENTIFIER().getText()
#         list_ele = self.visit(ctx.list_fields())
#         #### NEED TO ASK     
#         return StructType(struct_name,list_ele,[])


#     # Visit a parse tree produced by MiniGoParser#list_fields.
#     def visitList_fields(self, ctx:MiniGoParser.List_fieldsContext):
#         return self.visit(ctx.list_fields_init())


#     # Visit a parse tree produced by MiniGoParser#list_fields_init.
#     def visitList_fields_init(self, ctx:MiniGoParser.List_fields_initContext):
#         # return self.visitChildren(ctx)
#         return self.visit(ctx.fields()) if ctx.getChildCount() == 1 else self.visit(ctx.fields()) + self.visit(ctx.list_fields_init())


#     # Visit a parse tree produced by MiniGoParser#fields.
#     def visitFields(self, ctx:MiniGoParser.FieldsContext):
#         name = ctx.IDENTIFIER().getText()
#         type_ = self.visit(ctx.type_except_array())
#         return [(name, type_)]


#     # Visit a parse tree produced by MiniGoParser#struct_access.
#     def visitStruct_access(self, ctx:MiniGoParser.Struct_accessContext):
#         return self.visit(ctx.lhs())
#         ###### CHECK BUG_ HERE


#     # Visit a parse tree produced by MiniGoParser#struct_fields_assign.
#     def visitStruct_fields_assign(self, ctx:MiniGoParser.Struct_fields_assignContext):
#         # return self.visitChildren(ctx)
#         struct_access = self.visit(ctx.struct_access())
#         return Assign(struct_access, self.visit(ctx.expr()))


#     # Visit a parse tree produced by MiniGoParser#struct_instance.
#     def visitStruct_instance(self, ctx:MiniGoParser.Struct_instanceContext):
#         # return self.visitChildren(ctx)
#         pass


#     # Visit a parse tree produced by MiniGoParser#list_fields_value_null.
#     def visitList_fields_value_null(self, ctx:MiniGoParser.List_fields_value_nullContext):
#         # return None if ctx.getChildCount() == 0 else self.visit(ctx.list_fields_value())
#         return [] if ctx.getChildCount() == 0 else self.visit(ctx.list_fields_value())


#     # Visit a parse tree produced by MiniGoParser#list_fields_value.
#     def visitList_fields_value(self, ctx:MiniGoParser.List_fields_valueContext):
#         # return self.visitChildren(ctx)
#         return self.visit(ctx.list_fields_value_sub())


#     # Visit a parse tree produced by MiniGoParser#list_fields_value_sub.
#     def visitList_fields_value_sub(self, ctx:MiniGoParser.List_fields_value_subContext):
#         # return self.visitChildren(ctx)
#         return self.visit(ctx.fields_value()) if ctx.getChildCount() == 1 else self.visit(ctx.fields_value()) + self.visit(ctx.list_fields_value_sub())


#     # Visit a parse tree produced by MiniGoParser#fields_value.
#     def visitFields_value(self, ctx:MiniGoParser.Fields_valueContext):
#         name = ctx.IDENTIFIER().getText()
#         if ctx.primitive_value(): 
#             value_ = self.visit(ctx.primitive_value()) 
#             return [(name, value_)]
#         expr = self.visit(ctx.expr())
#         return [(name, expr)]

#     # Visit a parse tree produced by MiniGoParser#struct_value.
#     def visitStruct_value(self, ctx:MiniGoParser.Struct_valueContext):
#         return self.visit(ctx.list_fields_value_null())
    
#     def visitStruct_lit(self, ctx:MiniGoParser.Struct_litContext):
#         name = ctx.IDENTIFIER().getText()
#         struct_value = self.visit(ctx.struct_value())
#         return StructLiteral(name, struct_value)


#     # Visit a parse tree produced by MiniGoParser#interface_lit.
#     def visitInterface_lit(self, ctx:MiniGoParser.Interface_litContext):
#         name = ctx.IDENTIFIER().getText() 
#         list_methods = self.visit(ctx.list_methods())
#         return InterfaceType(name, list_methods)


#     # Visit a parse tree produced by MiniGoParser#list_methods.
#     def visitList_methods(self, ctx:MiniGoParser.List_methodsContext):
#         return [self.visit(ctx.methods())] if ctx.getChildCount() == 1 else [self.visit(ctx.methods())] + self.visit(ctx.list_methods())


#     # Visit a parse tree produced by MiniGoParser#methods.
#     def visitMethods(self, ctx:MiniGoParser.MethodsContext):
#         id = ctx.IDENTIFIER().getText()
#         list_para = self.visit(ctx.list_para()) if ctx.list_para() else []
#         if list_para != []:
#             list_para = [type_ for _, type_ in list_para]
#         type_ = self.visit(ctx.optional_return_type()) if ctx.optional_return_type() else VoidType()
#         return Prototype(id,list_para,type_)


#     # Visit a parse tree produced by MiniGoParser#list_para.
#     def visitList_para(self, ctx:MiniGoParser.List_paraContext):
#         return self.visit(ctx.list_para_mono()) if ctx.getChildCount() == 1 else self.visit(ctx.list_para_mono()) + self.visit(ctx.list_para())


#     # Visit a parse tree produced by MiniGoParser#list_para_mono.
#     def visitList_para_mono(self, ctx:MiniGoParser.List_para_monoContext):
#         return self.visit(ctx.sharing_type()) if ctx.sharing_type() else self.visit(ctx.common_type())

#     # Visit a parse tree produced by MiniGoParser#sharing_type.
#     def visitSharing_type(self, ctx:MiniGoParser.Sharing_typeContext):
#         id = ctx.IDENTIFIER().getText()
#         type_ = self.visit(ctx.type_except_array())
#         return [(id,type_)] if ctx.getChildCount() == 2 else [(id,type_)] + self.visit(ctx.sharing_type())
#         # return [(type_)] if ctx.getChildCount() == 2 else [(type_)] + self.visit(ctx.sharing_type())
#         ## DEBUG HERE WHY RETURN TUPLE OF ID AND TYPE
#         ## USING PARAMDECL HERE RIGHT? OR JUST NEED TO RETURN LIST OF TYPE


#     # Visit a parse tree produced by MiniGoParser#type_except_array.
#     def visitType_except_array(self, ctx:MiniGoParser.Type_except_arrayContext):
#         if ctx.getChildCount() == 1 : return self.visit(ctx.type_variable())
#         list_dim = self.visit(ctx.list_dim())
#         type_ = self.visit(ctx.type_variable())
#         return ArrayType(list_dim, type_)


#     # Visit a parse tree produced by MiniGoParser#common_type.
#     def visitCommon_type(self, ctx:MiniGoParser.Common_typeContext):
#         type_ = self.visit(ctx.type_except_array())
#         list_id = self.visit(ctx.common_type_sub())
#         return [(i,type_) for i in list_id]


#     # Visit a parse tree produced by MiniGoParser#common_type_sub.
#     def visitCommon_type_sub(self, ctx:MiniGoParser.Common_type_subContext):
#         return [ctx.IDENTIFIER().getText()] if ctx.getChildCount() == 1 else [ctx.IDENTIFIER().getText()] + self.visit(ctx.common_type_sub())


#     # Visit a parse tree produced by MiniGoParser#variable.
#     def visitVariable(self, ctx:MiniGoParser.VariableContext):
#         return self.visit(ctx.global_var())


#     # Visit a parse tree produced by MiniGoParser#optional_type.
#     def visitOptional_type(self, ctx:MiniGoParser.Optional_typeContext):
#         return self.visit(ctx.type_except_array()) if ctx.type_except_array() else None


#     # Visit a parse tree produced by MiniGoParser#global_var.
#     def visitGlobal_var(self, ctx:MiniGoParser.Global_varContext):
#         return self.visit(ctx.var_decl_init()) if ctx.var_decl_init() else self.visit(ctx.var_decl_no_init())


#     # Visit a parse tree produced by MiniGoParser#var_decl_no_init.
#     def visitVar_decl_no_init(self, ctx:MiniGoParser.Var_decl_no_initContext):
#         id = ctx.IDENTIFIER().getText()
#         type_ = self.visit(ctx.type_except_array())
#         return VarDecl(id,type_, None)


#     # Visit a parse tree produced by MiniGoParser#var_decl_init.
#     def visitVar_decl_init(self, ctx:MiniGoParser.Var_decl_initContext):
#         id = ctx.IDENTIFIER().getText()
#         type_ = self.visit(ctx.optional_type())
#         expr = self.visit(ctx.expr())
#         return VarDecl(id,type_, expr)


#     # Visit a parse tree produced by MiniGoParser#list_expr.
#     def visitList_expr(self, ctx:MiniGoParser.List_exprContext):
#         return [self.visit(ctx.expr())] if ctx.getChildCount() == 1 else [self.visit(ctx.expr())] + self.visit(ctx.list_expr())


#     # Visit a parse tree produced by MiniGoParser#expr.
#     def visitExpr(self, ctx:MiniGoParser.ExprContext):
#         if ctx.getChildCount() == 1: return self.visit(ctx.expr1())
#         op = "||"
#         left = self.visit(ctx.expr())
#         right = self.visit(ctx.expr1())
#         return BinaryOp(op, left, right)


#     # Visit a parse tree produced by MiniGoParser#expr1.
#     def visitExpr1(self, ctx:MiniGoParser.Expr1Context):
#         if ctx.getChildCount() == 1: return self.visit(ctx.expr2())
#         op = "&&"
#         left = self.visit(ctx.expr1())
#         right = self.visit(ctx.expr2())
#         return BinaryOp(op, left, right)


#     # Visit a parse tree produced by MiniGoParser#expr2.
#     def visitExpr2(self, ctx:MiniGoParser.Expr2Context):
#         if ctx.getChildCount() == 1: return self.visit(ctx.expr3())
#         if ctx.EQUAL(): op = "=="
#         elif ctx.DIFFER() : op = "!="
#         elif ctx.LESS() : op = "<"
#         elif ctx.LESS_OR_EQUAL() : op = "<="
#         elif ctx.GREATER() : op = ">"
#         elif ctx.GREATER_OR_EQUAL() : op = ">="
#         left = self.visit(ctx.expr2())
#         right = self.visit(ctx.expr3())
#         return BinaryOp(op, left, right)


#     # Visit a parse tree produced by MiniGoParser#expr3.
#     def visitExpr3(self, ctx:MiniGoParser.Expr3Context):
#         if ctx.getChildCount() == 1: return self.visit(ctx.expr4())
#         if ctx.PLUS(): op = "+"
#         elif ctx.MINUS() : op = "-"
#         left = self.visit(ctx.expr3())
#         right = self.visit(ctx.expr4())
#         return BinaryOp(op, left, right)


#     # Visit a parse tree produced by MiniGoParser#expr4.
#     def visitExpr4(self, ctx:MiniGoParser.Expr4Context):
#         if ctx.getChildCount() == 1: return self.visit(ctx.expr5())
#         if ctx.ASTERISK(): op = "*"
#         elif ctx.DIVIDE() : op = "/"
#         elif ctx.MODULO() : op = "%"
#         left = self.visit(ctx.expr4())
#         right = self.visit(ctx.expr5())
#         return BinaryOp(op, left, right)


#     # Visit a parse tree produced by MiniGoParser#expr5.
#     def visitExpr5(self, ctx:MiniGoParser.Expr5Context):
#         if ctx.getChildCount() == 1: return self.visit(ctx.expr6())
#         if ctx.NOT(): op = "!"
#         elif ctx.MINUS() : op = "-"
#         body = self.visit(ctx.expr5())
#         return UnaryOp(op, body)


#     # Visit a parse tree produced by MiniGoParser#expr6.
#     def visitExpr6(self, ctx:MiniGoParser.Expr6Context):
#         if ctx.getChildCount() == 1: return self.visit(ctx.expr7())
#         # elif ctx.expr(): 
#         #     # print("\n\nhehe\n\n")
#         #     return ArrayCell(self.visit(ctx.expr6()), [self.visit(ctx.expr())])
#         elif ctx.list_dim_array_access():
#             return ArrayCell(self.visit(ctx.expr6()),self.visit(ctx.list_dim_array_access()))
#         # elif ctx.IDENTIFIER() : return MethCall(self.visit(ctx.expr6()), ctx.IDENTIFIER().getText(),[])
#         elif ctx.IDENTIFIER() : return FieldAccess(self.visit(ctx.expr6()), ctx.IDENTIFIER().getText())
#         func_call = self.visit(ctx.function_call())
#         return MethCall(self.visit(ctx.expr6()), func_call.funName, func_call.args)

#     # Visit a parse tree produced by MiniGoParser#expr7.
#     def visitExpr7(self, ctx:MiniGoParser.Expr7Context):
#         if ctx.getChildCount() > 1 : return self.visit(ctx.expr())
#         if ctx.primitive_value(): return self.visit(ctx.primitive_value())
#         # elif ctx.array_access() : return self.visit(ctx.array_access())
#         # elif ctx.array_access() : 
#         #     [(a,b)] = self.visit(ctx.array_access())
#         #     return ArrayCell(a,b)
#         # elif ctx.list_fields_value() : return self.visit(ctx.list_fields_value())
#         elif ctx.lhs() : return self.visit(ctx.lhs())
#         elif ctx.array_lit() : return self.visit(ctx.array_lit())   
#         elif ctx.NIL() : return NilLiteral()
#         # elif ctx.IDENTIFIER() : return str(Id(ctx.IDENTIFIER().getText()))
#         elif ctx.IDENTIFIER() : return (Id(ctx.IDENTIFIER()))
#         elif ctx.function_call() : return self.visit(ctx.function_call())
#         return self.visit(ctx.struct_lit())
#         # if ctx.getChildCount() > 1:  
#         #     print("\n\n\n\n\n 1 \n\n\n\n\n")  
#         #     return self.visit(ctx.expr())

#         # if ctx.primitive_value():  
#         #     print("\n\n\n\n\n 2 \n\n\n\n\n")  
#         #     return self.visit(ctx.primitive_value())

#         # elif ctx.array_access():  
#         #     print("\n\n\n\n\n 3 \n\n\n\n\n")  
#         #     return self.visit(ctx.array_access())

#         # elif ctx.list_fields_value():  
#         #     print("\n\n\n\n\n 4 \n\n\n\n\n")  
#         #     return self.visit(ctx.list_fields_value())

#         # elif ctx.array_lit():  
#         #     print("\n\n\n\n\n 5 \n\n\n\n\n")  
#         #     return self.visit(ctx.array_lit())

#         # elif ctx.NIL():  
#         #     print("\n\n\n\n\n 6 \n\n\n\n\n")  
#         #     return NilLiteral()

#         # elif ctx.IDENTIFIER():  
#         #     print("\n\n\n\n\n 7 \n\n\n\n\n")  
#         #     return str(Id(ctx.IDENTIFIER().getText()))

#         # elif ctx.function_call():  
#         #     print("\n\n\n\n\n 8 \n\n\n\n\n")  
#         #     return self.visit(ctx.function_call())

#         # print("\n\n\n\n\n 9 \n\n\n\n\n")  
#         # return self.visit(ctx.struct_lit())



#     # Visit a parse tree produced by MiniGoParser#end_var.
#     def visitEnd_var(self, ctx:MiniGoParser.End_varContext):
#         pass
        
#     def visitList_dim_array_access(self, ctx:MiniGoParser.List_dim_array_accessContext):
#         if ctx.getChildCount() == 3:
#             return [self.visit(ctx.expr())]
#         return [self.visit(ctx.expr())] + self.visit(ctx.list_dim_array_access())

#     # Visit a parse tree produced by MiniGoParser#constants.
#     def visitConstants(self, ctx:MiniGoParser.ConstantsContext):
#         name = ctx.IDENTIFIER().getText()
#         expr = self.visit(ctx.expr())
#         return ConstDecl(name,None,expr)


#     # Visit a parse tree produced by MiniGoParser#constants_stmt.
#     def visitConstants_stmt(self, ctx:MiniGoParser.Constants_stmtContext):
#         return self.visit(ctx.constants())


#     # Visit a parse tree produced by MiniGoParser#function.
#     def visitFunction(self, ctx:MiniGoParser.FunctionContext):
#         name = ctx.IDENTIFIER().getText()
#         list_para = self.visit(ctx.list_para()) if ctx.list_para() else []
#         if list_para != [] :
#             lst_paradecl = [ParamDecl(i,j) for i,j in list_para]
#             list_para = lst_paradecl
#         type_ = self.visit(ctx.optional_return_type())
#         function_body = Block(self.visit(ctx.function_body()))
#         return FuncDecl(name, list_para, type_, function_body)


#     # Visit a parse tree produced by MiniGoParser#optional_return_type.
#     def visitOptional_return_type(self, ctx:MiniGoParser.Optional_return_typeContext):
#         return VoidType() if ctx.getChildCount() == 0 else self.visit(ctx.type_except_array())


#     # Visit a parse tree produced by MiniGoParser#function_body.
#     def visitFunction_body(self, ctx:MiniGoParser.Function_bodyContext):
#         return self.visit(ctx.list_stmt())


#     # Visit a parse tree produced by MiniGoParser#function_call.
#     def visitFunction_call(self, ctx:MiniGoParser.Function_callContext):
#         name = ctx.IDENTIFIER().getText()
#         list_para_value = self.visit(ctx.list_para_value())
#         return FuncCall(name, list_para_value)


#     # Visit a parse tree produced by MiniGoParser#list_para_value.
#     def visitList_para_value(self, ctx:MiniGoParser.List_para_valueContext):
#         return [] if ctx.getChildCount() == 0 else self.visit(ctx.list_para_value_notnull())


#     # Visit a parse tree produced by MiniGoParser#list_para_value_notnull.
#     def visitList_para_value_notnull(self, ctx:MiniGoParser.List_para_value_notnullContext):
#         return [self.visit(ctx.para_value())] if ctx.getChildCount() == 1 else [self.visit(ctx.para_value())] + self.visit(ctx.list_para_value_notnull())


#     # Visit a parse tree produced by MiniGoParser#para_value.
#     def visitPara_value(self, ctx:MiniGoParser.Para_valueContext):
#         if ctx.primitive_value() : return self.visit(ctx.primitive_value())
#         if ctx.IDENTIFIER() : return Id(ctx.IDENTIFIER().getText())
#         if ctx.lhs() : return self.visit(ctx.lhs())
#         if ctx.struct_lit() : return self.visit(ctx.struct_lit())
#         if ctx.expr() : return self.visit(ctx.expr())
#         if ctx.method_func_call() : return self.visit(ctx.method_func_call())
#         if ctx.function_call() : return self.visit(ctx.function_call())


#     # Visit a parse tree produced by MiniGoParser#method_func.
#     def visitMethod_func(self, ctx:MiniGoParser.Method_funcContext):
#         [(receiver, recType)] = self.visit(ctx.receiver()) # why type of receiver is type
#         fun_name = ctx.IDENTIFIER().getText()
#         fun_para = self.visit(ctx.list_para()) if ctx.list_para() else []
#         if fun_para != [] :
#             # print("\n\n\n\n\n\n hap hoi \n\n\n\n\n\n")
#             lst_paradecl = [ParamDecl(i,j) for i,j in fun_para]
#             fun_para = lst_paradecl
#         fun_type = self.visit(ctx.optional_return_type())
#         fun_body = Block(self.visit(ctx.function_body()))
#         return MethodDecl(receiver, str(Id(recType)), FuncDecl(fun_name,fun_para, fun_type, fun_body))


#     # Visit a parse tree produced by MiniGoParser#receiver.
#     def visitReceiver(self, ctx:MiniGoParser.ReceiverContext):
#         return [(ctx.IDENTIFIER(0).getText(), ctx.IDENTIFIER(1).getText())]


#     # Visit a parse tree produced by MiniGoParser#method_func_call.
#     def visitMethod_func_call(self, ctx:MiniGoParser.Method_func_callContext):
#         receiver = self.visit(ctx.expr6())
#         obj = self.visit(ctx.function_call())
#         return MethCall(receiver, obj.funName, obj.args)


#     # Visit a parse tree produced by MiniGoParser#stmt.
#     def visitStmt(self, ctx:MiniGoParser.StmtContext):
#         if ctx.variable() : return self.visit(ctx.variable())
#         elif ctx.constants_stmt() : return self.visit(ctx.constants_stmt())
#         elif ctx.assign_stmt() : return self.visit(ctx.assign_stmt())
#         elif ctx.if_stmt_end() : return self.visit(ctx.if_stmt_end())
#         elif ctx.for_stmt() : return self.visit(ctx.for_stmt())
#         elif ctx.break_stmt() : return self.visit(ctx.break_stmt())
#         elif ctx.continue_stmt() : return self.visit(ctx.continue_stmt())
#         elif ctx.call_stmt() : return self.visit(ctx.call_stmt())
#         elif ctx.return_stmt() : return self.visit(ctx.return_stmt())
#         # if ctx.variable(): 
#         #     print("\n1\n")
#         #     return self.visit(ctx.variable())

#         # elif ctx.constants_stmt(): 
#         #     print("\n2\n")
#         #     return self.visit(ctx.constants_stmt())

#         # elif ctx.assign_stmt(): 
#         #     print("\n3\n")
#         #     return self.visit(ctx.assign_stmt())

#         # elif ctx.if_stmt_end(): 
#         #     print("\n4\n")
#         #     return self.visit(ctx.if_stmt_end())

#         # elif ctx.for_stmt(): 
#         #     print("\n5\n")
#         #     return self.visit(ctx.for_stmt())

#         # elif ctx.break_stmt(): 
#         #     print("\n6\n")
#         #     return self.visit(ctx.break_stmt())

#         # elif ctx.continue_stmt(): 
#         #     print("\n7\n")
#         #     return self.visit(ctx.continue_stmt())

#         # elif ctx.call_stmt(): 
#         #     print("\n8\n")
#         #     return self.visit(ctx.call_stmt())

#         # elif ctx.return_stmt(): 
#         #     print("\n9\n")
#         #     return self.visit(ctx.return_stmt())


#     # def visitIf_mono_stmt(self, ctx:MiniGoParser.If_mono_stmtContext):
#     #     self.visit(ctx.if_mono())
        
#     # def visitIf_mono(self, ctx:MiniGoParser.If_monoContext):
#     #     self.visit(ctx.getChild(0))

#     # Visit a parse tree produced by MiniGoParser#list_stmt.
#     def visitList_stmt(self, ctx:MiniGoParser.List_stmtContext):
#         return [self.visit(ctx.stmt())] if ctx.getChildCount() == 1 else [self.visit(ctx.stmt())] + self.visit(ctx.list_stmt())
    
    
#     # Visit a parse tree produced by MiniGoParser#assign_stmt.
#     def visitAssign_stmt(self, ctx:MiniGoParser.Assign_stmtContext):
#         return self.visit(ctx.assign_stmt_no_end())


#     # Visit a parse tree produced by MiniGoParser#assign_stmt_no_end.
#     def visitAssign_stmt_no_end(self, ctx:MiniGoParser.Assign_stmt_no_endContext):
#         lhs = self.visit(ctx.lhs())
#         op = self.visit(ctx.assign_op())
#         rhs = self.visit(ctx.expr())
#         if op != ":=" : rhs = BinaryOp(op,lhs,rhs)
#         return Assign(lhs,rhs)

#     # Visit a parse tree produced by MiniGoParser#lhs.
#     def visitLhs(self, ctx:MiniGoParser.LhsContext):
#         if ctx.getChildCount() == 1 : return str(Id(ctx.IDENTIFIER().getText()))
#         lhs = self.visit(ctx.lhs())
#         if ctx.IDENTIFIER() : 
#             rhs = ctx.IDENTIFIER().getText()
#             return FieldAccess(lhs,rhs) ## AS THE RECEIVER IS THE EXPRESSION SO CAN WE BELIEVE THAT LHS NEXT LEVEL AUTO IS ...
#         expr = self.visit(ctx.expr())
#         # Ensure `idx` is a list and accumulate indices for nested array accesses
#         if isinstance(lhs, ArrayCell):
#             return ArrayCell(lhs.arr, lhs.idx + [expr])  # Append new index to existing list
#         else:
#             return ArrayCell(lhs, [expr])  # Start new index list
#         # DEBUG HERE: HOW TO APPEND THE LIST OF DIM
#         # elif ctx.IDENTIFIER() : return self.visit(ctx.lhs()) + ctx.IDENTIFIER().getText()
#         # return self.visit(ctx.lhs()) + self.visit(ctx.expr())
#         # DEBUG HERE, DO WE NEED TO SET UP ARRAY ACCESS OR FIELDS ACCESS


#     # Visit a parse tree produced by MiniGoParser#assign_op.
#     # ALREADY CHANGE TO STRING
#     def visitAssign_op(self, ctx:MiniGoParser.Assign_opContext):
#         if ctx.ASSIGN_LOGIC() : return ":="
#         elif ctx.PLUS_EQUAL() : return "+"
#         elif ctx.MINUS_EQUAL() : return "-"
#         elif ctx.ASTERISK_EQUAL() : return "*"
#         elif ctx.DIVIDE_EQUAL() : return "/"
#         elif ctx.MODULO_EQUAL() : return "%"

#     def visitIf_stmt_end(self, ctx:MiniGoParser.If_stmt_endContext):
#         return self.visit(ctx.if_stmt())
    
#     def visitIf_stmt(self, ctx:MiniGoParser.If_stmtContext):
#         expr = self.visit(ctx.expr())
#         thenStmt = Block(self.visit(ctx.list_stmt()))
#         elseStmt = self.visit(ctx.else_stmt())
#         if elseStmt is None: return If(expr,thenStmt, None)
#         return If(expr,thenStmt,elseStmt)


#     # Visit a parse tree produced by MiniGoParser#else_stmt.
#     def visitElse_stmt(self, ctx:MiniGoParser.Else_stmtContext):
#         # return self.visitChildren(ctx)
#         if ctx.getChildCount() == 0 : return None
#         elif ctx.if_stmt() : return self.visit(ctx.if_stmt())
#         return Block(self.visit(ctx.list_stmt()))


#     # Visit a parse tree produced by MiniGoParser#for_stmt.
#     def visitFor_stmt(self, ctx:MiniGoParser.For_stmtContext):
#         return self.visit(ctx.getChild(0))


#     # Visit a parse tree produced by MiniGoParser#basic_form.
#     def visitBasic_form(self, ctx:MiniGoParser.Basic_formContext):
#         # return self.visitChildren(ctx)
#         cond = self.visit(ctx.condition())
#         loop = Block(self.visit(ctx.list_stmt()))
#         return ForBasic(cond, loop)
        

#     # Visit a parse tree produced by MiniGoParser#condition.
#     def visitCondition(self, ctx:MiniGoParser.ConditionContext):
#         return self.visit(ctx.expr())


#     # Visit a parse tree produced by MiniGoParser#init_form.
#     def visitInit_form(self, ctx:MiniGoParser.Init_formContext):
#         init = self.visit(ctx.initilization())
#         cond = self.visit(ctx.condition())
#         upda = self.visit(ctx.update())
#         loop = Block(self.visit(ctx.list_stmt()))
#         return ForStep(init, cond, upda, loop)

#     # Visit a parse tree produced by MiniGoParser#initilization.
#     def visitInitilization(self, ctx:MiniGoParser.InitilizationContext):
#         if ctx.getChildCount() == 1 : return self.visit(ctx.var_decl_init())
#         lhs = Id(ctx.IDENTIFIER().getText())
#         rhs = self.visit(ctx.expr())
#         op = self.visit(ctx.assign_op())
#         if (op != ":="):
#             rhs = BinaryOp(op,lhs,rhs)
#         return Assign(lhs, rhs)


#     # Visit a parse tree produced by MiniGoParser#update.
#     def visitUpdate(self, ctx:MiniGoParser.UpdateContext):
#         lhs = Id(ctx.IDENTIFIER().getText())
#         rhs = self.visit(ctx.expr())
#         op = self.visit(ctx.assign_op())
#         if (op != ":="):
#             rhs = BinaryOp(op,lhs,rhs)
#         return Assign(lhs, rhs)


#     # Visit a parse tree produced by MiniGoParser#range_form.
#     def visitRange_form(self, ctx:MiniGoParser.Range_formContext):
#         idx = self.visit(ctx.index())
#         value = self.visit(ctx.value())
#         arr = self.visit(ctx.expr())
#         loop = Block(self.visit(ctx.list_stmt()))
#         return ForEach(idx,value,arr,loop)


#     # Visit a parse tree produced by MiniGoParser#index.
#     def visitIndex(self, ctx:MiniGoParser.IndexContext):
#         # return str(Id(ctx.IDENTIFIER().getText()))
#         return (Id(ctx.IDENTIFIER().getText()))


#     # Visit a parse tree produced by MiniGoParser#value.
#     def visitValue(self, ctx:MiniGoParser.ValueContext):
#         # return str(Id(ctx.IDENTIFIER().getText()))
#         return (Id(ctx.IDENTIFIER().getText()))


#     # Visit a parse tree produced by MiniGoParser#break_stmt.
#     def visitBreak_stmt(self, ctx:MiniGoParser.Break_stmtContext):
#         # return self.visitChildren(ctx)
#         return Break()


#     # Visit a parse tree produced by MiniGoParser#continue_stmt.
#     def visitContinue_stmt(self, ctx:MiniGoParser.Continue_stmtContext):
#         # return self.visitChildren(ctx)
#         return Continue()


#     # Visit a parse tree produced by MiniGoParser#call_stmt.
#     def visitCall_stmt(self, ctx:MiniGoParser.Call_stmtContext):
#         return self.visit(ctx.getChild(0))


#     # Visit a parse tree produced by MiniGoParser#return_stmt.
#     def visitReturn_stmt(self, ctx:MiniGoParser.Return_stmtContext):
#         return self.visit(ctx.return_tail())


#     # Visit a parse tree produced by MiniGoParser#return_tail.
#     def visitReturn_tail(self, ctx:MiniGoParser.Return_tailContext):
#         return Return(None) if ctx.getChildCount() == 0 else Return(self.visit(ctx.expr()))


from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *

class ASTGeneration(MiniGoVisitor):
     # program: program_element_list EOF;
     # list[Decl]
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return Program(self.visit(ctx.program_element_list()))


    # program_element_list:
	# declaration program_element_list
	# | declaration;
    def visitProgram_element_list(self, ctx:MiniGoParser.Program_element_listContext):
        if ctx.program_element_list():
            return [self.visit(ctx.declaration())] + self.visit(ctx.program_element_list())
        return [self.visit(ctx.declaration())]


    # optional_variable_type: variable_type |;
    def visitOptional_variable_type(self, ctx:MiniGoParser.Optional_variable_typeContext):
        if ctx.variable_type():
            return self.visit(ctx.variable_type())
        return None


    # variable_type: primitive_type | array_type;
    def visitVariable_type(self, ctx:MiniGoParser.Variable_typeContext):
        if ctx.primitive_type():
            return self.visit(ctx.primitive_type())
        return self.visit(ctx.array_type())


    # primitive_type: INT | FLOAT | STRING | BOOL | ID;
    def visitPrimitive_type(self, ctx:MiniGoParser.Primitive_typeContext):
        if ctx.INT():
            return IntType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.STRING():
            return StringType()
        if ctx.BOOL():
            return BoolType()
        return Id(ctx.ID().getText())


    # literal:
	# INT_LIT
	# | FLOAT_LIT
	# | STRING_LIT
	# | TRUE
	# | FALSE
	# | array_literal
	# | struct_literal
	# | NIL;
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        if ctx.INT_LIT():
            text = ctx.INT_LIT().getText()
            result = eval(text)
            # if 'x' in text or 'X' in text:
            #     result = hex(result).replace('x', 'X') if 'X' in text else hex(result)
            # if 'b' in text or 'B' in text:
            #     result = bin(result).replace('b', 'B') if 'B' in text else bin(result)
            # if 'o' in text or 'O' in text:
            #     result = oct(result).replace('o', 'O') if 'O' in text else oct(result)
            return IntLiteral(eval(ctx.INT_LIT().getText()))
        if ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        if ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        if ctx.TRUE():
            return BooleanLiteral(True)
        if ctx.FALSE():
            return BooleanLiteral(False)
        if ctx.array_literal():
            return self.visit(ctx.array_literal())
        if ctx.struct_literal():
            return self.visit(ctx.struct_literal())
        return NilLiteral()


    # array_literal: array_type LBRACE array_block RBRACE;
    # dimens: list[Expr], eleType: Type, value: NestedList
    def visitArray_literal(self, ctx:MiniGoParser.Array_literalContext):
        array_type = self.visit(ctx.array_type())
        dimensions = array_type.dimens  
        elementType = array_type.eleType
        value = self.visit(ctx.array_block())
        return ArrayLiteral(dimensions, elementType, value)


    # array_pre_element:
	# INT_LIT
	# | FLOAT_LIT
	# | ID
	# | STRING_LIT
	# | TRUE
	# | FALSE
	# | struct_literal
	# | NIL;
    def visitArray_pre_element(self, ctx:MiniGoParser.Array_pre_elementContext):
        if ctx.INT_LIT():
            return IntLiteral(eval(ctx.INT_LIT().getText()))
        if ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        if ctx.ID():
            return Id(ctx.ID().getText())
        if ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        if ctx.TRUE():
            return BooleanLiteral(True)
        if ctx.FALSE():
            return BooleanLiteral(False)
        if ctx.struct_literal():
            return self.visit(ctx.struct_literal())
        return NilLiteral()


    # array_pre_element_list:
	# array_pre_element COMMA array_pre_element_list
	# | array_pre_element;
    def visitArray_pre_element_list(self, ctx:MiniGoParser.Array_pre_element_listContext):
        if ctx.array_pre_element_list():
            return [self.visit(ctx.array_pre_element())] + self.visit(ctx.array_pre_element_list())
        return [self.visit(ctx.array_pre_element())]


    # array_pre_element_array_lit:
    #  LBRACE array_pre_element_array_lit RBRACE
	# | LBRACE array_pre_element_array_lit COMMA array_pre_element_array_lit RBRACE
	# | array_pre_element_list;
    def visitArray_pre_element_array_lit(self, ctx:MiniGoParser.Array_pre_element_array_litContext):
        if ctx.getChildCount() == 3:
            recur = ctx.array_pre_element_array_lit(0)
            if recur.array_pre_element_array_lit(0):
                a =  [self.visit(recur.array_pre_element_array_lit(0))]
                return a
            return self.visit(ctx.array_pre_element_array_lit(0))
        if ctx.getChildCount() == 1:
            return self.visit(ctx.array_pre_element_list())
        if ctx.getChildCount() == 5:
            left = ctx.array_pre_element_array_lit(0)
            if left.array_pre_element_list():
                left = self.visit(left.array_pre_element_list())
            else:
                left = [ctx.array_pre_element_array_lit(0)]
            right = ctx.array_pre_element_array_lit(1)
            if right.array_pre_element_list():
                right = self.visit(right.array_pre_element_list())
            else:
                right = [self.visit(ctx.array_pre_element_array_lit(1))]
            return left + right
        


    # array_element: array_pre_element | array_pre_element_array_lit;
    def visitArray_element(self, ctx:MiniGoParser.Array_elementContext):
        if ctx.array_pre_element():
            return self.visit(ctx.array_pre_element())
        return self.visit(ctx.array_pre_element_array_lit())


    # array_block: array_element COMMA array_block | array_element;
    def visitArray_block(self, ctx:MiniGoParser.Array_blockContext):
        if ctx.array_block():
            return [self.visit(ctx.array_element())] + self.visit(ctx.array_block())
        return [self.visit(ctx.array_element())]


    # array_type: multiple_dimension variable_type;
    # dimension: list[Expr], eleType: Type
    def visitArray_type(self, ctx:MiniGoParser.Array_typeContext):
        return ArrayType(self.visit(ctx.multiple_dimension()), self.visit(ctx.variable_type()))


    # Visit a parse tree produced by MiniGoParser#multiple_dimension.
    # multiple_dimension:
	# LBRACK dim_literal RBRACK multiple_dimension
	# | LBRACK dim_literal RBRACK;
    def visitMultiple_dimension(self, ctx:MiniGoParser.Multiple_dimensionContext):
        if ctx.multiple_dimension():
            return [self.visit(ctx.dim_literal())] + self.visit(ctx.multiple_dimension())
        return [self.visit(ctx.dim_literal())]


    # Visit a parse tree produced by MiniGoParser#dim_literal.
    # dim_literal: INT_LIT | ID;
    def visitDim_literal(self, ctx:MiniGoParser.Dim_literalContext):
        return IntLiteral(eval(ctx.INT_LIT().getText())) if ctx.INT_LIT() else Id(ctx.ID().getText())


    # struct_literal: ID LBRACE optional_field_values RBRACE;
    # name: str, fields: list[tuple(str,Expr)]
    def visitStruct_literal(self, ctx:MiniGoParser.Struct_literalContext):
        name = ctx.ID().getText()
        fields = self.visit(ctx.optional_field_values())
        return StructLiteral(name, fields)


    # optional_field_values: field_values |;
    def visitOptional_field_values(self, ctx:MiniGoParser.Optional_field_valuesContext):
        if ctx.field_values():
            return self.visit(ctx.field_values())
        return []


    # field_values: field_value COMMA field_values | field_value;
    def visitField_values(self, ctx:MiniGoParser.Field_valuesContext):
        if ctx.field_values():
            return [self.visit(ctx.field_value())] + self.visit(ctx.field_values())
        return [self.visit(ctx.field_value())]


    # field_value: ID COLON expression1;
    def visitField_value(self, ctx:MiniGoParser.Field_valueContext):
        return (ctx.ID().getText(), self.visit(ctx.expression1()))


    # optional_list_expression: list_expression |;
    def visitOptional_list_expression(self, ctx:MiniGoParser.Optional_list_expressionContext):
        if ctx.list_expression():
            return self.visit(ctx.list_expression())
        return []


    # list_expression:
	# expression1 COMMA list_expression
	# | expression1;
    def visitList_expression(self, ctx:MiniGoParser.List_expressionContext):
        if ctx.list_expression():
            return [self.visit(ctx.expression1())] + self.visit(ctx.list_expression())
        return [self.visit(ctx.expression1())]


    # expression1: expression1 OR expression2 | expression2;
    def visitExpression1(self, ctx:MiniGoParser.Expression1Context):
        if ctx.expression1():
            return BinaryOp(ctx.OR().getText(), self.visit(ctx.expression1()), self.visit(ctx.expression2()))
        return self.visit(ctx.expression2())
            


    # expression2: expression2 AND expression3 | expression3;
    def visitExpression2(self, ctx:MiniGoParser.Expression2Context):
        if ctx.expression2():
            return BinaryOp(ctx.AND().getText(), self.visit(ctx.expression2()), self.visit(ctx.expression3()))
        return self.visit(ctx.expression3())


    # expression3:
	# expression3 (EQ | NEQ | LT | LE | GE | GT) expression4
	# | expression4;
    def visitExpression3(self, ctx:MiniGoParser.Expression3Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expression3()), self.visit(ctx.expression4()))
        return self.visit(ctx.expression4())


    # expression4: expression4 (ADD | SUB) expression5 | expression5;
    def visitExpression4(self, ctx:MiniGoParser.Expression4Context):
        if ctx.expression4():
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expression4()), self.visit(ctx.expression5()))
        return self.visit(ctx.expression5())


    # expression5:
	# expression5 (MUL | DIV | MOD) expression6
	# | expression6;
    def visitExpression5(self, ctx:MiniGoParser.Expression5Context):
        if ctx.expression5():
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expression5()), self.visit(ctx.expression6()))
        return self.visit(ctx.expression6())


    # expression6: (SUB | NOT) expression6 | expression7;
    def visitExpression6(self, ctx:MiniGoParser.Expression6Context):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.expression6()))
        return self.visit(ctx.expression7())


    # expression7:
	# expression7 LBRACK expression1 RBRACK
	# | expression7 DOT ID (LPAREN optional_list_expression RPAREN)?
	# // method call and struct field access
	# | expression8;
    # method_call: receiver: Expr, metName: str, args: List[Expr]
    # field_access: receiverL Expr, field: str
    # array_cell: arr: Expr, idx: List[Expr]
    def visitExpression7(self, ctx:MiniGoParser.Expression7Context):
        if ctx.optional_list_expression():
            receiver = self.visit(ctx.expression7()) 
            metname = ctx.ID().getText()
            args = self.visit(ctx.optional_list_expression())
            return MethCall(receiver, metname, args)
        if ctx.ID():
            receiver = self.visit(ctx.expression7())
            field = ctx.ID().getText()
            return FieldAccess(receiver, field)
        if ctx.expression1():
            ids = [self.visit(ctx.expression1())]
            arr = ctx.expression7()
            while arr.getChildCount() == 4:
                ids.append(self.visit(arr.expression1()))
                arr = arr.expression7()
            ids = ids[::-1]
            arr = self.visit(arr)
            return ArrayCell(arr, ids)
        return self.visit(ctx.expression8())

            

    # expression8:
	# literal
	# | ID
	# | function_call
	# | LPAREN expression1 RPAREN;
    def visitExpression8(self, ctx:MiniGoParser.Expression8Context):
        if ctx.literal():
            return self.visit(ctx.literal())
        if ctx.ID():
            return Id(ctx.ID().getText())
        if ctx.function_call():
            return self.visit(ctx.function_call())
        if ctx.expression1():
            return self.visit(ctx.expression1())
        


    # function_call: ID LPAREN optional_list_expression RPAREN;
    # name: str, args: list[Expr]
    def visitFunction_call(self, ctx:MiniGoParser.Function_callContext):
        name = ctx.ID().getText()
        args = self.visit(ctx.optional_list_expression())
        return FuncCall(name, args)


# declaration:
# 	(
# 		variable_declaration
# 		| constant_declaration
# 		| func_declaration
# 		| type_declaration
# 	) SEMI;
    def visitDeclaration(self, ctx:MiniGoParser.DeclarationContext):
        if ctx.variable_declaration():
            return self.visit(ctx.variable_declaration())
        if ctx.constant_declaration():
            return self.visit(ctx.constant_declaration())
        if ctx.func_declaration():
            return self.visit(ctx.func_declaration())
        if ctx.type_declaration():
            return self.visit(ctx.type_declaration())


    # variable_declaration: VAR ID variable_characteristic;
    # name: str, type: Type, init: Expr
    def visitVariable_declaration(self, ctx:MiniGoParser.Variable_declarationContext):
        name = ctx.ID().getText()
        vtype, vinit = self.visit(ctx.variable_characteristic())
        return VarDecl(name, vtype, vinit)


    # variable_characteristic:
	# variable_type
	# | optional_variable_type initialization;
    # return Type, Expr None if not available 
    def visitVariable_characteristic(self, ctx:MiniGoParser.Variable_characteristicContext):
        if ctx.variable_type():
            return self.visit(ctx.variable_type()), None
        return self.visit(ctx.optional_variable_type()), self.visit(ctx.initialization())


    # initialization: ASSIGN expression1;
    def visitInitialization(self, ctx:MiniGoParser.InitializationContext):
        return self.visit(ctx.expression1())


    # constant_declaration: CONST ID ASSIGN expression1;
    # conName: str, conType: Type, initExpr: Expr
    def visitConstant_declaration(self, ctx:MiniGoParser.Constant_declarationContext):
        conName = ctx.ID().getText()
        conType = None
        initExpr = self.visit(ctx.expression1())
        return ConstDecl(conName, conType, initExpr)


    # func_declaration: function_method_declaration;
    def visitFunc_declaration(self, ctx:MiniGoParser.Func_declarationContext):
        return self.visit(ctx.function_method_declaration())


# function_method_declaration:
# 	FUNC (LPAREN ID ID RPAREN)? ID LPAREN list_param RPAREN optional_variable_type statement_block;
# name: str, param: list[ParamDecl], returnType: Type, body: Block
    def visitFunction_method_declaration(self, ctx:MiniGoParser.Function_method_declarationContext):
        ids = ctx.ID()
        params = self.visit(ctx.list_param())
        returnType = self.visit(ctx.optional_variable_type())
        if returnType is None:
            returnType = VoidType()
        body = self.visit(ctx.statement_block())
        if len(ids) == 1:
            name = ids[0].getText()
            return FuncDecl(name, params, returnType, body)
        receiver = ids[0].getText()
        reType = Id(ids[1].getText())
        name = ids[2].getText()
        func = FuncDecl(name, params, returnType, body)
        return MethodDecl(receiver, reType, func)
        
            


    # Visit a parse tree produced by MiniGoParser#list_param.
    # list_param: no_null_list_param |;
    def visitList_param(self, ctx:MiniGoParser.List_paramContext):
        return self.visit(ctx.no_null_list_param()) if ctx.no_null_list_param() else []


    # no_null_list_param:
	# parameter COMMA no_null_list_param
	# | parameter;
    def visitNo_null_list_param(self, ctx:MiniGoParser.No_null_list_paramContext):
        if ctx.no_null_list_param():
            return self.visit(ctx.parameter()) + self.visit(ctx.no_null_list_param())
        return self.visit(ctx.parameter())


    # parameter: ID COMMA parameter | ID variable_type;
    # name: str, type: Type
    def visitParameter(self, ctx:MiniGoParser.ParameterContext):
        if not ctx.parameter():
            name = ctx.ID().getText()
            type = self.visit(ctx.variable_type())
            return [ParamDecl(name, type)]
        ids = [ctx.ID().getText()]
        parameter = ctx.parameter()
        while parameter.getChildCount() == 3:
            ids.append(parameter.ID().getText())
            parameter = parameter.parameter()
        type = self.visit(parameter.variable_type())
        ids.append(parameter.ID().getText())
        return [ParamDecl(x, type) for x in ids]
        

    # type_declaration: struct_declaration | interface_declaration;
    def visitType_declaration(self, ctx:MiniGoParser.Type_declarationContext):
        return self.visit(ctx.struct_declaration()) if ctx.struct_declaration() else self.visit(ctx.interface_declaration())


    # struct_declaration: TYPE ID STRUCT LBRACE list_of_fields RBRACE;
    # name: str, elements: list[tuple(str,Type)], methods: List[MethodDecl]
    def visitStruct_declaration(self, ctx:MiniGoParser.Struct_declarationContext):
        name = ctx.ID().getText()
        methods = []
        elements = self.visit(ctx.list_of_fields())
        return StructType(name, elements, methods)


    # Visit a parse tree produced by MiniGoParser#list_of_fields.
    # list_of_fields:
	# struct_parameter SEMI list_of_fields
	# | struct_parameter SEMI;
    def visitList_of_fields(self, ctx:MiniGoParser.List_of_fieldsContext):
        if ctx.list_of_fields():
            return [self.visit(ctx.struct_parameter())] + self.visit(ctx.list_of_fields())
        return [self.visit(ctx.struct_parameter())]


    # struct_parameter: ID variable_type;
    def visitStruct_parameter(self, ctx:MiniGoParser.Struct_parameterContext):
        return (ctx.ID().getText(), self.visit(ctx.variable_type()))


    # interface_declaration:
	# TYPE ID INTERFACE LBRACE list_of_interface_methods RBRACE;
    # name: str, methods: List[Prototype]
    def visitInterface_declaration(self, ctx:MiniGoParser.Interface_declarationContext):
        name = ctx.ID().getText()
        methods = self.visit(ctx.list_of_interface_methods())
        return InterfaceType(name, methods)


    # list_of_interface_methods:
	# interface_method list_of_interface_methods
	# | interface_method;
    def visitList_of_interface_methods(self, ctx:MiniGoParser.List_of_interface_methodsContext):
        if ctx.list_of_interface_methods():
            return [self.visit(ctx.interface_method())] + self.visit(ctx.list_of_interface_methods())
        return [self.visit(ctx.interface_method())]


    # name: str, param: List[Type], returnType: Type
    # interface_method:
	# ID LPAREN list_param RPAREN optional_variable_type SEMI;
    def visitInterface_method(self, ctx:MiniGoParser.Interface_methodContext):
        name = ctx.ID().getText()
        param = self.visit(ctx.list_param())
        params = [x.parType for x in param]
        returnType = self.visit(ctx.optional_variable_type())
        if returnType is None:
            returnType = VoidType()
        return Prototype(name, params, returnType)
         


    # list_statement: statement list_statement | statement;
    def visitList_statement(self, ctx:MiniGoParser.List_statementContext):
        if ctx.list_statement():
            return [self.visit(ctx.statement())] + self.visit(ctx.list_statement())
        return [self.visit(ctx.statement())]


    # statement:
	# (
	# 	declaration_stmt
	# 	| assign_statement
	# 	| if_statement
	# 	| for_statement
	# 	| break_statement
	# 	| continue_statement
	# 	| call_statement
	# 	| return_statement
	# );
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        if ctx.declaration_stmt():
            return self.visit(ctx.declaration_stmt())
        if ctx.assign_statement():
            return self.visit(ctx.assign_statement())
        if ctx.if_statement():
            return self.visit(ctx.if_statement())
        if ctx.for_statement():
            return self.visit(ctx.for_statement())
        if ctx.break_statement():
            return self.visit(ctx.break_statement())
        if ctx.continue_statement():
            return self.visit(ctx.continue_statement())
        if ctx.call_statement():
            return self.visit(ctx.call_statement())
        return self.visit(ctx.return_statement()) 


    # declaration_stmt: (variable_declaration | constant_declaration) SEMI;
    def visitDeclaration_stmt(self, ctx:MiniGoParser.Declaration_stmtContext):
        if ctx.variable_declaration():
            return self.visit(ctx.variable_declaration())
        return self.visit(ctx.constant_declaration())

    # assign_statement:
	# lhs_assign (
	# 	COLON_ASSIGN
	# 	| ADD_ASSIGN
	# 	| SUB_ASSIGN
	# 	| MUL_ASSIGN
	# 	| DIV_ASSIGN
	# 	| MOD_ASSIGN
	# ) expression1 SEMI;
    # lhs: LHS, rhs: Expr
    def visitAssign_statement(self, ctx:MiniGoParser.Assign_statementContext):
        lhs = self.visit(ctx.lhs_assign())
        rhs = self.visit(ctx.expression1())
        if ctx.ADD_ASSIGN():
            rhs = BinaryOp('+', lhs, rhs)
        if ctx.SUB_ASSIGN():
            rhs = BinaryOp('-', lhs, rhs)
        if ctx.MUL_ASSIGN():
            rhs = BinaryOp('*', lhs, rhs)
        if ctx.DIV_ASSIGN():
            rhs = BinaryOp('/', lhs, rhs)
        if ctx.MOD_ASSIGN():
            rhs = BinaryOp('%', lhs, rhs)
        return Assign(lhs, rhs)

    # lhs_assign:
	# lhs_assign LBRACK expression1 RBRACK
	# | lhs_assign DOT ID
	# | ID;
    # method_call: receiver: Expr, metName: str, args: List[Expr]
    # field_access: receiverL Expr, field: str
    # array_cell: arr: Expr, idx: List[Expr]
    def visitLhs_assign(self, ctx:MiniGoParser.Lhs_assignContext):
        if ctx.getChildCount() == 3:
            revceiver = self.visit(ctx.lhs_assign())
            field = ctx.ID().getText()
            return FieldAccess(revceiver, field)
        if ctx.expression1():
            ids = [self.visit(ctx.expression1())]
            arr = ctx.lhs_assign()
            while arr.getChildCount() == 4:
                ids.append(self.visit(arr.expression1()))
                arr = arr.lhs_assign()
            ids = ids[::-1]
            arr = self.visit(arr)
            return ArrayCell(arr, ids)
        return Id(ctx.ID().getText())
        
            


    # statement_block: LBRACE list_statement RBRACE;
    def visitStatement_block(self, ctx:MiniGoParser.Statement_blockContext):
        return Block(self.visit(ctx.list_statement()))


    # if_statement:
	# IF LPAREN expression1 RPAREN statement_block else_if_statement? else_statement? SEMI;
    # expr: Expr, thenStmt: Stmt, elseStmt: Stmt
    def visitIf_statement(self, ctx:MiniGoParser.If_statementContext):
        expr = self.visit(ctx.expression1())
        thenStmt = self.visit(ctx.statement_block())
        elseStmt = None
        if not (ctx.else_if_statement() or ctx.else_statement()):
            return If(expr, thenStmt, elseStmt)
        if not ctx.else_if_statement():
            elseStmt = self.visit(ctx.else_statement())
            return If(expr, thenStmt, elseStmt)
        # eis = ctx.else_if_statement()
        # ifThen = []
        # while eis.else_if_statement():
        #     ifThen.append((self.visit(eis.expression1()), self.visit(eis.statement_block())))
        #     eis = eis.else_if_statement()
        # ifThen.append((self.visit(eis.expression1()), self.visit(eis.statement_block())))
        # return reduce(lambda x, y: If(y[0], y[1], x), ifThen, self.visit(ctx.else_statement()))
        def recursive_else_stmt(elifStmt, elseStmt):
            if not elifStmt.else_if_statement():
                else_stmt = self.visit(elseStmt) if elseStmt else None
                return If(self.visit(elifStmt.expression1()), self.visit(elifStmt.statement_block()), else_stmt)
            return If(self.visit(elifStmt.expression1()), self.visit(elifStmt.statement_block()), recursive_else_stmt(elifStmt.else_if_statement(), elseStmt))  
        elseStmt = recursive_else_stmt(ctx.else_if_statement(), ctx.else_statement())
        return If(expr, thenStmt, elseStmt)    


    # else_statement: ELSE statement_block;
    def visitElse_statement(self, ctx:MiniGoParser.Else_statementContext):
        return self.visit(ctx.statement_block())


    # else_if_statement:
	# ELSE IF LPAREN expression1 RPAREN statement_block else_if_statement
	# | ELSE IF LPAREN expression1 RPAREN statement_block;
    def visitElse_if_statement(self, ctx:MiniGoParser.Else_if_statementContext):
        pass


    # for_statement:
	# (basic_for_loop | for_loop_icu | for_loop_range) SEMI;
    def visitFor_statement(self, ctx:MiniGoParser.For_statementContext):
        if ctx.basic_for_loop():
            return self.visit(ctx.basic_for_loop())
        if ctx.for_loop_icu():
            return self.visit(ctx.for_loop_icu())
        return self.visit(ctx.for_loop_range())


    # basic_for_loop: FOR expression1 statement_block;
    # cond: Expr, loop: Block
    def visitBasic_for_loop(self, ctx:MiniGoParser.Basic_for_loopContext):
        cond = self.visit(ctx.expression1())
        loop = self.visit(ctx.statement_block())
        return ForBasic(cond, loop)


    # for_loop_icu:
	# FOR init_statement SEMI expression1 SEMI init_assign statement_block;
    # init: Stmt, cond: Expr, upda: Assign, loop: Block
    def visitFor_loop_icu(self, ctx:MiniGoParser.For_loop_icuContext):
        init = self.visit(ctx.init_statement())
        cond = self.visit(ctx.expression1())
        upda = self.visit(ctx.init_assign())
        loop = self.visit(ctx.statement_block())
        return ForStep(init, cond, upda, loop)


    # init_statement: init_assign | init_declared;
    def visitInit_statement(self, ctx:MiniGoParser.Init_statementContext):
        if ctx.init_assign():
            return self.visit(ctx.init_assign())
        return self.visit(ctx.init_declared())


    # init_assign:
	# ID (
	# 	COLON_ASSIGN
	# 	| ADD_ASSIGN
	# 	| SUB_ASSIGN
	# 	| MUL_ASSIGN
	# 	| DIV_ASSIGN
	# 	| MOD_ASSIGN
	# ) expression1;
    # lhs: LHS, rhs: Expr
    def visitInit_assign(self, ctx:MiniGoParser.Init_assignContext):
        lhs = Id(ctx.ID().getText())
        rhs = self.visit(ctx.expression1())
        if ctx.ADD_ASSIGN():
            rhs = BinaryOp('+', lhs, rhs)
        if ctx.SUB_ASSIGN():
            rhs = BinaryOp('-', lhs, rhs)
        if ctx.MUL_ASSIGN():
            rhs = BinaryOp('*', lhs, rhs)
        if ctx.DIV_ASSIGN():
            rhs = BinaryOp('/', lhs, rhs)
        if ctx.MOD_ASSIGN():
            rhs = BinaryOp('%', lhs, rhs)
        return Assign(lhs, rhs)


    # init_declared: VAR ID variable_type? ASSIGN expression1;
    # name: str, varType: Type, init: Expr
    def visitInit_declared(self, ctx:MiniGoParser.Init_declaredContext):
        name = ctx.ID().getText()
        varType = self.visit(ctx.variable_type()) if ctx.variable_type() else None
        init = self.visit(ctx.expression1())
        return VarDecl(name, varType, init)


    # for_loop_range:
	# FOR ID COMMA ID COLON_ASSIGN RANGE expression1 statement_block;
    # idx: Id, value: Id, arr: Expr, loop: Block
    def visitFor_loop_range(self, ctx:MiniGoParser.For_loop_rangeContext):
        idx = Id(ctx.ID(0).getText())
        value = Id(ctx.ID(1).getText())
        arr = self.visit(ctx.expression1())
        loop = self.visit(ctx.statement_block())
        return ForEach(idx, value, arr, loop)


    # Visit a parse tree produced by MiniGoParser#break_statement.
    def visitBreak_statement(self, ctx:MiniGoParser.Break_statementContext):
        return Break()


    # Visit a parse tree produced by MiniGoParser#continue_statement.
    def visitContinue_statement(self, ctx:MiniGoParser.Continue_statementContext):
        return Continue()


    # call_statement: function_method_call_stmt SEMI;
    def visitCall_statement(self, ctx:MiniGoParser.Call_statementContext):
        return self.visit(ctx.function_method_call_stmt())


    # function_method_call_stmt:
	# optional_instance_stmt ID LPAREN optional_list_expression RPAREN;
    # receiver: Expr, metName: str, args: List[Expr]
    def visitFunction_method_call_stmt(self, ctx:MiniGoParser.Function_method_call_stmtContext):
        receiver = self.visit((ctx.optional_instance_stmt()))
        metName = ctx.ID().getText()
        args = self.visit(ctx.optional_list_expression())
        if receiver is None:
            return FuncCall(metName, args)
        return MethCall(receiver, metName, args)
            


    # optional_instance_stmt: expression7 DOT |;
    def visitOptional_instance_stmt(self, ctx:MiniGoParser.Optional_instance_stmtContext):
        if ctx.expression7():
            return self.visit(ctx.expression7())
        return None


    # return_statement: RETURN expression1? SEMI;
    def visitReturn_statement(self, ctx:MiniGoParser.Return_statementContext):
        expr = self.visit(ctx.expression1()) if ctx.expression1() else None
        return Return(expr)

    

