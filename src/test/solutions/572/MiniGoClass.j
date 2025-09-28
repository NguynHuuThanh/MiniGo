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
	bipush 15
.var 2 is b I from Label2 to Label3
	bipush 15
	istore_2
	iconst_5
.var 3 is c I from Label2 to Label3
	iconst_5
	istore_3
	iload_1
	iload_2
	if_icmple Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	iload_1
	iload_3
	if_icmple Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	iand
	ifle Label4
Label10:
	iload_1
	invokestatic io/putInt(I)V
Label11:
	goto Label5
Label4:
	iload_2
	iload_1
	if_icmple Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	iload_2
	iload_3
	if_icmple Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	iand
	ifle Label12
Label18:
	iload_2
	invokestatic io/putInt(I)V
Label19:
	goto Label13
Label12:
Label20:
	iload_3
	invokestatic io/putInt(I)V
Label21:
Label13:
Label5:
Label3:
Label1:
	return
.limit stack 31
.limit locals 4
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
