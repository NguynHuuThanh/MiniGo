.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public <init>()V
.var 0 is this LMiniGoClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
	bipush 10
.var 1 is a I from Label2 to Label3
	bipush 10
	istore_1
	bipush 20
.var 2 is b I from Label2 to Label3
	bipush 20
	istore_2
	iload_1
	iconst_5
	if_icmple Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	iload_2
	bipush 30
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	iand
	invokestatic io/putBoolLn(Z)V
	iload_1
	bipush 15
	if_icmple Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	iload_2
	bipush 30
	if_icmpge Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ior
	invokestatic io/putBoolLn(Z)V
	iload_1
	iload_2
	if_icmpne Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifgt Label14
	iconst_0
	goto Label15
Label14:
	iconst_0
Label15:
	invokestatic io/putBoolLn(Z)V
Label3:
Label1:
	return
.limit stack 35
.limit locals 3
.end method

.method public static <clinit>()V
Label0:
Label2:
Label3:
Label1:
	return
.limit stack 0
.limit locals 0
.end method
