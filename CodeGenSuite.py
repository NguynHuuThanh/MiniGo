import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_int_literal(self):
        input = """func main() {putInt(5);};"""
        expect = "5"
        self.assertTrue(TestCodeGen.test(input,expect,501))
    def test_local_var(self):
        input = """func main() {var a int = 20;  putInt(a);};"""
        expect = "20"
        self.assertTrue(TestCodeGen.test(input,expect,502))
    def test_gllobal_var(self):
        input = """var a int = 10; func main() { putInt(a);};"""
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,503))
    def test_int_ast(self):
        input = Program([FuncDecl("main",[],VoidType(),Block([FuncCall("putInt", [IntLiteral(25)])]))])
        expect = "25"
        self.assertTrue(TestCodeGen.test(input,expect,504))
    def test_local_var_ast(self):
        input = Program([FuncDecl("main",[],VoidType(),Block([VarDecl("a",IntType(),IntLiteral(500)),FuncCall("putInt", [Id("a")])]))])
        expect = "500"
        self.assertTrue(TestCodeGen.test(input,expect,505))
    def test_global_var_ast(self):  
        input = Program([VarDecl("a",IntType(),IntLiteral(5000)),FuncDecl("main",[],VoidType(),Block([FuncCall("putInt", [Id("a")])]))])
        expect = "5000"
        self.assertTrue(TestCodeGen.test(input,expect,506))

    def test_001(self):
        input = """
func fvoid() {putStringLn("VoTien");}

var global = fint()
func main() {
    fvoid();
    putFloatLn(global + 2.0)

    var local = "a";
    putBoolLn(local <= "b")
    local += "c"
    putStringLn(local)

};

func fint() int {return 1;}
"""
        self.assertTrue(TestCodeGen.test(input,"VoTien\n3.0\ntrue\nac\n",507)) 
    
    def test_002(self):
        input = """
func main() {
    putBoolLn(5.0 > 2.0)
    putBoolLn(5.0 < 2.0)
    putBoolLn(5.0 <= 5.0)
    putBoolLn(5.0 >= 5.0)
    putBoolLn(5.0 == 5.0)
    putBoolLn(5.0 != 5.0)
}
"""
        self.assertTrue(TestCodeGen.test(input,"true\nfalse\ntrue\ntrue\ntrue\nfalse\n",508)) 

    def test_003(self):
        input = """
func main() {
    var a [1] int ;
    a[0] := 1
    putInt(a[0]);
}
    """
        self.assertTrue(TestCodeGen.test(input,"1",509))

    def test_004(self):
        input = """
func main() {
    var a [1][1][1] int  = [1][1][1] int {{{0}}};
    a[0][0][0] := 1
    putInt(a[0][0][0]);
}
    """
        self.assertTrue(TestCodeGen.test(input,"1",510))

    def test_005(self):
        input = """
func main() {
    var a [2] int = [2] int {10, 20};
    putInt(a[0])
}
    """
        self.assertTrue(TestCodeGen.test(input,"10",511))

    def test_006(self):
        input = """
func main() {
    var a [2] int;
    a[0] := 100
    a[1] += a[0] + a[0]
    putInt(a[1])
}
    """
        self.assertTrue(TestCodeGen.test(input,"200",512))
    
    def test_007(self):
        input = """
    var a [2] int;
    var b int;
func main() {
    a[0] := 100
    a[1] += a[0] + a[0]
    putInt(a[1])
}
    """
        self.assertTrue(TestCodeGen.test(input,"200",513))

    def test_008(self):
        input = """
func main() {
    if (true) {
        putBool(true)
    } 
}
    """
        self.assertTrue(TestCodeGen.test(input,"true",514))

    def test_009(self):
        input = """
func main() {
    if (true) {
        putBool(true)
    } else {
        putBool(false)     
    }
}
    """
        self.assertTrue(TestCodeGen.test(input,"true",515))

    def test_010(self):
        input = """
func main() {
    if (false) {
        putBool(true)
    } else {
        putBool(false)     
    }
}
    """
        self.assertTrue(TestCodeGen.test(input,"false",516))

    def test_011(self):
        input = """
func main() {
    var i = 0;
    for i < 3 {
        putInt(i);
        i += 1;
    }
    putInt(i);
}
        """
        self.assertTrue(TestCodeGen.test(input, "0123", 517))

    def test_012(self):
        input = """
func main() {
    var i = 0;
    for i < 5 {
        if (i == 3) {
            break;
        }
        putInt(i);
        i += 1;
    }
    putInt(i);
}
        """
        self.assertTrue(TestCodeGen.test(input, "0123", 518))

    def test_013(self):
        input = """
func main() {
    var i = 0;
    for i < 5 {
        i += 1;
        if (i % 2 == 0) {
            continue;
        }
        putInt(i);
    }
    putInt(i);
}
        """
        self.assertTrue(TestCodeGen.test(input, "1355", 519))
        
    def test_014(self):
        input = """
func fvoid() {putStringLn("VoTien");}

var global = fint()
func main() {
    fvoid();
    putFloatLn(global + 2.0)

    var local = "a";
    putBoolLn(local <= "b")
    local += "c"
    putStringLn(local)

};

func fint() int {return 1;}
"""
        self.assertTrue(TestCodeGen.test(input,"VoTien\n3.0\ntrue\nac\n",600)) 

    def test_015(self):
        input = """
func main() {
    putBoolLn(5.0 > 2.0)
    putBoolLn(5.0 < 2.0)
    putBoolLn(5.0 <= 5.0)
    putBoolLn(5.0 >= 5.0)
    putBoolLn(5.0 == 5.0)
    putBoolLn(5.0 != 5.0)
}
"""
        self.assertTrue(TestCodeGen.test(input,"true\nfalse\ntrue\ntrue\ntrue\nfalse\n",601)) 

    def test_016(self):
        input = """
func main() {
    var a [1] int ;
    a[0] := 1
    putInt(a[0]);
}
    """
        self.assertTrue(TestCodeGen.test(input,"1",602))

    def test_017(self):
        input = """
func main() {
    var a [1][1][1] int  = [1][1][1] int {{{0}}};
    a[0][0][0] := 1
    putInt(a[0][0][0]);
}
    """
        self.assertTrue(TestCodeGen.test(input,"1",603))

    def test_018(self):
        input = """
func main() {
    var a [2] int = [2] int {10, 20};
    putInt(a[0])
}
    """
        self.assertTrue(TestCodeGen.test(input,"10",604))

    def test_019(self):
        input = """
func main() {
    var a [2] int;
    a[0] := 100
    a[1] += a[0] + a[0]
    putInt(a[1])
}
    """
        self.assertTrue(TestCodeGen.test(input,"200",605))
    
    def test_020(self):
        input = """
    var a [2] int;
    var b int;
func main() {
    a[0] := 100
    a[1] += a[0] + a[0]
    putInt(a[1])
}
    """
        self.assertTrue(TestCodeGen.test(input,"200",606))

    def test_021(self):
        input = """
func main() {
    if (true) {
        putBool(true)
    } 
}
    """
        self.assertTrue(TestCodeGen.test(input,"true",607))

    def test_022(self):
        input = """
func main() {
    if (true) {
        putBool(true)
    } else {
        putBool(false)     
    }
}
    """
        self.assertTrue(TestCodeGen.test(input,"true",608))

    def test_023(self):
        input = """
func main() {
    if (false) {
        putBool(true)
    } else {
        putBool(false)     
    }
}
    """
        self.assertTrue(TestCodeGen.test(input,"false",609))

    def test_024(self):
        input = """
func main() {
    var i = 0;
    for i < 3 {
        putInt(i);
        i += 1;
    }
    putInt(i);
}
        """
        self.assertTrue(TestCodeGen.test(input, "0123", 610))

    def test_025(self):
        input = """
func main() {
    var i = 0;
    for i < 5 {
        if (i == 3) {
            break;
        }
        putInt(i);
        i += 1;
    }
    putInt(i);
}
        """
        self.assertTrue(TestCodeGen.test(input, "0123", 611))

    def test_026(self):
        input = """
func main() {
    var i = 0;
    for i < 5 {
        i += 1;
        if (i % 2 == 0) {
            continue;
        }
        putInt(i);
    }
    putInt(i);
}
        """
        self.assertTrue(TestCodeGen.test(input, "1355", 612))

    def test_027(self):
        input = """
func fvoid() {putStringLn("VoTien");}

var global = fint()
func main() {
    fvoid();
    putFloatLn(global + 2.0)

    var local = "a";
    putBoolLn(local <= "b")
    local += "c"
    putStringLn(local)

};

func fint() int {return 1;}
"""
        self.assertTrue(TestCodeGen.test(input,"VoTien\n3.0\ntrue\nac\n",613)) 

    def test_028(self):
        input = """
func main() {
    putBoolLn(5.0 > 2.0)
    putBoolLn(5.0 < 2.0)
    putBoolLn(5.0 <= 5.0)
    putBoolLn(5.0 >= 5.0)
    putBoolLn(5.0 == 5.0)
    putBoolLn(5.0 != 5.0)
}
"""
        self.assertTrue(TestCodeGen.test(input,"true\nfalse\ntrue\ntrue\ntrue\nfalse\n",614)) 

    def test_029(self):
        input = """
func main() {
    var a [1] int ;
    a[0] := 1
    putInt(a[0]);
}
    """
        self.assertTrue(TestCodeGen.test(input,"1",615))

    def test_030(self):
        input = """
func main() {
    var a [1][1][1] int  = [1][1][1] int {{{0}}};
    a[0][0][0] := 1
    putInt(a[0][0][0]);
}
    """
        self.assertTrue(TestCodeGen.test(input,"1",616))

    def test_031(self):
        input = """
func main() {
    var a [2] int = [2] int {10, 20};
    putInt(a[0])
}
    """
        self.assertTrue(TestCodeGen.test(input,"10",617))

    def test_032(self):
        input = """
func main() {
    var a [2] int;
    a[0] := 100
    a[1] += a[0] + a[0]
    putInt(a[1])
}
    """
        self.assertTrue(TestCodeGen.test(input,"200",618))
    
    def test_033(self):
        input = """
    var a [2] int;
    var b int;
func main() {
    a[0] := 100
    a[1] += a[0] + a[0]
    putInt(a[1])
}
    """
        self.assertTrue(TestCodeGen.test(input,"200",619))

    def test_034(self):
        input = """
func main() {
    if (true) {
        putBool(true)
    } 
}
    """
        self.assertTrue(TestCodeGen.test(input,"true",620))

    def test_035(self):
        input = """
func main() {
    if (true) {
        putBool(true)
    } else {
        putBool(false)     
    }
}
    """
        self.assertTrue(TestCodeGen.test(input,"true",621))

    def test_036(self):
        input = """
func main() {
    if (false) {
        putBool(true)
    } else {
        putBool(false)     
    }
}
    """
        self.assertTrue(TestCodeGen.test(input,"false",622))

    def test_037(self):
        input = """
func main() {
    var i = 0;
    for i < 3 {
        putInt(i);
        i += 1;
    }
    putInt(i);
}
        """
        self.assertTrue(TestCodeGen.test(input, "0123", 623))

    def test_038(self):
        input = """
func main() {
    var i = 0;
    for i < 5 {
        if (i == 3) {
            break;
        }
        putInt(i);
        i += 1;
    }
    putInt(i);
}
        """
        self.assertTrue(TestCodeGen.test(input, "0123", 624))

    def test_039(self):
        input = """
func main() {
    var i = 0;
    for i < 5 {
        i += 1;
        if (i % 2 == 0) {
            continue;
        }
        putInt(i);
    }
    putInt(i);
}
        """
        self.assertTrue(TestCodeGen.test(input, "1355", 625))

    def test_040(self):
        input = """
func fvoid() {putStringLn("VoTien");}

var global = fint()
func main() {
    fvoid();
    putFloatLn(global + 2.0)

    var local = "a";
    putBoolLn(local <= "b")
    local += "c"
    putStringLn(local)

};

func fint() int {return 1;}
"""
        self.assertTrue(TestCodeGen.test(input,"VoTien\n3.0\ntrue\nac\n",626)) 

    def test_041(self):
        input = """
func main() {
    putBoolLn(5.0 > 2.0)
    putBoolLn(5.0 < 2.0)
    putBoolLn(5.0 <= 5.0)
    putBoolLn(5.0 >= 5.0)
    putBoolLn(5.0 == 5.0)
    putBoolLn(5.0 != 5.0)
}
"""
        self.assertTrue(TestCodeGen.test(input,"true\nfalse\ntrue\ntrue\ntrue\nfalse\n",627)) 

    def test_042(self):
        input = """
func main() {
    var a [1] int ;
    a[0] := 1
    putInt(a[0]);
}
    """
        self.assertTrue(TestCodeGen.test(input,"1",628))

    def test_043(self):
        input = """
func main() {
    var a [1][1][1] int  = [1][1][1] int {{{0}}};
    a[0][0][0] := 1
    putInt(a[0][0][0]);
}
    """
        self.assertTrue(TestCodeGen.test(input,"1",629))

    def test_044(self):
        input = """
func main() {
    var a [2] int = [2] int {10, 20};
    putInt(a[0])
}
    """
        self.assertTrue(TestCodeGen.test(input,"10",630))

    def test_045(self):
        input = """
func main() {
    var a [2] int;
    a[0] := 100
    a[1] += a[0] + a[0]
    putInt(a[1])
}
    """
        self.assertTrue(TestCodeGen.test(input,"200",631))
    
    def test_046(self):
        input = """
    var a [2] int;
    var b int;
func main() {
    a[0] := 100
    a[1] += a[0] + a[0]
    putInt(a[1])
}
    """
        self.assertTrue(TestCodeGen.test(input,"200",632))

    def test_047(self):
        input = """
func main() {
    if (true) {
        putBool(true)
    } 
}
    """
        self.assertTrue(TestCodeGen.test(input,"true",633))

    def test_048(self):
        input = """
func main() {
    if (true) {
        putBool(true)
    } else {
        putBool(false)     
    }
}
    """
        self.assertTrue(TestCodeGen.test(input,"true",634))

    def test_049(self):
        input = """
func main() {
    if (false) {
        putBool(true)
    } else {
        putBool(false)     
    }
}
    """
        self.assertTrue(TestCodeGen.test(input,"false",635))

    def test_050(self):
        input = """
func main() {
    var i = 0;
    for i < 3 {
        putInt(i);
        i += 1;
    }
    putInt(i);
}
        """
        self.assertTrue(TestCodeGen.test(input, "0123", 636))

    def test_051(self):
        input = """
func main() {
    var i = 0;
    for i < 5 {
        if (i == 3) {
            break;
        }
        putInt(i);
        i += 1;
    }
    putInt(i);
}
        """
        self.assertTrue(TestCodeGen.test(input, "0123", 637))

    def test_052(self):
        input = """
func main() {
    var i = 0;
    for i < 5 {
        i += 1;
        if (i % 2 == 0) {
            continue;
        }
        putInt(i);
    }
    putInt(i);
}
        """
        self.assertTrue(TestCodeGen.test(input, "1355", 638))


    def test_053(self):
        input = """
func fvoid() {putStringLn("VoTien");}

var global = fint()
func main() {
    fvoid();
    putFloatLn(global + 2.0)

    var local = "a";
    putBoolLn(local <= "b")
    local += "c"
    putStringLn(local)

};

func fint() int {return 1;}
"""
        self.assertTrue(TestCodeGen.test(input,"VoTien\n3.0\ntrue\nac\n",639)) 

    def test_054(self):
        input = """
func main() {
    putBoolLn(5.0 > 2.0)
    putBoolLn(5.0 < 2.0)
    putBoolLn(5.0 <= 5.0)
    putBoolLn(5.0 >= 5.0)
    putBoolLn(5.0 == 5.0)
    putBoolLn(5.0 != 5.0)
}
"""
        self.assertTrue(TestCodeGen.test(input,"true\nfalse\ntrue\ntrue\ntrue\nfalse\n",640)) 

    def test_055(self):
        input = """
func main() {
    var a [1] int ;
    a[0] := 1
    putInt(a[0]);
}
    """
        self.assertTrue(TestCodeGen.test(input,"1",641))

    def test_056(self):
        input = """
func main() {
    var a [1][1][1] int  = [1][1][1] int {{{0}}};
    a[0][0][0] := 1
    putInt(a[0][0][0]);
}
    """
        self.assertTrue(TestCodeGen.test(input,"1",642))

    def test_057(self):
        input = """
func main() {
    var a [2] int = [2] int {10, 20};
    putInt(a[0])
}
    """
        self.assertTrue(TestCodeGen.test(input,"10",643))

    def test_058(self):
        input = """
func main() {
    var a [2] int;
    a[0] := 100
    a[1] += a[0] + a[0]
    putInt(a[1])
}
    """
        self.assertTrue(TestCodeGen.test(input,"200",644))
    
    def test_059(self):
        input = """
    var a [2] int;
    var b int;
func main() {
    a[0] := 100
    a[1] += a[0] + a[0]
    putInt(a[1])
}
    """
        self.assertTrue(TestCodeGen.test(input,"200",645))

    def test_060(self):
        input = """
func main() {
    if (true) {
        putBool(true)
    } 
}
    """
        self.assertTrue(TestCodeGen.test(input,"true",646))

    def test_061(self):
        input = """
func main() {
    if (true) {
        putBool(true)
    } else {
        putBool(false)     
    }
}
    """
        self.assertTrue(TestCodeGen.test(input,"true",647))

    def test_062(self):
        input = """
func main() {
    if (false) {
        putBool(true)
    } else {
        putBool(false)     
    }
}
    """
        self.assertTrue(TestCodeGen.test(input,"false",648))

    def test_063(self):
        input = """
func main() {
    var i = 0;
    for i < 3 {
        putInt(i);
        i += 1;
    }
    putInt(i);
}
        """
        self.assertTrue(TestCodeGen.test(input, "0123", 649))

    def test_064(self):
        input = """
func main() {
    var i = 0;
    for i < 5 {
        if (i == 3) {
            break;
        }
        putInt(i);
        i += 1;
    }
    putInt(i);
}
        """
        self.assertTrue(TestCodeGen.test(input, "0123", 650))

    def test_065(self):
        input = """
func main() {
    var i = 0;
    for i < 5 {
        i += 1;
        if (i % 2 == 0) {
            continue;
        }
        putInt(i);
    }
    putInt(i);
}
        """
        self.assertTrue(TestCodeGen.test(input, "1355", 651))

    def test_066(self):
        input = """
func fvoid() {putStringLn("VoTien");}

var global = fint()
func main() {
    fvoid();
    putFloatLn(global + 2.0)

    var local = "a";
    putBoolLn(local <= "b")
    local += "c"
    putStringLn(local)

};

func fint() int {return 1;}
"""
        self.assertTrue(TestCodeGen.test(input,"VoTien\n3.0\ntrue\nac\n",652)) 

    def test_067(self):
        input = """
func main() {
    putBoolLn(5.0 > 2.0)
    putBoolLn(5.0 < 2.0)
    putBoolLn(5.0 <= 5.0)
    putBoolLn(5.0 >= 5.0)
    putBoolLn(5.0 == 5.0)
    putBoolLn(5.0 != 5.0)
}
"""
        self.assertTrue(TestCodeGen.test(input,"true\nfalse\ntrue\ntrue\ntrue\nfalse\n",653)) 

    def test_068(self):
        input = """
func main() {
    var a [1] int ;
    a[0] := 1
    putInt(a[0]);
}
    """
        self.assertTrue(TestCodeGen.test(input,"1",654))

    def test_069(self):
        input = """
func main() {
    var a [1][1][1] int  = [1][1][1] int {{{0}}};
    a[0][0][0] := 1
    putInt(a[0][0][0]);
}
    """
        self.assertTrue(TestCodeGen.test(input,"1",655))

    def test_070(self):
        input = """
func main() {
    var a [2] int = [2] int {10, 20};
    putInt(a[0])
}
    """
        self.assertTrue(TestCodeGen.test(input,"10",656))

    def test_071(self):
        input = """
func main() {
    var a [2] int;
    a[0] := 100
    a[1] += a[0] + a[0]
    putInt(a[1])
}
    """
        self.assertTrue(TestCodeGen.test(input,"200",657))
    
    def test_072(self):
        input = """
    var a [2] int;
    var b int;
func main() {
    a[0] := 100
    a[1] += a[0] + a[0]
    putInt(a[1])
}
    """
        self.assertTrue(TestCodeGen.test(input,"200",658))

    def test_073(self):
        input = """
func main() {
    if (true) {
        putBool(true)
    } 
}
    """
        self.assertTrue(TestCodeGen.test(input,"true",659))

    def test_074(self):
        input = """
func main() {
    if (true) {
        putBool(true)
    } else {
        putBool(false)     
    }
}
    """
        self.assertTrue(TestCodeGen.test(input,"true",660))

    def test_075(self):
        input = """
func main() {
    if (false) {
        putBool(true)
    } else {
        putBool(false)     
    }
}
    """
        self.assertTrue(TestCodeGen.test(input,"false",661))

    def test_076(self):
        input = """
func main() {
    var i = 0;
    for i < 3 {
        putInt(i);
        i += 1;
    }
    putInt(i);
}
        """
        self.assertTrue(TestCodeGen.test(input, "0123", 662))

    def test_077(self):
        input = """
func main() {
    var i = 0;
    for i < 5 {
        if (i == 3) {
            break;
        }
        putInt(i);
        i += 1;
    }
    putInt(i);
}
        """
        self.assertTrue(TestCodeGen.test(input, "0123", 663))

    def test_078(self):
        input = """
func main() {
    var i = 0;
    for i < 5 {
        i += 1;
        if (i % 2 == 0) {
            continue;
        }
        putInt(i);
    }
    putInt(i);
}
        """
        self.assertTrue(TestCodeGen.test(input, "1355", 664))

    def test_079(self):
        input = """
func main() {
    var i = 0;
    for i < 5 {
        i += 1;
        if (i % 2 == 0) {
            continue;
        }
        putInt(i);
    }
    putInt(i);
}
        """
        self.assertTrue(TestCodeGen.test(input, "1355", 665))

    def test_080(self):
        input = """
func main() {
    var i = 0;
    for i < 5 {
        i += 1;
        if (i % 2 == 0) {
            continue;
        }
        putInt(i);
    }
    putInt(i);
}
        """
        self.assertTrue(TestCodeGen.test(input, "1355", 666))

    def test_081(self):
        input = """
func main() {
    var i = 0;
    for i < 5 {
        i += 1;
        if (i % 2 == 0) {
            continue;
        }
        putInt(i);
    }
    putInt(i);
}
        """
        self.assertTrue(TestCodeGen.test(input, "1355", 667))

    def test_082(self):
        input = """
func main() {
    var i = 0;
    for i < 5 {
        i += 1;
        if (i % 2 == 0) {
            continue;
        }
        putInt(i);
    }
    putInt(i);
}
        """
        self.assertTrue(TestCodeGen.test(input, "1355", 668))

    def test_083(self):
        input = """
func main() {
    var i = 0;
    for i < 5 {
        i += 1;
        if (i % 2 == 0) {
            continue;
        }
        putInt(i);
    }
    putInt(i);
}
        """
        self.assertTrue(TestCodeGen.test(input, "1355", 669))

    def test_084(self):
        input = """
func main() {
    var i = 0;
    for i < 5 {
        i += 1;
        if (i % 2 == 0) {
            continue;
        }
        putInt(i);
    }
    putInt(i);
}
        """
        self.assertTrue(TestCodeGen.test(input, "1355", 670))

    def test_085(self):
        input = """
func main() {
    var i = 0;
    for i < 5 {
        i += 1;
        if (i % 2 == 0) {
            continue;
        }
        putInt(i);
    }
    putInt(i);
}
        """
        self.assertTrue(TestCodeGen.test(input, "1355", 671))

    def test_086(self):
        input = """
func main() {
    var i = 0;
    for i < 5 {
        i += 1;
        if (i % 2 == 0) {
            continue;
        }
        putInt(i);
    }
    putInt(i);
}
        """
        self.assertTrue(TestCodeGen.test(input, "1355", 672))

    def test_087(self):
        input = """
func main() {
    var i = 0;
    for i < 5 {
        i += 1;
        if (i % 2 == 0) {
            continue;
        }
        putInt(i);
    }
    putInt(i);
}
        """
        self.assertTrue(TestCodeGen.test(input, "1355", 673))

    def test_088(self):
        input = """
func main() {
    var i = 0;
    for i < 5 {
        i += 1;
        if (i % 2 == 0) {
            continue;
        }
        putInt(i);
    }
    putInt(i);
}
        """
        self.assertTrue(TestCodeGen.test(input, "1355", 674))

    def test_089(self):
        input = """
func main() {
    var i = 0;
    for i < 5 {
        i += 1;
        if (i % 2 == 0) {
            continue;
        }
        putInt(i);
    }
    putInt(i);
}
        """
        self.assertTrue(TestCodeGen.test(input, "1355", 675))

    def test_090(self):
        input = """
func main() {
    var i = 0;
    for i < 5 {
        i += 1;
        if (i % 2 == 0) {
            continue;
        }
        putInt(i);
    }
    putInt(i);
}
        """
        self.assertTrue(TestCodeGen.test(input, "1355", 676))

    def test_091(self):
        input = """
func main() {
    var i = 0;
    for i < 5 {
        i += 1;
        if (i % 2 == 0) {
            continue;
        }
        putInt(i);
    }
    putInt(i);
}
        """
        self.assertTrue(TestCodeGen.test(input, "1355", 677))

    def test_092(self):
        input = """
func main() {
    var i = 0;
    for i < 5 {
        i += 1;
        if (i % 2 == 0) {
            continue;
        }
        putInt(i);
    }
    putInt(i);
}
        """
        self.assertTrue(TestCodeGen.test(input, "1355", 678))

    def test_093(self):
        input = """
func main() {
    var i = 0;
    for i < 5 {
        i += 1;
        if (i % 2 == 0) {
            continue;
        }
        putInt(i);
    }
    putInt(i);
}
        """
        self.assertTrue(TestCodeGen.test(input, "1355", 679))

    def test_094(self):
        input = """
func main() {
    var i = 0;
    for i < 5 {
        i += 1;
        if (i % 2 == 0) {
            continue;
        }
        putInt(i);
    }
    putInt(i);
}
        """
        self.assertTrue(TestCodeGen.test(input, "1355", 680))
