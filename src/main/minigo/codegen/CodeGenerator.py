'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod
from functools import reduce


class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value,isStatic=True):
        #value: String
        self.isStatic = isStatic
        self.value = value

class ClassType(Type):
    def __init__(self, name):
        #value: Id
        self.name = name

    
class CodeGenerator(BaseVisitor,Utils):
    def __init__(self):
        self.className = "MiniGoClass"
        self.astTree = None
        self.path = None
        self.emit = None
        self.first_time = True
        self.clinit = False
        self.take_func = True
        self.list_struct = []
        self.take_struct = False
        self.struct = None
        self.visitMethod = False
        self.funcCall = False
        
    def initValue(self, type_, o):
        if type(type_) is IntType:
            return IntLiteral(0)
        elif type(type_) is FloatType:
            return FloatLiteral(0.0)
        elif type(type_) is StringType:
            return StringLiteral("\"\"")
        elif type(type_) is BoolType:
            return BooleanLiteral(False)
            
        # elif type(type_) is StructType:
            

    def init(self):
        mem = [Symbol("putInt",MType([IntType()],VoidType()),CName("io",True)),
                Symbol("putIntLn",MType([IntType()],VoidType()),CName("io",True)),
                Symbol("putFloat",MType([FloatType()],VoidType()),CName("io",True)),
                Symbol("putFloatLn",MType([FloatType()],VoidType()),CName("io",True)),
                Symbol("putString",MType([StringType()],VoidType()),CName("io",True)),
                Symbol("putStringLn",MType([StringType()],VoidType()),CName("io",True)),
                Symbol("putBool",MType([BoolType()],VoidType()),CName("io",True)),
                Symbol("putBoolLn",MType([BoolType()],VoidType()),CName("io",True)),
                Symbol("putLn",MType([],VoidType()),CName("io",True)),
                
                Symbol("getInt",MType([],IntType()),CName("io",True)),
                Symbol("getFloat",MType([],FloatType()),CName("io",True)),
                Symbol("getString",MType([],StringType()),CName("io",True)),
                Symbol("getBool",MType([],BoolType()),CName("io",True)),
                ]
        return mem

    def gen(self, ast, dir_):
        gl = self.init()
        self.astTree = ast
        self.path = dir_
        self.emit = Emitter(dir_ + "/" + self.className + ".j")
        self.visit(ast, gl)
       
        
    def emitObjectInit(self):
        frame = Frame("<init>", VoidType())  
        self.emit.printout(self.emit.emitMETHOD("<init>", MType([], VoidType()), False, frame))  # Bắt đầu định nghĩa phương thức <init>
        frame.enterScope(True)  
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))  # Tạo biến "this" trong phương thức <init>
        
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))  
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))  
    
        
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))  
        self.emit.printout(self.emit.emitENDMETHOD(frame))  
        frame.exitScope()  
        
    def emitStructInit(self, ast) :
        frame = Frame("<init>", VoidType())
        self.emit.printout(self.emit.emitMETHOD("<init>", MType([], VoidType()), False, frame))
        frame.enterScope(True)
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(ast.name), frame.getStartLabel(), frame.getEndLabel(), frame))
        
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        self.emit.printout(self.emit.emitREADVAR("this", ClassType(ast.name), 0, frame))  
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))  
        
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))  
        self.emit.printout(self.emit.emitENDMETHOD(frame))  
        frame.exitScope()  
        
    def emitObjectCInit(self, ast, env) :
        frame = Frame("<clinit>", VoidType())  
        self.emit.printout(self.emit.emitMETHOD("<clinit>", MType([], VoidType()), True, frame))  # Bắt đầu định nghĩa phương thức <init>
        frame.enterScope(True)  
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
    
        env['frame'] = frame
        
        self.visit(Block([
            Assign(Id(item.varName) if isinstance(item, VarDecl) else Id(item.conName),
            item.varInit if isinstance(item, VarDecl) else item.iniExpr)
            for item in ast.decl if (isinstance(item, VarDecl) and type(item.varType) is not ArrayType ) or (isinstance(item, ConstDecl))
            # for item in ast.decl if isinstance(item, (VarDecl, ConstDecl))
        ]), env)
        
        for item in ast.decl :
            if isinstance(item, VarDecl) :
                if isinstance(item.varType, ArrayType) :
                    self.visit(ArrayType(item.varType.dimens, item.varType.eleType), env)
                    tmp = "[" * len(item.varType.dimens)
                    if type(item.varType.eleType) is IntType: tmp += "I"
                    elif type(item.varType.eleType) is FloatType: tmp += "F"
                    elif type(item.varType.eleType) is StringType: tmp += "java/lang/String;"
                    elif type(item.varType.eleType) is BoolType: tmp += "Z"
                    self.emit.printout(self.emit.emitPUTSTATIC(f"{self.className}/{item.varName}", tmp, env['frame']))
        
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))  
        self.emit.printout(self.emit.emitENDMETHOD(frame))  
        frame.exitScope()  

    def visitProgram(self, ast, c):
        for x in ast.decl :
            if isinstance(x, (StructType, InterfaceType)) :
                self.list_struct.append(x)
                
        for struct in self.list_struct:
            if isinstance(struct, InterfaceType):
                struct.methods.sort(key=lambda m: m.name)  # Sort by name

        for y in ast.decl:
            if isinstance(y, MethodDecl):
                name_struct = str(y.recType)[3:-1]
                for s in self.list_struct:
                    if s.name == name_struct:
                        s.methods.append(y)
                        s.methods.sort(key=lambda m: m.fun.name)  # Sort after each insert
                        break
        
        env ={}
        env['env'] = [c]
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        
        env = reduce(lambda a,x: self.visit(x,a) if isinstance(x, FuncDecl) else a, ast.decl, env) # for name func, var, const
        self.take_func = False
        
        env = reduce(lambda a,x: self.visit(x,a) if not isinstance(x,(StructType, InterfaceType, MethodDecl)) else a, ast.decl, env) # for name func, var, const
        
        self.emitObjectInit()
        self.first_time = False

        env = reduce(lambda a,x: self.visit(x,a) if isinstance(x, FuncDecl) else a, ast.decl, env) # for func body

        ## For assign value
        self.clinit = True
        env_temp = env.copy()
        self.emitObjectCInit(ast, env_temp)
        self.clinit = False
        
        self.emit.printout(self.emit.emitEPILOG())
        env_temp['visitStruct'] = True
        
        # for x in ast.decl :
        #     if x is isinstance(x, (StructType, InterfaceType)) :
        #         self.emit = Emitter(self.path + "/" + x.name)
        #         self.visit(x, env_temp)
        
        for x in self.list_struct :
            self.emit = Emitter(self.path + "/" + x.name + ".j")
            self.visit(x, env_temp)
        
        return env
    
    def checkType(self, lhs, rhs, list_type_permission) :
        return None
    
    def visitStructType(self, ast, o):
        if o is None or 'visitStruct' not in o :
            return o    
        
        self.emit.printout(self.emit.emitPROLOG(ast.name, "java.lang.Object"))
        
        # for x in self.list_struct :
        #     if isinstance(x, StructType) :
        #         ### find struct object
        #         for y in x.methods :
        #             for interface in self.list_struct:
        #                 if isinstance(interface, InterfaceType) :
        
        # lst_methods = self.list_struct[ast.name].methods
        lst_methods = ast.methods
        lst_interface = [x for x in self.list_struct if isinstance(x, InterfaceType)]
        if not lst_interface:
            lst_interface = [] 
        if lst_interface != [] :
            lst_implement = {}
            founded = False
            for each_meth in lst_methods :
                for interface_ in lst_interface :
                    for each_proto in interface_.methods :
                        if each_meth.fun.name == each_proto.name and each_meth.fun.retType == each_proto.retType and len(each_meth.fun.params) == len(each_proto.params) :
                            lst_implement[interface_.name] = 1
                            founded = True
                            break
                    if founded == True : break
                founded = False
        
        for x in lst_implement :
            self.emit.printout(".implements " + x)
            
        for item in ast.elements :
            self.emit.printout(self.emit.emitFIELD(item[0], item[1], False))

        env = o.copy()
        env['isLeft'] = True
        
        self.struct = ast.name
        
        self.visit(MethodDecl(None, Id(ast.name), FuncDecl("<init>", 
                                                   [ParamDecl(item[0], item[1]) for item in ast.elements], 
                                                   VoidType(), 
                                                    Block([Assign(FieldAccess(StringLiteral("this"), item[0]), self.initValue(item[1], o)) for x in ast.elements]))), env)

        self.struct = None
        
        self.emitStructInit(ast)
        
        for item in ast.methods : self.visit(item, o)
        
        self.emit.printout(self.emit.emitEPILOG())
        return o     
        
    def visitInterfaceType(self, ast, o):
        self.emit.printout(self.emit.emitPROLOG(ast.name + "!", "java.lang.Object"))
        for item in ast.methods:
            mtype = MType(list(map(lambda x : x , item.params)), item.retType)
            self.emit.printout(self.emit.emitMETHOD(item.name, mtype, False, True))  ## Cheat at here as frame not use
            # self.visit()
            self.emit.printout(self.emit.emitENDMETHOD(True))
        self.emit.printout(self.emit.emitEPILOG())
        return o
    
    def visitMethodDecl(self, ast, o):
        self.function = ast.fun
        frame = Frame(ast.fun.name, ast.fun.retType)
        
        mtype = MType(list(map(lambda x: x.parType, ast.fun.params)), ast.fun.retType)
        
        self.struct = str(ast.recType)[3:-1]
        
        env = o.copy()
        env['frame'] = frame
        self.emit.printout(self.emit.emitMETHOD(ast.fun.name, mtype, False, frame))
        frame.enterScope(True)
        
        name_str = str(ast.recType)[3:-1]
        
        o['env'][0].append(Symbol(ast.receiver, Id(name_str), None))
        
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(name_str), frame.getStartLabel(), frame.getEndLabel(), frame))
        
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        
        if ast.receiver is None :
            self.emit.printout(self.emit.emitREADVAR("this", ast.recType, 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
            
        env['env'] = [[]] + env['env']
        
        env = reduce(lambda acc, e: self.visit(e, acc), ast.fun.params, env)
        
        self.visitMethod = True
        self.visit(ast.fun.body, env)
        
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(ast.fun.retType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
        
        self.struct = None
        
        return o
    
    def visitFieldAccess(self, ast, o):
        temp_o = o.copy()
        temp_o['receiver'] = True
        # _ , typ = self.visit(ast.receiver, temp_o)
        o['frame'].push()
        obj_ = None
        if isinstance(ast.receiver, Id) :
            name_str = str(ast.receiver)[3:-1]
        else : name_str = ast.receiver.value
        if name_str == "this" :
            # check_this = True
            name_str = self.struct
        else : 
            # print(name_str)
            # print(o['env'][0][0])
            sym = next(filter(lambda x: x.name == name_str, o['env'][0]),None)
            if (sym is None) :
                name_str = self.struct
            else :
                obj_ = sym 
                name_str = str(sym.mtype)[3:-1]
        tuple_field = tuple
        for x in self.list_struct :
            if isinstance(x, StructType) :
                if x.name == name_str :
                    tuple_field = [t for t in x.elements if t[0] == ast.field]
        # tuple_field = [t for t in self.list_struct[typ].elements if t[0] == ast.field]
        ### typ in getfield is Id(...) or just ...
        t = tuple_field
        if 'isLeft' in o and o['isLeft'] == True :
            self.emit.printout(self.emit.emitPUTFIELD(f"{name_str}/{ast.field}", tuple_field[0][1], o['frame']))
        else : 
            if self.visitMethod == True :
                self.emit.printout(self.emit.emitREADVAR("this",StringType(), 0, o['frame']))
            else : 
                self.emit.printout(self.emit.emitREADVAR("", StringType(), obj_.value.value, o['frame']))
            self.emit.printout(self.emit.emitGETFIELD(f"{name_str}/{ast.field}", tuple_field[0][1], o['frame']))
        return "FieldAccess", tuple_field[0][1]
    
    def visitMethCall(self, ast, o):
        # temp_o = o.copy()
        # temp_o['receiver'] = True
        self.funcCall = True
        _ , typ = self.visit(ast.receiver, o)
        
        if isinstance(typ, Id) :
            # typ = self.list_struct[str(typ)[3:-1]]
            t = str(typ)[3:-1]
            for x in self.list_struct :
                if x.name == t :
                    typ = x
                    break
        
        is_stmt = o.pop("stmt", False)
        
        env = o.copy()
        
        env['isLeft'] = False
        for x in ast.args:
            self.visit(x, env)[0] 
            
        type_re = None
        
        if isinstance(typ, StructType):
            # method = [x for x in typ.methods if x.fun.name == ast.metName]
            for tmp in typ.methods:
                if tmp.fun.name == ast.metName : 
                    method = tmp
                    break
            mtype = MType(list(map(lambda x : x.parType, method.fun.params)), method.fun.retType)
            type_re = method.fun.retType
            ### lexeme here is ast.metName right ???
            o['frame'].push()
            self.emit.emitINVOKEVIRTUAL(ast.metName, mtype, o['frame'])
            
        elif isinstance(typ, InterfaceType) :
            # prototype = [x for x in typ.methods if x.name == ast.metName]
            for tmp in typ.methods :
                if tmp.name == ast.metName :
                    prototype = tmp
                    break
            mtype = MType([list(map(lambda x : x, prototype.params))], prototype.retType)
            type_re = prototype.retType
            
            ### lexeme here is ast.metName right ???
            o['frame'].push()
            self.emit.emitINVOKEVIRTUAL(ast.metName, mtype, o['frame'])
        
        self.funcCall = False
        
        return "MethodCall", type_re
    
    def visitStructLiteral(self, ast, o):
        self.emit.printout(self.emit.emitNEW(ast.name, o['frame']))
        self.emit.printout(self.emit.emitDUP(o['frame']))
        
        list_type = []
        
        for item in ast.elements:
            c, t = self.visit(item[1], o)
            list_type.append(t)
            
        ### handle auto init: a := Person{};
        if o is None or len(ast.elements) == 0 :
            for x in self.list_struct :
                if x.name == ast.name : struct_obj = x
            # struct_obj = self.list_struct[ast.name]
            # list_type = list(map(lambda x : x[1], struct_obj.elements))
            for x in struct_obj.elements :
                if (type(x[1]) is IntType) : self.emit.printout(self.emit.emitPUSHCONST(0, IntType(), o['frame']))
                elif (type(x[1]) is FloatType) : self.emit.printout(self.emit.emitPUSHCONST(0.0, FloatType(), o['frame']))
                elif (type(x[1]) is BoolType) : self.emit.printout(self.emit.emitPUSHCONST(False, BoolType(), o['frame']))
                elif (type(x[1]) is StringType) : self.emit.printout(self.emit.emitPUSHCONST("", StringType(), o['frame']))
                else:
                    ### x[0] == name
                    ### x[1].elements where x[1] is StructType, so access the
                    self.visit(StructLiteral(x[0], []))
                list_type.append(x[1])
            
        mtype = MType(list_type, VoidType())
        self.emit.printout(self.emit.emitINVOKESPECIAL(o['frame'], f"{ast.name}/<init>",mtype))
        
        # return "StructLiteral", StructType(ast.name, self.list_struct[ast.name].elements, self.list_struct[ast.name].methods, self.list_struct[ast.name].implements)
        return "StructLiteral", Id(ast.name)
        
    def visitNilLiteral(self, ast, o) :
        self.emit.printout(self.emit.emitPUSHNULL())
        return "NilLiteral", Id("")
    
    def visitPrototype(self, ast, o):
        return o

    def visitFuncDecl(self, ast, o):
        # if self.first_time == True : return o
        frame = Frame(ast.name, ast.retType)
        isMain = ast.name == "main"
        if isMain:
            mtype = MType([ArrayType([None],StringType())], VoidType())
        else:
            mtype = MType(list(map(lambda x: x.parType, ast.params)), ast.retType)
        if self.take_func == True : 
            o['env'][0].append(Symbol(ast.name, mtype, CName(self.className)))
            return o
        if self.first_time == True : 
            return o

        env = o.copy()
        env['frame'] = frame
        self.emit.printout(self.emit.emitMETHOD(ast.name, mtype,True, frame))
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        env['env'] = [[]] + env['env']
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType([None],StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            env = reduce(lambda acc,e: self.visit(e,acc), ast.params,env)
        self.visit(ast.body,env)
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(ast.retType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame)) 
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
        return o
    
    def visitVarDecl(self, ast, o):
        ## Handle case there is only init
        if self.clinit == True : return o
        # if self.first_time == True and (type(ast.varType) is ArrayType or type(ast.varInit) is ArrayLiteral) : return o
        if ast.varInit and (ast.varType is None) :
            value, typ = self.visit(ast.varInit, o)
            ast.varType = typ
            
        dim_arr = None    
        if type(ast.varType) is ArrayType : 
            dim_arr, typ_ = self.visit(ast.varType, o)  
            
        if ast.varInit is None :
            ast.varInit = self.initValue(ast.varType, o)
        
        ## Case global scope
        if 'frame' not in o:
            if self.first_time != True : return o
            o['env'][0].append(Symbol(ast.varName, ast.varType, CName(self.className)))
            # self.emit.printout(self.emit.emitATTRIBUTE(ast.varName, ast.varType, True, False, str(ast.varInit.value) if ast.varInit else None))
            if isinstance(ast.varType, Id) : 
                tm = ClassType(str(ast.varType)[3:-1])
                self.emit.printout(self.emit.emitATTRIBUTE(ast.varName, tm, True, False, None))
            else : self.emit.printout(self.emit.emitATTRIBUTE(ast.varName, ast.varType if dim_arr is None else dim_arr, True, False, None))
        ## Case local  scope
        else :
            if self.first_time != True :
                frame = o['frame']
                index = frame.getNewIndex()
                o['env'][0].append(Symbol(ast.varName, ast.varType, Index(index)))
                if type(ast.varType) is ArrayType :
                    self.emit.printout(self.emit.emitWRITEVAR(ast.varName, ast.varType, index, frame))
                if isinstance(ast.varType, Id) : 
                    tm = ClassType(str(ast.varType)[3:-1])
                    self.emit.printout(self.emit.emitVAR(index, ast.varName, tm, frame.getStartLabel(), frame.getEndLabel(), frame))
                else : self.emit.printout(self.emit.emitVAR(index, ast.varName, ast.varType if dim_arr is None else dim_arr, frame.getStartLabel(), frame.getEndLabel(), frame))
                if ast.varInit :
                    check = False
                    if type(ast.varInit) is IntLiteral: 
                        self.emit.printout(self.emit.emitPUSHICONST(ast.varInit.value, frame))
                        if type(ast.varType) is FloatType: self.emit.printout(self.emit.emitI2F(frame))
                    elif type(ast.varInit) is FloatLiteral: self.emit.printout(self.emit.emitPUSHFCONST(ast.varInit.value, frame))
                    elif type(ast.varInit) is BooleanLiteral: self.emit.printout(self.emit.emitPUSHICONST(str(ast.varInit.value), frame))
                    elif type(ast.varInit) is StringLiteral: self.emit.printout(self.emit.jvm.emitLDC(ast.varInit.value))
                    elif type(ast.varInit) is ArrayLiteral : 
                        # self.emit.printout(self.emit.emitREADVAR(ast.varName, StringType(), index, frame))
                        if type(ast.varInit.value[0]) is list : check = True 
                        else : self.visit(ast.varInit, o)
                    # else : handle array, struct and interface here
                    elif type(ast.varInit) is StructLiteral : 
                        self.visit(ast.varInit, o)
                    if check == False : self.emit.printout(self.emit.emitWRITEVAR(ast.varName, ast.varType, index, frame))
        return o

    
    def visitConstDecl(self, ast, o):
        if self.clinit == True : return o
        if ast.conType is None:
            code, typ = self.visit(ast.iniExpr, o)
            ast.conType = typ

        if 'frame' not in o:
            if self.first_time != True : return o
        # if o['frame'] is not None and o['frame'].name == 'global':
            o['env'][0].append(Symbol(ast.conName, ast.conType, CName(self.className)))
            # self.emit.printout(self.emit.emitATTRIBUTE(ast.conName, ast.conType, True, True, str(ast.iniExpr.value)))
            self.emit.printout(self.emit.emitATTRIBUTE(ast.conName, ast.conType, True, True, None))
        else:
            if self.first_time != True :
                frame = o['frame']
                index = frame.getNewIndex()
                o['env'][0].append(Symbol(ast.conName, ast.conType, Index(index)))
                self.emit.printout(self.emit.emitVAR(index, ast.conName, ast.conType, frame.getStartLabel(), frame.getEndLabel(), frame))
                self.emit.printout(self.emit.emitPUSHCONST(ast.iniExpr.value, ast.iniExpr, frame))
                self.emit.printout(self.emit.emitWRITEVAR(ast.conName, ast.conType, index, frame))
        return o
    
    def visitFuncCall(self, ast, o):
        self.funcCall = True
        sym = next(filter(lambda x: x.name == ast.funName, o['env'][-1]),None)
        if self.first_time == True : return ast.funName, sym.mtype.rettype
        env = o.copy()
        env['isLeft'] = False
        # [self.visit(x, env)[0] for x in ast.args] ## Delete self.emit.printout() at here
        for x in ast.args:
            # if isinstance(x, StringLiteral) : env['frame'].push()
            # self.emit.printout(str(env['frame'].push()))
            self.visit(x, env)[0] 
        
        self.emit.printout(self.emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}",sym.mtype, o['frame']))
        self.funcCall = False
        return ast.funName, sym.mtype.rettype
    
    def visitBlock(self, ast, o):
        env = o.copy()
        env['env'] = [[]] + env['env']
        env['frame'].enterScope(False)
        self.emit.printout(self.emit.emitLABEL(env['frame'].getStartLabel(), env['frame']))
        # env = reduce(lambda acc,e: self.visit(e,acc),ast.member,env)
        for e in ast.member:
            if isinstance(e, (MethCall, FuncCall, Return)) :
                self.visit(e, env)
            else : env = self.visit(e, env)

        self.emit.printout(self.emit.emitLABEL(env['frame'].getEndLabel(), env['frame']))
        env['frame'].exitScope()
        return o
    
    def visitBinaryOp(self, ast, o):
        if 'BinaryOp' in o and o['BinaryOp'] == 2 and 'BinaryOp_new' in o and o['BinaryOp_new'] == 1:
            self.emit.printout(self.emit.emitI2F(o['frame']))
        env = o.copy()
        env['BinaryOp'] = 1 ## first check
        ## env['BinaryOp'] = 2 when left is Int and Right is Float => I2F first then Right
        ## env['BinaryOp'] = 3 when left is Float and Right is Int => Right first then I2F
        v_left, type_left = self.visit(ast.left, env)
        if type(type_left) is IntType : env['BinaryOp'] = 2
        elif type(type_left) is FloatType : env['BinaryOp'] = 3
        v_right, type_right = self.visit(ast.right, env)
        if type(type_right) is FloatType :
            env['BinaryOp_new'] = 1
        # REMEMBER TO PRINT WHEN Traverse EACH type
        o['frame'].push()
        o['frame'].push()
        o['frame'].push()
        
        typ_re = None
        ### Case: Int and Int, Int and Float, Float and Int, Float and Float  
        if (type(type_left) is IntType and type(type_right) is IntType):
            if ast.op in ["+" , "-"] :
                self.emit.printout(self.emit.emitADDOP(ast.op, type_left, o['frame']))
            elif ast.op in ["*", "/"] :
                self.emit.printout(self.emit.emitMULOP(ast.op, type_left, o['frame']))
            elif ast.op == "%" :
                self.emit.printout(self.emit.emitMOD(o['frame']))
            typ_re = IntType()
            
            if ast.op in [">" , "<" , ">=" , "<=" , "!=" , "=="] :
                self.emit.printout(self.emit.emitREOP(ast.op, type_left, o['frame']))
                typ_re = BoolType()
          
        elif (type(type_left) is FloatType and type(type_right) is FloatType) or (type(type_left) is IntType and type(type_right) is FloatType) or (type(type_left) is FloatType and type(type_right) is IntType) :
            if ast.op in ["+" , "-"] :
                # if (type(type_left) is IntType or type(type_right) is IntType): self.emit.printout(self.emit.emitI2F(o['frame']))
                self.emit.printout(self.emit.emitADDOP(ast.op, FloatType(), o['frame']))
            elif ast.op in ["*", "/"] :
                # if (type(type_left) is IntType or type(type_right) is IntType): self.emit.printout(self.emit.emitI2F(o['frame']))
                self.emit.printout(self.emit.emitMULOP(ast.op, FloatType(), o['frame']))
            typ_re = FloatType()
            
            if ast.op in [">" , "<" , ">=" , "<=" , "!=" , "=="] and type(type_left) is FloatType and type(type_right) is FloatType:
                self.emit.printout(self.emit.emitREOP(ast.op, type_left, o['frame']))
                typ_re = BoolType()
                
        elif type(type_left) is StringType and type(type_right) is StringType :
            if ast.op in [">" , "<" , ">=" , "<=" , "!=" , "=="] :
                self.emit.printout(self.emit.emitREOP(ast.op, type_left, o['frame']))
                typ_re = BoolType()
            elif ast.op == "+" :
                self.emit.printout(self.emit.emitREOP(ast.op, type_left, o['frame']))
                typ_re = StringType()
        
        elif type(type_left) is BoolType and type(type_right) is BoolType :
            if ast.op == "&&" :
                self.emit.printout(self.emit.emitANDOP(o['frame']))
            elif ast.op == "||":
                self.emit.printout(self.emit.emitOROP(o['frame']))
            typ_re = BoolType()
            
        if 'BinaryOp' in o and o['BinaryOp'] == 3 and (type(type_left) is IntType and type(type_right) is IntType):
            self.emit.printout(self.emit.emitI2F(o['frame']))
               
        return "BinaryOp", typ_re 
    
    def visitUnaryOp(self, ast, o):
        v_body, type_body = self.visit(ast.body, o)
        if ast.op == "-" : 
            self.emit.printout(self.emit.emitNEGOP(type_body, o['frame']))
        else :  self.emit.printout(self.emit.emitNOT(type_body, o['frame']))
        return "UnaryOp", type_body
    
    def visitAssign(self, ast, o):
        ### REMEMBER TO HANDLE ISLEFT : lhs, rhs
        ### lhs: Array Cell, Struct Literal, Id
        # if (type(ast.lhs) is Id) : print(str(ast.lhs))
        if isinstance(ast.lhs, ArrayCell) :
            o['isLeft'] = True
            env = o.copy()
            v_left, type_left = self.visit(ast.lhs, env)
            o['isLeft'] = False
            v_right, type_right = self.visit(ast.rhs, o)
            if type(type_left) is FloatType and type(type_right) is IntType:
                self.emit.printout(self.emit.emitI2F(o['frame']))
                
            self.emit.printout(self.emit.emitWRITEVAR2(str(v_left), type_left, o['frame']))
            
        else :
            if isinstance(ast.lhs, Id) :
                env2 = o.copy()
                env2['special_undecl'] = True
                special_undecl, typ = self.visit(ast.lhs, env2)
                
                if special_undecl == True :
                    n = str(ast.lhs)
                    self.visit(VarDecl(n[3:-1], None, ast.rhs), o)
                    return o
            
            o['isLeft'] = False
            v_right, type_right = self.visit(ast.rhs, o)
            
            o['isLeft'] = True
            env = o.copy()
            env['checkvar'] = type(type_right) is IntType
            v_left, type_left = self.visit(ast.lhs, env)
            
        
        # if type(type_left) is FloatType and type(type_right) is IntType :
        #     self.emit.printout(self.emit.emitI2F(o['frame']))
        
        return o
    
    def visitId(self, ast, o):
        sym = next(filter(lambda x: x.name == ast.name, [j for i in o['env'] for j in i]),None)
        
        if sym is None: return True, VoidType()
        if 'special_undecl' in o and o['special_undecl'] == True :
            return False, VoidType()
        if 'isLeft' in o and o['isLeft'] == False :
            if type(sym.value) is Index:
                # return self.emit.emitREADVAR(ast.name, sym.mtype, sym.value.value, o['frame']),sym.mtype
                self.emit.printout(self.emit.emitREADVAR(ast.name, sym.mtype, sym.value.value, o['frame']))
                if 'receiver' in o :
                    return "FieldAccess", ast.name
                return "IsRight", sym.mtype
            else:         
                # return self.emit.emitGETSTATIC(f"{self.className}/{sym.name}",sym.mtype,o['frame']),sym.mtype
                self.emit.printout(self.emit.emitGETSTATIC(f"{self.className}/{sym.name}",sym.mtype,o['frame']))
                if 'receiver' in o :
                    return "FieldAccess", ast.name
                return "IsRight", sym.mtype
        else :
            if type(sym.value) is Index:
                if 'checkvar' in o and o['checkvar'] == True and type(sym.mtype) is FloatType :
                    self.emit.printout(self.emit.emitI2F(o['frame']))
                if self.funcCall != True : self.emit.printout(self.emit.emitWRITEVAR(ast.name, sym.mtype, sym.value.value, o['frame']))
                if 'receiver' in o :
                    return "FieldAccess", ast.name
                return "IsLeft" , sym.mtype
            else :
                if 'checkvar' in o and o['checkvar'] == True and type(sym.mtype) is FloatType :
                    self.emit.printout(self.emit.emitI2F(o['frame']))
                if self.funcCall != True : self.emit.printout(self.emit.emitPUTSTATIC(f"{self.className}/{sym.name}", sym.mtype, o['frame']))
                if 'receiver' in o :
                    return "FieldAccess", ast.name
                return "IsLeft", sym.mtype
            
        
    def visitIntLiteral(self, ast, o):
        if 'frame' not in o: return "None", IntType()
        # return self.emit.emitPUSHICONST(ast.value, o['frame']), IntType()
        self.emit.printout(self.emit.emitPUSHICONST(ast.value, o['frame']))
        if 'BinaryOp' in o and o['BinaryOp'] == 3: 
            self.emit.printout(self.emit.emitI2F(o['frame']))
        return "IntLiteral", IntType()
    
    def visitFloatLiteral(self, ast, o):
        if 'frame' not in o: return "None", FloatType()
        if 'BinaryOp' in o and o['BinaryOp'] == 2: 
            self.emit.printout(self.emit.emitI2F(o['frame']))
        # return self.emit.emitPUSHFCONST(ast.value, o['frame']), FloatType()
        self.emit.printout(self.emit.emitPUSHFCONST(ast.value, o['frame']))
        return "FloatLiteral", FloatType()
    
    def visitBooleanLiteral(self, ast, o):
        if 'frame' not in o: return "None", BoolType()
        # return self.emit.emitPUSHICONST(ast.value, o['frame']), BoolType()
        self.emit.printout(self.emit.emitPUSHICONST(ast.value, o['frame']))
        return "BooleanLiteral", BoolType()
    
    def visitStringLiteral(self, ast, o):
        if 'frame' not in o: return "None", StringType()
        # return self.emit.jvm.emitLDC(ast.value), StringType()
        # frame = o['frame']
        o['frame'].push()
        self.emit.printout(self.emit.jvm.emitLDC(ast.value))
        # o['frame'].pop()

        return "StringLiteral", StringType()
     
###################################################################
###################################################################
###################################################################
    
    
    def visitParamDecl(self, ast, o):
        frame = o['frame']
        index = frame.getNewIndex()
        o['env'][0].append(Symbol(ast.parName, ast.parType, Index(index)))
        self.emit.printout(self.emit.emitVAR(index, ast.parName, ast.parType, frame.getStartLabel(), frame.getEndLabel(), frame))
        return o
    
    def visitReturn(self, ast, o):
        if ast.expr is None: return "None", VoidType()
        
        temp_o = o.copy()
        temp_o['Return'] = True
        temp_o['isLeft'] = False

        val, typ = self.visit(ast.expr, temp_o)
        o['frame'].push()
        self.emit.printout(self.emit.emitRETURN(typ, o['frame']))
        return "return", typ
    
    def visitArrayCell(self, ast, o):
        temp_o = o.copy()
        temp_o['isLeft'] = False
        ### REMEMBER THAT TYP SHOULD RETURN ARRAY LITERAL OBJECT 
        val_expr, typ = self.visit(ast.arr, temp_o)
        
        for idx, item in enumerate(ast.idx) :
            o['frame'].push()
            val = self.visit(item, temp_o)[0]
            if idx != len(ast.idx) - 1:
                self.emit.printout(self.emit.emitALOAD(typ, o['frame']))
        
        type_re = None
        
        if (len(typ.dimens)) == len(ast.idx):
            type_re = typ.eleType
            if not o.get('isLeft'):
                self.emit.printout(self.emit.emitREADVAR2(str(val_expr), type_re, o['frame']))
                o['frame'].pop()
            else :
                if 'checkvar' in o and o['checkvar'] == True and type(type_re) is FloatType:
                    self.emit.printout(self.emit.emitI2F(o['frame']))
                # self.emit.printout(self.emit.emitWRITEVAR2(str(val_expr), type_re, o['frame']))
        else :
            return
        return "ArrayCell", type_re
    
    # def visitArrayLiteral(self, ast, o):
    #     def nestedEach(dim, o) :
    #         if type(dim[0]) is not list :
    #             # o['frame'].push()
    #             self.emit.printout(self.emit.emitPUSHCONST(len(dim), ast.eleType, o['frame']))
    #             if type(ast.eleType) is IntType: lexeme = "int"
    #             elif type(ast.eleType) is FloatType: lexeme = "float"
    #             elif type(ast.eleType) is BoolType: lexeme = "boolean"
    #             elif type(ast.eleType) is StringType: lexeme = "java/lang/String"
    #             self.emit.printout(self.emit.emitMULTIANEWARRAY(1, ast.eleType, lexeme, o['frame']))
    #             for idx, item in enumerate(dim):
    #                 self.emit.printout(self.emit.emitDUP(o['frame']))
    #                 self.emit.printout(self.emit.emitPUSHCONST(idx, IntType(), o['frame']))
    #                 o['isLeft'] = False
    #                 self.visit(item, o)
    #                 self.emit.printout(self.emit.emitASTORE(ast.eleType, o['frame']))
    #             return "ArrayLiteral", ArrayType(ast.dimens, ast.eleType)
        
    #     if type(ast.value[0]) is not list: return nestedEach(ast.value, o)
    #     else :
    
    # def visitArrayLiteral(self, ast, o):
    #     def handleNestedArray(dim, dimCount, eleType, frame):
    #         size = len(dim)
    #         self.emit.printout(self.emit.emitPUSHCONST(size, IntType(), frame))

    #         if dimCount == 1:
    #             # Base case: 1D array
    #             if isinstance(eleType, IntType): lexeme = "int"
    #             elif isinstance(eleType, FloatType): lexeme = "float"
    #             elif isinstance(eleType, BoolType): lexeme = "boolean"
    #             elif isinstance(eleType, StringType): lexeme = "java/lang/String"
    #             self.emit.printout(self.emit.emitMULTIANEWARRAY(1, eleType, lexeme, frame))
    #             for idx, item in enumerate(dim):
    #                 # self.emit.printout("check 1\n")
    #                 self.emit.printout(self.emit.emitDUP(frame))
    #                 self.emit.printout(self.emit.emitPUSHCONST(idx, IntType(), frame))
    #                 o['isLeft'] = False

    #                 for sub in item :
    #                     self.visit(sub, o)
    #                 self.emit.printout(self.emit.emitASTORE(eleType, frame))
    #         else:
    #             # Recursive case: nested arrays
    #             # self.emit.printout(self.emit.emitANEWARRAY("[{}{}".format("[" * (dimCount - 1), "I" if isinstance(eleType, IntType) else "F" if isinstance(eleType, FloatType) else "Z" if isinstance(eleType, BoolType) else "Ljava/lang/String;"), frame))
    #             if isinstance(eleType, IntType): lexeme = "int"
    #             elif isinstance(eleType, FloatType): lexeme = "float"
    #             elif isinstance(eleType, BoolType): lexeme = "boolean"
    #             elif isinstance(eleType, StringType): lexeme = "java/lang/String"
    #             self.emit.printout(self.emit.emitMULTIANEWARRAY(1, eleType, lexeme, frame))
                
    #             for idx, sub in enumerate(dim):
    #                 self.emit.printout(self.emit.emitDUP(frame))
    #                 self.emit.printout(self.emit.emitPUSHCONST(idx, IntType(), frame))
    #                 # self.emit.printout("check 2\n")
    #                 handleNestedArray(sub, dimCount - 1, eleType, frame)  # recursively build sub-array
    #                 # self.emit.printout("check 3\n")
    #                 self.emit.printout(self.emit.emitASTORE(StringType(), frame))

    #     dims = ast.dimens
    #     eleType = ast.eleType
    #     frame = o['frame']
    #     handleNestedArray(ast.value, len(dims), eleType, frame)
    #     return "ArrayLiteral", ArrayType(dims, eleType)

    
    def visitArrayType(self, ast, o):
        if 'frame' not in o :
            # if len(ast.dimens) == 1 :
                tmp = "[" * len(ast.dimens)
                if type(ast.eleType) is IntType: tmp += "I"
                elif type(ast.eleType) is FloatType: tmp += "F"
                elif type(ast.eleType) is StringType: tmp += "java/lang/String;"
                elif type(ast.eleType) is BoolType: tmp += "Z"
                return tmp, ArrayType(ast.dimens, ast.eleType)
        
        temp_o = o.copy()
        temp_o['isLeft'] = False
        if len(ast.dimens) == 1 :
            self.visit(ast.dimens[0], temp_o)
            o['frame'].push()
            if type(ast.eleType) is IntType :
                self.emit.printout(self.emit.emitMULTIANEWARRAY(1, ast.eleType, "int", o['frame']))
            elif type(ast.eleType) is FloatType:
                self.emit.printout(self.emit.emitMULTIANEWARRAY(1, ast.eleType, "float", o['frame']))
            elif type(ast.eleType) is BoolType:
                self.emit.printout(self.emit.emitMULTIANEWARRAY(1, ast.eleType, "boolean", o['frame']))
            elif type(ast.eleType) is StringType:
                self.emit.printout(self.emit.emitMULTIANEWARRAY(1, ast.eleType, "java/lang/String", o['frame']))
            return None, ArrayType(ast.dimens, ast.eleType)
        else :
            for x in ast.dimens:
                self.visit(x, temp_o)
                o['frame'].push()
            tmp = "[" * len(ast.dimens)
            if type(ast.eleType) is IntType : tmp += "I"
            elif type(ast.eleType) is FloatType : tmp += "F"
            elif type(ast.eleType) is BoolType : tmp += "Z"
            elif type(ast.eleType) is StringType : tmp += "java/lang/String;"

            self.emit.printout(self.emit.emitMULTIANEWARRAY(len(ast.dimens), ast.eleType, tmp, o['frame']))
            return tmp , ArrayType(ast.dimens, ast.eleType)
    
    def visitBreak(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(o['breakLabel'], o['frame']))
        return o

    def visitContinue(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(o['continueLabel'], o['frame']))
        return o

    def visitIf(self, ast, o):
        frame = o['frame']
        env = o.copy()
        env['isLeft'] = False
        falseLabel = frame.getNewLabel()
        endLabel = frame.getNewLabel()
        self.visit(ast.expr, env)
        
        self.emit.printout(self.emit.emitIFFALSE(falseLabel, frame))
        
        self.visit(ast.thenStmt, o)
        self.emit.printout(self.emit.emitGOTO(endLabel, frame))
        
        self.emit.printout(self.emit.emitLABEL(falseLabel, frame))
        if ast.elseStmt: self.visit(ast.elseStmt, o)
        
        self.emit.printout(self.emit.emitLABEL(endLabel, frame))
        return o
    
    def visitForBasic(self, ast, o):
        frame = o['frame']
        env = o.copy()
        env['isLeft'] = False

        # Generate labels
        condLabel = frame.getNewLabel()
        bodyLabel = frame.getNewLabel()
        endLabel = frame.getNewLabel()

        # Set break/continue targets for nested visitBreak/visitContinue
        env['continueLabel'] = condLabel
        env['breakLabel'] = endLabel

        self.emit.printout(self.emit.emitLABEL(condLabel, frame))  # loop condition label
        self.visit(ast.cond, env)  # visit the loop condition expression

        self.emit.printout(self.emit.emitIFFALSE(endLabel, frame))  # if false, jump to end
        self.emit.printout(self.emit.emitLABEL(bodyLabel, frame))   # loop body label

        self.visit(ast.loop, env)  # loop body block

        self.emit.printout(self.emit.emitGOTO(condLabel, frame))    # jump back to condition
        self.emit.printout(self.emit.emitLABEL(endLabel, frame))    # end of loop

        return o

    
    def visitForStep(self, ast, o):
        frame = o['frame']
        env = o.copy()
        env['isLeft'] = False
        
        startLabel = frame.getNewLabel()  # condition check
        updateLabel = frame.getNewLabel()  # update step
        endLabel = frame.getNewLabel()  # loop exit

        # Set labels for break and continue
        env['continueLabel'] = updateLabel
        env['breakLabel'] = endLabel

        # 1. Emit initialization: i := 0
        self.visit(ast.init, env)

        # 2. Condition check
        self.emit.printout(self.emit.emitLABEL(startLabel, frame))
        self.visit(ast.cond, env)  # result of i < 10 should be on stack
        self.emit.printout(self.emit.emitIFFALSE(endLabel, frame))  # if false, break

        # 3. Loop body
        self.visit(ast.loop, env)

        # 4. Update step (i += 1)
        self.emit.printout(self.emit.emitLABEL(updateLabel, frame))
        self.visit(ast.upda, env)

        # 5. Jump to condition check
        self.emit.printout(self.emit.emitGOTO(startLabel, frame))

        # 6. End of loop
        self.emit.printout(self.emit.emitLABEL(endLabel, frame))
        return o
    
    # def visitArrayLiteral(self, ast, o) :
    #     self.visit(ast.dimens, o)    ## dimension of array literal for example: [1][2]
    #     self.visit(ast.eleType, o)   ## type of this array, note that the array just have primitive type: string, int, float, boolean
    #     self.visit(ast.value, o)     ## value of array literal in format {}, such as [2][2] will have value {{1,2},{3,4}}

    # def visitArrayLiteral(self, ast, o):
    #     frame = o['frame']
    #     eleType = ast.eleType  # assume already parsed as IntType, etc.
    #     dimenVals = ast.dimens  # [2,2] or more
    #     values = ast.value      # nested lists: [[1,2],[3,4]]

    #     # Step 1: Allocate the array (iconst_2, iconst_2, multianewarray)
    #     for dim in dimenVals:
    #         self.emit.printout(self.emit.emitPUSHICONST(dim, frame))
    #     # self.emit.printout(self.emit.emitMULTIANEWARRAY(dim, ArrayType(dimenVals, eleType), len(dimenVals), frame))

    #     self.emit.printout(
    #         self.emit.emitMULTIANEWARRAY(
    #             len(dimenVals),                          # number of dimensions (e.g., 2)
    #             eleType,                                 # element type (e.g., IntType)
    #             str(ArrayType(dimenVals, eleType)),      # lexeme: JVM array type string (e.g., "[[I")
    #             frame
    #         )
    #     )

    #     # Step 2: Store to a local variable
    #     idx = frame.getNewIndex()
    #     # self.emit.printout(self.emit.emitASTORE(idx, frame))
    #     self.emit.printout(self.emit.emitWRITEVAR("", StringType(), idx, frame))

    #     # Step 3: Generate assignments
    #     for i in range(len(values)):
    #         for j in range(len(values[i])):
    #             val = values[i][j]

    #             # self.emit.printout(self.emit.emitALOAD(idx, frame))  # load arr
    #             self.emit.printout(self.emit.emitREADVAR("", StringType(), idx, frame))
                
    #             self.emit.printout(self.emit.emitPUSHICONST(i, frame))  # row
                
    #             # self.emit.printout(self.emit.emitAALOAD(frame))         # arr[i]
    #             self.emit.printout(self.emit.emitREADVAR2("", StringType(), frame))
                
    #             self.emit.printout(self.emit.emitPUSHICONST(j, frame))  # column
    #             self.emit.printout(self.emit.emitPUSHICONST(val, frame))  # value
                
    #             # self.emit.printout(self.emit.emitIASTORE(frame))        # arr[i][j] = val
    #             self.emit.printout(self.emit.emitASTORE(ast.eleType, frame))

    #     return "idx", ArrayType(dimenVals, eleType)
    
    
    # def visitArrayLiteral(self, ast, o):
    #     def nested(typ, dat, o, times, duplicate) :
    #         if not isinstance(dat, list):
    #             return self.visit(dat, o)
    #         frame = o['frame']
    #         # self.emit.printout(f"{type(dat[0])}\n")
    #         # self.emit.printout(f"{type(dat[0][0])}\n" if type(dat[0]) is list else "None\n")
            
    #         # if type(dat) is list and type(dat[0]) is list and type(dat[0][0]) is not list :
    #         #     self.emit.printout(self.emit.emitPUSHCONST(len(dat), IntType(), frame))
    #         #     type_ = typ
    #         #     if type(type_) is IntType: lexeme = "int"
    #         #     elif type(type_) is FloatType: lexeme = "float"
    #         #     elif type(type_) is BoolType: lexeme = "boolean"
    #         #     elif type(type_) is StringType: lexeme = "java/lang/String"
    #         #     # if times == 1 :
    #         #     self.emit.printout(self.emit.emitMULTIANEWARRAY(1, type_, lexeme, frame))
    #         #     if duplicate == False : self.emit.printout(self.emit.emitDUP(frame))
            
    #         # self.emit.printout(f"checkvar1 + {times}\n")
    #         if times == 1 :
    #             # self.emit.printout("Check times\n")
    #             self.emit.printout(self.emit.emitPUSHCONST(len(dat), IntType(), frame))
    #         #########################################
    #             # self.emit.printout(f"checkvar1 + {times}\n")
    #             type_ = typ
    #             if type(type_) is IntType: lexeme = "int"
    #             elif type(type_) is FloatType: lexeme = "float"
    #             elif type(type_) is BoolType: lexeme = "boolean"
    #             elif type(type_) is StringType: lexeme = "java/lang/String"
    #             # if times == 1 :
    #             # self.emit.printout(self.emit.emitMULTIANEWARRAY(1, type_, lexeme, frame))
    #             self.emit.printout(self.emit.emitMULTIANEWARRAY(1, type_, lexeme, frame))
    #             if duplicate != False :  self.emit.printout(self.emit.emitDUP(frame))
    #             o['frame'].push()
    #         #########################################
    #             # self.emit.printout(f"checkvar2 + {times}\n")
    #         if not isinstance(dat[0], list):
                
    #             # type_ = typ
    #             # if type(type_) is IntType: lexeme = "int"
    #             # elif type(type_) is FloatType: lexeme = "float"
    #             # elif type(type_) is BoolType: lexeme = "boolean"
    #             # elif type(type_) is StringType: lexeme = "java/lang/String"
    #             # else : return  ### Case struct
    #             # self.emit.printout(self.emit.emitMULTIANEWARRAY(1, type_, lexeme, frame))
    #             if times == 1 :
    #                 for idx, item in enumerate(dat):
    #                     # self.emit.printout(f"in loop + {times}\n")
    #                     if idx != 0 : self.emit.printout(self.emit.emitDUP(frame))
    #                     self.emit.printout(self.emit.emitPUSHCONST(idx, IntType(), frame))
    #                     o['isLeft'] = False
    #                     self.visit(item, o)
    #                     # nested(typ, item, o, times)
    #                     self.emit.printout(self.emit.emitASTORE(ast.eleType, frame))
    #                 if times > 1 : self.emit.printout(self.emit.emitASTORE(StringType(), frame))
    #                 # self.emit.printout(f"haha +{duplicate}\n")
    #                 return "ArrayLiteral", ArrayType([], ast.eleType)
                
                
    #             if type(dat[0]) is list and type(dat[0][0]) is list: nested(typ, dat[1:], o, 2)
    #         # self.emit.printout(f"below loop + {times}\n")
    #         ############
    #         # _ , type_ = nested(typ, dat[0], o, 2)
    #         ###########
    #         # if type(type_) is IntType: lexeme = "int"
    #         # elif type(type_) is FloatType: lexeme = "float"
    #         # elif type(type_) is BoolType: lexeme = "boolean"
    #         # elif type(type_) is StringType: lexeme = "java/lang/String"
    #         # self.emit.printout(self.emit.emitMULTIANEWARRAY(1, type_, lexeme, frame))
                        
    #         for idx, item in enumerate(dat):
    #             # self.emit.printout(f"in loop 2 + {times}\n")
    #             self.emit.printout(self.emit.emitDUP(frame))
    #             self.emit.printout(self.emit.emitPUSHCONST(idx, IntType(), frame))
    #             # self.visit(item, o)
    #             nested(typ, item, o, times, True)
    #             self.emit.printout(self.emit.emitASTORE(StringType(), frame))
    #         return "ArrayLiteral", ArrayType([], ast.eleType)
        
    #     # self.emit.printout(f"{type(ast.value)}\n")
    #     # self.emit.printout(f"{type(ast.value[0])}\n")
    #     # self.emit.printout(f"{type(ast.value[0][0])}\n" if type(ast.value[0]) is list else "None\n")
    #     return nested(ast.eleType, ast.value, o, 1, False)
    
    
    def visitArrayLiteral(self, ast, o):
        def nested(typ, dat, o, times) :
            if not isinstance(dat, list):
                return self.visit(dat, o)
            frame = o['frame']
            # self.emit.printout("checkvar1\n")
            self.emit.printout(self.emit.emitPUSHCONST(len(dat), IntType(), frame))
            # self.emit.printout("checkvar1\n")
            #########################################
            type_ = typ
            if type(type_) is IntType: lexeme = "int"
            elif type(type_) is FloatType: lexeme = "float"
            elif type(type_) is BoolType: lexeme = "boolean"
            elif type(type_) is StringType: lexeme = "java/lang/String"
            self.emit.printout(self.emit.emitMULTIANEWARRAY(1, type_, lexeme, frame))
            self.emit.printout(self.emit.emitDUP(frame))
            #########################################
            
            if not isinstance(dat[0], list):
                
                # type_ = typ
                # if type(type_) is IntType: lexeme = "int"
                # elif type(type_) is FloatType: lexeme = "float"
                # elif type(type_) is BoolType: lexeme = "boolean"
                # elif type(type_) is StringType: lexeme = "java/lang/String"
                # else : return  ### Case struct
                # self.emit.printout(self.emit.emitMULTIANEWARRAY(1, type_, lexeme, frame))
                
                for idx, item in enumerate(dat):
                    if idx != 0 : self.emit.printout(self.emit.emitDUP(frame))
                    self.emit.printout(self.emit.emitPUSHCONST(idx, IntType(), frame))
                    o['isLeft'] = False
                    # self.visit(item, o)
                    nested(typ, item, o, times)
                    self.emit.printout(self.emit.emitASTORE(ast.eleType, frame))
                if times > 1 : self.emit.printout(self.emit.emitASTORE(StringType(), frame))
                return "ArrayLiteral", ArrayType([], ast.eleType) 
            
            _ , type_ = nested(typ, dat[0], o, 2)
            if type(type_) is IntType: lexeme = "int"
            elif type(type_) is FloatType: lexeme = "float"
            elif type(type_) is BoolType: lexeme = "boolean"
            elif type(type_) is StringType: lexeme = "java/lang/String"
            else : return  ### Case struct
            self.emit.printout(self.emit.emitMULTIANEWARRAY(1, type_, lexeme, frame))
            
            for idx, item in enumerate(dat):
                self.emit.printout(self.emit.emitDUP(frame))
                self.emit.printout(self.emit.emitPUSHCONST(idx, IntType(), frame))
                # self.visit(item, o)
                nested(typ, item, o, times)
                self.emit.printout(self.emit.emitASTORE(ast.eleType, frame))
            return "ArrayLiteral", ArrayType([], ast.eleType)
        if type(ast.value[0]) is list :
            return "ArrayLiteral", ArrayType([], ast.eleType)      
        return nested(ast.eleType, ast.value, o, 1)