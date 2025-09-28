# import unittest
# from TestUtils import TestCodeGen
# from AST import *


# class CheckCodeGenSuite(unittest.TestCase):
# #     def test_int_literal(self):
# #         input = """func main() {putInt(5);};"""
# #         expect = "5"
# #         self.assertTrue(TestCodeGen.test(input,expect,501))
# #     def test_local_var(self):
# #         input = """func main() {var a int = 20;  putInt(a);};"""
# #         expect = "20"
# #         self.assertTrue(TestCodeGen.test(input,expect,502))
# #     def test_gllobal_var(self):
# #         input = """var a int = 10; func main() { putInt(a);};"""
# #         expect = "10"
# #         self.assertTrue(TestCodeGen.test(input,expect,503))
# #     def test_int_ast(self):
# #         input = Program([FuncDecl("main",[],VoidType(),Block([FuncCall("putInt", [IntLiteral(25)])]))])
# #         expect = "25"
# #         self.assertTrue(TestCodeGen.test(input,expect,504))
# #     def test_local_var_ast(self):
# #         input = Program([FuncDecl("main",[],VoidType(),Block([VarDecl("a",IntType(),IntLiteral(500)),FuncCall("putInt", [Id("a")])]))])
# #         expect = "500"
# #         self.assertTrue(TestCodeGen.test(input,expect,505))
# #     def test_global_var_ast(self):  
# #         input = Program([VarDecl("a",IntType(),IntLiteral(5000)),FuncDecl("main",[],VoidType(),Block([FuncCall("putInt", [Id("a")])]))])
# #         expect = "5000"
# #         self.assertTrue(TestCodeGen.test(input,expect,506))

# #     def test_001(self):
# #         input = """
# # func fvoid() {putStringLn("VoTien");}

# # var global = fint()
# # func main() {
# #     fvoid();
# #     putFloatLn(global + 2.0)

# #     var local = "a";
# #     putBoolLn(local <= "b")
# #     local += "c"
# #     putStringLn(local)

# # };

# # func fint() int {return 1;}
# # """
# #         self.assertTrue(TestCodeGen.test(input,"VoTien\n3.0\ntrue\nac\n",507)) 
    
# #     def test_002(self):
# #         input = """
# # func main() {
# #     putBoolLn(5.0 > 2.0)
# #     putBoolLn(5.0 < 2.0)
# #     putBoolLn(5.0 <= 5.0)
# #     putBoolLn(5.0 >= 5.0)
# #     putBoolLn(5.0 == 5.0)
# #     putBoolLn(5.0 != 5.0)
# # }
# # """
# #         self.assertTrue(TestCodeGen.test(input,"true\nfalse\ntrue\ntrue\ntrue\nfalse\n",508)) 

# #     def test_003(self):
# #         input = """
# # func main() {
# #     var a [1] int ;
# #     a[0] := 1
# #     putInt(a[0]);
# # }
# #     """
# #         self.assertTrue(TestCodeGen.test(input,"1",509))

# #     def test_004(self):
# #         input = """
# # func main() {
# #     var a [1][1][1] int  = [1][1][1] int {{{0}}};
# #     a[0][0][0] := 1
# #     putInt(a[0][0][0]);
# # }
# #     """
# #         self.assertTrue(TestCodeGen.test(input,"1",510))

# #     def test_005(self):
# #         input = """
# # func main() {
# #     var a [2] int = [2] int {10, 20};
# #     putInt(a[0])
# # }
# #     """
# #         self.assertTrue(TestCodeGen.test(input,"10",511))

# #     def test_006(self):
# #         input = """
# # func main() {
# #     var a [2] int;
# #     a[0] := 100
# #     a[1] += a[0] + a[0]
# #     putInt(a[1])
# # }
# #     """
# #         self.assertTrue(TestCodeGen.test(input,"200",512))
    
# #     def test_007(self):
# #         input = """
# #     var a [2] int;
# #     var b int;
# # func main() {
# #     a[0] := 100
# #     a[1] += a[0] + a[0]
# #     putInt(a[1])
# # }
# #     """
# #         self.assertTrue(TestCodeGen.test(input,"200",513))

# #     def test_008(self):
# #         input = """
# # func main() {
# #     if (true) {
# #         putBool(true)
# #     } 
# # }
# #     """
# #         self.assertTrue(TestCodeGen.test(input,"true",514))

# #     def test_009(self):
# #         input = """
# # func main() {
# #     if (true) {
# #         putBool(true)
# #     } else {
# #         putBool(false)     
# #     }
# # }
# #     """
# #         self.assertTrue(TestCodeGen.test(input,"true",515))

# #     def test_010(self):
# #         input = """
# # func main() {
# #     if (false) {
# #         putBool(true)
# #     } else {
# #         putBool(false)     
# #     }
# # }
# #     """
# #         self.assertTrue(TestCodeGen.test(input,"false",516))

# #     def test_011(self):
# #         input = """
# # func main() {
# #     var i = 0;
# #     for i < 3 {
# #         putInt(i);
# #         i += 1;
# #     }
# #     putInt(i);
# # }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "0123", 517))

# #     def test_012(self):
# #         input = """
# # func main() {
# #     var i = 0;
# #     for i < 5 {
# #         if (i == 3) {
# #             break;
# #         }
# #         putInt(i);
# #         i += 1;
# #     }
# #     putInt(i);
# # }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "0123", 518))

# #     def test_013(self):
# #         input = """
# # func main() {
# #     var i = 0;
# #     for i < 5 {
# #         i += 1;
# #         if (i % 2 == 0) {
# #             continue;
# #         }
# #         putInt(i);
# #     }
# #     putInt(i);
# # }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "1355", 519))

# #     def test_014(self):
# #         input = """
# #         var x int = 5;
# #         var y int = x;
# # func main() {
# #     var i int = 10;
# #     for var i int = 0; i < 2; i += 1 {
# #         putIntLn(i)
# #         break;
# #     }
# #     putInt(i)
# # }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "0\n10", 520))

# #     def test_015(self):
# #         input = """
# # const a = 1 + 1
# # const c = 5 - a
# # func main() {
# #   var b [a][c] int = [a][c] int {{1, 2, 3}, {5, 6, 7}};
# #   putInt(b[0][0]);
# #   b[0][0] := 20;
# #   putInt(b[0][0]);
# # }
# #       """
# #         self.assertTrue(TestCodeGen.test(input, "120", 521))

#     def test_016(self):
#         input = """
# type Course interface {study();}
# type PPL3 struct {number int;}
# func (p PPL3) study() {putInt(p.number);}

# func main(){
#     var a PPL3 = PPL3 {number: 10}
#     putIntLn(a.number)
#     a.study()
# }
#         """
#         self.assertTrue(TestCodeGen.test(input, "10\n10", 522))

# #     def test_017(self):
# #         input = """
# # type Course interface {study();}
# # type PPL3 struct {number int;}
# # func (p PPL3) study() {putInt(p.number);}

# # func main(){
# #     var a Course = nil
# #     a := PPL3 {number: 10}
# #     a.study()
# # }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "10", 523))

# #     def test_018(self):
# #         input = """
# # type PPL3 struct {number int;}

# # func main(){
# #     var a PPL3 = PPL3 {number: 10}
# #     putInt(a.number)
# # }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "10", 524))

# #     def test_019(self):
# #         input = """
# # type PPL3 struct {number int;}

# # func main(){
# #     var a PPL3
# #     a.number := 10
# #     putInt(a.number)
# # }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "10", 525))

# #     def test_020(self):
# #         input = """
# # type PPL2 struct {number int;}
# # type PPL3 struct {number int; ppl PPL2;}

# # func main(){
# #     var a PPL3
# #     a.ppl := PPL2 {number: 10}
# #    putInt(a.ppl.number)
# # }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "10", 526))

# #     def test_021(self):
# #         input = """
# # type PPL2 struct {number int;}
# # type PPL3 struct {number int; ppl PPL2;}

# # func main(){
# #     var a PPL3
# #     a.ppl := PPL2 {number: 10}
# #     a.ppl.number := 100
# #    putInt(a.ppl.number)
# # }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "100", 527))        

# #     def test_022(self):
# #         input = """
# # type Study interface { study(); }
# # type Play interface { play(); }

# # type PPL3 struct {number int;}

# # func (p PPL3) study() { putInt(p.number); }
# # func (p PPL3) play()  { putInt(p.number + 5); }

# # func main() {
# #     var a PPL3 = PPL3 {number: 1}
# #     a.study()
# #     a.play()
# # }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "16", 528))


# #     def test_023(self):
# #         input = """
# # type Study interface { study(); }
# # type Play interface { play(); }

# # type PPL3 struct {number int;}

# # func (p PPL3) study() { putInt(p.number); }
# # func (p PPL3) play()  { putInt(p.number + 5); }

# # func main() {
# #     var a PPL3 = PPL3 {number: 1}
# #     var b Study = a
# #     var c Play = a
# #     b.study()
# #     c.play()
# # }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "16", 529))

# #     def test_024(self):
# #         input = """
# # type Study interface { study(); }
# # type Play interface { play(); }

# # type PPL3 struct {number int;}

# # func (p PPL3) study() { putInt(p.number); }
# # func (p PPL3) play()  { putInt(p.number + 5); }

# # func main() {
# #     var a PPL3 = PPL3 {number: 1}
# #     var b Study = a
# #     var c Play = a
# #     b.study()
# #     c.play()
# # }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "16", 530))

# #     def test_025(self):
# #         input = """
# # type Worker interface { 
# #     study(); 
# #     play(); 
# # }

# # type PPL4 struct {number int;}
# # type PPL5 struct {number int;}

# # // Implement Worker cho PPL4
# # func (p PPL4) study() { putInt(p.number); }
# # func (p PPL4) play()  { putInt(p.number + 5); }

# # // Implement Worker cho PPL5
# # func (p PPL5) study() { putInt(p.number * 2); }
# # func (p PPL5) play()  { putInt(p.number * 3); }

# # func main() {
# #     var w1 Worker = PPL4 {number: 3}
# #     var w2 Worker = PPL5 {number: 4}

# #     w1.study(); // in: 3
# #     w1.play();  // in: 8

# #     w2.study(); // in: 8
# #     w2.play();  // in: 12
# # }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "38" "812", 531))

# #     def test_026(self):
# #         input = """
# # type Worker interface { 
# #     study(); 
# #     play(); 
# # }

# # type PPL4 struct {number int;}
# # type PPL5 struct {number int;}

# # // Implement Worker cho PPL4
# # func (p PPL4) study() { putInt(p.number); }
# # func (p PPL4) play()  { putInt(p.number + 5); }

# # // Implement Worker cho PPL5
# # func (p PPL5) study() { putInt(p.number * 2); }

# # func main() {
# #     var w1 Worker = PPL4 {number: 3}
# #     var w2 PPL5 = PPL5 {number: 4}

# #     w1.study(); // in: 3
# #     w1.play();  // in: 8

# #     w2.study(); // in: 8
# # }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "38" "8", 532))


# #     def test_027(self):
# #         input = """
# # type Speaker interface { speak(); }

# # type Human struct {name int; }

# # func (h Human) speak() { putIntLn(h.name); }

# # func saySomething(s Speaker) {
# #     s.speak();
# # }

# # func main() {
# #     var h Speaker = Human {name: 2025};
# #     saySomething(h);
# # }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "2025\n", 533))


# #     def test_028(self):
# #         input = """
# # type Speaker interface { speak(); }

# # type Human struct { name int; }

# # func (h Human) speak() { putIntLn(h.name); }

# # func main() {
# #     var people [3]Speaker;

# #     people[0] := Human {name: 1};
# #     people[1] := Human {name: 2};
# #     people[2] := Human {name: 3};

# #     people[0].speak(); // Output: 1
# #     people[1].speak(); // Output: 2
# #     people[2].speak(); // Output: 3
# # }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "1\n2\n3\n", 534))

# #     def test_029(self):
# #         input = """
# # type Speaker interface { speak(); }

# # type Human struct { name int; }

# # func (h Human) speak() { putIntLn(h.name); }

# # func main() {
# #     var people [3]Human;

# #     people[0] := Human {name: 1};
# #     people[1] := Human {name: 2};
# #     people[2] := Human {name: 3};

# #     people[0].speak(); // Output: 1
# #     people[1].speak(); // Output: 2
# #     people[2].speak(); // Output: 3
# # }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "1\n2\n3\n", 535))

# #     def test_030(self):
# #         input = """
# # type Calculator struct { x int; y int; }

# # func (c Calculator) sum() int {
# #     return c.x + c.y;
# # }

# # func main() {
# #     var cal Calculator = Calculator {x: 7, y: 8};
# #     var result int = cal.sum();
# #     putIntLn(result);
# # }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "15\n", 536))

# #     def test_031(self):
# #         input = """
# # type Calculator interface { sum() int; }

# # type BasicCalc struct { x int; y int; }

# # func (b BasicCalc) sum() int {
# #     return b.x + b.y;
# # }

# # func main() {
# #     var c Calculator = BasicCalc {x: 5, y: 15};
# #     var result int = c.sum();
# #     putIntLn(result);
# # }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "20\n", 537))

# #     def test_032(self):
# #         input = """
# # type Speaker interface { speak(); }

# # type Human struct { name int; }

# # func (h Human) speak() { putIntLn(h.name); }

# # func sayHello(s Speaker) {
# #     s.speak();
# # }

# # func main() {
# #     var h Human = Human {name: 100};
# #     sayHello(h);
# # }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "100\n", 538))

# #     def test_033(self):
# #         input = """
# # type Calculator interface { sum() int; }

# # type BasicCalc struct { x int; y int; }

# # func (b BasicCalc) sum() int {
# #     return b.x + b.y;
# # }

# # func calculate(c Calculator) int {
# #     return c.sum();
# # }

# # func main() {
# #     var b BasicCalc = BasicCalc {x: 20, y: 30};
# #     var result int = calculate(b);
# #     putIntLn(result);
# # }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "50\n", 539))

# #     def test_034(self):
# #         input = """
# # type Multiplier struct { factor int; }

# # func (m Multiplier) multiply(value int) int {
# #     return m.factor * value;
# # }

# # func main() {
# #     var mul Multiplier = Multiplier {factor: 5};
# #     var result int = mul.multiply(4);
# #     putIntLn(result);
# # }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "20\n", 540))

# #     def test_035(self):
# #         input = """
# # type Calculator interface { calculate(a int, b int) int; }

# # type BasicCalc struct {number int;}

# # func (b BasicCalc) calculate(a int, b int) int {
# #     return a + b;
# # }

# # func main() {
# #     var c Calculator = BasicCalc {};
# #     var result int = c.calculate(15, 25);
# #     putIntLn(result);
# # }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "40\n", 541))


# #     def test_036(self):
# #         input = """
# # type Calculator interface { calculate(a int, b int); }

# # type BasicCalc struct {number int;}

# # func (b BasicCalc) calculate(a int, b int) {
# #     putIntLn(a+b);
# # }

# # func main() {
# #     var c Calculator = BasicCalc {};
# #     c.calculate(15, 25);
# # }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "40\n", 542))

# #     def test_037(self):
# #         input = """
# # type Calculator interface { calculate(a int, b int); }

# # type BasicCalc struct {number int;}

# # func (b BasicCalc) calculate(a int, b int) {
# #     putIntLn(a+b);
# # }

# # func main() {
# #     var c BasicCalc
# #     c.calculate(15, 25);
# # }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "40\n", 543))

# #     def test_038(self):
# #         input = """
# # type Speaker interface { speak(); }

# # type Human struct { name int; }

# # func (h Human) speak() {
# #     putIntLn(h.name);
# # }

# # type Classroom struct {
# #     student Human;
# #     guest Speaker;
# # }

# # func main() {
# #     var h Human = Human {name: 777};
# #     var k Speaker = Human {name: 999};
# #     var room Classroom = Classroom {student: h, guest: k};

# #     putIntLn(room.student.name);
# #     room.guest.speak();
# # }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "777\n999\n", 544))

# #     def test_039(self):
# #         input = """
# #     type Person struct {
# #         name string;
# #         age int;
# #     }
# #     func main() {
# #         var p Person = Person{name: "Alice", age: 22};
# #         putStringLn(p.name);
# #         putIntLn(p.age);
# #     }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "Alice\n22\n", 545))

# #     def test_040(self):
# #         input = """
# #     type Greeter interface { greet(); }

# #     type Person struct {
# #         name string;
# #         age int;
# #     }
# #     func (p Person) greet() {
# #         putStringLn(p.name);
# #     }

# #     func main() {
# #         var g Greeter = Person{name: "Bob", age: 30};
# #         g.greet();
# #     }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "Bob\n", 546))

# #     def test_041(self):
# #         input = """
# #     type Person struct {
# #         name string;
# #         age int;
# #     }
# #     func (p Person) agePlus(n int) int {
# #         return p.age + n;
# #     }
# #     func main() {
# #         var p Person = Person{name: "Charlie", age: 18};
# #         var result int = p.agePlus(5);
# #         putIntLn(result);
# #     }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "23\n", 547))

# #     def test_042(self):
# #         input = """
# #     type Person struct {
# #         name string;
# #         age int;
# #     }
# #     func sumAges(p1 Person, p2 Person) int {
# #         return p1.age + p2.age;
# #     }
# #     func main() {
# #         var p1 Person = Person{name: "Dan", age: 20};
# #         var p2 Person = Person{name: "Eve", age: 25};
# #         var total int = sumAges(p1, p2);
# #         putIntLn(total);
# #     }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "45\n", 548))

# #     def test_043(self):
# #         input = """
# #     type Person struct {
# #         name string;
# #         age int;
# #     }
# #     func (p Person) printInfo() {
# #         putStringLn(p.name);
# #         putIntLn(p.age);
# #     }
# #     func main() {
# #         var people [1]Person
# #         people[0] := Person{name: "Anna", age: 19};
# #         people[0].printInfo() 
# #     }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "Anna\n19\n", 549))

# #     def test_044(self):
# #         input = """
# #     type Speaker interface { speak(); }
# #     type Person struct {
# #         name string;
# #         age int;
# #     }
# #     func (p Person) speak() {
# #         putStringLn(p.name);
# #     }
# #     func announce(s Speaker) {
# #         s.speak();
# #     }
# #     func main() {
# #         var p Person = Person{name: "Grace", age: 27};
# #         announce(p);
# #     }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "Grace\n", 550))

# #     def test_045(self):
# #         input = """
# #     type Person struct {
# #         name string;
# #         age int;
# #     }
# #     func createPerson(n string, a int) Person {
# #         return Person{name: n, age: a};
# #     }
# #     func main() {
# #         var p Person = createPerson("Helen", 24);
# #         putStringLn(p.name);
# #         putIntLn(p.age);
# #     }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "Helen\n24\n", 551))

# #     def test_046(self):
# #         input = """
# #     type Person struct {
# #         name string;
# #         age int;
# #     }
# #     func (p Person) isAdult() boolean {
# #         return p.age >= 18;
# #     }
# #     func main() {
# #         var p Person = Person{name: "Ivy", age: 17};
# #         if (p.isAdult()) {
# #             putStringLn("Adult");
# #         } else {
# #             putStringLn("Minor");
# #         }
# #     }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "Minor\n", 552))

# #     def test_047(self):
# #         input = """
# #     type Person struct {
# #         name string;
# #         age int;
# #     }
# #     func (p Person) duplicate() Person {
# #         return Person{name: p.name, age: p.age};
# #     }
# #     func main() {
# #         var p1 Person = Person{name: "Jack", age: 31};
# #         var p2 Person = p1.duplicate();
# #         putStringLn(p2.name);
# #         putIntLn(p2.age);
# #     }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "Jack\n31\n", 553))

# #     def test_048(self):
# #         input = """
# #     type Person struct {
# #         name string;
# #         age int;
# #     }
# #     func (p Person) printInfo() {
# #         putStringLn(p.name);
# #         putIntLn(p.age);
# #     }
# #     func main() {
# #         var people [2]Person = [2]Person{Person{name: "Anna", age: 19},Person{name: "Bill", age: 21}};
# #         people[0].printInfo();
# #         people[1].printInfo();
# #     }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "Anna\n19\nBill\n21\n", 554))

# #     def test_049(self):
# #         input = """
# # var prefix string;

# # type Person struct {
# #     name string;
# #     age int;
# # }

# # func getGreeting(name string) string {
# #     return prefix + name;
# # }

# # func (p Person) greet() string {
# #     return getGreeting(p.name);
# # }

# # func main() {
# #     var votien Person = Person{name: "Votien", age: 19};
# #     prefix := "Hello, my name is ";
# #     var msg string = votien.greet();
# #     putStringLn(msg);
# # }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "Hello, my name is Votien\n", 555))

# #     def test_050(self):
# #         input = """
# # func foo(){
# #     a := 5;
# #     putInt(a)
# # }

# # var a int = 3
        
# # func main(){
# #     foo()
# #     putInt(a)
# # }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "53", 556))

# #     def test_051(self):
# #         input = """

# # func main() {
# #     putBoolLn(! true)
# #     putBoolLn(! false)
# #     putIntLn(-1)
# #     putFloatLn(-1.0)
# # }
# # """
# #         self.assertTrue(TestCodeGen.test(input,"false\ntrue\n-1\n-1.0\n",557)) 
    
# #     def test_052(self):
# #         """Test complex recursive array operation"""
# #         input = """
# #         func transform(a [2]int, index int) {
# #             if (index >= 2) { return; }
# #             a[index] := a[index] * 2;
# #             transform(a, index + 1);
# #         }
# #         func main() {
# #             var a [2]int = [2]int {5, 10};
# #             transform(a, 0);
# #             putInt(a[1]);
# #         }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "20", 558))

# #     def test_053(self):
# #         """Test complex recursive array operation"""
# #         input = """
# #         func main() {
# #             var x = 3.14;
# #             var y float;

# #             putFloatLn(x)
# #             putFloat(y)
# #         }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "3.14\n0.0", 559))

# #     def test_054(self):
# #         """Test array with conditional sum"""
# #         input = """
# #         func main() {
# #             var a [3]int = [3]int {1, 2, 3};
# #             var sum int;
# #             for i := 0; i < 3; i += 1 {
# #                 if (a[i] > 1) {
# #                     sum += a[i];
# #                 }
# #             }
# #             putInt(sum);
# #         }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "5", 560))

# #     def test_055(self):
# #         """Test global struct array with method"""
# #         input = """
# #         type Person struct { id int; }
# #         func (p Person) getId() int { return p.id; }
# #         var a [2]Person = [2]Person {Person {id: 1}, Person {id: 2}};
# #         func main() {
# #             putInt(a[0].getId());
# #         }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "1", 561))
    
# #     def test_056(self):
# #         """Test recursive array min element"""
# #         input = """
# #         func minArray(a [3]int, index int) int {
# #             if (index >= 3) { return a[0]; }
# #             var rest int = minArray(a, index + 1);
# #             if (a[index] < rest) { return a[index]; }
# #             return rest;
# #         }
# #         func main() {
# #             var a [3]int = [3]int {10, 5, 15};
# #             putInt(minArray(a, 0));
# #         }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "5", 562))

# #     def test_057(self):
# #         """Test array with function modifying elements"""
# #         input = """
# #         func double(a [2]int) {
# #             for i := 0; i < 2; i += 1 {
# #                 a[i] := a[i] * 2;
# #             }
# #         }
# #         func main() {
# #             var a [2]int = [2]int {5, 10};
# #             double(a);
# #             putInt(a[1]);
# #         }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "20", 563))

# #     def test_058(self):
# #         """Test interface with recursive method"""
# #         input = """
# #         type Counter interface { count(n int) int; }
# #         type Device struct { value int; }
# #         func (d Device) count(n int) int {
# #             if (n == 0) { return d.value; }
# #             d.value := d.value + 1;
# #             return d.count(n - 1);
# #         }
# #         func main() {
# #             var c Counter = Device {value: 0};
# #             putInt(c.count(2));
# #         }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "2", 564))
    
# #     def test_059(self):
# #         """Test array sorting (bubble sort)"""
# #         input = """
# #         func bubbleSort(a [3]int) {
# #             for i := 0; i < 2; i += 1 {
# #                 for j := 0; j < 2 - i; j += 1 {
# #                     if (a[j] > a[j + 1]) {
# #                         var temp int = a[j];
# #                         a[j] := a[j + 1];
# #                         a[j + 1] := temp;
# #                     }
# #                 }
# #             }
# #         }
# #         func main() {
# #             var a [3]int = [3]int {3, 1, 2};
# #             bubbleSort(a);
# #             putInt(a[0]);
# #         }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "1", 565))

# #     def test_060(self):
# #         """Test global array of structs"""
# #         input = """
# #         type Person struct { id int; }
# #         var people [2]Person = [2]Person {Person {id: 1}, Person {id: 2}};
# #         func main() {
# #             putInt(people[1].id);
# #         }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "2", 566))

# #     def test_061(self):
# #         """Test array with negative index calculation"""
# #         input = """
# #         func main() {
# #             var a [3]int = [3]int {10, 20, 30};
# #             var i int = 3;
# #             putInt(a[i - 1]);
# #         }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "30", 567))

# #     def test_062(self):
# #         """Test struct with pointer-like behavior (assignment)"""
# #         input = """
# #         type Person struct { id int; }
# #         func main() {
# #             var p1 Person = Person {id: 10};
# #             var p2 Person = p1;
# #             putInt(p2.id);
# #         }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "10", 568))

# #     def test_063(self):
# #         """Test array of booleans with logical operations"""
# #         input = """
# #         func main() {
# #             var a [2]boolean = [2]boolean {true, false};
# #             putBool(a[0] || a[1]);
# #         }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "true", 569))

# #     def test_064(self):
# #         """Test function with struct parameter"""
# #         input = """
# #         type Person struct { age int; }
# #         func getAge(p Person) int {
# #             return p.age;
# #         }
# #         func main() {
# #             var p Person = Person {age: 25};
# #             putInt(getAge(p));
# #         }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "25", 570))

# #     def test_065(self):
# #         """Test array initialization with loop"""
# #         input = """
# #         func main() {
# #             var a [3]int;
# #             for i := 0; i < 3; i += 1 {
# #                 a[i] := (i + 1) * 10;
# #             }
# #             putInt(a[2]);
# #         }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "30", 571))

# #     def test_066(self):
# #         """Test interface with multiple implementations"""
# #         input = """
# #         type Speaker interface { speak(); }
# #         type Person struct { name string; }
# #         type Robot struct { code int; }
# #         func (p Person) speak() { putString(p.name); }
# #         func (r Robot) speak() { putInt(r.code); }
# #         func main() {
# #             var s Speaker = Robot {code: 100};
# #             s.speak();
# #         }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "100", 572))

# #     def test_067(self):
# #         """Test array element modification in function"""
# #         input = """
# #         func update(a [2]int) {
# #             a[0] := 50;
# #         }
# #         func main() {
# #             var a [2]int = [2]int {10, 20};
# #             update(a);
# #             putInt(a[0]);
# #         }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "50", 573))

# #     def test_068(self):
# #         """Test recursive array sum with base case"""
# #         input = """
# #         func sumArray(a [2]int, index int) int {
# #             if (index >= 2) { return 0; }
# #             return a[index] + sumArray(a, index + 1);
# #         }
# #         func main() {
# #             var a [2]int = [2]int {5, 5};
# #             putInt(sumArray(a, 0));
# #         }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "10", 574))

# #     def test_069(self):
# #         """Test global constant string"""
# #         input = """
# #         const s = "Hello";
# #         func main() {
# #             putString(s);
# #         }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "Hello", 575))

# #     def test_070(self):
# #         """Test array with complex indexing"""
# #         input = """
# #         func main() {
# #             var a [3]int = [3]int {10, 20, 30};
# #             var i int = 1;
# #             putInt(a[i + 1]);
# #         }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "30", 576))

# #     def test_071(self):
# #         """Test struct with multiple methods"""
# #         input = """
# #         type Person struct { name string; age int; }
# #         func (p Person) getName() string { return p.name; }
# #         func (p Person) getAge() int { return p.age; }
# #         func main() {
# #             var p Person = Person {name: "Alice", age: 30};
# #             putString(p.getName());
# #         }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "Alice", 577))

# #     def test_072(self):
# #         """Test array of structs with loop"""
# #         input = """
# #         type Person struct { id int; }
# #         func main() {
# #             var people [2]Person = [2]Person {Person {id: 1}, Person {id: 2}};
# #             for i := 0; i < 2; i += 1 {
# #                 putInt(people[i].id);
# #             }
# #         }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "12", 578))

# #     def test_073(self):
# #         """Test recursive power function"""
# #         input = """
# #         func power(base int, exp int) int {
# #             if (exp == 0) { return 1; }
# #             return base * power(base, exp - 1);
# #         }
# #         func main() {
# #             putInt(power(2, 3));
# #         }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "8", 579))

# #     def test_074(self):
# #         """Test nested if-else with struct"""
# #         input = """
# #         type Person struct { age int; }
# #         func main() {
# #             var p Person = Person {age: 20};
# #             if (p.age > 18) {
# #                 if (p.age < 25) {
# #                     putInt(p.age);
# #                 }
# #             }
# #         }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "20", 580))

# #     def test_075(self):
# #         """Test array with dynamic size (constant)"""
# #         input = """
# #         const n = 3;
# #         func main() {
# #             var a [n]int = [n]int {1, 2, 3};
# #             putInt(a[2]);
# #         }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "3", 582))

# #     def test_076(self):
# #         """Test array element swap in loop"""
# #         input = """
# #         func main() {
# #             var a [3]int = [3]int {1, 2, 3};
# #             for i := 0; i < 2; i += 1 {
# #                 var temp int = a[i];
# #                 a[i] := a[2 - i];
# #                 a[2 - i] := temp;
# #             }
# #             putInt(a[0]);
# #         }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "3", 583))

# #     def test_077(self):
# #         """Test struct with interface and array"""
# #         input = """
# #         type Speaker interface { speak(); }
# #         type Person struct { id int; }
# #         func (p Person) speak() { putInt(p.id); }
# #         func main() {
# #             var a [2]Speaker = [2]Speaker {Person {id: 1}, Person {id: 2}};
# #             a[0].speak();
# #         }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "1", 584))

# #     def test_078(self):
# #         """Test recursive array reverse"""
# #         input = """
# #         func reverse(a [3]int, start int, end int) {
# #             if (start >= end) { return; }
# #             var temp int = a[start];
# #             a[start] := a[end];
# #             a[end] := temp;
# #             reverse(a, start + 1, end - 1);
# #         }
# #         func main() {
# #             var a [3]int = [3]int {1, 2, 3};
# #             reverse(a, 0, 2);
# #             putInt(a[0]);
# #         }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "3", 585))

# #     def test_079(self):
# #         """Test global boolean array"""
# #         input = """
# #         var a [2]boolean = [2]boolean {true, false};
# #         func main() {
# #             putBool(a[0]);
# #         }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "true", 586))

# #     def test_080(self):
# #         """Test array with struct indexing"""
# #         input = """
# #         type Person struct { id int; }
# #         func main() {
# #             var a [2]Person = [2]Person {Person {id: 1}, Person {id: 2}};
# #             var i int = 1;
# #             putInt(a[i].id);
# #         }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "2", 587))

# #     def test_081(self):
# #         """Test function with nested array parameter"""
# #         input = """
# #         func get(a [2][2]int) int {
# #             return a[1][1];
# #         }
# #         func main() {
# #             var a [2][2]int = [2][2]int {{1, 2}, {3, 4}};
# #             putInt(get(a));
# #         }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "4", 588))

# #     def test_083(self):
# #         """Test array initialization with function call"""
# #         input = """
# #         func getValue() int { return 42; }
# #         func main() {
# #             var a [2]int = [2]int {42, 20};
# #             putInt(a[0]);
# #         }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "42", 589))

# #     def test_084(self):
# #         """Test struct with recursive method"""
# #         input = """
# #         type Counter struct { value int; }
# #         func (c Counter) inc(n int) int {
# #             if (n == 0) { return c.value; }
# #             c.value := c.value + 1;
# #             return c.inc(n - 1);
# #         }
# #         func main() {
# #             var c Counter = Counter {value: 0};
# #             putInt(c.inc(3));
# #         }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "3", 590))

# #     def test_085(self):
# #         input = """
# # type PPL3 struct {number int;}
# # func (p PPL3) foo1() {
# #     a := 5;
# #     putInt(a);
# # }

# # var a = 8;

# # func (p PPL3) foo2() {
# #     putInt(a);
# #     a := 7;
# #     putInt(a);
# # }

# # func main(){
# #     b := PPL3 {number: 10}
# #     b.foo1()
# #     b.foo2()
# #     putInt(a)
# # }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "5877", 591))

# #     def test_086(self):
# #         """Test break statement in loop"""
# #         input = """
# #         func main() {
# #             for i := 0; i < 5; i += 1 {
# #                 if (i == 3) { break; }
# #                 putInt(i);
# #             }
# #         }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "012", 592))

# #     def test_283(self):
# #         """Test array with type conversion and loop"""
# #         input = """
# #         func main() {
# #             var a [2]int = [2]int {1, 2};
# #             var b [2]float;
# #             for i := 0; i < 2; i += 1 {
# #                 b[i] := a[i];
# #             }
# #             putFloat(b[1]);
# #         }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "2.0", 593))

# #     def test_284(self):
# #         """Test interface with struct array parameter"""
# #         input = """
# #         type Printer interface { print(a [2]int); }
# #         type Device struct { id int; }
# #         func (d Device) print(a [2]int) { putInt(a[0]); }
# #         func main() {
# #             var p Printer = Device {id: 1};
# #             p.print([2]int {10, 20});
# #         }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "10", 594))

# #     def test_285(self):
# #         """Test array with recursive search"""
# #         input = """
# #         func find(a [3]int, target int, index int) int {
# #             if (index >= 3) { return -1; }
# #             if (a[index] == target) { return index; }
# #             return find(a, target, index + 1);
# #         }
# #         func main() {
# #             var a [3]int = [3]int {10, 20, 30};
# #             putInt(find(a, 20, 0));
# #         }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "1", 595))

# #     def test_286(self):
# #         """Test global array with struct assignment"""
# #         input = """
# #         type Person struct { id int; }
# #         var a [2]Person = [2]Person {Person {id: 1}, Person {id: 2}};
# #         func main() {
# #             putInt(a[0].id);
# #         }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "1", 596))

# #     def test_287(self):
# #         """Test array with conditional modification"""
# #         input = """
# #         func main() {
# #             var a [3]int = [3]int {1, 2, 3};
# #             for i := 0; i < 3; i += 1 {
# #                 if (a[i] % 2 == 0) {
# #                     a[i] += 10;
# #                 }
# #             }
# #             putInt(a[1]);
# #         }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "12", 597))

# #     def test_288(self):
# #         """Test struct with array of structs"""
# #         input = """
# #         type Person struct { id int; }
# #         type Group struct { members [2]Person; }
# #         func main() {
# #             var g Group = Group {members: [2]Person {Person {id: 1}, Person {id: 2}}};
# #             putInt(g.members[1].id);
# #         }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "2", 598))

# #     def test_289(self):
# #         """Test function with array and struct parameter"""
# #         input = """
# #         type Person struct { id int; }
# #         func process(a [2]int, p Person) int {
# #             return a[0] + p.id;
# #         }
# #         func main() {
# #             var a [2]int = [2]int {5, 10};
# #             var p Person = Person {id: 15};
# #             putInt(process(a, p));
# #         }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "20", 599))

# #     def test_290(self):
# #         """Test array with recursive merge"""
# #         input = """
# #         func merge(a [2]int, start int, end int) {
# #             if (start >= end) { return; }
# #             a[start] := a[start] + a[end];
# #             merge(a, start + 1, end - 1);
# #         }
# #         func main() {
# #             var a [2]int = [2]int {10, 20};
# #             merge(a, 0, 1);
# #             putInt(a[0]);
# #         }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "30", 600))

# #     def test_292(self):
# #         """Test nested loops with struct array"""
# #         input = """
# #         type Person struct { id int; }
# #         func main() {
# #             var a [2][2]Person = [2][2]Person {{Person {id: 1}, Person {id: 2}}, {Person {id: 3}, Person {id: 4}}};
# #             for i := 0; i < 2; i += 1 {
# #                 for j := 0; j < 2; j += 1 {
# #                     putInt(a[i][j].id);
# #                 }
# #             }
# #         }
# #         """
# #         self.assertTrue(TestCodeGen.test(input, "1234", 500))


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
